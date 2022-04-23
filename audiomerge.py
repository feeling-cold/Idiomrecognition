from pydub import AudioSegment

def audiomerge(a):
    parameters = None
    input_music_1 = AudioSegment.from_wav("1.wav")
    input_music_2 = AudioSegment.from_wav("2.wav")
    input_music_3 = AudioSegment.from_wav("3.wav")
    input_music_4 = AudioSegment.from_wav("4.wav")

    # 获取两个音频的响度（音量）
    input_music_1_db = input_music_1.dBFS
    input_music_2_db = input_music_2.dBFS
    input_music_3_db = input_music_3.dBFS
    input_music_4_db = input_music_4.dBFS

    # 获取两个音频的时长，单位为毫秒
    input_music_1_time = len(input_music_1)
    input_music_2_time = len(input_music_2)
    input_music_3_time = len(input_music_3)
    input_music_4_time = len(input_music_4)
    # 调整两个音频的响度一致

    # 合并音频
    output_music = input_music_1 + input_music_2 + input_music_3 + input_music_4
    # 简单输入合并之后的音频
    output_music.export("C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\ASRTrecordvoice\\"+str(a)+".wav", format="wav")  # 前面是保存路径，后面是保存格式

'''
print(len(output_music), output_music.channels)  # 合并音频的时长，音频的声道，1是单声道，2是立体声
'''