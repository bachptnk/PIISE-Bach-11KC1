import torch
import re
import librosa
from datasets import load_dataset, load_metric,Dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from utils import *
import os 
from ctcdecode import CTCBeamDecoder

MODEL_ID = "model/checkpoint-45000"
DEVICE = "cuda"

wer = load_metric("wer")
cer = load_metric("cer")

processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
model.to(DEVICE)

vocab = processor.tokenizer.get_vocab()
vocab.pop('<s>')
vocab.pop('</s>')
blank_id = vocab.get("|")
decoder = CTCBeamDecoder(
    vocab,
    model_path=None,
    alpha=0,
    beta=0,
    cutoff_top_n=40,
    cutoff_prob=1.0,
    beam_width=100,
    num_processes=4,
    blank_id=0,
    log_probs_input=True  ##True if raw_logits False if 
)


def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = librosa.load(batch["file"], sr=16_000)
    batch["speech"] = speech_array
    batch["sentence"] = batch["text"]
    return batch

def load_dataset(filename=None,filepath='./cache/train10.json',wav_path='data/sound/',script_path='data/transcript/',data_type='json'):
    if data_type == 'json':
        tmp_test_data = open_json(filepath)
        test_dataset = Dataset.from_dict(tmp_test_data)
    elif data_type == 'wav':
        tmp = {}
        with open(script_path+filename+'.txt','r') as fp:
            text = fp.read()
        text = clean(text)
        tmp['file'] = [wav_path + filename+'.wav']
        tmp['text'] = [text]
        test_dataset = Dataset.from_dict(tmp)
    return test_dataset

test_dataset = load_dataset(data_type= 'json')
test_dataset = test_dataset.map(speech_file_to_array_fn)

def evaluate_with_greedy(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True).to(DEVICE)
    with torch.no_grad():
        logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits
    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

def evaluate_with_beamsearch(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True).to(DEVICE)
    with torch.no_grad():
        logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits
    beam_results, beam_scores, timesteps, out_lens = decoder.decode(logits)
    pred_ids = torch.Tensor()
    for i in range(beam_results.shape[0]):
        real_value=out_lens[i][0]
        n_time_step = beam_results.shape[2]
        padding = torch.ones(n_time_step-real_value) * blank_id
        b_results = torch.concat((beam_results[i][0][:real_value],padding),dim=-1)
        pred_ids = torch.concat((pred_ids,b_results.unsqueeze(dim=0)),dim=0)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

def display_result(function_eval,method):
    result = test_dataset.map(function_eval, batched=True, batch_size=8)
    predictions = [x.lower() for x in result["pred_strings"]]
    references = [x.lower() for x in result["sentence"]]
    print("predict of {}: ".format(method),predictions)
    print("ref: ",references)

    print(f"WER: {wer.compute(predictions=predictions, references=references) * 100}")
    print(f"CER: {cer.compute(predictions=predictions, references=references) * 100}")

display_result(evaluate_with_greedy,method = "greedy")
display_result(evaluate_with_beamsearch,method = "beamsearch")
