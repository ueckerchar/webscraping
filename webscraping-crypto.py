from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.investing.com/crypto/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
crypto_rows = soup.findAll('tr')


for x in range(1,6):
    td = crypto_rows[x].findAll('td')
    rank = td[0].text.strip()
    coin_name = td[2].text.strip()

    current_price = float(td[4].text.replace(',',''))
    fullday_change = float(td[8].text.replace(',','').replace('%',''))
    cor_price = round(current_price *((100.00-fullday_change)/100.00),2)

    print(f"Coin Rank: {rank}")
    print(f"Coin Name: {coin_name}")
    print(f"Current Price: ${current_price}")
    print(f"24 hour Change: {fullday_change}%")
    print(f"Corresponding Price: ${cor_price}")
    input()
    
#have to do twillio
import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.authToken)

TwilioNumber = "+15095122748"

myCellPhone = "+13619467052"

for row in range(1,6):
    td = crypto_rows[x].findAll("td")
    name = (td[2].text.strip())
    current_price2 = float(td[4].text.replace(",",""))
    if name == "Bitcoin" and current_price2 < 40000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="BTC is below $40,000")

    if name == "Ethereum" and current_price2 < 3000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="ETH is below $3,000")
