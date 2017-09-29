import re
import os


def rename(html,path):
	filename = html#生成的html
	path = path#下载后视频存在路径

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




if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"}
    print("基于网易云课堂视频下载工具V1.2 beta1 Author:Lz1y 修改下载视频名称")
    print("Author:wen")

    
    html = input("\n请输入html文件名:\n")
    path = input("\n请输视频地址:\n")
    rename(html,path)
