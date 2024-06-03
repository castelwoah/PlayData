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



---
# 2024.04.25

## 장고 가상환경 구축

## virtualenv 
 - python module 
 - 현재 설치된 파이썬 버전을 따라감 
 - python -m virtualenv venv
   -> 폴더 생성  (venv)  
   -> 가상환경 사용하기 
- source ./venv/bin/activate 

## conda 
 - anaconda, miniconda를 설치해야 사용 가능 
 - conda -> 32bit 환경 세팅 가능 
 - 다양한 버전의 파이썬을 세팅가능 

장고는 웹 프레임워크




## views.py
```
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

  

def TellHello(request):

    html = "<h1> Hi!!!! </h1>"

    return HttpResponse(html)
```



## url.py
```
from django.contrib import admin

from django.urls import path

from practice import views

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path('Hello/', views.TellHello),

]
```


http://127.0.0.1:8000/

127.0.0.1 = 본인 자신 아이피 / 전세계 공통


코드: 
`question = models.ForeignKey(Question, on_delete=models.CASCADE)`

on_delete=models.CASCADE = 더미 데이터가 생기지 않게 자동으로 지워 달라는 옵션


동기: 요청하고 계속 기다림


비동기: 요청하고 끝나면 알려줌


---
<오후 수업>
비용함수 = 사용자가 정의하는 하이퍼파라미터

역행렬 이용방법으로 
경사하강이라는 방법을 사용할 것 이다.


---
---

# 2024.04.26



## 범주형 데이터


인공지능이 인식을 하지 못한다.

one-hot encoder를 사용하면 컬럼들이 더 늘어난다.


### 스케일러
- 각각의 컬럼들의 단위가 다르기 때문에 의미가 다르다 이를 보완하기 위해 스케일링을 사용한다.
- 또한 속도향상을 위해

(참고)
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=demian7607&logNo=222009975984




트레인 시켰던 스케일러로만 변경을 시켜줘야 한다.

StandardScaler
- 표준화 방식
- 컬럼들의 평균 0, 표준편자 1
- 최솟값, 최댓값 제한 없음
- 평균과 표준 표준 편차를 쓰기 때문에 이상치에 민감하다 
- 회귀보다 분류에 유용

MinMaxScaler
- 컬럼들의 값이 0~1사이
- 최소값 0, 최댓값 1
- 이상치에 매우 민감
- 분류보다 회귀에 유용


MaxAbsScaler
- 최대절댓값이 1 최솟값이 0이 되도록 스케일링
- 모든 값이 -1 ~ 1 사이에 표현됨
- 데이터가 양수만 있을 경우 MinMax 와 동일
- 이상치에 매우 민감
- 분류보다 회귀에 유용
- 별로 안씀


RobustScaler
- 평균과 분산 대신 중앙값과 사분위 값
- 중앙값 0 으로 설정 IQR을 사용하여 이상치에 영향을 최소화(이것이 목표)
- quantile_range 파라미터로 조정하여 이상치 제어



AUTO 인코더 
ex) GAN



### 단순선형회귀


상관관계: 두 가지 변수간의 어떤 선형적 관계를 갖고 있는지를 분석

인과관계: 외부 요인을 통제한 상태에서 두 젼수가 원인과 결과의 관계를 맺고 있는지 분석



### 로지스틱 회귀

선형 데이터는 붙여도 선형이기 때문에 비선형으로 한번 꼬아주는데 시그모이드 함수가 대표적인 예시이다.

확률로 얘기해준다.




---
---

# 2024.04.29

## ML
- 구분
	- 지도    - 회귀 - regression - 규제 - Ridge
								 - Lasso
			- 분류 - K-NN - 거리
				   - 로지스틱
				   - 
	- 비지도

- 성능
	- 회귀    - MSE(Mean Squre Error) - 작게하는 것이 목표
			- MAE
			- R^2
	- 확인    - overfitting
			- underfitting
	- 분류    - ACCURACY
			- confusion matrix    - recall
						    -  precision
						    - f1-score
						    - auc
						    - roc

- 전처리
	- EDA
	- 


## 규제

weight 값의 차이를 줄이기 위해 (Lasso)L1, (Ridge)L2 사용
과적합 문제를 일반화 시키는 과정




> 우리가 집중해야 할 것은 성능지표이다.



---

## 정규식

![[Pasted image 20240429111647.png]]

. = 모든 문자


![[Pasted image 20240429111804.png]]
+= 앞에 문자 한번이상 반복


![[Pasted image 20240429111923.png]]


![[Pasted image 20240429111952.png]]


![[Pasted image 20240429112454.png]]



![[Pasted image 20240429113129.png]]



![[Pasted image 20240429113409.png]]




---
---

# 2024.04.30




---
---


# 2024.05.02

## 트리
- 트리 구조는 비선형
- 너무 많은 데이터의 정보는 일반화를 어렵게 만들어 과적합에 빠질 수 있다.
- 단점: 오버피팅이 잘 된다. depth를 제한해줘야 한다.


`from sklearn.model_selection import StratifiedKFold`
- 데이터를 섞어주는 모듈


딥러닝에서는 교차검증이 필요없다.
-> 데이터가 많이 있으니까

머신러닝에서는 데이터가 부족하고 그와중에 검증세트를 빼야하기때문에 교차 검증을 많이 한다.



### 랜덤서치

샘플링하기 때문에 시간은 적게 걸릴 수 있으나 최적의 파라미터인지 확인이 불가하다.


## OPTUNA


---


서브넷 계산법

	172.      26.     224.      1
10101100.00011010.00011000.0000001




---
---

# 2024.05.03

1. wsl -d Ubuntu-20.04 -u root ip addr add 192.168.45.250/24 broadcast 192.168.45.255 dev eth0 label eth0:1
	netsh interface ip add address "vEthernet (WSL)" 192.168.45.100 255.255.255.0
	192.168.45.100 255.255.255.0
	(메모장에 wsl.bat 이름으로 저장)

2. 윈도우에서 작업 스케줄러 검색

3. 새작업 만들기
	- 일반 - 이름 설정
	- 트리거 - 로그온할때
	- 동작 - 파일경로 지




---
---

# 2024.05.07


echo $ 환경변수





---
---

# 2024.05.08






---
---

# 2024.05.09


### 군집 알고리즘



### KMeans 알고리즘
* 대표적인 군집 알고리즘



## 주성분 분석

#### pca
- 선형모델 만들건데 변수가 너무 많을때 변수를 선택하지 않고 압축하여 사용할때

 1. 입력 데이터 세트의 공분산 행렬을 생성
 2. 공분산 행렬의 고유벡터와 고윳값을 계산
 3. 고윳값이 가장 큰 순으로 K개(PCA 변환 차수만큼) 고유벡터를 추출
 4. 고윳값이 가장 큰 순으로 추출된 고유벡터를 이용해 새롭게 입력 데이터를 변환

- 머신러닝의 기반이 되는 개념이다
- 공분산이 큰 방향으로 벡터를 만들고 투영시킨다




### airflow

- 귀찮은 일을 python 을 통해서 자동화 하는 툴





---
---

# 2024.05.10

## convolution

- 데이터의 크기를 축소시킨다

## 패딩

- 데이터를 0으로 감싼다
- 데이터의 크기가 줄어들지 않는다
- 적당한 패딩은 이처럼 이미지 주변에 있는 정보를 잃어버리지 않도록 한다


## 스트라이드

- 한 번 합성곱 연산한 후 다음 계산 영역을 선택할 때 얼마나 이동할지 간격을 정하는 값


## 풀링

- 데이터 차원을 줄이는 방법




![[Pasted image 20240510094149.png]]

답) 3








---
---

# 2024.05.13


### gpu 커널 사용해보기

1. 가상환경 만들기
2. pip install tensorflow == 2.10.0
3. pip install tensorflow-directml-plugin
4. pip install ipykernel
5.  python -m ipykernel install --user --name venv --display-name gpu_venv




커널의 개수가 깊이를 결정한다


### 옵티마이저






\\wsl.localhost\Ubuntu-20.04\root\workspace\teachingcode\dog_model_service\CIFAR모델\model
![[Pasted image 20240513150405.png]]

model.h5 = weight 값

model.jason = 모델구조



---
---
# 2024.05.14


### 활성화 함수
선형을 비선형으로 변환하여 데이터에서 패턴을 찾기 위해

종류
- sigmoid
	- 로지스틱 함수 
- ReLu
	- 이미지 CNN
- Softmax
- tanh
	- RNN
- step function

### 행렬


1차원 -> 벡터
2차원 -> 행렬
3차원 -> 텐서


편향이 낮고 분산이 높으면 과적합
편향이 높고 분산이 낮으면 과소적합



feed forward


### 손실함수

- 학습이 잘 되었는지를 확인하기 위해서
- MSE, RMSE
	- SUM((정답 - 추론값)^2)
	- 작을수록 좋은것



---
오후
django

base.html = 부모파일

user: 
pwd: EnCoRo!23




---
---
# 2024.05.16

- 처음부터 read_csv 메서드를 사용해서 데이터를 읽을 때 컬럼 타입을 지정해서 읽으면 해당 타입으로 데이터프레임이 만들어 진다.
- 메모리도 절약할수 있다.

- pairplot을 도식화 하는 이유: 변수들간의 관계성을 알기 위해



### pandas_profiling

``` python
pip install pandas_profiling
import ydata_profiling
df.profile_report()
```



### 결측치 시각화

``` python
pip install missingno
import pandas as pd 
import missingno
from sklearn.impute import SimpleImputer #결측치 처리함수

missingno.matrix(X)
plt.show()
```




### Django

- Nginx (web)
- Gunicorn (was)



### airflow



### rnn



### container
- kubernetes (k8s)
	- 컨테이너 관리 소프트웨어



### hadoop
- aws s3




---
---
# 2024.05.17

불균형 데이터를 어떻게 처리할 것인가?



## RNN



### gensim 




### word enbeding
단어를 벡터화 시키는것




---
---
# 2024.05.20


오차 역적파법



---
---
# 2024.05.21


LSTM  -> 감성분석 모델 -> BERT 모델 전이학습

### kobert 
- sk 가 사전학습 시킨 모델


### KB-ALBERT
- kb 그룹에서 만든 모델
- 홍보용으로 대충 만들어서 공개함


### ETRI
- 한국전자통신연구원



### 마르코프 체인
- 벨만 방정식
	- dynamic programming




---
---

# 2024.05.22


진행상황:
- LSTM 활용한 주가 예측 ipynb 파일 설명
- 






---
---
# 2024.05.23


### ssh 비번 입력 없이 로그인 하는 법

호스트파일 편

ssh-keygen -t rsa
.ssh 

id_rsa.pub 
내용 복사 

ssh encore@jupyter 

vim ~/.ssh/authorized_keys

위 공개키 붙여넣기 

  
  

config

  

Host jupyter

Hostname 192.168.56.111

User encore







---
---
# 2024.05.29

vs code 자바 확장팩 설치
![[Pasted image 20240529113505.png]]


open jdk 

JDK 개발도구
JRE  개발환경
JVM 개발머신


f1 누르고 create java project

** maven, gradle: 버전 맞춰주는 팩

java 파일을 컴파일 하면 class 파일이 생성된다.
class 파일은 사람이 읽을 수 없다. low 레벨 파일이다.

현재 자바 버전 확인 코드 
```
java --version
```

파이썬과 다른 점은 ";" (세미콜론)을 넣어줘야한다.

java 에서 주석은 
``` java
// 한줄 주석
/*

 * 여러줄 주석은 이렇게

 * 자동으로 달린다.

 */
```


``` java
public static void main(String[] args)
```

이 코드가 가장 먼저 실행된다.


java 타입
![[Pasted image 20240529122535.png]]



### 컴퓨터가 음수를 취급하는 방법

1의 보수

**
1001 -> 9

0110

  

+1 

0111

2의 보수
**
![[Pasted image 20240529123535.png]]




### 덕 타이핑




spring = 모놀리식 방식 = 일체형

msa(microservice architecture) = 모듈화
ex) spring boot, django, flask



Hadoop
자바기반 서비스
Hadoop    -> Hive 

                -> Db -> Hadoop -> 마이그레이션 -> sqoop

                -> pig 

                 - spark 

                - kafka 

                - elk



### 형변환




---
---
# 2024.05.30

### 배치정규화
- Batch Normalization은 **학습 과정**에서 각 배치 단위 별 다양한 분포를 가진 데이터를 각 배치별로 **평균**과 **분산**을 이용해 **정규화**하는 것이다.
- Batch Normalization는 별도의 과정으로 있는 것이 아닌, 신경망 안에 포함되어 학습시 평균과 분산으로 조정하는 과정이다.
- 평균은 0, 표준 편차는 1로 데이터의 분포를 조정할 수 있다.



### 자바 논리연산자
![[Pasted image 20240530102407.png]]




### switch case 구문



## 도커

### 컨테이너





---
---
# 2024.05.31

클래스는 같은 폴더 안에 있어야 한다



### 컨테이너


```
# 현재디스크 용량확인
(base) encore@jupyter:~$ df -h

(base) encore@jupyter:~$ docker images

# 다시 docker 안으로 들어가기
(base) encore@jupyter:/$ docker attach encore

마운트 = 연결


exit -> 도커 종료

# 도커전체 삭제
(base) encore@jupyter:/$ docker ps -a -q
# 삭제 환경변수로 지정
(base) encore@jupyter:/$ docker rm $(docker ps -a -q)
be14560c9454
5fab808980a0
2a0472992810
(base) encore@jupyter:/$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


(base) encore@jupyter:/$ docker run -it --name encore -p 80:80 ubuntu:14.04


root@97542fef4c17:/# apt update
root@97542fef4c17:/# apt install apache2 -y
root@97542fef4c17:/# service apache2 status
 * apache2 is not running
root@97542fef4c17:/# service apache2 start
root@97542fef4c17:/# service apache2 status
 * apache2 is running

```


### 아파치
- 웹 서버
- 기본 80번 포트
(base) encore@jupyter:/$ docker run -it --name encore -p 80:80 ubuntu:14.04
- 외부에서 80번 포트를 내부의 80번 포트로 연결하는 명령어

사용법 : [host port] : [container port]



### 워드프레스 서버 구축
```
(base) encore@jupyter:/$ docker run -d --name wordpressdb -e MYSQL_ROOT_PASSWORD=encore -e MYSQL_DATABASE=wordpress mysql:5.7

(base) encore@jupyter:~$ docker run -d -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=encore -e WORDPRESS_DB_NAME=wordpress --name wordpress --link wordpressdb:mysql -p 80:80 wordpress
```

-d : 백그라운드

mysql을 찾아서 없으면 설치(링크를 통해서)

wordpress와 wordpressdb가 서로 통신한다.



docker 비번
GAnm5rxpLOhWNXyVy%



```
(base) encore@jupyter:~$ docker stop wordpress
wordpress
(base) encore@jupyter:~$ docker stop wordpressdb
wordpressdb
```



```
# 도커 아이디만 확인하는 명령어
(base) encore@jupyter:~$ docker ps -a -q
```



```
(base) encore@jupyter:~$ docker run -d --name mydb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=encore -e MYSQL_DATABASE=wordpress -v ~/data:/var/lib/mysql mysql:5.7


```




-v 옵션 뒤에 있는 위치에 파일 생성 후 동기화 한다.
-> 새롭게 만들어도 복원 가능하다





---
---
# 2024.06.03


# 상속

- 모든 객체는 클래스의 생성자를 호출해야만 생성
- 자식이 부모의 생성자를 직접적으로 호출하지 않더라도 컴파일러가 아래처럼 호출


# 메서드 재정의

- 부모 클래스의 모든 메서드를 자식 클래스가 상속 받아서 기능 그대로 사용할 수도 있지만 기능을 변경해야 할 때도 생긴다.
- 이런 경우 상속된 일부 메서드를 자식 클래스에서 다시 수정해서 사용해야 한다.
- 자바는 이런 경우를 위해 메서드 재정의(overriding) 기능을 제공한다.

## 방법

- 메서드 재정의는 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것을 의미
- 메서드를 재정의할 때는 다음과 같은 규칙ㅇ르 주의해야한다.
	- 부모의 메서드와 동일한 시그니처(리턴 타입, 메서드 이름, 매개 변수 목록)을 가져야 함
	- 접근 제한을 더 강하게 재정의할 수 없음
	- 새로운 예외를 throws할 수 없음


# 부모 메서드 호출

``` java
super.부모메서드()
```

# final 클래스와 final 메서드

- final 키워드는 클래스, 필드, 메서드를 선언할 때 사용할 수 있음
- 해당 선언이 최종 상태이고 그 뒤에 수정될 수 없음을 뜻함
- 상수 취급한다고 말함
## 상속불가

``` java
public final class 클래스 {...}
```

# 재정의 불가


## protected 접근 제한다

- 같은 패키지에서는 default 와 같이 접근 제한이 없지만 다른 패키지에서는 자식 클래스만 접근을 허용


## 타입 변환과 다형성

- 부모 타입으로 자동 타입 변환된 이후에는 부모 클래스에 선언된 필드와 메서드만 접근이 가능
- 변수는 자식 객체를 참조하지만 변수로 접근 가능한 멤버는 부모 클래스 멤버로만 한정됨
- 예외로는 메서드가 자기 클래스에서 재정의되었다면 자식 클래스의 메서드가 대신 호출




---
# 오후

# kafka


## zookeeper

- 하둡 에코 시스템에 포함되어 있음
- 주키퍼의













