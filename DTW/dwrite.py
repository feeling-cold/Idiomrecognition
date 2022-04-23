# coding:utf-8

with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt', 'r') as f:
    content = f.read()
    #print(content)
    #print(type(content))

    if "大好河山" in content:
        print("ok")
        with  open('C:\\Users\\凉意\\Desktop\\ASRT\\DTW\\cydict.txt', 'a') as fw:
            fw.write("\n"+"123")
            fw.close()
    f.close()
    #f.write("\n"+'../testRecordedVoice/22-1.wav  ../ASRTMFCC/22-1.mfc')
    #f.close()



"""with  open('HTK-EndPointedVoice\\ASRTlist.scp') as f:
    content = f.read()
    print(content)
    f.close()
"""