import requests
from bs4 import BeautifulSoup


sum = 0
for a in range(1,174):
    url = 'http://www.risultati-ammissione.polimi.it/2019_20064_html/2019_20064_grad_'+ str(a) + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    info = soup.select(".Dati1")

    length = len(info)

    i = 0
    counter = 0

    while i < length:
        if (i+6) <= length:
            points = float(info[i+1].text.replace(',','.'))
            status = info[i+5].text
            if( float(points) >= 59.50 and not("Non idoneo / Not eligible" in status or
                     "Immatricolazione non consentita / Enrolment is not possible" in status)):
                counter+=1
            i+=6
    sum+=counter
print(sum)
