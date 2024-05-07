# 2024.04.01
CLI - Command Line Interface 
 
 - Port  22 
  - telnet 
  -> ssh 

GUI - Graphic User Interface 


# 디렉토리 변경 
# cd 
cd ~ 

# pwd 
# 현재 폴더 위치 

# 폴더 생성 
mkdir workspace 


sudo apt update
sudo apt install python3-pip 
sudo apt install python3-pip  -y

# jupyter 설치하기 
pip install jupyter 

# vs code 설치하기 
https://code.visualstudio.com/docs/?dv=win64user

# vs code 실행 
extensions -> wsl 설치 

f1 -> connect to wsl 





text3 = "오늘도 아침엔 입에 빵을 물고"

text4 = """오늘도 아침엔 입에 빵을 물고
똑같이 하루를 시작하고
온종일 한 손엔 아이스 아메리카노
피곤해 죽겠네

지하철 속 이 장면 어제 꿈에서 봤나
아참 매일이지 지나치고
바쁜 이 삶에 그냥 흔한 날에
그 애를 보고 말야

평온했던 하늘이 무너지고
어둡던 눈앞이 붉어지며
뭔가 잊고 온 게 있는 것 같아
괜히 이상하게 막 울 것만 같고
그냥 지나치는 게 나을 것 같아
나는 생각은 딱 질색이니까

카페인으로 잡은 정신은 빠졌고
하루 종일 신경 쓰여 토할 것 같아
저녁이 돼도 배고픔까지 까먹고
그치 이상하지 근데 말야 있잖아

처음 본 순간 뭐라 할까 그립달까
나도 웃긴데 말야

평온했던 하늘이 무너지고
어둡던 눈앞이 붉어지며
뭔가 잊고 온 게 있는 것 같아
괜히 이상하게 막 울 것만 같고
그냥 지나치는 게 나을 것 같아
나는 생각은 딱 질색이니까

오랫동안 나를 아는
슬픈 표정을 하고 Oh
흔적 없는 기억 밖
혹 과거에 미래에 딴 차원에 세계에
1 2 3 4 5 6 7 8

평온했던 하늘이 무너지고
어둡던 눈앞이 붉어져도
다시 놓쳐버리는 것만 같아
괜히 이상하게 막 울 것만 같고
그냥 지나치는 게 나을 것 같아
나는 생각은 딱 질색이니까

아냐 지나치는 게 나을 것 같아
나는 아픈 건 딱 질색이니까"""



loan = "김미영팀장입니다. {}님께서는 최저이율로 최고 3000만원가지 입금 가능합니다."

name = ["권시은","기석광","김가현","김기호","김대건","김동현","김승주","김예송","김하영","김현지","노석현","박성우","변수현","신소영","원정인","유선우","유정연","이서연","이재연","이충원","이하은","이희재","정다인","조명아","조태식","조혜민","차민혁","최성현","최태성","한다솜",]



import requests
url = "https://www.starbucks.co.kr/store/getStore.do?r=EXRPGE2OU7"
payload = {"in_biz_cds" : "0","in_scodes" : "0","ins_lat" : "37.4947","ins_lng" : "127.0493","search_text" : "","p_sido_cd" : "01","p_gugun_cd" : "","isError" : "true","in_distance" : "0","in_biz_cd" : "","iend" : "1000","searchType" : "C","set_date" : "","rndCod" : "Q878EXUG04","all_store" : "0","T03" : "0","T01" : "0","T27" : "0","T12" : "0","T09" : "0","T30" : "0","T05" : "0","T22" : "0","T21" : "0","T10" : "0","T36" : "0","T43" : "0","T48" : "0","Z9999" : "0","P02" : "0","P10" : "0","P50" : "0","P20" : "0","P60" : "0","P30" : "0","P70" : "0","P40" : "0","P80" : "0","whcroad_yn" : "0","P90" : "0","P01" : "0","new_bool" : "0",}
r = requests.post(url, data=payload)
data = r.json()


#int, #float, #list, #for #if~elif~else


내일 학습 : 
# list comprehension
# dict
# 사용자 함수
# lambda 
# break
# continue 
# 데이터 수집 
# 워드 카운트




2024.04.02

DNS 
Domain Name Server 

TCP/ IP

Protocol -> 약속 


IP -> 



jupyter notebook --generate-config



cd ~ 
pwd


# 목록 보기 
ls 
# 목록 보기 - 상세 
ls -al

drwxr-xr-x 1 gen2 gen2 4096 Apr  2 09:48 .jupyter

drwxr-xr-x 
	- d : directory  , - : file

 rwx        r-x      r-x 
내꺼     그룹    제3자 
r: read, w: write, x: execute 


echo "hi" > a.txt
chmod 646 a.txt 

other 
chmod o-w a.txt
chmod g+w a.txt
chmod u-w a.txt


cd .jupyter 

vim


비주얼 모드 
i 버튼 -> 쓰기 모드 

: -> 명령어 모드 


강제로 탈출 -> q! 

쓰기 w 

쓰고 나가기 wq 


ipython
from jupyter_server.auth import passwd

passwd()

vim jupyter_notebook_config.py


# password 키워드  찾기 
:/password 

n : 다음 찾기 
N : 이전 찾기 






:/notebook_dir 


c.ServerApp.notebook_dir = ""
c.ServerApp.password = ""

# 쓰고 나가기 
:/wq 


empty_list =[]
for x in range(0,10):
    if x % 2 == 0:
        empty_list.append(x)

# list comprehension(리스트 축약형)

empty_list2 = [x for x in range(0, 10) if x % 2 ==0]



from datetime import date, datetime, timedelta

for t in range(0, 1001, 100):
    print(date.today() + timedelta(days=t))

master = dict(zip(range(0,7), "월화수목금토일"))

from datetime import date, datetime, timedelta

for t in range(0, 1001, 100):
    # f-string 3.6이상 
    print(f"{t}일째 - {date.today() + timedelta(days=t)} - {master[(date.today() + timedelta(days=t)).weekday()]}")



# 요일 키 추가 
for star in data['list']:
    star['요일'] = master[datetime.strptime(star['open_dt'], "%Y%m%d").weekday()]


#cnt_dict = {}
cnt_dict = {}
for x in data['list']:
    # print(x['요일'])
    if x['요일'] in cnt_dict:
        #cnt_dict[x['요일']] = cnt_dict[x['요일']] + 1 
        cnt_dict[x['요일']] +=  1 
    else:
        cnt_dict[x['요일']] = 1



[x['s_name']  for x in data['list'] if x['s_name'][-2:] == "DT"]

[x['addr'].split()[1] for x in data['list']]



len(list(set(([x['addr'].split()[1] for x in data['list']]))))



list_data = ['1', '2', '3','4', '5', '6', '7', '8']
for x in list_data:
    print(int(x) ** 2)


def tmp(x):
    return int(x) ** 2
list(map(tmp, list_data))


url = "https://www.genie.co.kr/chart/top200"


head = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}

r = requests.get(url, headers=head)

r.text 


from bs4 import BeautifulSoup
bs = BeautifulSoup(r.text)



for idx, x in enumerate(bs.findAll("td",class_='info')):
    title = x.find("a", class_="title ellipsis").text.strip()
    artist = x.find("a", class_="artist ellipsis").text
    print(f"{idx+1}위 -> {title} - {artist}")


lyric = "https://www.genie.co.kr/detail/songInfo?xgnm={}"
for idx, x in enumerate(bs.findAll("td",class_='info')):
    title = x.find("a", class_="title ellipsis").text.strip()
    artist = x.find("a", class_="artist ellipsis").text
    id_ = x.find("a", class_="title ellipsis")['onclick'].split("'")[1]
    print(f"{idx+1}위 -> {title} - {artist} ")
    print(lyric.format(id_))


r2 = requests.get("https://www.genie.co.kr/detail/songInfo?xgnm=105544013", headers=head)

bs2 = BeautifulSoup(r2.text)
# 상대경로 -> ./ -> 현재 폴더 
# ../ -> 현재 경로에서 상위 폴더 
# 절대경로 
f = open('./a.txt', "w", encoding='utf-8')
f.write(bs2.find("pre", id="pLyrics").text.strip())
f.close()

target = "./lyric"
if not os.path.isdir(target):
    os.mkdir(target)
1

# 50위까지 노래 가사 저장하기 
저장 위치 -> ./lyric
# 파일 형식 -> 가수_제목.txt 







2024.04.03

# 프로세스 확인 
ps 
## 모든 프로세스 확인 
ps -ef 

## | 
## grep 패턴 
ps -ef | grep python

# 프로세스 kill
kill -9 [pid]




cd ~/workspace



# shell
-> bash 


ls -al ~/


# ssh 설치 
sudo apt update 


sudo apt install openssh-server 



sudo service ssh start

sudo service ssh status



# 가상환경 만들기 
pip install virtualenv 

python3 -m virtualenv venv 

ls -al 

python3 -m virtualenv venv


# pip 설치 방법 
pip install pandas 

pip install pandas==1.2.0

pip uninstall pandas 

# 패키지 버전 확인 
pip list 
pip freeze 


# requirements.txt 
pip install -r requirements.txt


# nohup -> session 유지 
# & -> background 
nohup jupyter-notebook &





import os
from tqdm import tqdm
lyrics_url = "https://www.genie.co.kr/detail/songInfo?xgnm={}"
if not os.path.isdir("./lyrics"):
    os.mkdir("./lyrics")
for x in tqdm(bs.find("div", {'class': \
                          "music-list-wrap"}).findAll("td", {"class" : "info"})):
    
    title = x.find("a", class_="title ellipsis").text.strip()
    artist = x.find("a", class_="artist ellipsis").text
    f = open(f"./lyrics/{artist}_{title}.txt", "w", encoding='utf-8')
    #print(f"{artist}-{title}.txt")
    r3 = requests.get(lyrics_url.format(p.findall(str(x))[0]),headers=head)
    f.write(BeautifulSoup(r3.text).find("pre", id="pLyrics").text.strip())
    f.close()




# linux 

# 이동 및 이름 바꾸기 
-> mv [원본] [타켓] 

# 삭제 
rm 
## 폴더 삭제 
rm -rf [폴더] 

# 복사 
cp 
# 하위폴더까지 복사 
cp -R [대상]



https://finance.naver.com/


url = "https://m.stock.naver.com/front-api/v1/external/chart/domestic/info?symbol={}&requestType=1&startTime={}&endTime={}&timeframe=day"


r = requests.get(url.format('005930', '20230102', '20240402'))


import csv 
f = open("./삼성전자.csv", 'w', newline='')
write_stock = csv.writer(f)
write_stock.writerows(data)
f.close()


# 아래 주소에서 api를 찾아서 데이터를 가져오고 
# kospi 만 
# 네이버 주식 api를 이용해서 
# stock폴더를 만들고 그 안에 종목이름.csv 
# 네이버에서 데이터 가져와서 저장하는 기능을 사용자 함수로 만들것
def get_naver_stock(code, start_date, end_date):
    """
    code -> 종목 코드 넣어 
    start_date -> 시작 날짜 
    end_date -> 끝나는 날짜
    """
    pass


http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201





2024.04.04
# 인터넷에 있는 파일 다운로드 받을때 사용 wget 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb



public ip 
private ip 



sudo apt install ./google-chrome-stable_current_amd64.deb -y




# 일반계정 
nohup jupyter-notebook --ip=0.0.0.0 & 

# root
nohup jupyter-notebook --allow-root --ip=0.0.0.0 & 


# 네트워크 프로그램 설치 
sudo apt install net-tools 



# port 
sudo netstat -ntlp | grep [포트] 

# 실행되고 있는 실행파일의 위치 
which 
which google-chrome


cd /opt/google/

pip install webdriver_manager



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="123.0.6312.105").install()))

driver.get("https://www.koreabaseball.com/")

from selenium.webdriver.common.by import By
driver.find_element(By.CSS_SELECTOR, "#lnb > li:nth-child(3) > a").click()
driver.page_source




import time
import re
pattern = re.compile("playerId=([0-9]+)")

select_page = "#cphContents_cphContents_cphContents_ucPager_btnNo{}"
select_team = "#cphContents_cphContents_cphContents_ddlTeam > option:nth-child({})"
playid = []
for x in range(2,12):
    for_1 = select_team.format(x)
    driver.find_element(By.CSS_SELECTOR, for_1).click()
    time.sleep(2)
    #playid.extend(pattern.findall(driver.page_source))
    for y in range(1,6):
        f2 = select_page.format(y)
        try:
            driver.find_element(By.CSS_SELECTOR, f2).click()
            time.sleep(1)
            playid.extend(pattern.findall(driver.page_source))
        except Exception as e:
            print ("page 없음 ")
        time.sleep(2)





import pickle 
# binary save , load 
with open("./kbo.pkl", "wb") as f:
    pickle.dump(playid, f)


import pickle
with open("./kbo.pkl", "rb") as f:
    abc = pickle.load(f)






#lnb > li:nth-child(3) > a




https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe



# conda 가상환경 
conda create --name [이름] python=[버전] 


conda install jupyter 
pip install selenium webdriver_manager



play_url = "https://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId={}"
from bs4 import BeautifulSoup as BS 
import requests 


def get_kbo(id_):
    kbo_r = requests.get(play_url.format(id_))
    bs = BS(kbo_r.text)
    data = {x.text.split(":")[0] : x.text.split(":")[1] for x in bs.find("div", class_= "player_basic").findAll("li")}
    data['team'] = bs.find("h4", id="h4Team").text
    return data





2024.04.05

import requests 

payload = {"ajax": "true",
"curCd": "",
"tmpInqStrDt": "2024-04-03",
"pbldDvCd": "0",
"pbldSqn": "",
"hid_key_data": "",
"inqStrDt": "20240403",
"inqKindCd": "1",
"hid_enc_data": "",
"requestTarget": "searchContentDiv",}

url = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"

r = requests.post(url, data=payload)

hana = pd.read_html(r.text)[0]



def get_exchange(code_, date_=None):
    return hana[hana['통화_통화'].str.find(f"{code_}") > -1]





def get_exchange(code_="USD", date_=None):
    """
     code_ = 통화코드 
         예) USD 
     date_ = 예) '2024-01-02'
    """
    payload = {"ajax": "true",
            "curCd": "",
            "pbldDvCd": "0",
            "pbldSqn": "",
            "hid_key_data": "",
            "inqKindCd": "1",
            "hid_enc_data": "",
            "requestTarget": "searchContentDiv",}
    payload['tmpInqStrDt'] = date_
    payload['inqStrDt'] = date_.replace("-", "")
    url = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"
    r = requests.post(url, data=payload)
    exchange = pd.read_html(r.text)[0]
    exchange.columns = ["_".join(x[:2]) for x in exchange.columns]
    return exchange.loc[exchange['통화_통화'].str.find(f"{code_.upper()}") > -1, '현찰_파실 때'].iloc[0,0]



----

from datetime import date, datetime
import requests 
import pandas as pd 

def get_exchange(code_="USD", date_=None):
    """
     code_ = 통화코드 
         예) USD 
     date_ = 예) '2024-01-02'
    """
    payload = {"ajax": "true",
            "curCd": "",
            "pbldDvCd": "0",
            "pbldSqn": "",
            "hid_key_data": "",
            "inqKindCd": "1",
            "hid_enc_data": "",
            "requestTarget": "searchContentDiv",}
    # 날짜 형식 검사
    try:
        datetime.strptime(date_, "%Y-%m-%d")
    except:
        print ("값 확인해!!")
        return -1
        
    
    payload['tmpInqStrDt'] = date_
    payload['inqStrDt'] = date_.replace("-", "")
    url = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"
    r = requests.post(url, data=payload)
    exchange = pd.read_html(r.text)[0]
    exchange.columns = ["_".join(x[:2]) for x in exchange.columns]
    return exchange.loc[exchange['통화_통화'].str.find(f"{code_.upper()}") > -1, '현찰_파실 때'].iloc[0,0]





f = open("./file.txt", "w", encoding="utf-8")
for roots, dirs, files in os.walk("/home/gen2"):
    for file in files:
        f.write(f"{roots}/{file}\n")
f.close()




# dict comprehension 
code_master = {x1.split()[0] : x1.split()[1] for x1 in hana['통화_통화']}



kbo2 = kbo_df[kbo_df.연봉.str.find("달러") > -1].copy()



# warning 숨기기 
import warnings
warnings.filterwarnings(action='ignore')


exchange =  get_exchange('usd', '2024-01-02')

kbo2['연봉'] = kbo2.연봉.apply(lambda x : int(x[:-2]) * exchange) / 10000



kbo3 = kbo_df[~kbo_df.연봉.str.find("달러") > -1].copy()


# and -> % 
# or -> | 
# not -> ~



kbo4 = kbo3[~kbo3.연봉.apply(lambda x : len(x) < 3)].copy()

kbo4.연봉 = kbo4.연봉.apply(lambda x : int(x[:-2]))


final = pd.concat([kbo2, kbo4])


final.groupby(['team'])[['연봉']].mean().sort_values(by=['연봉'], ascending=False)



final.groupby(['team'])[['연봉']].agg(['mean', 'median', 'var'])




공개키 (public key) 
개인키(private key)


sudo apt install unzip 
unzip ./이름_생년_성별_10000.zip -d ./data


파일 분리하여 저장 
남성 -> 남성 폴더에 저장 
여성 -> 여성 폴더에 저장 

'1', '3' 
'2', '4' 

남성, 여성 컬럼으로 DataFrame으로 
.to_csv("./report.csv", index=False, encoding='utf-8-sig')


# 파일 복사 
import shutil
shutil.move("./result.csv", "/home/gen2")







2024.04.08
kbo['초등'] = kbo['경력'].apply(lambda x : x.split("-")[0])



kbo['생년월일'].apply(lambda x : datetime.strptime(x.strip(), "%Y년 %m월 %d일"))

kbo['생년월일'] = kbo['생년월일'].apply(lambda x : datetime.strptime(x.strip(), "%Y년 %m월 %d일"))

kbo['생존일'] = kbo['생년월일'].apply(lambda x : (datetime.now() - x).days)

kbo.sort_values(by=['생존일', '선수명'], ascending=[False, True])


kbo['나이'] = kbo['생년월일'].apply(lambda x : datetime.now().year - x.year)


kbo.loc[kbo.team == "고양 히어로즈", 'team']  = '키움 히어로즈'



매장/서비스 > 매장검색 | 대한민국 대표편의점 GS25 (gsretail.com)



import requests 
from bs4 import BeautifulSoup as BS 

r= requests.get("http://gs25.gsretail.com/gscvs/ko/store-services/locations")

bs = BS(r.text)

#<form id="CSRFForm" action="/gscvs/ko/store-services/locations" method="post"><input type="hidden" name="CSRFToken" value="406690e8-0340-4931-b372-4b5519577c3c" />
bs.find("input", {'name': "CSRFToken"})



with requests.Session() as s:
    r = s.get("http://gs25.gsretail.com/gscvs/ko/store-services/locations")
    bs = BS(r.text)
    token = bs.find("input", {'name': "CSRFToken"})
    print(bs.find("input", {'name': "CSRFToken"}))
    target = f"http://gs25.gsretail.com/gscvs/ko/store-services/locationList?CSRFToken={token}"
    





payload = {"pageNum": "1",
"pageSize": "5",
"searchShopName": "",
"searchSido": "26",
"searchGugun": "2671",
"searchDong": "26710310",
"searchType": "",
"searchTypeService": "0",
"searchTypeToto": "0",
"searchTypeCafe25": "0",
"searchTypeInstant": "0",
"searchTypeDrug": "0",
"searchTypeSelf25": "0",
"searchTypePost": "0",
"searchTypeATM": "0",
"searchTypeWithdrawal": "0",
"searchTypeTaxrefund": "0",
"searchTypeSmartAtm": "0",
"searchTypeSelfCookingUtensils": "0",
"searchTypeDeliveryService": "0",
"searchTypeParcelService": "0",
"searchTypePotatoes": "0",
"searchTypeCardiacDefi": "0",
"searchTypeFishShapedBun": "0",}
with requests.Session() as s:
    r = s.get("http://gs25.gsretail.com/gscvs/ko/store-services/locations")
    bs = BS(r.text)
    token = bs.find("input", {'name': "CSRFToken"})['value']
    #print(bs.find("input", {'name': "CSRFToken"}))
    target = f"http://gs25.gsretail.com/gscvs/ko/store-services/locationList?CSRFToken={token}"
    r2 = s.post(target, data=payload)




pd.DataFrame(eval(r2.json())['results'])





payload = {"pageNum": "1",
"pageSize": "5",
"searchShopName": "",
"searchSido": "",
"searchGugun": "",
"searchDong": "",
"searchType": "",
"searchTypeService": "0",
"searchTypeToto": "0",
"searchTypeCafe25": "0",
"searchTypeInstant": "0",
"searchTypeDrug": "0",
"searchTypeSelf25": "0",
"searchTypePost": "0",
"searchTypeATM": "0",
"searchTypeWithdrawal": "0",
"searchTypeTaxrefund": "0",
"searchTypeSmartAtm": "0",
"searchTypeSelfCookingUtensils": "0",
"searchTypeDeliveryService": "0",
"searchTypeParcelService": "0",
"searchTypePotatoes": "0",
"searchTypeCardiacDefi": "0",
"searchTypeFishShapedBun": "0",}
total = []
with requests.Session() as s:
    r = s.get("http://gs25.gsretail.com/gscvs/ko/store-services/locations")
    bs = BS(r.text)
    token = bs.find("input", {'name': "CSRFToken"})['value']
    #print(bs.find("input", {'name': "CSRFToken"}))
    target = f"http://gs25.gsretail.com/gscvs/ko/store-services/locationList?CSRFToken={token}"
    for x in range(1,3):
        if x % 10 == 0: print(x)
        payload['pageNum'] = x 
        r2 = s.post(target, data=payload)
        total.append( pd.DataFrame(eval(r2.json())['results']))


gs25.reset_index(drop=True, inplace=True)





----




2024.04.09 
DataBase(RDBMS)
Mysql 
MariaDB 	- 
	- Line 
Postgresql 
	-> Graph DB 

Oracle -> 비쌈 
	Google, SAP
DB2 

SQL(Structured Query Language)
시퀄 

ANSI SQL 2005 

Hadoop 
sudo apt install mysql-server
sudo service mysql status

sudo service mysql start[stop/status/restart]


wsl -> 윈도우 
-> 리얼 -> 
sudo systemctl enable mysql 











ERP -> 전사적자원관리 
	1. SAP 
		- Samsung, LG, SK, ... 
		- Abap(월 2,3천)  
		- MM, SD, PP, HR, .... 
   	2. HANA 
		- In-memory


 sudo mysql -uroot -p


select user, host from mysql.user;



create user gen@'%' identified by 'encore';
# 모든 데이터베이스의 테이블 권한 주기 
grant all privileges on *.* to gen@'%';


exit;


sudo mysql -ugen -p

# mysql 환경 파일 			
cd /etc/mysql/mysql.conf.d

sudo vim mysqld.cnf
		

bind-address            = 0.0.0.0



# mysql 재가동 




import sqlalchemy
from urllib import parse

user = '뷁뷁뷁뷁'
password = '뷁뷁뷁뷁뷁뷁뷁'
host='뷁뷁뷁뷁뷁'
port = 3306
database = 'encore'
password = parse.quote_plus(password)
engine = sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")



unique_cu.to_sql('cu', index=False, if_exists="append", con=engine)




---





2024.04.11

import pickle
import pandas as pd 



with open("./seven_stores.pkl", "rb") as f:
    seven_df = pickle.load(f)



tmp = set()
seven_df.able_services.apply(lambda x : [tmp.add(y) for y in x])


for service in tmp:
    seven_df[service] = seven_df.able_services.apply(lambda x : 1 if service in x else 0)


seven_df.drop(['able_services'], axis=1, inplace=True)



seven_df['sido'] = seven_df['address'].apply(lambda x : x.split()[0])


pd.set_option('display.max_rows', None)


import requests 
r = requests.post("https://www.7-eleven.co.kr/util/storeLayerPop.asp")
from bs4 import BeautifulSoup
sido_name = [x.text for x in BeautifulSoup(r.text).find("select", id="storeLaySido").findAll('option')[1:]]



seven_df.loc[seven_df.sido == '주소', 'address'] = "서울시 서대문구 충정로7 구세군빌딩1층"
seven_df.loc[seven_df.sido == '주소', 'sido'] = "서울특별시"


seven_df.loc[seven_df.sido == '전라북도전주시', 'sido'] = "전라북도"
seven_df.loc[seven_df.sido == '경상북도영주시광복로', 'sido'] = "경상북도"
seven_df['sido'].value_counts()


seven_df = seven_df[['company', 'name', 'sido', 'address', '24시간', '무인택배접수', '카페', '베이커리', '시디', 'ATM', '무인락커',
       '치킨', '의약품', '소프트아이스크림', '토토', '고구마·붕어빵', '스마트픽', '예약주문', '페덱스서비스',
        ]].copy()


seven_melt = pd.melt(seven_df, id_vars=['company', 'name', 'sido', 'address'])



con =pymysql.connect(host='뷁뷁뷁', user='뷁뷁뷁', password='뷁뷁뷁뷁', db='뷁뷁뷁', charset='utf8')
cur = con.cursor()




CREATE Table store
(
    `brand` VARCHAR(10) NOT NULL, 
    `store_name` VARCHAR(30) NOT NULL, 
    `sido` CHAR(7) NOT NULL, 
    `store_tel` CHAR(14) Default NULL,
    `store_code` CHAR(5) Default NULL,
    `lat` FLOAT Default null, 
    `longs` FLOAT Default null,
    `open_time` CHAR(20) Default Null,
    `store_address` VARCHAR(100) NOT NULL,
    `service` VARCHAR(20) NOT NULL, 
    `available` INT NOT NULL,
    PRIMARY KEY(`store_name`, `store_address`)
);



INSERT INTO store VALUES ('엔코아', '서초동이야', '서울', '02-777-7777', 
							NULL, NULL, NULL, '08:00~21:30', '효령로 ....', '공부', 1);



SELECT * FROM store;



python-->
sql = "INSERT INTO store VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# "" -> None 교체 
df.store_tel = df.store_tel.replace("", None)

# NaN -> None 으로 replace 
df2 = df.where(pd.notnull(df), None)


df2.available = df2.available.astype(int)

cur.execute(sql, df2.iloc[0].values.tolist())


con.commit()




drop table store;

CREATE Table store
(
    `brand` VARCHAR(10) NOT NULL, 
    `store_name` VARCHAR(30) NOT NULL, 
    `sido` CHAR(7) NOT NULL, 
    `store_tel` CHAR(14) Default NULL,
    `store_code` CHAR(5) Default NULL,
    `lat` FLOAT Default null, 
    `longs` FLOAT Default null,
    `open_time` CHAR(20) Default Null,
    `store_address` VARCHAR(100) NOT NULL,
    `service` VARCHAR(20) NOT NULL, 
    `available` INT NOT NULL,
    PRIMARY KEY(`store_name`, `store_address`, `service`)
);




import pymysql
import pandas as pd
con =pymysql.connect(host='172.23.78.97', user='gen', password='encore', db='encore', charset='utf8')
cur = con.cursor()

store_df = pd.read_sql_query("select * from store", con=con)


https://apis.data.go.kr/B552584/EvCharger/getChargerInfo?serviceKey=34lIyWAciAsJlGtIZ4ltpLy2sLZDR%2BBRWvAv8RgoADNEd%2BKCgHe84XiSRUwL8JMMIubzsFW3ddjcNlhZHhvJIQ%3D%3D&pageNo=1&numOfRows=10&zcode=11



import requests 
r = requests.get("http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?serviceKey=34lIyWAciAsJlGtIZ4ltpLy2sLZDR%2BBRWvAv8RgoADNEd%2BKCgHe84XiSRUwL8JMMIubzsFW3ddjcNlhZHhvJIQ%3D%3D&pageNo=1&numOfRows=10&zcode=11")
import xml.etree.ElementTree as ET
root  = ET.fromstring(r.text)


items = root.iter('item')
df1 = pd.DataFrame([{y.tag : y.text for y in element} for element in items])
    


items = root.iter('item')
total = []
for element in items:
    tmp = {} 
    for y in element:
        tmp[y.tag] = y.text
    total.append(tmp)
df2 = pd.DataFrame(total)
    


---




2024.04.12

import requests
import pandas as pd
url = "https://www.starbucks.co.kr/store/getStore.do?r=U1GAWL"
payload = {"in_biz_cds": "0","in_scodes": "0","ins_lat": "37.4909","ins_lng": "127.0231","search_text": "","p_sido_cd": "01","p_gugun_cd": "","in_distance": "0","isError": "true","in_biz_cd": "","iend": "1000","searchType": "C","set_date": "","rndCod": "1EMUI1PR4R","all_store": "0","T03": "0","T01": "0","T27": "0","T12": "0","T09": "0","T30": "0","T05": "0","T22": "0","T21": "0","T10": "0","T36": "0","T43": "0","T48": "0","Z9999": "0","P02": "0","P10": "0","P50": "0","P20": "0","P60": "0","P30": "0","P70": "0","P40": "0","P80": "0","whcroad_yn": "0","P90": "0","P01": "0","new_bool": "0",}
df = pd.DataFrame(requests.post(url, data=payload).json()['list'])


pd.set_option('display.max_columns', None)


star_df = df[['addr', 's_name', 'tel', 'fax', 'gugun_name', 'defaultimage', 'lat', 'lot']].copy()



pip install folium


import folum

map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles="cartodb positron")


import json

geo_str = requests.get("https://t1.daumcdn.net/cfile/tistory/272C224C58B4BD540B").json()

df = pd.DataFrame(data)
df.reset_index(inplace=True)
df.rename(columns={'count' : 'value'}, inplace=True)
folium.Choropleth(geo_str, 
                  data = df, 
                  columns=['gugun_name', 'value'],
                  fill_color= "PuRd",
                  key_on = 'feature.id').add_to(map)




for idx, row in star_df[['s_name', 'lat', 'lot']].iterrows():
    folium.Marker([row.lat, row.lot], popup=row.s_name).add_to(map)


map.save("./starbuck_loaction.html")



실습 
------

하나의 DataFrame 만들기 

-> DB Insert 

-> 1년 동안 승,하차 집계 -> 서울시 위에 히트맵 

-> 강남 승,하차 시각화 



---




2024.04.15

def fibo(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# 재귀 
def fibo_recu(n):
    if n < 2 : return n
    return fibo_recu(n-1) + fibo_recu(n-2)




# 제너레이터(generator)
def fib_generator():
    a, b = 0, 1 
    while True:
        yield b 
        a, b = b, a + b

fg = fib_generator()


for _ in range(10):
    print(next(fg))




# notebook에서 sql 사용하기 
pip install ipython-sql

import pandas as pd
pd.read_sql_query("select * from customers", con=engine)



# mysqlclient 설치 에러나는 분들 

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config


----
df1 = pd.read_sql_query("select * from orders", con=con)
df2 = pd.read_sql_query("select * from orderdetails", con=con)

pd.merge(df1, df2, left_on=['orderNumber'], right_on=['orderNumber'], how='inner')


SELECT * 
FROM orders A 
LEFT JOIN 
orderdetails B 
ON A.orderNumber = B.orderNumber;

pd_rt1 = pd.merge(df1, df2, left_on=['orderNumber'], right_on=['orderNumber'], how='left')
sql = """SELECT * 
FROM orders A 
LEFT JOIN 
orderdetails B 
ON A.orderNumber = B.orderNumber;"""
sql_rt1 = pd.read_sql_query(sql, con=con)



Merge, join, concatenate and compare — pandas 2.2.2 documentation (pydata.org)


left = pd.DataFrame(
   {
      "key1": ["K0", "K0", "K1", "K2"],
      "key2": ["K0", "K1", "K0", "K1"],
      "A": ["A0", "A1", "A2", "A3"],
      "B": ["B0", "B1", "B2", "B3"],
   }
)


right = pd.DataFrame(
   {
      "key1": ["K0", "K1", "K1", "K2"],
      "key2": ["K0", "K0", "K0", "K0"],
      "C": ["C0", "C1", "C2", "C3"],
      "D": ["D0", "D1", "D2", "D3"],
   }
)


result = pd.merge(left, right, how="left", on=["key1", "key2"])




https://www.notion.so/SQL-323e197320d642f58a2fa106e6269ef8?pvs=4



CREATE VIEW tmp_orders AS 
SELECT * FROM orders LIMIT 10;



select COUNT(*) 
FROM (SELECT DISTINCT(orderNumber) FROM orders) A



df2[df2.orderNumber.isin(orders_df1.orderNumber.tolist())].shape





https://seasoned-tree-375.notion.site/SQL-323e197320d642f58a2fa106e6269ef8?pvs=4


import glob 

subway_total = [pd.read_csv(file_locate, encoding='cp949') \
                for file_locate in glob.glob("./data/*.csv")]



import os 
target = sorted(glob.glob("./data/*.csv"), key=os.path.getctime)

subway_total = [pd.read_csv(file_locate, encoding='cp949') \
                for file_locate in target ]


# 참고 
# 변수명 데이터프레임 만들기 
for file in target:
    locals()[f'{file.split(".")[1].split("/")[-1]}'] = \
       pd.read_csv(file, encoding='cp949')




for x in subway_total:
    display(x.head(1))
    print("-" * 100)


subway_df1= pd.concat(subway_total[:5])


sub_df1_1 = subway_df1.drop('할인', axis=1).groupby(['날짜', '호선', '역명', '구 분'], 
                                     as_index=False).sum()


sub_df1_1.columns = sub_df1_1.columns.str.replace(" ", "").tolist()




import re 
p = re.compile("(\([0-9]+\))")

sub_df1_1['역명'] = sub_df1_1.역명.apply(lambda x : re.sub(p,  "", x))

----
subway_df1= pd.concat(subway_total[:5])
sub_df1_1 = subway_df1.drop(['할인','호선'], axis=1).groupby(['날짜', '역명', '구 분'], 
                                     as_index=False).sum()
sub_df1_1.columns = sub_df1_1.columns.str.replace(" ", "").tolist()
import re 
p = re.compile("(\([0-9]+\))")
sub_df1_1['역명'] = sub_df1_1.역명.apply(lambda x : re.sub(p,  "", x))
sub_df1_2 = sub_df1_1.groupby(['날짜', '역명', '구분'], as_index=False).sum()
-----------


subway_df2 = pd.concat(subway_total[5:-1])
subway_df2.drop("01~02", axis=1, inplace=True)
subway_df2['역명'] = subway_df2.역명.apply(lambda x : re.sub(p, "", x))
subway_df2_1 = subway_df2.groupby(['역명', '날짜', '구분'],as_index=False).sum()

sub_01_11 = pd.concat([sub_df1_2, subway_df2_1])


-------
sub_01_11.query(" 역명 == '사당' and 날짜 == '2016-05-01'")
sub_01_11[(sub_01_11.역명 == "사당") & (sub_01_11.날짜 == '2016-05-01')]
---
subway_df3 = subway_total[-1]
subway_df3.columns = subway_df3.columns.str.replace("시", "")

subway_df3.drop('01~02', axis=1, inplace=True)
subway_df3.역명 = subway_df3.역명.apply(lambda x : re.sub(p, "", x))
subway_df3_1 = subway_df3.groupby(['역명', '날짜', '구분'], as_index=False).sum()


subway = pd.concat([sub_01_11,  subway_df3_1])

sql  = """CREATE TABLE subway(
    date_ DATE NOT NULL, 
    station VARCHAR(3) NOT NULL, 
    gubun CHAR(2) NOT NULL, 
    timeline CHAR(7) NOT NULL, 
    value INT(5) NOT NULL)"""
cur.execute(sql)

subway_melt = pd.melt(subway, id_vars=['날짜','역명', '구분'])

sql = "INSERT INTO subway VALUES (%s, %s, %s, %s, %s)"

cur.execute(sql, subway_melt.iloc[0].tolist())




---




2024.04.16
# db backup 
sudo mysqldump -uroot classicmodels > ~/backup.sql

# db 복원 
mysql -uroot [db명] < ~/backup.sql 



# ssh
ssh id@ip


# 계정 비밀번호 설정 
sudo passwd [계정]

whoami 
pwd 

# 윈도우의 터미널에서 
ssh-keygen -t rsa

~/.ssh 생성 
id_rsa
id_rsa.pub




# ssh 
cat id_rsa.pub >> authorized_keys

chmod 600 authorized_keys


1. 윈도우 .ssh 폴더에서 
2. id_rsa.pub 메모장 열기 -> 내용 복사 
3. wsl(서버) authorized_keys
vim authorized_key 
마지막줄에 복사한 내용 붙여넣기, 저장하기 
4. 윈도우에서 
ssh id@ip 



------------------------
1) 일별 매출액 조회 
SELECT A.orderDate, B.priceEach * B.quantityOrdered
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber;

SELECT orders.orderDate, orderdetails.priceEach * orderdetails.quantityOrdered
FROM orders 
LEFT JOIN orderdetails 
ON orders.orderNumber = orderdetails.orderNumber;



SELECT A.orderDate, B.priceEach * B.quantityOrdered AS RESULT
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber;



SELECT A.orderDate, SUM(B.priceEach * B.quantityOrdered) AS SALES
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
GROUP BY A.orderDate;


SELECT A.orderDate, SUM(B.priceEach * B.quantityOrdered) AS SALES
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
GROUP BY 1



SELECT A.orderDate, SUM(B.priceEach * B.quantityOrdered) AS SALES
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
GROUP BY 1
ORDER BY 2 DESC;


SELECT SUBSTR('2004-11-24', 1,7);

# 월별 매출 합계 구하기
 -> 정렬은 날짜순으로....


SELECT SUBSTR(A.orderDate, 1,4) AS YY, SUM(B.priceEach * B.quantityOrdered) AS SALES
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
GROUP BY 1
ORDER BY 1;




-------
건당 구매 금액(ATV, Average Transaction Value) 

https://blog.naver.com/PostView.nhn?blogId=insidecompany&logNo=222030886283&parentCategoryNo=&categoryNo=24&viewDate=&isShowPopularPosts=true&from=search

Q : 1건의 거래는 평균적으로 얼마의 매출을 발생시키는가? 

매출 / 구매 건수  -> ATV
 

YY , cnt_purchaser, sales, atv


SELECT SUBSTR(A.orderDate, 1,4) AS YY, COUNT(DISTINCT (A.orderNumber)) AS cnt_purchaser,
SUM(B.priceEach * B.quantityOrdered) AS SALES, 
SUM(B.priceEach * B.quantityOrdered) / COUNT(DISTINCT (A.orderNumber)) AS atv
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
GROUP BY 1
ORDER BY 1;



------------------
국가별, 도시별 매출액 


SELECT *
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber;



-> country, city, sales 

-> groupby(['country', 'city'])

마이그레이션 



SELECT C.country, C.city, 
SUM(B.priceEach * B.quantityOrdered) AS sales
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber
GROUP BY 1, 2 
ORDER by 1;


order = pd.read_sql_query("select * from orders", con=con)
orderdetails = pd.read_sql_query("select * from orderdetails", con=con)
customers = pd.read_sql_query("select * from customers", con=con)


df = pd.merge(pd.merge(order, orderdetails, on='orderNumber', how='left'), customers, on="customerNumber", how='left')


df['tmp'] = df['priceEach'] * df['quantityOrdered']


df.groupby(['country', 'city'],as_index=False)[['tmp']].sum().sort_values(by=['country', 'city'])



----------
CASE WHEN 조건 THEN 결과 END

SELECT CASE WHEN COUNTRY IN ('USA', 'Canada') THEN 'North America'
ELSE 'Others' END COUNTRY_GRP 
FROM customers;
북미, 비북미 매출액 비교해줘 

SELECT CASE WHEN C.COUNTRY IN ('USA', 'Canada') THEN 'North America'
ELSE 'Others' END COUNTRY_GRP,
SUM(B.priceEach * B.quantityOrdered) AS sales
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber
GROUP BY 1;



CREATE TABLE STAT AS 
SELECT C.country, C.city, 
SUM(B.priceEach * B.quantityOrdered) AS sales
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber
GROUP BY 1, 2 
ORDER by 1;


SELECT COUNTRY, SALES,
DENSE_RANK() OVER(ORDER BY SALES DESC) RNK
FROM STAT;



CREATE VIEW tmp AS 
SELECT COUNTRY, SALES,
DENSE_RANK() OVER(ORDER BY SALES DESC) RNK
FROM STAT;


CREATE VIEW tmp AS 
SELECT COUNTRY, SALES,
DENSE_RANK() OVER(ORDER BY SALES DESC) RNK
FROM STAT;


SELECT * 
FROM tmp 
WHERE RNK BETWEEN 1 AND 5;

SELECT * 
FROM tmp 
WHERE RNK >= 1 
AND RNK <= 5;



sub-query 
SELECT COUNT(*) FROM 
( SELECT C.country, C.city, 
SUM(B.priceEach * B.quantityOrdered) AS sales
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber
GROUP BY 1, 2 
ORDER BY 1) D;


SELECT * 
FROM 
(
SELECT COUNTRY, SALES,
DENSE_RANK() OVER(ORDER BY SALES DESC) RNK
FROM
(
    	SELECT C.country, C.city, 
SUM(B.priceEach * B.quantityOrdered) AS sales
FROM orders A
LEFT JOIN orderdetails B
ON A.orderNumber = B.orderNumber
LEFT JOIN customers C
ON A.customerNumber = C.customerNumber
GROUP BY 1, 2 
ORDER by 1
) D
) E
WHERE RNK <= 5;



df2 = df.groupby(['country', 'city'],as_index=False)[['tmp']].sum().sort_values(by=['country', \
                                        'city']).rename(columns={'tmp' : 'sales'})



sql = """CREATE Table dataset2
(
    `Clothing ID` INT,
    `Age` INT,
    `Title` VARCHAR(30),
    `Review Text` TEXT,
    `Rating` INT,
    `Recommended IND` INT,
    `Positive Feedback Count` INT,
    `Division Name` VARCHAR(30),
    `Department Name` VARCHAR(30),
    `Class Name` VARCHAR(30)
)"""

cur.execute(sql)
con.commit()



ALTER TABLE dataset2 MODIFY COLUMN `Title` VARCHAR(200);

----------
data = pd.read_csv("./data/dataset2.csv", delimiter=";")


def tmp(x):
    global var_x 
    var_x = x
    cur.execute("INSERT  INTO dataset2 VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", x.tolist())
    return 0

data=  data.where(pd.notnull(data), None)

data.apply(tmp, axis=1)
con.commit()

----------


insert_sql = "INSERT  INTO dataset2 VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
data.apply(lambda x : cur.execute(insert_sql, x.tolist() ), axis=1)



• Clothing ID: 상품 번호(Unique Value) 
• Age: 리뷰작성자의 연령 
• Title: 리뷰 제목 
• ReviewText: 리뷰내용 
• Rating: 리뷰 작성자가 제출한 평점 
• Recommended IND: 리뷰어에 의한 상품 추천 여부 
• Positive Feedback Count: 긍정 적 피드백 수 
• Division Name: 상품이 속한 Division 
• Department Name: 상품이 속한 Department 
• Class Name: 상품의 타입


Division name별 평균 평점 

AVG

SELECT `Division Name`,
AVG(RATING) AVG_RATE
FROM dataset2
GROUP BY 1;
______


data.groupby(['Division Name'])[['Rating']].mean().sort_values(by=['Rating'], ascending=True)

def tmp(x):
    if x < 20:
        return '청소년'
    elif x < 50:
        return "청년"
    else:
        return "중년"
data['Age'].apply(tmp)


data['Age'].apply(lambda x :  '청소년' if x < 20  else ("청년" if x < 50 else "중년" ))



SELECT CASE WHEN AGE BETWEEN 0 AND 19 THEN '청소년'
WHEN AGE BETWEEN 20 AND 49 THEN '청년'
WHEN AGE BETWEEN 49 AND 99 THEN '중년' END age_class, age
from dataset2;



SELECT count(age_class)
FROM 
(SELECT CASE WHEN AGE BETWEEN 0 AND 19 THEN '청소년'
WHEN AGE BETWEEN 20 AND 49 THEN '청년'
WHEN AGE BETWEEN 49 AND 99 THEN '중년' END age_class, age
from dataset2) A
GROUP BY age_class;



https://codeshare.io/XLNMpz


ssh ubuntu@3.36.58.92


# 내 wsl안에서.... 
git config --global user.name "사용자이름"
git config --global user.email "이메일"

# 변경 
git config --global user.name [이름]



cd ~ 
git clone ssh://ubuntu@3.36.58.92:/home/ubuntu/repos






---

2024.04.22
billyrohh/instacart_dataset (github.com)


import pandas as pd
import os, glob

for file in glob.glob("./instacart_dataset/*.csv"):
    locals()[file.split("/")[-1].split(".")[0]] = pd.read_csv(file)
    print(file)



from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, DateTime, Date



import sqlalchemy
from urllib import parse

user = 'gen'
password = '123'
host='localhost'
port = 3306
database = 'encore'
password = parse.quote_plus(password)
engine = sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")


metadata = MetaData()




table = Table('aisles', metadata, 
      Column('aisle_id', Integer),
      Column('aisle', String(100)),
     )
metadata.create_all(engine)




# 
# orders table 
# 1. 주문 건수 구하기 
# 2. 구매자 수 구하기 
# 3. 상품별 주문 건수 
# - order_products__prior , products 


# 계정이 gen일때 password 123(백업)
mysqldump -ugen -p123 encore > ~/instacart.sql

(복원)
mysql -ugen -p123 encore < ~/instacart.sql



# 비밀번호 변경 
alter user 'gen'@'%' identified by '123';





--  1. 주문 건수 구하기 
SELECT COUNT(DISTINCT order_id) cnt
FROM orders;
--  2. 구매자 수 구하기 
SELECT COUNT(DISTINCT user_id) user_cnt
FROM orders;
--  3. 상품별 주문 건수 
--  order_products__prior , products 
SELECT B.product_name, COUNT(DISTINCT A.order_id) cnt 
FROM order_products__prior A
LEFT JOIN products B 
ON A.product_id = B.product_id
GROUP BY 1
ORDER BY 2 DESC;



pd.merge(order_products__prior, \
         products, on='product_id', \
         how='left').groupby(['product_name'])['order_id'].count().sort_values(ascending=False)





--- 

2024.04.23
https://math100.tistory.com/45














t-분포표 





import pandas as pd
import numpy as np
import scipy as sc 

상반기 = pd.read_csv("./data/상반기 주유소 판매가격.csv",
                  encoding='cp949')
하반기 = pd.read_csv("./data/하반기 주유소 판매가격.csv",
                  encoding='cp949')
주유소 = pd.concat([상반기, 하반기])


주유소[['지역', '상호', '상표']].drop_duplicates().groupby(['지역', '상표'])[['상표']].count()



집계결과 = 주유소[['지역', '상호', '상표']].drop_duplicates().groupby(['지역',
                 '상표'])[['상표']].count().rename(columns={'상표' : '집계'}).reset_index()


집계결과.sort_values(by=['집계'], 
                 ascending=False).groupby(['지역']).first()



주유소_365 = 주유소.groupby(['상호'])['번호'].count()[주유소.groupby(['상호'])['번호'].count() == 365].index

주유소_ = 주유소[~주유소.상호.isin(주유소_365)].copy()


주유소_['월'] = 주유소_['기간'].apply(lambda x : str(x)[4:6])



폐업 = 주유소_[['주소', '월']].drop_duplicates().\
    groupby(['월'])[['주소']].count()

폐업['현황'] = 폐업.주소 - 폐업.주소.shift(1)


폐업.fillna(0).rename(columns={'주소' : '집계', '현황' : "폐업갯수"}).reset_index()


강남구  = 주유소_.query(" 지역 == '서울 강남구'")
도봉구  = 주유소_.query(" 지역 == '서울 도봉구'")



sc.stats.ttest_ind(a =  강남구.groupby(['상호'])['휘발유'].mean().values,
                   b =  도봉구.groupby(['상호'])['휘발유'].mean().values)



----
테이블 설명 
aisles, departments는 삼품의 카테고리를 의미 
order_products__prior는 각 주문 번호의 상세 구매 내역 
oders는 주문 대표 정보 
products 상품 정보를 포함 


pd.read_sql_query("select * from order_products__prior", con=engine)


df['first']= df.add_to_cart_order.apply(lambda x :  1 if x == 1 else 0)
df2 = df.groupby(['product_id'], as_index=False)[['first']].sum()


df3 = df2.sort_values(by=['first'], ascending=False).reset_index(drop=True)
df3['rank'] = df3['first'].rank(ascending = False)
df3['rank'] = df3['rank'].astype(int)




SELECT *, 
ROW_NUMBER() OVER(ORDER BY FIRST DESC) rnk
FROM 
(SELECT  product_id,  SUM(CASE WHEN ADD_TO_CART_ORDER = 1 THEN 1 ELSE 0 END) FIRST
FROM order_products__prior
GROUP BY 1) A LIMIT 10;



---
---


2024. 04.24



Garbage In, Garbage Out 



첨도와 왜도 
첨도( kurtosis ) 
- 확률분포의 뽀족한 정도를 나타내는 값 
 


왜도 : 
skewness 
확률분포의 비대칭을 나타내는 값 
왜도값이 0인 경우에는 정규분포와 유사 



EDA 
목적 
 - 데이터의 형태와 척도가 분석에 알맞게 되어 있는지... 확인 
 - 데이터의 평균, 분산, 분포, 패턴 등의 확인을 통해 데이터 특성 파악 
 - 결측치, 이상치 파악, 보완 
 - 변수 간의 관계성 파악 
 - 분석 목적과 방향성 점검 및 보정 



공분산과 상관분석 
변수 Y와 변수 X와의 관계 




공분산 
양의 상관관계 : X_1이 커지면 X_2 커진다. 
음의 상관관계 : X_1이 커지면 X_2 작아진다. 
무 상관관계 : X_1, X_2는 선형적인 관계성이 없음 

공분산 값은 100 양수 값을 갖는다면 X, Y의 두 확률 분포가 어느 정도 선형성이 있는지 알수 없다.













상관계수 
- 공분산의 문제를 해결하는 값으로 -1 ~ 1 사이의 값을 가짐 
- 공분산을 X의 표준편차, Y의 표준편차 모두로 나눈 값 






# 시간별 주문 건수 
SELECT order_hour_of_day,
COUNT(DISTINCT order_id) result
FROM orders 
GROUP BY 1 
ORDER BY 1;


# 첫 구매 후 다음 구매까지 걸린 평균 일수 

SELECT AVG(days_since_prior_order) avg_result
FROM orders 
WHERE order_number = 2;



# 주문 건당 평균 구매 상품 수

SELECT COUNT(product_id) / COUNT(DISTINCT order_id) result
FROM order_products__prior;



# 상품별 재구매율 계산, 1~10, 상품명

SELECT A.product_id, B.product_name, A.result
FROM 
(SELECT product_id, (SUM(reordered) / COUNT(*)) result
FROM order_products__prior
GROUP BY 1) A
LEFT JOIN products B
ON A.product_id=B.product_id
ORDER BY 3 DESC;




---
---

# 2024.04.25

# virtualenv 
 - python module 
 - 현재 설치된 파이썬 버전을 따라감 
 - python -m virtualenv venv
   -> 폴더 생성  (venv)  
   -> 가상환경 사용하기 
       - source ./venv/bin/activate 

# conda 
 - anaconda, miniconda를 설치해야 사 - 다양한 버전의 파이썬을 세팅가능 


# 서버 가동 
python manage.py runserver 
# Ctrl + c 

python manage.py migrate
















from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def TellHello(request):
    html = "<h1> Hi!!!! </h1>"
    return HttpResponse(html)



from django.contrib import admin
from django.urls import path
from practice import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hello/', views.TellHello),
]




from django.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




python manage.py makemigrations 

python manage.py sqlmigrate mypolls 0001


python manage.py migrate 




from django.contrib import admin
from mypolls.models import Question, Choice


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)


python manage.py createsuperuser


pip install mysqlclient 

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config


settings.py

 'default' :{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' :'encore',
        'USER' : 'encore',
        'PASSWORD' : 'EnCore#@!',
        'HOST' : "43.203.251.100",
        'PORT' : 3306
    }




from django.urls import path
from mypolls import views




urlpatterns=[
    path('', views.index)
]




from sklearn.datasets import fetch_california_housing
#from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings

from sklearn.datasets import fetch_openml
housing = fetch_openml(name="house_prices", as_frame=True)
from sklearn.datasets import fetch_openml
boston = fetch_openml(name="house_prices", as_frame=True)

warnings.filterwarnings(action='ignore')

dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
dataset['target'] = boston.target




from django.shortcuts import render
from models import Question, Choice


# Create your views here.
def index(request):
    latest_question = Question.objects.all().order_by("-pub_date")[:5]
    context = {"latest_question" : latest_question}
    return render(request, "polls/index.html", context)







{% if latest_question %}
    {% for question in latest_question %}
        <li><a href="/polls/{{ question.id }}">{{ question.question_text }}</a></li>
    {% endfor %}
{% else %}
    <p>No Polls are availiable.</p>
{% endif %}




urlpatterns=[
    path('', views.index),
    path("<int:question_id>/", views.detail),
]





{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}"
           value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
    {% endfor %}
    <input type="submit" value="Vote" />
</form>




def vote(request, question_id):
   
    question = get_object_or_404(Question, pk=question_id)
    select_choice = question.choice_set.get(pk=request.POST['choice'])
    select_choice = select_choice + 1
    select_choice.save()
    return HttpResponseRedirect('polls:results', args=(question.id))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/results.html', {'question' : question})






<h1> {{ question.question_text }}</h1>


<ul>
    {% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} - {{ choice.votes }}</li>
    {% endfor %}
</ul>




---
---

# 2024.04.26
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine_load = load_wine()

wine = pd.DataFrame(wine_load.data, columns=wine_load.feature_names)
wine['Class'] = wine_load.target

wine['Class'] = wine['Class'].map({0: 'class_0',  1 : 'class_1', 2 : 'class_2'})


import matplotlib.pyplot as plt

plt.boxplot(wine['color_intensity'], whis=1.5)
plt.title('color_intensity')
plt.show()



import numpy as np

def outliers_iqr(dt, col):
    quartile_1, quartile_3 = np.percentile(dt[col], [25, 75])
    iqr = quartile_3 - quartile_1
    lower_whis = quartile_1 - (iqr * 1.5)
    upper_whis = quartile_3 + (iqr * 1.5)
    outliers = dt[(dt[col] > upper_whis) | (dt[col] < lower_whis)]
    return outliers[[col]]




wine_outliers = wine.drop(index=outliers_iqr(wine, 'color_intensity').index)





import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()



iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['Class'] = list(map(lambda x : {0 : 'Setosa', 1: 'Versicolour', 2:'Virginica'}[x], iris.target))


iris_df['Class'] = pd.Categorical(iris_df['Class'])



X_train, X_test, y_train, y_test = train_test_split(iris_df.drop(columns='Class'), iris_df['Class'], test_size = 0.2)



X_train, X_test, y_train, y_test = train_test_split(iris_df.drop(columns='Class'), iris_df['Class'], test_size = 0.2,
                                                  stratify = iris_df['Class']     )



from sklearn.preprocessing import StandardScaler, MinMaxScaler
StdScaler = StandardScaler()

# Train 데이터의 fitting과 스케일링
StdScaler.fit(X_train)
X_train_sc = StdScaler.transform(X_train)
# StdScaler.fit_transform(X_train)
# Test 데이터의 스케일링
X_test_sc = StdScaler.transform(X_test)


print("\t\t(min, max) (mean, std)")
print("Train_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_train_sc.min(), X_train_sc.max(),  X_train_sc.mean(),  X_train_sc.std()))
print("Test_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_test_sc.min(), X_test_sc.max(),  X_test_sc.mean(),  X_test_sc.std()))


- 표준화 방식 
- 컬럼들의 평균 0, 표준편차 1 
- 최솟값, 최댓값 제한 없음 
- 이상치에 민감 
- 회귀보다 분류에 유용 



MmScaler = MinMaxScaler()

# Train 데이터의 fitting과 스케일링
MmScaler.fit(X_train)
X_train_sc = MmScaler.transform(X_train)

# Test 데이터의 스케일링
X_test_sc = MmScaler.transform(X_test)


print("\t\t(min, max) (mean, std)")
print("Train_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_train_sc.min(), X_train_sc.max(),  X_train_sc.mean(),  X_train_sc.std()))
print("Test_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_test_sc.min(), X_test_sc.max(),  X_test_sc.mean(),  X_test_sc.std()))
     
- 컬럼들의 값이 0 ~ 1 사이 
- 최솟값 : 0 
- 최댓값 : 1 
- 이상치 매우 민감 
- 분류보다 회귀에 유용


from sklearn.preprocessing import MaxAbsScaler

MaScaler = MaxAbsScaler()

# Train 데이터의 fitting과 스케일링
MaScaler.fit(X_train)
X_train_sc = MaScaler.transform(X_train)

# Test 데이터의 스케일링
X_test_sc = MaScaler.transform(X_test)


print("\t\t(min, max) (mean, std)")
print("Train_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_train_sc.min(), X_train_sc.max(),  X_train_sc.mean(),  X_train_sc.std()))
print("Test_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_test_sc.min(), X_test_sc.max(),  X_test_sc.mean(),  X_test_sc.std()))



from sklearn.preprocessing import MaxAbsScaler

MaScaler = MaxAbsScaler()

# Train 데이터의 fitting과 스케일링
MaScaler.fit(X_train)
X_train_sc = MaScaler.transform(X_train)

# Test 데이터의 스케일링
X_test_sc = MaScaler.transform(X_test)


print("\t\t(min, max) (mean, std)")
print("Train_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_train_sc.min(), X_train_sc.max(),  X_train_sc.mean(),  X_train_sc.std()))
print("Test_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_test_sc.min(), X_test_sc.max(),  X_test_sc.mean(),  X_test_sc.std()))


- 최대 절댓값과 0이 각각 1, 0이 되도록 스케일링
- 모든 값이 -1 ~ 1 사이에 표현 
- 데이터가 양수만 있을 경우 Min-Max와 동일 
- 이상치에 매우 민감 
- 분류보다 회귀 유용 







from sklearn.preprocessing import RobustScaler

RuScaler = RobustScaler()

# Train 데이터의 fitting과 스케일링
RuScaler.fit(X_train)
X_train_sc = RuScaler.transform(X_train)

# Test 데이터의 스케일링
X_test_sc = RuScaler.transform(X_test)


print("\t\t(min, max) (mean, std)")
print("Train_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_train_sc.min(), X_train_sc.max(),  X_train_sc.mean(),  X_train_sc.std()))
print("Test_scaled (%.2f, %.2f) (%.2f, %.2f)"%(X_test_sc.min(), X_test_sc.max(),  X_test_sc.mean(),  X_test_sc.std()))



- 평균과 분산 대신 중앙값과 사분위 값 
- 중앙값을 0으로 설정 IQR을 사용하여 이상치 영향을 최소화 
- quantile_range 파라미터로 조정하여 이상치 제어 


- 데이터 원복 
display(pd.DataFrame(X_train_sc).head(3))
X_Original = RuScaler.inverse_transform(X_train_sc)
display(pd.DataFrame(X_Original).head(3))





# 수치형 데이터만 추출
features = ['수치형변수1', '수치형변수2']
x = iris_df.drop(columns = 'Class')

# 수치형 변수 정규화
from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(x)

pd.DataFrame(x).head()


from sklearn.decomposition import PCA
pca = PCA( n_components = 4) 
pca_fit = pca.fit(x)

print("고유 값 : ", pca.singular_values_)
print("분산 설명력: ", pca.explained_variance_ratio_)


import matplotlib.pyplot as plt

plt.title('Scree Plot')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.plot(pca.explained_variance_ratio_ , 'o-')
plt.show()
     


import matplotlib.pyplot as plt
import seaborn as sns

plt.title('2 component PCA' )
sns.scatterplot(x = 'pc1', y = 'pc2', hue = iris_df.Class,  data = principal_iris)
plt.show()

 




python manage.py startapp restapi


settings.py 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mypolls.apps.MypollsConfig',
    'restapi.apps.RestapiConfig',
]


pip install djangorestframework


polls -> urls.py
 path('predict/', include('restapi.urls')),


restapi -> urls.py 
파일 생성 

from django.urls import path
from restapi import views


app_name = 'api'


urlpatterns=[
    path('knn/', views.knn),
]


Restful API 만들기 




from django.shortcuts import render
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def knn(request):
    weight = request.data.get('weight')
    length = request.data.get('length')
    print(f"weight -> {weight}, length -> {length}")


    return Response({"result" : "작업중"})








https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm






http://127.0.0.1:8000/predict/knn/






import pickle

with open("./knn_class_model.pk" , "rb" ) as f:
    model1 = pickle.load(f)


import numpy as np
train_scaled = (np.array([ 11.8,   9.9]) - model1['mean']) / model1['std']
model1['model'].predict(train_scaled.reshape(1,2))




-----
pip install numpy 
pip install scikit-learn

from django.shortcuts import render
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
# Create your views here.


# 경로 및 파일 명, 확장자 확인 
with open("./restapi/knn_class_model.pk" , "rb" ) as f:
    model1 = pickle.load(f)




@api_view(['POST'])
def knn(request):
    weight = request.data.get('weight')
    length = request.data.get('length')
    print(f"weight -> {weight}, length -> {length}")


    train_scaled = (np.array([float(weight), float(length)]) - model1['mean']) / model1['std']
    if model1['model'].predict(train_scaled.reshape(1,2)).tolist()[0] == 0.0:
        print('{result: 빙어}')
        return Response('{result: 빙어}')
    else:
        print('{result : 도미}')
        return Response('{result: 도미}')





---
---

# 2024.04.29



django-admin startproject config .


python manage.py migrate


which python
which pip
pip list


python manage.py startapp encore
settings.py에 등록


'encore.apps.EncoreConfig'




from django.urls import path


from . import views




urlpatterns = [
    path('', views.index),
]


views.py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("안녕하세요")









python manage.py runserver 

http://127.0.0.1:8000/encore/

models.py 
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content 




python manage.py makemigrations 

# sql 문법으로 보고 싶다면..

python manage.py sqlmigrate encore 0001


python manage.py shell

# django - shell 편하게...
pip install django-extensions


settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'encore.apps.EncoreConfig',
    'django_extensions',
]


pip install ipython


python manage.py shell_plus


from encore.models import Question, Answer
from django.utils import timezone


q = Question(subject='4월 29일', content='모레는 쉼', create_date=timezone.now())


Question.objects.all()


for x in range(100):
q = Question(subject='4월 29일', content='모레는 쉼', create_date=timezone.now())
            q.save()


# 데이터 조회 
q = Question.objects.get(id=10)

q 

# 수정 
q.subject = ""

# 저장 
q.save()


q.delete()





Answer 


q = Question.objects.get(id=2)


a = Answer(question=q, content='ㅎㅎㅎㅎㅎ', create_date=timezone.now())

# 저정하기 
a.save()


# q(id=2)로 외래키로 연결된 answer의 값 보기 
q.answer_set.all()


a1 = Answer.objects.get(id=1)





---
---

# 2024.04.30


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return 
        current = self.head
        while current.next:
            current = current.next 
        current.next = Node(data)

        

    def print_list(self):
        current = self.head
        if self.head:
            print(self.head.data)
        while current.next:
            current = current.next
            print(current.data)

    def search(self, target):
        """
            사용자 찾는 데이터 있으면 True return 
            없으면 false 
        """
        if self.head == None:
            return False
        current = self.head 
        if self.head.data == target:
            return True 
        while current.next:
            if current.data == target:
                return True 
            current = current.next
        return False



---
---

# 2024.05.02

hflight.groupby(['Origin', 'Dest'], as_index=False)[['DepDelay', 'ArrDelay']].mean()


tmp2 = hflight[hflight.ArrDelay >= 5].groupby(['Dest'], as_index=False)[['Year']].count() 
hflight2 = hflight.Dest.isin(tmp2[tmp2.Year >= 2000].Dest)

hfight_2_result = hflight[hflight2].copy()









SELECT Origin, Dest, round(AVG(DepDelay),2) AS DepDelay , 
	round(AVG(ArrDelay),2) Arrive_Delay
FROM hflight 
GROUP BY Origin, Dest


CREATE VIEW hflight2 AS
SELECT * 
FROM hflight 
WHERE Dest IN 
	(SELECT Dest 
		FROM (
			SELECT Dest, COUNT(DAYOFWEEK) cnt
			FROM hflight
			WHERE ArrDelay >= 5
			GROUP BY Dest
			HAVING cnt >= 2000) a
	)



SELECT Dest, COUNT(*) total 
FROM hflight2 
GROUP BY Dest;


SELECT Dest, COUNT(*) total 
FROM hflight2
WHERE Cancelled = 1 
GROUP BY Dest;


SELECT Dest, COUNT(*) total 
FROM hflight2
WHERE Diverted = 1 
GROUP BY Dest;


SELECT a.dest, a.total, b.Cancelled, c.Diverted,
 (a.total - b.Cancelled - c.Diverted) air 
FROM (SELECT Dest, COUNT(*) total 
	FROM hflight2 
	GROUP BY Dest) a
LEFT JOIN (
		SELECT Dest, COUNT(*) Cancelled 
		FROM hflight2
		WHERE Cancelled = 1 
		GROUP BY Dest
	) b 
ON a.Dest = b.Dest 
LEFT JOIN (
		SELECT Dest, COUNT(*) Diverted 
		FROM hflight2
		WHERE Diverted = 1 
		GROUP BY Dest
)	c
ON a.Dest=c.Dest;



wsl -d Ubuntu-22.04 -u root ip addr add 192.168.45.250/24 broadcast 192.168.45.255 dev eth0 label eth0:1

netsh interface ip add address "vEthernet (WSL)" 192.168.45.100 255.255.255.0


wsl2 버전 

wsl --set-default-version 2  
wsl --set-version Ubuntu-22.04 2 




2024.05.03
all_df.honorific = all_df.honorific.apply(lambda x : x.strip())
all_df.loc[~all_df.honorific.isin(['Mr', 'Miss', 'Mrs', 'Master']), 'honorific' ] = 'Other'


categories = all_df.dtypes[all_df.dtypes == 'object'].index.tolist()
for cate in categories:
    le = LabelEncoder()
    le.fit(all_df[cate])
    all_df[cate] = le.transform(all_df[cate])


vim ~/.bashrc 


PROMPT_DIRTRIM=1


source ~/.bashrc





views.py
def index(request):
    question_object = Question.objects.order_by('-create_date')
    return render(request, 'encore/question_list.html',
            {'question_list' : question_object}      )





question_list.html

{% if question_list %}
    <ul>
        {% for question in question_list %}
            <li>{{ question.subject }}</li>
        {% endfor %}
    </ul>
{% else  %}
    <p> 없음 </p>
{% endif %}

---
---

# 2024.05.07
ssh ubuntu@43.202.5.70
https://codeshare.io/Q8OYlx


cd ~/.ssh
ls 

id_rsa  id_rsa.pub

cat id_rsa.pub 




git clone ssh://ubuntu@43.202.5.70:/home/ubuntu/workspace/repos2




ssh-keygen -t rsa 



export AIRFLOW_HOME=/home/{여러분계정}/airflow
예) export AIRFLOW_HOME=/home/gen/airflow

export AIRFLOW_HOME=/root/airflow

vim ~/.bashrc

위에 경로 입력 
bashrc 저장 하고 나온 뒤에 

source ~/.bashrc 
# $ 환경변수 
echo $AIRFLOW_HOME


echo $PATH
-------

AIRFLOW_VERSION=2.8.1

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.8.1 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
------




airflow standalone

