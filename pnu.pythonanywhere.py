import pandas as pd
import jdatetime
import requests

GROUP_ID = ''
BOT_TOKEN = ''
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_ID}&text='
df = pd.read_csv('data.csv')
jdatetime.set_locale('fa_IR')

def send_msg(base, text):
    requests.get(f'{base}{text}').json()

send_msg(BASE_URL, f'Bot started {str(jdatetime.datetime.today())}')

flag = True
today = jdatetime.date.today().strftime("%Y/%m/%d")
for index, row in df.iterrows():
    if(row['date'] == today):
        flag = False
        text = f"{row['name']}\n{row['date']}"
        send_msg(BASE_URL, text)
if flag:
    send_msg(BASE_URL, 'Enjoy your day!')
