#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from LanguageModel2 import ModelLanguage
from speech_features import Spectrogram
from speech_model import ModelSpeech
from speech_model_zoo import SpeechModel251
from sql import sql, sqlmean, onesql, aftersql
from distancedemo import string_similar

"""
def beforepredict():
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    AUDIO_LENGTH = 1600
    AUDIO_FEATURE_LENGTH = 200
    CHANNELS = 1
    OUTPUT_SIZE = 1428
    sm251 = SpeechModel251(
        input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
        output_size=OUTPUT_SIZE
    )
    feat = Spectrogram()
    ms = ModelSpeech(sm251, feat, max_label_length=64)

    ms.load_model('save_models/' + sm251.get_model_name() + '.model.h5')
    # print('save_models/' + sm251.get_model_name() + '.model.h5')
    # res = ms.recognize_speech_from_file('E://4.wav')
    # print(res)
    res = ms.recognize_speech_from_file('5.wav')
    #res = ms.recognize_speech_from_file('C:\\Users\\凉意\\Documents\\SpeakerRecord\\1-5.wav')
    print(res)


    ml = ModelLanguage('model_language')
    ml.LoadModel()
    str_pinyin = res
    oldres = ml.SpeechToText(str_pinyin)
    print(oldres)

    string = ""
    for i in res:
        string = string + i
    newstring = ''.join([i for i in string if not i.isdigit()])

    #onepre = sql(newstring,res)

    #print(onepre)

    return newstring

"""

def ASRT(a):
    list = []
    for j in range(4):

        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        AUDIO_LENGTH = 1600
        AUDIO_FEATURE_LENGTH = 200
        CHANNELS = 1
        OUTPUT_SIZE = 1428
        sm251 = SpeechModel251(
            input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
            output_size=OUTPUT_SIZE
        )
        feat = Spectrogram()
        ms = ModelSpeech(sm251, feat, max_label_length=64)
        ms.load_model('save_models/' + sm251.get_model_name() + '.model.h5')

        res = ms.recognize_speech_from_file('testrecord\\' + str(a) + '-' + str(j + 1) + '.wav')
        #res = ms.recognize_speech_from_file(str(j + 1) + '.wav')
        list += res
        # print(list)

    ml = ModelLanguage('model_language')
    ml.LoadModel()
    str_pinyin = list
    oldres = ml.SpeechToText(str_pinyin)
    # print('ASRT原识别结果:'+oldres)

    return oldres

def afterpredict(a):
    list = []
    for j in range(4):

        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        AUDIO_LENGTH = 1600
        AUDIO_FEATURE_LENGTH = 200
        CHANNELS = 1
        OUTPUT_SIZE = 1428
        sm251 = SpeechModel251(
            input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
            output_size=OUTPUT_SIZE
        )
        feat = Spectrogram()
        ms = ModelSpeech(sm251, feat, max_label_length=64)
        ms.load_model('save_models/' + sm251.get_model_name() + '.model.h5')

        res = ms.recognize_speech_from_file('testrecord\\'+str(a)+'-' + str(j + 1) + '.wav')
        #res = ms.recognize_speech_from_file(str(j + 1) + '.wav')
        list += res
        #print(list)

        string = ""
        for i in list:
            string = string + i
        newstring = ''.join([i for i in string if not i.isdigit()])

        #print(newstring)

    ml = ModelLanguage('model_language')
    ml.LoadModel()
    str_pinyin = list
    oldres = ml.SpeechToText(str_pinyin)
    #print('ASRT原识别结果:'+oldres)

    return newstring, list ,oldres

def get_output(a):


    s2, prelist ,oldres = afterpredict(a)
    #print("s2 为"+s2)

    s1, cy= onesql(s2)
    #print(s1)
    #print("s1 为"+s1)

    #print(prelist)
    #print(string_similar(s1, s2))


    if string_similar(s1, s2) >= 0.7:
        if len(prelist) != 4:
            output = cy
            mean = sqlmean(output)
            #print(output)
            #print(mean)
            #return output

        else:
            output = aftersql(s2, prelist)
            mean = sqlmean(output)
            #print(output)
            #print(mean)

    else:
        warning = "录音不准确，请重新录音"
        print("录音不准确，请重新录音")

    return output, mean ,oldres


"""
cy, mean, oldres= get_output(7)
print(cy)


ASRTlist = []
prelist = []

for i in range(1,31):
    cy, mean, oldres= get_output(i)
    prelist.append(cy)

    oldres = ASRT(i)
    ASRTlist.append(oldres)

print(prelist)
print(ASRTlist)



for i in range(1,21):
   cy, mean, oldres= get_output(i)
   prelist.append(cy)
   ASRTlist.append(oldres)

print(prelist)
"""


#print(cy)
#print(mean)
#get_output()

def useafterpredict():
    list = []
    for j in range(4):

        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        AUDIO_LENGTH = 1600
        AUDIO_FEATURE_LENGTH = 200
        CHANNELS = 1
        OUTPUT_SIZE = 1428
        sm251 = SpeechModel251(
            input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
            output_size=OUTPUT_SIZE
        )
        feat = Spectrogram()
        ms = ModelSpeech(sm251, feat, max_label_length=64)
        ms.load_model('save_models/' + sm251.get_model_name() + '.model.h5')

        #res = ms.recognize_speech_from_file('C:\\Users\\凉意\\Desktop\\ASRT\\testrecord\\89-'+str(j+1)+'.wav')
        res = ms.recognize_speech_from_file(str(j + 1) + '.wav')
        list += res
        #print(list)

        string = ""
        for i in list:
            string = string + i
        newstring = ''.join([i for i in string if not i.isdigit()])

        # print(newstring)

    ml = ModelLanguage('model_language')
    ml.LoadModel()
    str_pinyin = list
    oldres = ml.SpeechToText(str_pinyin)
    # print('ASRT原识别结果:'+oldres)

    return newstring, list

def useget_output():
    s2, prelist = useafterpredict()
    #print("s2 为"+s2)

    s1, cy = onesql(s2)
    #print(s1)
    #print("s1 为" + s1)

    #print(prelist)
    #print(string_similar(s1, s2))

    if string_similar(s1, s2) >= 0.7:
        if len(prelist) != 4:
            output = cy
            mean = sqlmean(output)
            # print(output)
            # print(mean)
            # return output

        else:
            output = aftersql(s2, prelist)
            mean = sqlmean(output)
            # print(output)
            # print(mean)

    else:
        output = "录音不准确，请重新录音"
        mean = "无"
        print("录音不准确，请重新录音")

    return output, mean