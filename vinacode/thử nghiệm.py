from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import threading
import pyttsx3
import io
from pydub import AudioSegment
import webbrowser as wb
import datetime
import random
import sys
def quit():
    sys.exit()
import os
from time import sleep
import playsound
from playsound import playsound
import speech_recognition as sr

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# load model and tokenizer
Bach_processor = Wav2Vec2Processor.from_pretrained("assets/vietnamese-model")
model = Wav2Vec2ForCTC.from_pretrained("assets/vietnamese-model")#wav2vec2-bachptnk-model
model.to(device)

PTNK_AI_assistant=pyttsx3.init()  # My name is Bach. I am learning in grade 10 in HIGH SCHOOL FOR THE GIFTED (PTNK)
voice=PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
Brate = 200
PTNK_AI_assistant.setProperty('rate',Brate)
def speak(audio):
    print('PTNK_AI_assistant: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()



def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p') #giải thích nè ^^: %I là giờ loại 12 tiếng, %M là phút, %p là AM hay PM
    speak('bây giờ là')
    speak(Time)
def date():
    today=datetime.datetime.now().strftime('Hôm nay là ngày %d-%m-%Y')

    speak(today)
    
def welcome(): #đây là mình tạo một cái function chào hỏi dựa theo thời gian mỗi khi khởi động PTNK_AI_ASSISTANT
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Chào buổi sáng')
    elif hour >=12 and hour <18:
        speak('Chào buổi chiều')
    elif hour >=18 and hour <21:
        speak('Chào buổi tối')
    elif hour >=21 and hour <24:
        speak('Chúc bạn ngủ ngon và có giấc mơ đẹp')
    elif hour >=0 and hour <3:
        speak('Cũng khuya rồi, bạn hãy đi ngủ để tốt cho sức khỏe nhé')
    speak('Tôi có thể giúp gì cho bạn')


rec_Bach = sr.Recognizer()
def command():
  with sr.Microphone(sample_rate=16000) as source:  
    try:
      rec_Bach.pause_threshold=1
      #rec_Bach.adjust_for_ambient_noise(source)
      print('You can start speaking now!')
      audio = rec_Bach.listen(source, phrase_time_limit=5)
      data = io.BytesIO(audio.get_wav_data())
      clip = AudioSegment.from_file(data)
      x = torch.FloatTensor(clip.get_array_of_samples())
      inputs = Bach_processor(x, sampling_rate=16000, return_tensors='pt', padding='longest').input_values
      logits = model(inputs.to(device)).logits
      tokens = torch.argmax(logits, axis=-1)
      text = Bach_processor.batch_decode(tokens)
      print('You said: ', str(text))
    except:
      pass
    return text
playsound('assets/PTNK-on.mp3')
def thực_thi_trợ_lý_ảo_STEAM_PTNK():
  while True:
    textaBach=command() #textaBach is a list, not a string
    text=''
    for x in textaBach:
      text += ' '+x #convert list to string
    if ("vi na" in text) or ("vina" in text) or ("ví na" in text) or ("vì na" in text) or ("vỉ na" in text) or ("vị na" in text) or ("vi nà" in text) or ("vi ná" in text) or ("vi nả" in text) or ("vi nạ" in text) or ("ví nạ" in text) or ("vì nà" in text) or ("vi ne" in text) or ("vì nè" in text) or ("vi nè" in text) or ("vì nạ" in text) or ("vii na" in text) or ("vin a" in text) or ("viì na" in text) or ("vií na" in text):
      answers = ["Chào bạn, tôi giúp gì được cho bạn?",
      "Tôi đây tôi đây, bạn cần tôi giúp gì?",
      "Vâng, tôi đây, tôi có thể giúp gì được cho bạn?",
      "Dạ, bạn hãy nói cho tôi bạn đang cần gì ạ. Tôi sẽ giúp đỡ bạn trong khả năng của tôi ạ",
      "Chào bạn, tôi có thể giúp bạn điều gì?"
      ]
      important_number=random.randint(1, 4)
      if important_number == 1:
          welcome()
      else:
          speak(random.choice(answers))

      
      textabach2=command()
      text2=''
      for x in textabach2:
        text2+= ' ' + x
      if ('bạn là ai' in text2) or ('vi na là' in text2) or ('vina là' in text2) or ("ví na là" in text) or ("vì na là" in text) or ("vỉ na là" in text) or ("vị na là" in text) or ("vi nà là" in text) or ("vi ná là" in text) or ("vi nả là" in text) or ("vi nạ là" in text) or ("ví nạ là" in text) or ("vì nà là" in text) or ("vin a là" in text) or ("vi ne là" in text) or ("vì nè là" in text) or ("vi nè là" in text) or ("vì nạ là" in text) or ("vii na là" in text) or ('ai tạo ra' in text2) or ('ai tạo nên' in text2) or ('ai lập trình' in text2) or ('ai đây' in text2) or ('bạn đến từ' in text2):
        answers = ["Tôi là trợ lý ảo của bạn được lập trình bởi Bách, trường Phổ thông năng khiếu, đại học quốc gia thành phố Hồ Chí Minh.",
        "Vi na là một trợ lý ảo được lập trình bởi Bách, trường Phổ thông năng khiếu, đại học quốc gia thành phố Hồ Chí Minh.",
        "Bách trường Phổ thông năng khiếu thành phố Hồ Chí Minh là người đã tạo ra trợ lý ảo vi na",
        "Theo thông tin cập nhật mới nhất, Vi na là một trợ lý ảo được lập trình bởi Bách, học trường Phổ thông năng khiếu trực thuộc đại học quốc gia thành phố hồ chí minh"
        ]
        speak(random.choice(answers))
      elif ('khỏe khôn' in text2) or ('khỏe chứ' in text2) or ('ổn không' in text2) or ('ổn chứ' in text2):
        ansz = ["Tôi cảm thấy khỏe. Tôi có thể giúp gì được cho bạn?",
        "Tôi rất khỏe, cảm ơn bạn. Vậy, giờ bạn cần tôi giúp gì?",
        "Tôi cảm thấy tuyệt vời. Tôi có thể làm gì cho bạn bây giờ?"
        ]
        speak(random.choice(ansz))
      elif ('hẹn gặp' in text2) or ('tạm biệt' in text2) or ('bái bai' in text2) or ('bai' in text2) or ('bải bai' in text2) or ('bái bài' in text2) or ('bai bài' in text2):
        speak('Vi na chuyển sang chế độ ngủ. Bạn có thể nói "vi na" để bật lại')
        playsound('assets/success.mp3')
      elif ('tắt máy' in text2) or ('tắt trợ lý' in text2) or ('tắc máy' in text2) or ('tắc trợ lý' in text2) or ('tác máy' in text2) or ('tác trợ lý' in text2) or ('tắt vi na' in text2) or ('tắc vi na' in text2) or ('tác vi na' in text2):
        speak('Vi na đã tắt. Bạn không thể nói "vi na" để gọi tôi')
        playsound('assets/Windows Notify Calendar.wav')
        quit()
      elif ('chuyện đùa' in text2) or ('chuyên đua' in text2)  or ('trò đùa' in text2) or ('truyện cười' in text2) or ('chuyện cười' in text2) or ('chuyện vui' in text2) or ('truyện vui' in text2) or ('ai lập trình' in text2) or ('ai đây' in text2) or ('chuẩn đùa' in text2) or ('chuận đùa' in text2) or ('chuyẩn đùa' in text2) or ('truyên đua' in text2) or ('chuyện đồ' in text2) or ('chuyện đò' in text2) or ('hài' in text2):
        answers = ["Kỳ thi sinh viên quốc tế năm ấy về chủ đề Lịch sử và thi vấn đáp. Một sinh viên Việt Nam học “tủ” lệch nên đành ghé vách nghe trộm. Giám thị người Liên Xô đọc đề cho một sinh viên Cuba: Anh có 3 câu hỏi. Dạ. Cách mạng Tháng Mười Nga thành công vào năm nào? Năm 1917. Do ai lãnh đạo? Do lê nin lãnh đạo. Tốt, câu hỏi phụ: Theo anh thì có ma hay không? Dạ, Nhân dân thì bảo có, Cách mạng bảo không, còn Khoa học đang nghiên cứu ạ! Tốt lắm Kha ra sô! mười điểm, về chỗ. Đến lượt sinh viên Việt Nam vào. Anh có 3 câu hỏi. Dạ. Cách mạng tháng 8 thành công năm nào, do ai lãnh đạo? Dạ năm 1917, do Lê nin lãnh đạo. Giám thị quát anh có bị làm sao không đấy? Sinh viên trả lời: Dạ, Nhân dân bảo có, Cách mạng thì bảo không, còn Khoa học đang nghiên cứu ạ!",
        "Chàng trai trở về nhà sau cuộc thi sát hạch lấy bằng lái xe với vẻ mặt hoang mang: Thật là rắc rối , Anh ta nói với ông bố : Chiếc xe tải đó có vấn đề. Vậy, Nghĩa là con bị đánh trượt? Điều đó chưa rõ. Cả Ban giám khảo có còn ai chấm được điểm đâu ạ!", 
        "Hai người bạn ngồi trong một quán bar đang kể cho nhau nghe về những giấc mơ của họ. Một người nói : Tôi mơ thấy mình đang đi nghỉ má Chỉ có tôi, cái cần câu và một cái hồ lớn tuyệt đẹp. Thật thơ mộng làm sao. Người kia kể :Tối qua, tôi cũng có một giấc mơ đẹp,  Tôi mơ thấy mình đang trong vòng tay của hai cô gái xinh đẹp và cả ba đã có một đêm thật tuyệt! Người đầu tiên mở to mắt nói: Cái gì, anh ở với hai cô gái xinh đẹp mà lại không gọi cho tôi à, thật là đồ. Ồ có chứ , Người kia trả lời:  Tôi đã gọi nhưng vợ anh nói anh đi câu cá rồi!",
        "Chàng trai nói với cô gái mà anh vừa chinh phục thành công: “Anh không uống rượu, không hút thuốc lá, không bài bạc, không lăng nhăng trai gái. Ma túy là thứ anh lánh xa. Thế nhưng, anh vẫn có một khuyết điểm nho nhỏ, em à!”  Cô gái chớp chớp mắt:  Là gì vậy, anh nói đi! Em sẵn sàng tha thứ hết. Anh có bao nhiêu ưu điểm thế cơ mà!  À! Chả là anh hay nói dối.",
        "Thấy cơ thể mình đột nhiên có nhiều thay đổi, một phụ nữ đi khám bệnh và được bác sĩ cho biết, chị đã có thai. Chị ta giận dữ mắng cho bác sĩ một trận và một mực cho rằng điều đó không thể xảy ra vì chồng mình đã đi công tác nước ngoài hơn 1 năm. Một tuần lễ sau, bệnh nhân đó lại đến phòng mạch và nhỏ nhẹ:  Thưa bác sĩ, lần trước tôi quên khuấy mất là cách đây 2 tháng chồng tôi có về phép! Ông bác sĩ tủm tỉm cười:  Nghe có vẻ khá hơn rồi đấy, nhưng cô cần nhớ kỹ lại một chút nữa, vì cái thai đã sang tháng thứ tư rồi.",
        "Một ông chồng và bà vợ đi cân, khi ông chồng bước lên, cái cân nói: “Bạn quá gầy, cần bồi dưỡng thêm”. Đến khi bà vợ lên, cái cân im lặng. Bà vợ lên lần nữa, cân vẫn im lặng. Đến khi bà bước xuống, cái cân lên tiếng:  Xin các bạn đừng chen lấn, vui lòng lên từng người một.",
        "Trông nhà ngươi giống ta như như đúc,công tước nói với một chàng trai tình cờ gặp ngoài đường. Mẹ nhà ngươi có khi nào đã từng làm người hầu trong cung điện của nhà ta hay không? Bẩm không ạ,  chàng trai được hỏi lễ phép trả lời, chỉ có cha em là đã có thời gian từng làm người quản ngựa cho quý bà sinh ra ngài thôi ạ.",
        "Trước khi xử bắn, trưởng đội thi hành án nói với tử tù: Anh được phép nói lời trăn trối cuối cùng. Tử tù rụt rè: Dạ thưa, Cán bộ cho em mặc áo chống đạn",
        "Tí nói với Tèo : Thầy tớ dạy cứ mỗi khi bị rắn cắn thì lấy dây cột chặt kế bên vết thương để chặn không cho nọc độc chạy vào người, trong khi chờ cấp cứu. Tèo hỏi: Nếu rắn cắn trúng mặt thì sao? Thì lấy dây cột cổ cho thật chặt, không để nọc độc xuống phần dưới cơ thể!",
        "Trong giờ kiểm tra môn Tiếng Việt ở Đại Học. Đề bài ra có một câu như sau Phụ nữ không có đàn ông không là gì cả và yêu cầu các sinh viên phải đặt dấu câu cho đúng. Khi chấm bài giảng viên phát hiện ra tất cả các nam sinh viên đều viết: Phụ nữ không có đàn ông, không là gì cả. Trong khi đó các nữ sinh viên thì lại viết: Phụ nữ không có, đàn ông không là gì cả. ",
        "Thầy bói xem chỉ tay một người đàn ông.  Nửa đầu cuộc đời, ông khổ sở vì thiếu tiền, sau đó… sẽ đỡ hơn nhiều.  Vì tôi sẽ kiếm ra tiền ư?  Không, vì ông sẽ quen đi.",
        "Hai anh em nói chuyện với nhau: Anh hỏi em: Nếu có một cái ôtô bằng sô cô la thì em sẽ ăn bộ phận nào trước? Em: Em sẽ chén ngay mấy cái bánh xe trước. Anh: Tại sao vậy? Em: Em phải ăn mấy cái bánh xe trước để nó không chạy được nữa. Nếu mình ăn các bộ phận khác thì xe chạy mất làm sao?"
        ]
        speak(random.choice(answers))
      elif ('giờ' in text2) or ('thời gian' in text2)  or ('mấy giơ' in text2) or ('mấy giờ' in text2) or ('mây giơ' in text2) or ('mấy giờ' in text2) or ('mẩy giờ' in text2) or ('mẩy giơ' in text2) or ('thời giản' in text2):
        time()
      elif ('ngày' in text2) or ('tháng' in text2)  or ('năm' in text2) or ('nam bao nhiêu' in text2) or ('nam gì' in text2):
        date()
      elif ('nhạc' in text2) or ('hát' in text2)  or ('bài ca' in text2) or ('bai ca' in text2) or ('mở nhạt' in text2) or ("phát nhạt" in text2) or ("thư giãn" in text2) or ("thư giản" in text2) or ("mở nhà" in text2) or ("mởi nhà" in text2) or ("mời nhà" in text2) or ("bàn nhà" in text2) or ("bạn nhà" in text2):
          answers = ["Đây là một bài nhạc bạn có thể thích, hãy tận hưởng nó",
          "Tôi nghĩ bạn sẽ thích bài nhạc này. Tôi mở nó lên ngay đây",
          "Tôi hi vọng bạn thích bài nhạc này",
          "Tôi nghĩ bài nhạc này sẽ giúp bạn cảm thấy tốt hơn"

          ]
          speak(random.choice(answers))
          decisive_number=random.randint(1, 15)#1 15
          if decisive_number == 1:
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Remember when')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Alan Jackson')
              a=os.getcwd()
              directory=(a + '\\important datas\\Alan Jackson  Remember When Official Music Video.mp3')
              os.startfile(directory)
              sleep(269) #266
          if decisive_number == 2:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Amarillo By Morning')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('George Strait')
              a=os.getcwd()
              directory=(a + '\\important datas\\Amarillo by morning lyrics.mp3')
              os.startfile(directory)
              sleep(177)
          if decisive_number == 3:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Always On My Mind')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Michael Bublé')
              a=os.getcwd()
              directory=(a + '\\important datas\\Michael Bublé  Always On My Mind HQ Music.mp3')
              os.startfile(directory)
              sleep(273)
          if decisive_number == 4:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Every Day I Love You')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Boyzone')
              a=os.getcwd()
              directory=(a + '\\important datas\\Boyzone Every Day I Love You Official Video.mp3')
              os.startfile(directory)
              sleep(213)
          if decisive_number == 5:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('You Needed Me')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Anne Murray')
              a=os.getcwd()
              directory=(a + '\\important datas\\You Needed Me by Anne Murray lyrics.mp3')
              os.startfile(directory)
              sleep(221)
          if decisive_number == 6:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Yesterday Once More')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('The Carpenters')
              a=os.getcwd()
              directory=(a + '\\important datas\\Yesterday Once More  The Carpenters.mp3')
              os.startfile(directory)
              sleep(240)
          if decisive_number == 7:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('A Thousand Years')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Christina Perri')
              a=os.getcwd()
              directory=(a + '\\important datas\\Christina Perri  A Thousand Years Lyrics.mp3')
              os.startfile(directory)
              sleep(334)
          if decisive_number == 8:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Perfect')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Ed Sheeran')
              a=os.getcwd()
              directory=(a + '\\important datas\\Ed Sheeran  Perfect Lyrics.mp3')
              os.startfile(directory)
              sleep(312)
          if decisive_number == 9:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('All of Me')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('John Legend')
              a=os.getcwd()
              directory=(a + '\\important datas\\John Legend  All of Me Lyrics.mp3')
              os.startfile(directory)
              sleep(272)
          if decisive_number == 10:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Take Me Home, Country Roads')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('John Denver')
              a=os.getcwd()
              directory=(a + '\\important datas\\John Denver  Take Me Home Country Roads Official Audio.mp3')
              os.startfile(directory)
              sleep(201)
          if decisive_number == 11:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Memories')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Maroon 5')
              a=os.getcwd()
              directory=(a + '\\important datas\\Maroon 5  Memories Official Video.mp3')
              os.startfile(directory)
              sleep(198)
          if decisive_number == 12:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Me and My Broken Heart')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Rixton')
              a=os.getcwd()
              directory=(a + '\\important datas\\Rixton  Me and My Broken Heart Official Video.mp3')
              os.startfile(directory)
              sleep(198)
          if decisive_number == 13:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Can You Feel The Love Tonight')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Elton John')
              a=os.getcwd()
              directory=(a + '\\important datas\\Elton John  Can You Feel The Love Tonight.mp3')
              os.startfile(directory)
              sleep(245)
          if decisive_number == 14:
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Bài hát là')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Never Thought That I Could Love')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('của')
              assistant_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
              PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
              speak('Dan Hill')
              a=os.getcwd()
              directory=(a + '\\important datas\\Never Thought That I Could Love  Dan Hill.mp3')
              os.startfile(directory)
              sleep(219)
          if decisive_number == 15:
              
              a=os.getcwd()
              directory=(a + '\\important datas\\5 Minute Meditation Music  with Earth Resonance Frequency for Deeper Relaxation.mp3')
              os.startfile(directory)
              sleep(310)
      elif ('tắt máy' in text2) or ('tắt trợ lý' in text2) or ('tắc máy' in text2) or ('tắc trợ lý' in text2) or ('tác máy' in text2) or ('tác trợ lý' in text2) or ('tắt vi na' in text2) or ('tắc vi na' in text2) or ('tác vi na' in text2) or ('dừng' in text2) or ('ngưng' in text2):
        speak('Vi na đã tắt. Bạn không thể nói "vi na" để gọi tôi')
        playsound('assets/Windows Notify Calendar.wav')
        quit()
      elif ('có thể làm' in text2) or ('chức năng' in text2) or ('khả năng' in text2) or ('làm được' in text2):
        speak('Tôi có thể cảnh báo căng thẳng cho bạn')
        speak('Tôi có thể mở nhạc cho bạn thư giãn')
        speak('Tôi cũng có thể mở một trò chơi nhỏ')
        speak('Với tôi, thời gian và ngày tháng năm chỉ là chuyện nhỏ. Bạn có thể hỏi tôi dễ dàng')
        speak('Khi bạn chuyển sang chế độ online, bạn có thể: tra google nhanh chóng bằng giọng nói chỉ với câu "vi na" , mở youtube, tra cứu nhiệt độ')
        speak('Và hơn hết, tôi là trợ lý ảo duy nhất Việt Nam tính đến thời điểm năm 2022 có thể nghe bạn nói khi không có internet với độ chính xác gần như tuyệt đối')  
      elif ('chơi' in text2) or ('trò chơi' in text2) or ('tro chơi' in text2):
        speak('Vi na đang mở trò chơi, xin đợi vài giây')
        os.startfile('ball.exe')
      elif ('từ điển' in text2) or ('từ điến' in text2) or ('từ điểng' in text2): 
          url=f'https://www.dict.cc/'
          wb.get().open(url)
          speak(f'Đây là từ điển tiếng anh, đức')
          url2=f'https://jdict.net/'
          speak('...')
          speak('...')
          wb.get().open(url2)
          speak('Đây là từ điển tiếng Việt, Nhật')
          url3=f'https://translate.google.com/'
          speak('...')
          speak('...')
          wb.get().open(url3)
          speak('Đây là google dịch')
          url4=f'https://www.oxfordlearnersdictionaries.com/'
          speak('...')
          speak('...')
          wb.get().open(url4)
          speak('Đây là từ điển oxford')

















    if ('tắt máy' in text) or ('tắt trợ lý' in text) or ('tắc máy' in text) or ('tắc trợ lý' in text) or ('tác máy' in text) or ('tác trợ lý' in text) or ('tắt vi na' in text) or ('tắc vi na' in text) or ('tác vi na' in text) or ('dừng' in text) or ('ngưng' in text):
      speak('Vi na đã tắt. Bạn không thể nói "vi na" để gọi tôi')
      playsound('assets/Windows Notify Calendar.wav')
      quit()
    
        
thực_thi_trợ_lý_ảo_STEAM_PTNK()



