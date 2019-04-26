import psycopg2

conn = psycopg2.connect("user=postgres password=password")
current = conn.cursor()
#tableList=["StatisticsTable","ProfilesTable","FinancesTable"]

current.execute("DROP TABLE IF EXISTS StatisticsTable")
current.execute("DROP TABLE IF EXISTS ProfilesTable")
current.execute("DROP TABLE IF EXISTS FinancesTable")

StatisticsTable = current.execute("CREATE TABLE StatisticsTable (stat_ticker varchar PRIMARY KEY,marketcap  varchar,enterprise_value varchar,profit_margin varchar ,return_on_assets varchar,gross_profit varchar ,total_cash varchar ,total_debt varchar ,current_ratio varchar  ,operating_cash_flow varchar ,levered_free_cash_flow varchar );")
ProfilesTable = current.execute("CREATE TABLE ProfilesTable (sprof_ticker varchar PRIMARY KEY,name  varchar,Address  varchar,phonenum varchar,website  varchar ,sector  varchar ,industry  varchar ,full_time  varchar ,bus_summ varchar );")
FinancesTable = current.execute("CREATE TABLE FinancesTable (Fin_ticker  varchar PRIMARY KEY,Total_Revenue  varchar,Cost_of_Revenue  varchar,Income_Before_Tax varchar,Net_Income  varchar);")

# no = int(input("Enter rollNo = "))
# name = input("Enter name = ")
#
# query = "INSERT INTO Student (id,name) VALUES (%s,%s)"
# data = (no, name)
# current.execute(query,data)

conn.commit()
conn.close()
current.close()