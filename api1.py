from sqlite3 import paramstyle
import streamlit as st
#rom dotenv import load_dotenv
import requests
#import os
#load_dotenv()
#servicekey=os.getenv('key')
serviceKey=st.secrets['key']
url = 'http://apis.data.go.kr/1360000/RoadWthrInfoService/getCctvStnRoadWthr'
params ={'serviceKey' : 'key', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'eqmtId' : '0500C00001', 'hhCode' : '00' }

response = requests.get(url, params=params)
print(response.content)