from bs4 import BeautifulSoup #this is going to makeit work

with open("a21basic.html",'r') as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content,'lxml')
    #soup.prettify() #if you want formatting..
    tags=soup.findAll('span',class_='empdet')
    for tag in tags:
        print(tag.text)




#have a look at
#https://github.com/J4NN0/linkedin-web-scraper
#https://www.youtube.com/watch?v=XVv6mJpFOb0










