import psycopg2

conn = psycopg2.connect("user=postgres password=password")
current = conn.cursor()

# read tables file
f=open('config.txt','r')
file1=f.read()

# read stopwords file
f2=open('stopwords.txt','r')
file2=f2.read()

# read file tickers
genTik = []
genName= []
with open("tickers.txt") as fil:
    for line in fil:
        n=line.split("--->")
        genTik.append(n[0].rstrip())
        genName.append(n[1].rstrip())

# to remove stopwords
new=[]
file1Data = file1.split(";")

q = input("Enter A Querie  ")
que = q.split(" ")
if que[0]=="how" and que[1]=="much" :
    new.append("how much")
if que[0]=="how" and que[1]=="many" :
    new.append("how many")


for i in range(0,len(que)):
      if '"'+que[i]+'"' not in file2:
          new.append(que[i])

print(new)

tickerPrimaryKey = "null"
# to generate tickers
for j in new:
    for k in range(len(genName)):
        p = genName[k].split(" ")
        if j == p[0]:
            tickerPrimaryKey = genTik[k]
            print(genTik[k])
col2 = ""
tableIndex=5
for tables in range(len(file1Data)):
    tab = file1Data[tables].split("\n")
    #print(tab,"++++")
    for line in range(len(tab)-1):
        col = tab[line].split(":")
        col1 = col[0].replace("_"," ").rstrip()
        #print(col1.lstrip())
        if q.find(col1) == -1:
            continue
        else:
             if col[1].__contains__(que[0]):
                print(col[1])
                col2 = col1.replace(" ", "_")
                tableIndex = tables

if q.__contains__("highest"):


    print(col2)
    print(tableIndex)
    print(tickerPrimaryKey)

    if tickerPrimaryKey == "null":
        if tableIndex == 0:
            querieToDatabase = "select stat_ticker from StatisticsTable  where " + col2 + "= (select Max(" + col2 + ") from StatisticsTable );"
        elif tableIndex == 1:
            querieToDatabase = "select sprof_ticker from ProfilesTable  where " + col2 + "= (select Max(" + col2 + ") from ProfilesTable );"
        elif tableIndex == 2:
            querieToDatabase = "select Fin_ticker from FinancesTable  where " + col2 + "= (select Max(" + col2 + ") from FinancesTable );"

        current.execute(querieToDatabase)
        dat = current.fetchone()
        # data = current.fecthall()
        st = str(dat)
        st = st.replace("(", " ")
        st = st.replace(")", " ")
        st = st.replace(",", " ")
        st = st.rstrip()
        for v in range(len(genTik)):
            d = " " + "'" + genTik[v] + "'"
            if d == st:
                print(genName[v] + " has the highest " + col2)





elif tableIndex == 0:
    querieToDatabase = "select "+col2+" from StatisticsTable where stat_ticker = "+"'{}'".format(tickerPrimaryKey)+";"
elif tableIndex == 1:
    querieToDatabase = "select "+col2+" from ProfilesTable where sprof_ticker = "+"'{}'".format(tickerPrimaryKey)+";"
elif tableIndex == 2:
    querieToDatabase = "select "+col2+" from FinancesTable where fin_ticker = "+"'{}'".format(tickerPrimaryKey)+";"
# elif tickerPrimaryKey =="":






print(querieToDatabase)

current.execute(querieToDatabase)
dat = current.fetchone()
print(dat)
#data = current.fecthall()


conn.commit()
conn.close()
current.close()