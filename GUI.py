import os
import tkinter
import wave
from tkinter import *
import tkinter.messagebox
import pyttsx3
import winsound

import alg_tts
from DTWGUI import DWTWindow
from audiomerge import audiomerge
from predict_speech_file import get_output, useget_output
from speech_recorder import record_wave
from threading import Thread

def playaudio(output,mean):
    alg_tts.init()
    alg_tts.ttsSpeak(output)
    alg_tts.ttsSpeak("解释是" + mean)

def winplayaudio():
    filename = 'C:\\Users\\凉意\\Desktop\\ASRT\\ttswave\\tts.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

class srWindow:
    def __init__(self, win, ww, wh):
        self.win = win
        self.ww = ww
        self.wh = wh
        self.win.title("智能成语识别系统")
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, 200, 50))
        self.img_src_path = None

        self.textlabe = Label(text="智能成语识别系统", fg="white", bg='black', font=("微软雅黑", 21))
        self.textlabe.place(x=385, y=35)

        self.text = Text(height=20, width=50)
        self.text.place(x=325, y=130)

        self.button1 = Button(self.win, text='DTW入口', width=10, height=2, command=self.dtw)
        self.button1.place(x=665, y=450)

        self.button3 = Button(self.win, text='录取音频', width=10, height=2, command=self.spilt)
        self.button3.place(x=275, y=450)

        self.button2 = Button(self.win, text='智能识别', width=10, height=2, command=self.speechrec)
        self.button2.place(x=405, y=450)

        self.button4 = Button(self.win, text='录入词库', width=10, height=2, command=self.write)
        self.button4.place(x=535, y=450)

    def dtw(self):

        win.destroy()

        dtwwin = Tk()
        ww = 1000
        wh = 600
        img_gif = tkinter.PhotoImage(file="3.gif")
        label_img = tkinter.Label(dtwwin, image=img_gif, width="1000", height="600")
        label_img.place(x=0, y=0)
        DWTWindow(dtwwin, ww, wh)
        screenWidth, screenHeight = dtwwin.maxsize()
        geometryParam = '%dx%d+%d+%d' % (
            ww, wh, (screenWidth - ww) / 2, (screenHeight - wh) / 2)
        dtwwin.geometry(geometryParam)
        dtwwin.resizable(False, False)
        dtwwin.mainloop()

    def write(self):

        #output, mean = useget_output()

        with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt', 'r') as fr:
            content = fr.read()
            if self.output not in content:

                path = 'C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\ASRTrecordvoice'
                files = os.listdir(path)
                num = len(files)
                # print(num)

                audiomerge(num + 1)
                tkinter.messagebox.showinfo('提示', '音频存储成功')

                with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt', 'a') as f:
                    f.write("\n"+self.output)
                    f.close()

                with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\HTK-EndPointedVoice\\ASRTlist.scp', 'a') as f:
                    f.write("\n" + '../ASRTrecordvoice/' + str(num + 1) + '.wav  ../ASRTMFCC/' + str(num + 1) + '.mfc')
                    f.close()

            else:
                tkinter.messagebox.showinfo("提示","词库已存在本成语")

            fr.close()




    """
    def start(self):
        from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

        parser = ArgumentParser(description='Simple Wave Audio Recorder',
                                formatter_class=ArgumentDefaultsHelpFormatter)
        parser.add_argument('-d', '--duration', type=int,
                            default=5, help='maximum duration in seconds')
        parser.add_argument('-r', '--sampling-rate', type=int,
                            default=16000, help='sampling rate')
        parser.add_argument('-b', '--sampling-bits', type=int,
                            default=16, choices=(8, 16, 24, 32), help='sampling bits')
        parser.add_argument('-c', '--channels', type=int,
                            default=1, help='audio channels')
        parser.add_argument('output', nargs='?', default='5.wav',
                            help='audio file to store audio stream')
        args = parser.parse_args()
        tkinter.messagebox.showinfo('提示', '5.wav开始录制')
        record_wave(args.output, duration=args.duration,
                    channels=args.channels,
                    sampling_bits=args.sampling_bits,
                    sampling_rate=args.sampling_rate)

        tkinter.messagebox.showinfo('提示', '5.wav存储成功')
    """

    def spilt(self):
        from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

        for i in range(4):

            parser = ArgumentParser(description='Simple Wave Audio Recorder',
                                    formatter_class=ArgumentDefaultsHelpFormatter)
            parser.add_argument('-d', '--duration', type=int,
                                default=2, help='maximum duration in seconds')
            parser.add_argument('-r', '--sampling-rate', type=int,
                                default=16000, help='sampling rate')
            parser.add_argument('-b', '--sampling-bits', type=int,
                                default=16, choices=(8, 16, 24, 32), help='sampling bits')
            parser.add_argument('-c', '--channels', type=int,
                                default=1, help='audio channels')

            """
            
            parser.add_argument('output', nargs='?', default='C:\\Users\\凉意\\Desktop\\ASRT\\testrecord\\89-'+str(i + 1) + '.wav',
                                help='audio file to store audio stream')
            """
            parser.add_argument('output', nargs='?', default=str(i+1)+'.wav',
                                help='audio file to store audio stream')

            args = parser.parse_args()

            #tkinter.messagebox.showinfo('提示', str(i + 1)+'.wav'+'开始录制')

            record_wave(args.output, duration=args.duration,
                        channels=args.channels,
                        sampling_bits=args.sampling_bits,
                        sampling_rate=args.sampling_rate)

        tkinter.messagebox.showinfo('提示', '音频存储成功')

    def speechrec(self):
        alg_tts.init()
        self.text.delete('1.0','end')
        self.output,self.mean = useget_output()
        self.text.insert('end',self.output+"\n"+"【释义】："+"\n"+self.mean)

        alg_tts.ttsSaveToFile(self.output + "释义是" + self.mean, "C:\\Users\\凉意\\Desktop\\ASRT\\ttswave\\tts.wav")

        tnd = Thread(target=winplayaudio)
        tnd.start()
        """
        tnd = Thread(target=playaudio,args=(self.output,self.mean))
        tnd.start()
    
        """

if __name__ == '__main__':
    win = Tk()
    ww = 1000
    wh = 600
    img_gif = tkinter.PhotoImage(file="3.gif")
    label_img = tkinter.Label(win, image=img_gif, width="1000", height="600")
    label_img.place(x=0, y=0)
    srWindow(win, ww, wh)
    screenWidth, screenHeight = win.maxsize()
    geometryParam = '%dx%d+%d+%d' % (
        ww, wh, (screenWidth - ww) / 2, (screenHeight - wh) / 2)
    win.geometry(geometryParam)
    win.resizable(False, False)
    win.mainloop()
