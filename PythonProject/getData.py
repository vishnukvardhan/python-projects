import requests
from bs4 import BeautifulSoup
import re
import psycopg2

# connecting to DataBase
conn = psycopg2.connect("user=postgres password=password")
current = conn.cursor()
# read from file
num = 0
comName = []
tickerToInsert = []
with open("tickers.txt") as fil:
    for line in fil:
        n=line.split("--->")
        tickerToInsert.append(n[0].rstrip())
        comName.append(n[1].rstrip())


for add in comName:
# to Staristics
    listToFindData1 = ["Market Cap (intraday) 5","Enterprise Value 3","Return on Assets (ttm)","Total Cash (mrq)","Operating Cash Flow (ttm)","Levered Free Cash Flow (ttm)","Total Debt (mrq)","Current Ratio (mrq)","Gross Profit (ttm)","Profit Margin "]
    listData1 = []
    site = open('/Users/vishnuk/PycharmProjects/untitled1/'+add+'/statistics.html')
    soup = BeautifulSoup(site,'html.parser')
    table = soup.find(class_='Fl(start) W(50%) smartphone_W(100%)')
    lines = [th.get_text() for th in table.find('tr').find_all('th')]
    for rows in table.find_all('tr')[0:]:
        data = [td.get_text() for td in rows.find_all('td')]
        if listToFindData1.__contains__(data[0]):
            listData1.append(data[1])
# store in DataBase
    query ="INSERT INTO StatisticsTable (stat_ticker,marketcap,enterprise_value,profit_margin ,return_on_assets,gross_profit,total_cash,total_debt,current_ratio,operating_cash_flow,levered_free_cash_flow) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (tickerToInsert[num],listData1[0],listData1[1],listData1[2],listData1[3],listData1[4],listData1[5],listData1[6],listData1[7],listData1[8],listData1[9])
    current.execute(query, data)

# to Financials
    listToFindData = ["Total Revenue","Cost of Revenue","Income Before Tax","Net Income"]
    listData = []
    site = open('/Users/vishnuk/PycharmProjects/untitled1/'+add+'/financials.html')
    soup = BeautifulSoup(site,'html.parser')
    table = soup.find(class_='Mt(10px) Ovx(a) W(100%)')
    lines = [th.get_text() for th in table.find('tr').find_all('th')]
    for rows in table.find_all('tr')[0:]:
        data = [td.get_text() for td in rows.find_all('td')]
        if len(data) > 3 :
            if listToFindData.__contains__(data[0]):
                listData.append(data[1])
# store in DataBase
    query = "INSERT INTO FinancesTable (Fin_ticker,Total_Revenue,Cost_of_Revenue,Income_Before_Tax,Net_Income) VALUES (%s,%s,%s,%s,%s)"
    data = (tickerToInsert[num],listData[0],listData[1],listData[2],listData[3])
    current.execute(query, data)


# to profile


    addData = []
    im = 1
    site = open('/Users/vishnuk/PycharmProjects/untitled1/'+add+'/profile.html')
    soup = BeautifulSoup(site,'html.parser')

    name = soup.find(class_='Fz(m) Mb(10px)')
    addData.append(name.get_text())

    table = soup.find(class_='Mb(25px)')
    table1 = table.find_all('p')
    table2 = table.find_all('a')
    for rows in table1:
        r =re.split("http://",rows.get_text())
        if im == 1:
            addData.append(r[0])
            im = 2
    for row in table2:
        addData.append(row.get_text())
    slp = re.split("Industry:\xa0|Sector:\xa0|Time Employees:\xa0",r[0])
    addData.append(slp[1])
    addData.append(slp[2])
    addData.append(slp[3])
    addData[1] = addData[1].translate({ord(i): None for i in addData[2]})
# store in DataBase
    query = "INSERT INTO ProfilesTable (sprof_ticker,name,Address,phonenum,website,sector,industry,full_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (tickerToInsert[num],addData[0],addData[1],addData[2],addData[3],addData[4],addData[5],addData[6])
    current.execute(query,data)


    num += 1


conn.commit()
conn.close()
current.close()


print("Data Storage Successful.......")