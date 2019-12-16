# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:32:20 2019

@author: zyb32
"""
import pyaudio
import wave
from aip import AipSpeech
from constants import APP_ID,API_KEY,SECRET_KEY

# 用Pyaudio库录制音频
#   out_file:输出音频文件名
#   rec_time:音频录制时间(秒)
def AudioRecord(out_file, rec_time):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16 #16bit编码格式
    CHANNELS = 1 #单声道
    RATE = 16000 #16000采样频率
    
    p = pyaudio.PyAudio()
    # 创建音频流 
    stream = p.open(format=FORMAT, # 音频流wav格式
                    channels=CHANNELS, # 单声道
                    rate=RATE, # 采样率16000
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start Recording...")

    frames = [] # 录制的音频流
    # 录制音频数据
    for i in range(0, int(RATE / CHUNK * rec_time)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    # 录制完成
    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Recording Done...")

    # 保存音频文件
    wf = wave.open(out_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()


def AipRecognize(file,fmt="pcm",devpid=1737):
    client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    result = client.asr(get_file_content(file),fmt,16000,{"dev_pid":devpid})
    if result["err_msg"] == "success.":
        return result["result"]
    else:
        return ""

"""
def preTrain(folder,names,labels,fmt="pcm",sample_time=2):
    os.makedirs(filepath0+folder)
    filepath = filepath0 + folder + "//"
    N = len(names)
    if len(labels)!=N :
        raise ValueError
        return
    training_data = dict(zip(names,labels))
    
    print("Are you ready to record?\n[y]/n\n")
    user_ans = input()
    if user_ans=="n":
        return
    
    text_name = filepath + "training_data.txt"
    for i in range(N):
        audio_name = filepath + names[i] + "."+fmt
        print("\n")
        print(names[i]+"."+fmt)
        print("\n----------------------------------\n")
        AudioRecord(audio_name,sample_time)
        
    
    with open(text_name,"w") as f:
        for key in training_data.keys():
            f.write(key+"."+fmt)
            f.write("\t")
            f.write(training_data[key])
            f.write("\n")
    
    print("\nSample Collection Complished\n")
"""