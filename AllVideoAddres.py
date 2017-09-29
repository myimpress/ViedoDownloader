import re
import os



filename = "1004014054.html"#生成的html
path = 'D:/迅雷下载/视频任务组_20170927_1730/'#下载后视频存在路径

f=open(filename,'r',encoding='utf-8')
LessonName=re.findall(r'(100.*?)<',f.read())
dic = {}
i=0
for tmp in LessonName:
    i = i+1

    url_name = tmp.split(">")
    url = re.findall(r'(100.*?.flv)',url_name[0])[0]
    name = url_name[1]
    dic[url] = str(i)+name

f.close()



movie_name = os.listdir(path)

for temp in movie_name:
    new_name = dic[temp]+".flv"
    os.rename(path+temp,path+new_name)

print("done")


