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
    payload['tmpInqStrDt'] = date_
    try:
        datetime.strptime(date_, "%Y-%m-%d")
    except:
        print("다시 입력")
        # date_ = str(date.today())
        return -1
    
    payload['inqStrDt'] = date_.replace("-", "")
    url = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"
    r = requests.post(url, data=payload)
    exchange = pd.read_html(r.text)[0]
    exchange.columns = ["_".join(x[:2]) for x in exchange.columns]
    return exchange.loc[exchange['통화_통화'].str.find(f"{code_.upper()}") > -1, '현찰_파실 때'].iloc[0,0]



from datetime import date
if __name__ == "__main__":
    print(f"get_exchange('usd', str(date.today()))")





