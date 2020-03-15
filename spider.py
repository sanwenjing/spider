from bs4 import BeautifulSoup
import os,com


def recommend(url):
    temp = []
    html = com.getHtml(url)
    #html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html, 'html.parser')
    div = bsObj.findAll(class_='f_title')
    #print div
    for i in div:
        #print i.a.attrs["href"]
        temp.append(i.a.attrs["href"])
        #print i.a.string
        #print i.a.text
    return temp
        
def recommend2(url):
    temp = []
    html = com.getHtml(url)
    #html.encoding = 'utf-8'
    bsObj = BeautifulSoup(html, 'html.parser')
    div = bsObj.findAll(class_='t_msgfont')
    if div:
      #print div
      for i in div[0].img.findAll("img"):
        temp.append(i.attrs["src"])
      return temp

def downImg(url,urlfix,path):
    #Note:url code must transferred
    for index,url3 in enumerate(recommend(url)):
        print index
        pageurl=urlfix+url3
        print pageurl
        #path="C:\Users\Administrator\Desktop\\test"
        os.system("mkdir {path}".format(path=path))
        path2="{path}\{index}".format(path=path,index=index)
        os.system("mkdir {path}".format(path=path2))
        #print recommend2(pageurl)
        for i,imgurl in enumerate(recommend2(pageurl)):
            os.system("start curl -o {path}\{index}.jpg {url}".format(path=path2,index=i,url=imgurl)) 



if __name__ == '__main__':
    print "hello!"
    url=""
    #print recommend(url)
    downImg(url,"","C:\Users\Administrator\Desktop\\test3")

