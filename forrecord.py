# -*- coding: utf-8 -*-

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from speech_recorder import record_wave

from accuarcy import prelist, ASRTlist
from predict_speech_file import get_output, ASRT


"""

a = 90
goon = 1
while(goon):
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

        parser.add_argument('output', nargs='?',
                            default='C:\\Users\\凉意\\Desktop\\ASRT\\testrecord\\'+str(a)+'-' + str(i + 1) + '.wav',
                            help='audio file to store audio stream')
       
        args = parser.parse_args()

        # tkinter.messagebox.showinfo('提示', str(i + 1)+'.wav'+'开始录制')

        record_wave(args.output, duration=args.duration,
                    channels=args.channels,
                    sampling_bits=args.sampling_bits,
                    sampling_rate=args.sampling_rate)

    print(str(a) + "ok")
    a = a+1


    print("go on ?")
    goon = input("please input goon")
  """

prelist = []
ASRTlist = []

for i in range(95,101):
    cy, mean, oldres= get_output(i)
    prelist.append(cy)
    oldres = ASRT(i)
    ASRTlist.append(oldres)
#print(ASRTlist)
print(prelist)

