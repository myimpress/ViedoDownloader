import re
import os



htmlfilename = "1003425004.html"#生成的html

f=open(htmlfilename,'r',encoding='utf-8')
LessonName=re.findall(r'href="(.*?a)">',f.read())
f.close()



txtfilename = "xunlei.txt"
with open(txtfilename,'a',encoding='utf-8') as of:
    for tmp in LessonName:
        of.write(tmp+"\r\n")










