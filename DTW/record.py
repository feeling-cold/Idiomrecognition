import wave

import pyaudio

framerate = 16000  # 采样频率 16000
channels = 1       # 声道数
sampwidth = 2

CHUNK = 1024         # 录音的块大小
RATE = 16000         # 采样频率 16000
RECORD_SECONDS = 8
#print("开始录音,请说话......")
def save_wave_file(filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)   # 声道
    wf.setsampwidth(sampwidth)  # 采样字节 1 or 2
    wf.setframerate(framerate)  # 采样频率 8000 or 16000
    wf.writeframes(b"".join(data))
    wf.close()

frames = []
pa = pyaudio.PyAudio()
stream = pa.open(format = pyaudio.paInt16, channels = 1, \
                       rate = framerate ,    input = True, \
                       frames_per_buffer = CHUNK)
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

#print("录音结束,请停止说话!!!")
#save_wave_file('testRecordedVoice-RealTime/recordedVoice_before.wav', frames)
