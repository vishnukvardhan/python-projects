import psycopg2
f=open('stopwords.txt','r')
Stop_Word_List=list(f)
Stop_word=[]
for i in Stop_Word_List:
	i=i.replace('"','')
	w=i.strip()
	Stop_word.append(w)
#print(Stop_word)
#checks if word is stopword or not
def isStopword(word,Stop_word):
	for k in Stop_word:
		if(k==word):
			return True
	return False
#creating quarty
def quary_gen(words,dict,dict1,comp,com):
	From="com"
	for i in words:
		if 'wh' in i:
			select="select"
			print("s")
			dict3=dict1.keys()
			print(dict3)
		elif i in dict3:
			att=i
			attri=dict1[i]
		elif i in comp:
			na=i
			From=i
		elif i in com:
			na=i
			From=i
		else:
			print("a")
	return select+" "+att+" "+"from"+" "+attri+" "+"where"+" "+na
#removing Stopwords
search=input("search")
search_list=search.split(' ')
req_query=[]
for k in search_list:
	if(isStopword(k,Stop_word)):
		print("")
	else:
		req_query.append(k)
# creating dict for tables in Database
dict={"stat_ticker" :"stat_ticker","marketcapital":"marketcap","marketcap": "marketcap","enterprise_value" :"enterprise_value","return_on_assets" : "return_on_assets","total_cash" : "total_cash","operating_cash" :"operating_cash_flow","levered_free_cash_flow" :"levered_free_cash_flow","total_debt" : "total_debt","current_ratio" :"current_ration","gross_profit" :"gross_profit","proffit_margin" :"profit_margin","ticker" :"prof_ticker","name" : "name","Address" : "address","phonenum" :"pno","website" : "web","sector" : "sector","industry" :"industry","full_time" :"full_time","bus_summ" :"bus_sum","Fin_ticker" : "fin_ticker","Total_Revenue": "total_rev","Cost_of_Revenue": "cost_rev","Income_Before_Tax" : "income_beftax","Net_Income" : "net_income"}
f=open("tickers.txt",'r')
Tickername=list(f)
Comp_names=[]
Com_names=[]
for i in Tickername:
	inc=i.split("::")
	Comp_names.append(inc[1])
	Com_names.append(inc[0])
#print(Comp_names)
dict1={"stat_ticker" :"statistics","marketcap":"statistics","enterprise_value" :"statistics","return_on_assets" : "statistics","total_cash" : "statistics","operating_cash_flow" :"statistics","levered_free_cash_flow" :"statistics","total_debt" : "statistics","current_ration" :"statistics","gross_profit" :"statistics","profit_margin" :"statistics","prof_ticker" :"profile","name" : "profile","address" : "profile","pno" :"profile","web" : "profile","sector" : "profile","industry" :"profile","full_time" :"profile","bus_sum" :"profile","fin_ticker" : "finances","total_rev": "finances","cost_rev": "finances","income_beftax" : "finances","net_income" : "finances"}
quary=quary_gen(req_query,dict,dict1,Comp_names,Com_names)
conn = psycopg2.connect("user=postgres password=password")
cur=conn.cursor()
cur.execute(quary)
rows=cur.fetchall()
print(rows)
conn.close()