from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
import csv
import time
import mysql.connector as msql


# SETTING UP DATE AND TIME #


time1=[]
datetimeObj=datetime.now()
date1 = datetimeObj.strftime("%d-%b-%Y")
time1 = datetimeObj.strftime("%H:%M:%S")
print("\n\n",date1,time1)
dt=date1+" "+time1


# WEB SCRAPPING #

indian=requests.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen').text

il=[]
a=1
it1=time.time()
indsoup = BeautifulSoup(indian,'lxml')
indnews = indsoup.find("div",class_="lBwEZb BL5WZb GndZbb")
print("\n\n")
print(" INDIAN ".center(150,'='))
print("\n\n")
for i in indnews:
    in_=i.h3.text
    in__=(a,".",in_,'\n')
    print(a,'.',in_,'\n')
    il.append(in_)
    a+=1
it2=time.time()
it=it2-it1
#print(it)
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" WORLD ".center(150,'='))
print("\n\n")

wl=[]
wt1=time.time()
world=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text

b=1
wrldsoup=BeautifulSoup(world,'lxml')
wrldnews=wrldsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for j in wrldnews:
    w=j.h3.text
    print(b,'.',w,'\n')
    wl.append(w)
    b+=1
wt2=time.time()
wt=wt2-wt1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" BUSSINESS ".center(150,'='))
print("\n\n")

bt1=time.time()
bl=[]
buss=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text

c=1
busssoup=BeautifulSoup(buss,'lxml')
bussnews=busssoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for k in bussnews:
    bn_=k.h3.text
    print(c,'.',bn_,'\n')
    bl.append(bn_)
    c+=1
bt2=time.time()
bt=bt2-bt1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" TECH ".center(150,'='))
print("\n\n")

tl=[]
tt1=time.time()
tech=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text

d=1
techsoup=BeautifulSoup(tech,'lxml')
technews=techsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for x in technews:
    tn=x.h3.text
    print(d,'.',tn,'\n')
    tl.append(tn)
    d+=1
tt2=time.time()
tt=tt2-tt1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" ENTERTAINMENT ".center(150,'='))
print("\n\n")

el=[]
et1=time.time()
ent=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text

e=1
entsoup=BeautifulSoup(ent,'lxml')
entnews=entsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for y in entnews:
    en=y.h3.text
    print(e,'.',en,'\n')
    el.append(en)
    e+=1
et2=time.time()
et=et2-et1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" SPORTS ".center(150,'='))
print("\n\n")
sl=[]
st1=time.time()
srt=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text
st=time.time()
f=1
srtsoup=BeautifulSoup(srt,'lxml')
srtnews=srtsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for z in srtnews:
    sn=z.h3.text
    print(f,'.',sn,'\n')
    sl.append(sn)
    f+=1
st2=time.time()
st=st2-st1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" SCIENCE ".center(150,'='))
print("\n\n")
scl=[]
scn=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen').text
sct1=time.time()
g=1
scnsoup=BeautifulSoup(scn,'lxml')
scnnews=scnsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for i_ in scnnews:
    scn_=i_.h3.text
    print(g,'.',scn_,'\n')
    scl.append(scn_)
    g+=1
sct2=time.time()
sct=sct2-sct1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))

print("\n\n")
print(" HEALTH ".center(150,'='))
print("\n\n")
hl=[]
hlt=requests.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen').text
ht1=time.time()
f=1
hltsoup=BeautifulSoup(hlt,'lxml')
hltnews=hltsoup.find('div',class_='lBwEZb BL5WZb GndZbb')
for j_ in hltnews:
    hln_=j_.h3.text
    print(f,'.',hln_,'\n')
    hl.append(hln_)
    f+=1
ht2=time.time()
ht=ht2-ht1
print("\n\n")
print("======".center(150,'='))
print("======".center(150,'='))


# SAVING THE SCRAPED NEWS IN A TEXTFILE #


f_=open('Newsfeed.txt','w',encoding="utf-8")
f_.write(dt+"\n\n")
f_.write(" INDIAN NEWS ".center(150,"=")+"\n\n")
for l in il:
   f__=f_.write(l+"\n\n")
f_.write(" WORLD NEWS ".center(150,"=")+"\n\n")
for l_ in wl:
    f_f=f_.write(l_+"\n\n")
f_.write(" BUSINESS NEWS ".center(150,"=")+"\n\n")
for l__ in bl:
    f__f=f_.write(l__+"\n\n")
f_.write(" TECH NEWS ".center(150,"=")+"\n\n")
for rl in tl:
    f___=f_.write(rl+"\n\n")
f_.write(" ENTERTAINMENT NEWS ".center(150,"=")+"\n\n")
for rl_ in el:
    fl=f_.write(rl_+"\n\n")
f_.write(" SPORT NEWS ".center(150,"=")+"\n\n")
for rl___ in sl:
    fl_=f_.write(rl___+"\n\n")
f_.write(" SCIENCE NEWS ".center(150,"=")+"\n\n")
for kl in scl:
    fl__=f_.write(kl+"\n\n")
f_.write(" HEALTH NEWS ".center(150,"=")+"\n\n")
for kl_ in hl:
    fl___=f_.write(kl_+"\n\n")
f_.write("=".center(150,"=")+"\n\n")
f_.close()


# SAVING ANALYSIS AS COMMA-SEPERATED VALUE (CSV) FILE #


def extractDigits(lst):
    return [[el] for el in lst]
                  
il=extractDigits(il)
wl=extractDigits(wl)
bl=extractDigits(bl)
tl=extractDigits(tl)
el=extractDigits(el)
sl=extractDigits(sl)
scl=extractDigits(scl)
hl=extractDigits(hl)

header=["S.no","Date & Time","News Category","No. of Headlines Scraped","Time taken for Scraping"]
indianiii=[1,dt,"Indian News",(a-1),it]
worldiii=[2,dt,"World News",(b-1),wt]
bussinessiii=[3,dt,"Business News",(c-1),bt]
techiii=[4,dt,"Tech News",(d-1),tt]
entiii=[5,dt,"Entertainment News",(e-1),et]
sportiii=[6,dt,"Sport News",(f-1),st]
scieiii=[7,dt,"Science News",(g-1),sct]
hlthiii=[8,dt,"Health News",(f-1),ht]

with open("Newsfeed Analysis.csv","w",encoding="utf-8")as x:
    data=csv.writer(x)
    data.writerow(header)
    data.writerow(indianiii)
    data.writerow(worldiii)
    data.writerow(bussinessiii)
    data.writerow(techiii)
    data.writerow(entiii)
    data.writerow(sportiii)
    data.writerow(scieiii)
    data.writerow(hlthiii)


# UPLOADING THE ANALYSIS IN THE DATABASE #


fl=[]
with open("Newsfeed Analysis.csv",'r',encoding='utf-8') as y:
    datax=csv.reader(y)
    for i in datax:
        if i==[]:
            pass
        else:
            fl.append(i)


conn = msql.connect(host='localhost', database='internship', user='root', password='12345')
cur=conn.cursor()
try:
    print("news table is being created....")
    time.sleep(5);
    cur.execute("CREATE TABLE newsfeed (S_No varchar(6) NOT NULL,\
               Date_Time varchar(100) not null,\
               News_Category varchar(100) not null,\
               Headline_count varchar(4) not null,\
               Time_taken_S varchar(200) not null)")
    print("news table is created....")
    for iii in fl[1:]:
        iii_=tuple(iii)
        print(iii_)
        cur.execute("insert into newsfeed values{}".format(iii_))
    print("Hold on! Your news analysis are being uploaded in the database...")
    time.sleep(5)
    ss=("-","-","-","-","-")
    cur.execute("insert into newsfeed values{}".format(ss))
    print("Records uploaded successfully...")
    conn.commit()


except:
    for iii in fl[1:]:
        iii_=tuple(iii)
        print(iii_)
        cur.execute("insert into newsfeed values{}".format(iii_))
    print("Hold on! Your news analysis are being uploaded in the database...")
    time.sleep(5)
    ss=("-","-","-","-","-")
    cur.execute("insert into newsfeed values{}".format(ss))
    print("Record uploaded successfully...")
    conn.commit()

