import os
import tkinter
import wave
from threading import Thread
from tkinter import *
import tkinter.messagebox

import pyaudio
import pyttsx3
import winsound

import alg_tts
from DTW.cytolist import cytolist
from DTW.rec import DTWrec
from DTW.record import save_wave_file
from sql import sqlmean

def dtwplayaudio(output,mean):
    alg_tts.init()
    alg_tts.ttsSpeak(output)
    alg_tts.ttsSpeak("解释是" + mean)

def windtwplayaudio():
    filename = 'C:\\Users\\凉意\\Desktop\\ASRT\\ttswave\\DTWtts.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)


class DWTWindow:
    def __init__(self, win, ww, wh):
        self.win = win
        self.ww = ww
        self.wh = wh
        self.win.title("DTW成语识别系统")
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, 200, 50))
        self.img_src_path = None



        self.textlabe = Label(text="DTW成语识别系统", fg="white", bg='black', font=("微软雅黑", 21))
        self.textlabe.place(x=385, y=35)

        self.text = Text(height=20, width=50)
        self.text.place(x=325, y=130)

        """
        self.button1 = Button(self.win, text='DTW入口', width=10, height=2, command=self.dtw)
        self.button1.place(x=645, y=35)
        
        self.button3 = Button(self.win, text='录取音频', width=10, height=2, command=self.spilt)
        self.button3.place(x=325, y=450)
        
        
        self.button5 = Button(self.win, text='<<', width=3, height=1, command=self.back)
        self.button5.place(x=10, y=10)
        
        """

        self.button1 = Button(self.win, text='提取特征', width=10, height=2, command=self.train)
        self.button1.place(x=275, y=450)

        self.button2 = Button(self.win, text='智能识别', width=10, height=2, command=self.speechrec)
        self.button2.place(x=535, y=450)

        self.button3 = Button(self.win, text='录取音频', width=10, height=2, command=self.record)
        self.button3.place(x=405, y=450)

        self.button4 = Button(self.win, text='查看词库', width=10, height=2, command=self.database)
        self.button4.place(x=665, y=450)

    """
    def back(self):
        win.destroy()

        GUItk = Tk()
        ww = 1000
        wh = 600
        img_gif = tkinter.PhotoImage(file="3.gif")
        label_img = tkinter.Label(GUItk, image=img_gif, width="1000", height="600")
        label_img.place(x=0, y=0)
        srWindow(GUItk, ww, wh)
        screenWidth, screenHeight = GUItk.maxsize()
        geometryParam = '%dx%d+%d+%d' % (
            ww, wh, (screenWidth - ww) / 2, (screenHeight - wh) / 2)
        GUItk.geometry(geometryParam)
        GUItk.resizable(False, False)
        GUItk.mainloop()
        
    """

    def record(self):
        framerate = 16000
        channels = 1
        sampwidth = 2

        CHUNK = 1024
        RATE = 16000
        RECORD_SECONDS = 8

        frames = []
        tkinter.messagebox.showinfo("提示", "录制开始")
        print("录音开始,请说话!!!")
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pyaudio.paInt16, channels=1, \
                         rate=framerate, input=True, \
                         frames_per_buffer=CHUNK)
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("录音结束,请停止说话!!!")
        save_wave_file('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\RecordedVoice-RealTime\\recordedVoice_before.wav', frames)
        tkinter.messagebox.showinfo("提示","录制成功")

    def train(self):

        os.chdir("C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\HTK-EndPointedVoice")
        os.system("hcopy -A -D -T 1 -C tr_wav.cfg -S .\ASRTlist.scp")
        os.chdir("C:\\Users\\凉意\\Desktop\\ASRT")
        tkinter.messagebox.showinfo('提示', '提取完成')

    def database(self):

        with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt', 'r') as f:
            content = f.read()
            # print(content)
            # print(type(content))
            f.close()

        self.text.delete('1.0', 'end')
        self.text.insert('end',content)


    def speechrec(self):
        alg_tts.init()
        path = 'C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\ASRTrecordvoice'
        files = os.listdir(path)
        num = len(files)
        flag = DTWrec(num)
        #print(flag)

        list = cytolist()
        #print(list)

        self.cy = list[flag]
        self.mean = sqlmean(self.cy)
        self.text.delete('1.0', 'end')
        self.text.insert('end', self.cy + "\n" + "【释义】：" + "\n" + self.mean)

        alg_tts.ttsSaveToFile(self.cy + "释义是" + self.mean, "C:\\Users\\凉意\\Desktop\\ASRT\\ttswave\\DTWtts.wav")

        tnd = Thread(target=windtwplayaudio)
        tnd.start()

        """
        
        filename = 'C:\\Users\\凉意\\Desktop\\ASRT\\ttswave\\DTWtts.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        
        tnd = Thread(target=dtwplayaudio, args=(self.cy, self.mean))
        tnd.start()
        
        """

if __name__ == '__main__':
    win = Tk()
    ww = 1000
    wh = 600
    img_gif = tkinter.PhotoImage(file="3.gif")
    label_img = tkinter.Label(win, image=img_gif, width="1000", height="600")
    label_img.place(x=0, y=0)
    #menubar = Menu(win)
    #filemenu = Menu(win, tearoff=0)
    #menubar.add_cascade(label='返回', menu=filemenu)
    #win.config(menu=menubar)
    DWTWindow(win, ww, wh)
    screenWidth, screenHeight = win.maxsize()
    geometryParam = '%dx%d+%d+%d' % (
        ww, wh, (screenWidth - ww) / 2, (screenHeight - wh) / 2)
    win.geometry(geometryParam)
    win.resizable(False, False)
    win.mainloop()
