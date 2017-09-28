import re
import os



filename = "1003425004.html"#生成的html
path = 'D:/迅雷下载/视频任务组_20170927_1722/'#下载后视频存在路径

f=open(filename,'r',encoding='utf-8')
LessonName=re.findall(r'(100.*?)<',f.read())
dic = {}

for tmp in LessonName:
    url_name = tmp.split(">")
    url = re.findall(r'(100.*?.flv)',url_name[0])[0]
    name = url_name[1]
    dic[url] = name

f.close()




movie_name = os.listdir(path)
i=0
for temp in movie_name:
    i = i+1
    new_name = dic[temp]+".flv"
    os.rename(path+temp,path+str(i)+new_name)

print("done")





