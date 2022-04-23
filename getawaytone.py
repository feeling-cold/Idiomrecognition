import unicodedata
mystr="dān móu lù lì"
res=unicodedata.normalize('NFKD', mystr).encode('ascii','ignore')
#print((res.decode()).replace(" ",""))
