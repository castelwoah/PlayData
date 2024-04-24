<1일차>
클라우드 환경으로 배보까지 해보는 실습을 할 것이다.

다른것보다 sql, linux, python(pandas)
통신관련내용도 어느정도 알고 있어야 한다.

앞으로 배울 내용
	- 데이터엔지니어링
		○ Linux
		○ Python
		○ Ml
		○ Deep Learning
		○ Hadoop
		○ Airflow
		○ Backend
			§ Springboot
			§ Django
		○ DB
			§ mySQL

<수업>
운영체제기반 역사
리눅스의 아버지 = 리눅스 토발즈
유닉스를 따라 만든 리눅스

레드햇 리눅스
백엔드에서 많이 씀

우분투 리눅스
딥러닝 직무에서 많이 사용함

윈도우 + r
appwiz.cpl 검색
Hyper-v
Linux 용 windows 하위 시스템

Port
데이터가 왔다갔다 하는 곳
포트는 다른 프로세스가 사용 중이면 사용 불가

ubuntu 22.04.3 LTS 다운로드
(실행후 에러가 뜰경우 커널 업데이트 실행)

python 설명
버전 설명 python 메인버젼.마이너버젼(업데이트).보안패치
사용버젼 = python 3.10.12
인터프리터 언어(소스코드가 곧 명령어)

python 분석 관련 패키지
numpy(선형대수 패키지) + scipy = tensorflow
jupyter
scikt-learn
deep learning
	- google tensorflow
 	- meta pytorch
pandas(데이터 전처리에 사용)

코딩, 통계, 도메인 세가지를 알아야 한다

# workspace 생성
mkdir workspace

우분투를 분석 서버라고 생각하고 진행할 것이다.
그때 필요한 확장팩 WSL 다운로드

인덱스가 있는 데이터를
sequence형 데이터

자료구조 - list
- 원소 - 객체혼합가능
- sequence 
	- positive index
	- negative index
 	- []

import request


---
<2일차>
jupyter-notebook 실행
터미널에 sudo apt install jupyter-core
명령어 jupyter-notebook 로 주피터 노트북 실행(링크 클릭)

TCP / IP 
데이터를 주고받을때 사용하는 프로토콜 = TCP
ip address
protocoll = 약속

ip 도 port 처럼 유일해야함 겹치면 안된다.
ip 주소를 도메인 이름으로 연결해주는것이 DNS(DOMAIN NAME SERVER)

주피터 서버 다시 여는것
juqyter notebook
컨피그 파일 생성
jupyter notebook --generate-config
Writing default config to: /home/swp/.jupyter/jupyter_notebook_config.py

d: 폴더 -: 파일
rwx	r-x	r-x
me	group	other
r:2^2	w:2^1	x:2^0
권한을 바꾸는 명령어: chmod 646 [파일명]
다른 방법: chmod [user, group, other]+[권한] [파일명] (권한 추가)
다른 방법: chmod [user, group, other]-[권한] [파일명] (권한 회수)

vim 설명
처음들어가면 보기모드
i : 쓰기모드
q : 강제 종료
w : 쓰기
wq : 쓰고나가기

주피터노트북 비밀번호 설정법
from jupyter_server.auth import passwd
passwd()
psw1
'비밀번호 토큰 확인'

vim jupyter_notebook_config.py


# password 키워드  찾기 
:/password 
c.ServerApp.password = ""
n : 다음 찾기 
N : 이전 찾기 

:/notebook_dir 
c.ServerApp.notebook_dir = ""

# 쓰고 나가기 
:wq 


크롤링
restful api
web	- get
	- post
 module	- requests
 



2024.04.03

# 프로세스 확인 
ps 
## 모든 프로세스 확인 
ps -ef 

## | 
## grep 
ps -ef | grep python
| = 왼쪽의 결과를 오른쪽으로 넘겨줌


커널
- 커널에는 제어하는 장치의 지원 여부 정보, 하드웨어 성능, 하드웨어를 제어하는 코드들이 들어있음
- 리누스 토발즈는 이를 커널이라고 부르는 리눅스의 핵심을 개발했고, 지금도 업데이트 중이다


openssh-server 설치
명령어: sudo apt install openssh-server

# 가상환경 만들기
pip install pip install virtualenv 
(설치)
python3 -m virtualenv venv 
(python으로 메세지 보내줘 virtualenv에 venv이름으로)

# pip 설치 방법
pip install pandas
pip install pandas==1.2.0
pip uninstall pandas 

# pip 버전 확인
pip list 
pip freeze 

# 가상환경 다른 사람한테 줄때
pip list --format=freeze > requirements.txt
pip list -format=freeze > requirements.txt

# requirements.txt 파일 일괄설치
pip install -r requirements.txt

# nohup -> session 유지 
# & -> background 
nohup jupyter-notebook &

# 일반계정 
nohup jupyter-notebook --ip=0.0.0.0 & 

# root
nohup jupyter-notebook --allow-root --ip=0.0.0.0 & 



ajax
비동기방식으로 


<미니과제>
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

error : 모든 파일에 동일한 데이터 저장됨
해결 : get_naver_stock()에서 pass 지우고 리턴을 만들어준다


데이터 수집을 위해 사용하는 것이 selenium
단점: 느리다

selenium 원래 목적: 자동화
많이 사용하는 분야는 QA




20240404
ip address 관련 설명
ip 구조는 

서로 망이다르면 라우터라는 장비를 사용해줘야한다
명령어: swp@LAPTOP-BTRBRSBB:~$ ping -c 3 8.8.8.8

8.8.8.8 = 구글의 DNS서버


# 네트워크 프로그램 설치 
sudo apt install net-tools 

# port 확인
sudo netstat -ntlp | grep [포트] 


# 실행되고 있는 실행파일의 위치 
which 
which google-chrome

pip install webdriver_manager


miniconda 설치
아나콘다로 가상환경 설정 가능
* 윈도우 powershell에서는 사용 불가

miniconda 실행 명령어
conda activate [서버이름] # 가상환경 활성화
conda dectivate [서버이름] # 가상환경 비활성화







20240408
리눅스 명령어
swp@LAPTOP-BTRBRSBB:~/workspace/남성$ ls -l | grep ^- | wc -l
ls : list
grep : 찾기
wc : word count


CSRF: 사이트간 위조를 방지하기 위한 기법

<인코딩>
라벨 인코딩:
원핫 인코딩:


ddof 자유도


t test: 샘플로 모집단을 예측하고 싶어 만든 것







2024.04.09
파이썬은 얇은 카피를 사용한다.

<class>
클래스는 객체지향 프로그래밍에서 가장 핵심이되는 개념이다.
객체지향(OOP): 
ex) tv 라는 클래스를 만든다하면 

class 내부에서 구현된 함수는 method라고 한다.

클래스 안에 사용가능한 함수 보는 명령어: dir(a)
내부에서 쓰는 기능중에 되도록 사용하지 말아야하는 것 

파이썬에서 외부로 공개하고 싶은 기능과 내부의 비공개 기능의 차이가 별로 없음
"__" 로 시작하는 함수들은 조심하기로 약속한 것이다.

객체는 상속이 가능하다.

모든 객체가 실행될때 초기화부터 시작하는데 클래스 생성시 def __init__(self): 를 만들어 주어야한다.

클래스로 인해 생성된 객체를 인스턴스라고 한다.
인스턴스는 독립적이다.

파이썬의 모든것들은 정확히 말하면 인스턴스객체이다.


의도적으로 에어를 출력하는 코드
raise ValueError('price must be positive')
의도적으로 에러를 만드는 이유: 파이썬 버전이 맞지 않거나 제작자의도와 달리 사용할때

같은 이름의 메서드를 다시 정의 하는것: 오버라이딩

파이썬에서는 다중상속이 가능하다.

모델 서빙: 장고, 플라스크을 사용하여 


<framework>
프레임워크: 이미 기능을 할 수 있도록 만들어놓은 프로그램



Web Application Server
-> WAS 서버라고 부른다
ex) Tomcat

Web Server
ex) Apache, Nginx


Load Balancing: 부하를 분산시켜줌
n 개의 web 서버를 모니터링한다.


Docker - 컨테이너 환경에서 돌 수 있도록 도와주는 프레임워크


Hadoop = Data Lake
(점점 인기가 식어가고 있음)
정형, 비정형, 반정형 데이터 모두 저장 가능
자바기반 Map Reduce 구현

Hive 

spark -> Functional Programming
	func -> func
 - 병렬/분산 처리 가능
 

 Scala언어 -> pyspark, sparkR
Spache Spark
- DateBricks(데이터를 만져서 머신러닝 돌리는 언어)



<mysql 설치>
sudo apt install mysql-server
sudo service mysql status


<mysql 서버 시작>
swp@LAPTOP-BTRBRSBB:~/workspace$ sudo service mysql start
sudo service mysql start[stop/status/restart]


<mysql 실행>
swp@LAPTOP-BTRBRSBB:~/workspace$  sudo mysql -uroot -p


sql에서 % = 모든 아이피를 허용하겠다.

mysql, mariaDB = 3306포트를 사용한다

사용자 생성

<mysql 실행시 에러>
swp@LAPTOP-BTRBRSBB:~/workspace$ mysql -uswp -p
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'
소켓오류 

해결1: sudo mysql -uswp -p
해결2: # mysql 환경파일의 폴더
cd /etc/mysql/mysql.conf.d
sudo vim mysqld.cnf 
bind-address            = 0.0.0.0


데이터에서 제일 빠른 기법은 hash

pip install sqlalchemy
sqlalchemy : ORM(Object Relational Mapping)





---
2024.04.11
<함수 데커레이터>
파이썬의 특수한 기법들


프로그램과 통신하는 모든 프로그램을 api라고 한다.
인터넷을 통해 전달받은 api를 RESTful API 라고한다.

질적 데이터
범주형 데이터

label encoding
a->0
b->1

onehot encoding
해당값을 1로 표시하는 인코딩


출력값을 ... 쓰지말고 다 보여줘 명령어
pd.set_option('display.max_rows', None)


<판다스 melt() 함수>
pd.melt(seven_df, id_vars=['company', 'name', 'sido', 'address'])
id_vars: 기준이되는 컬럼


# mysql에 직접 붙는 패키지
import pymysql


데이터 분석에서의 차원은 컬럼을 말한다.
데이터 분석에서 얘기하는 차원의 저주는 컬럼을 말하며 컬럼이 늘어날때 마다 데이터가 지수 그래프로 늘어나야 한다.


# "" -> None 교체 
df.store_tel = df.store_tel.replace("", None)

# NaN -> None 으로 replace 
df2 = df.where(pd.notnull(df), None)


# DB에 확정적으로 입력하기 위한 명령어
con.commit()







---
2024.04.15
재귀방식 = 스택구조를 가지고 있다
주의) 파이썬에서는 스택에 자한을 걸어놨다

코루틴방식 = yeild를 만나면 잠시 멈추었다가 시작하는것

Stack: FILO(first in last out)


 # jupyter notebook 에서 sql 사용하려면
 pip install ipython-sql

%load_exit sql



오류가 뜬다면
pip install mysqlclient


referance
Merge, join, concatenate and compare — pandas 2.2.2 documentation (pydata.org)
-> https://pandas.pydata.org/docs/user_guide/merging.html


concat()


merge()
RDBMS 에서 






2024.04.16
# db backup 
sudo mysqldump -uroot classicmodels > ~/backup.sql

# db 복원 
mysql -uroot [db명] < ~/backup.sql 


> : 기존내용 덮어씌우기
>> : 기존내용에 추가



<개인키와 공개키 설정>
# 윈도우의 터미널에서 
ssh-keygen -t rsa
아무것도 입력하지 말고 그냥 엔터*3


1. 윈도우 .ssh 폴더에서 
2. id_rsa.pub 메모장 열기 -> 내용 복사 
3. wsl(서버) authorized_key 
vim authorized_key 
마지막줄에 복사한 내용 붙여넣기, 저장하기 
4. 윈도우에서 
ssh {id}@{ip} 



<sql>
substr("문자열", 시작값, 갯수): 특정문자열 뽑아오는 함수

CASE WHEN 조건 THEN 결과 END

DENSE_RANK(): 
100점	1
100점	1
99점	2
99점	2
80점	3


RANK():
100점	1
100점	1
99점	3
99점	3
80점	5


서브쿼리
쿼리 안에 쿼리 넣을 수 있다. () 괄호로 감싸주고 이름을 지정해줘야 한다.







---
# 2024.04.24

인공지능 동의 용어표
https://realblack0.github.io/2020/03/23/thesaurus.html


bert paper
버트 모델은 자연어처리 알고리즘
















