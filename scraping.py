from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://eurovisionworld.com/odds/eurovision'

driver = webdriver.Chrome()
driver.get(url)

head = ['position', 'country', 'song', 'winning chance', 'BET365', 'UNIBET', 'COOL BET', 'BETFAIR SPORT', 'SKY BET', 'BETSSON',
    'COMEON', 'BET FRED', 'SMARKETS', '10BET', '888SPORT', 'BOYLE SPORTS', 'LAD BROKES',
    'BETWAY', 'WILLIAM HILL', 'BETFAIR EXCHANGE']

tbody = driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/main/div[1]/div[2]/div[3]/div[1]/table/tbody')

print(head)
for r in tbody.find_elements(By.XPATH,'./tr'):
    row = []
    for idx, c in enumerate(r.find_elements(By.XPATH,'./td')):
        if idx == 1:
            continue
        elif idx == 2:
            country_song = c.text.split()
            if (country_song[0] == 'San' or country_song[0] == 'United'):
                row.append(country_song[:2][0] + ' ' + country_song[:2][1])
                country = c.text.split(" ", 2)
                song = country_song[2:]
                row.append(' '.join(song))
            else:
                row.append(country_song[:1][0])
                country = c.text.split(" ", 1)
                song = c.text.replace(country[0], '')
                row.append(song[1:])
        else:
            row.append(c.text)
    print(row)