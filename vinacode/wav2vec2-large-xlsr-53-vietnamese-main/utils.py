import re
import json
import pickle as pkl
def remove_special_characters(text):
    chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�]'
    res = re.sub(chars_to_ignore_regex, '', text).lower() + " "
    return res

def clean(text):
    chars_to_ignore_regex = "[\'\,\?\.\!\-\;\:\"\“\%\‘\”\�]"
    res = re.sub(chars_to_ignore_regex, '', text).lower()
    res = re.sub("<unk>","",res)
    res = res.strip()
    return res

def get_file_name(text):
    name = " ".join(text.split('.')[:-1])
    return name

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def to_json(filepath,data):
    with open(filepath,'w+') as f:
        json.dump(data,f)

def open_json(filepath):
    with open(filepath,'r') as f:
        res = json.load(f)
    return res

def to_pkl(filepath,data):
    with open(filepath,'wb+') as f:
        pkl.dump(data,f)

def open_pkl(filepath):
    with open(filepath,'rb') as f:
        res = pkl.load(f)
    return res