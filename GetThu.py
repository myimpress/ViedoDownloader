import re
import os


def getThu(html):
	htmlfilename = html#生成的html
	htmlid = html.split(".")[0]

	f=open(htmlfilename,'r',encoding='utf-8')
	LessonName=re.findall(r'href="(.*?a)">',f.read())
	f.close()



	txtfilename = htmlid+"xunlei.txt"
	with open(txtfilename,'a',encoding='utf-8') as of:
	    for tmp in LessonName:
	        of.write(tmp+"\r\n")
	print("done")


if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"}
    print("基于网易云课堂视频下载工具V1.2 beta1 Author:Lz1y 提取所有链接迅雷下载")
    print("Author:wen")

    
    html = input("\n请输入html文件名:\n")
    getThu(html)






