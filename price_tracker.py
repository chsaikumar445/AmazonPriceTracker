import requests
from bs4 import BeautifulSoup

def check_price():

  url='https://www.amazon.in/Canon-EOS-200D-II-Digital/dp/B07RJWB548'
  headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

  page=requests.get(url,headers=headers)
  page_coverted=BeautifulSoup(page.content, 'html.parser')

  title=page_coverted.find(id='productTitle').get_text()
  title=title.strip()
  print(title)

  price=page_coverted.find(id='priceblock_ourprice').get_text()
  converted_price=price[2:8]
  splitted=converted_price.split(',')
  joined=splitted[0]+splitted[1]
  converted_price=int(joined)
  print(converted_price)

  if(converted_price < 50000):
    discord_notification()

  else:
    print('The current price is: '+ str(converted_price))



def discord_notification():

  payload={
    'content': "The price is below 50k check the canon 200d now in amazon"
  }
  header={
    'authorization' : 'NjExMTEwMzg0MTUzMjY0MTI5.X-is2A.KyF1AS3LJjpGYizQQQVW13SjRSo'
  }
  Request_URL='https://discord.com/api/v8/channels/792783399672610827/messages'
  discord_req= requests.post(Request_URL,
  data=payload,
  headers=header)





check_price()