import requests
import json
import datetime
import time
import pymysql
def index():
    url = 'https://eth.tokenview.com/v2api/chart/?coin=eth&type=daily_tx_cnt&splice=14'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    trade = [0 for _ in range(14)]
    time14 = [0 for _ in range(14)]
    time14[13] = datetime.date.today()
    for i in range(1, 14):
        time14[13 - i] = time14[13] - datetime.timedelta(days=i)
    for i in range(0, 14):
        trade[i] = data[i][time14[i].strftime('%Y-%m-%d')]
        # print(trade[i],time14[i])
    return  time14,trade

def index_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    date = index()[0]
    amount =index()[1]
    sql1 = "truncate table trade;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    for i in range(4,14):
        sql = "insert into trade (date_,amount) values ('%s','%d');" % (date[i].strftime('%y-%m-%d'),amount[i])
        try:
            db.begin()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

def index1():
    url = 'https://eth.tokenview.com/v2api/chart/?coin=eth&type=daily_price&splice=30'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    price = [0 for _ in range(30)]
    time30 = [0 for _ in range(30)]
    time30[29] = datetime.date.today()
    for i in range(1, 30):
        time30[29 - i] = time30[29] - datetime.timedelta(days=i)
    for i in range(0, 30):
        price[i] = data[i][time30[i].strftime('%Y-%m-%d')]
        price[i] = round(price[i], 2)
    return time30,price,

def index1_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    date = index1()[0]
    price =index1()[1]
    sql1 = "truncate table price;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    for i in range(20,30):
        sql = "insert into price (date,price,date1,price1) values ('%s','%f','%s','%f');" % (date[i].strftime('%y-%m-%d'),price[i],date[i].strftime('%y-%m-%d'),price[i])
        try:
            db.begin()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

def index2():
    url = 'https://eth.tokenview.com/api/chainstat/eth'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    priceUsd = data['priceUsd']
    changeUsd = data['changeUsd24h']
    totalSupply = data['totalSupply']
    sentValue = data['sentValue24H']
    hashrate = data['hashrate']
    addressCount = data['addressCount']
    difficulty = data['difficulty']
    blockn = data['block_no']
    txCount24 = data['txCount24H']
    size = data['size']
    holders = data['holders']
    txCount = data['txCount']
    turnoverRate = data['turnoverRate']
    return  priceUsd,changeUsd, totalSupply,sentValue,hashrate,  addressCount , difficulty ,  blockn, txCount24,size,holders,txCount,turnoverRate

def index2_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    priceUsd = index2()[0]
    priceUsd = float(priceUsd)
    changeUsd= index2()[1]
    changeUsd = float(changeUsd)
    changeUsd = round(changeUsd ,2)
    totalSupply= index2()[2]
    totalSupply = float(totalSupply)
    totalSupply = round(totalSupply,2)
    sentValue= index2()[3]
    sentValue = float(sentValue)
    sentValue = round(sentValue,2)
    hashrate= index2()[4]
    hashrate = float(hashrate)
    hashrate /= 1000000000000000
    hashrate = round(hashrate, 2)
    addressCount= index2()[5]
    addressCount = float(addressCount)
    difficulty= index2()[6]
    difficulty = float(difficulty)
    difficulty /= 1000000000000000
    difficulty = round(difficulty, 2)
    blockn= index2()[7]
    blockn = int(blockn)
    txCount24= index2()[8]
    size= index2()[9]
    # size = int(size)
    holders= index2()[10]
    holders = int(holders)
    txCount= index2()[11]
    turnoverRate = index2()[12]
    turnoverRate = float(turnoverRate)
    sql1 = "truncate table massage;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    sql = "insert into massage (priceUsd,changeUsd, totalSupply,sentValue,hashrate,  addressCount , difficulty ,  blockn, txCount24,size,holders,txCount,turnoverRate) values ('%f','%f','%f','%f','%f','%d','%f','%d','%d','%c','%d','%d','%f');" % (priceUsd,changeUsd, totalSupply,sentValue,hashrate,  addressCount , difficulty , blockn, txCount24,size,holders,txCount,turnoverRate)
    try:
        db.begin()
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

def index3():
    url = 'https://eth.tokenview.com/v2api/chart/?coin=eth&type=daily_active_address&splice=14'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    address = [0 for _ in range(14)]
    time14 = [0 for _ in range(14)]
    time14[13] = datetime.date.today()
    for i in range(1, 14):
        time14[13 - i] = time14[13] - datetime.timedelta(days=i)
    for i in range(0, 14):
        address[i] = data[i][time14[i].strftime('%Y-%m-%d')]
    return time14,address,

def index3_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    date = index3()[0]
    address =index3()[1]
    sql1 = "truncate table address;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    for i in range(4,14):
        sql = "insert into address (date__,address) values ('%s','%d');" % (date[i].strftime('%y-%m-%d'),address[i])
        try:
            db.begin()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

def index4():
    url = 'https://eth.tokenview.com/api/blocks/eth/1/10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    block_no = [0 for _ in range(10)]
    minerAlias = [0 for _ in range(10)]
    reward = [0 for _ in range(10)]
    txCnt = [0 for _ in range(10)]
    sentValue = [0 for _ in range(10)]
    for i in range(0, 10):
        block_no[i] = data[i]['block_no']
        try:
          minerAlias[i] = data[i]['minerAlias']
        except Exception as e:
          minerAlias[i] = '****'
        reward[i] = data[i]['reward']
        reward[i] = float(reward[i])
        reward[i] = round(reward[i],3)
        txCnt[i] = data[i]['txCnt']
        sentValue[i] = data[i]['sentValue']
        sentValue[i] = float(sentValue[i])
        sentValue[i] = round(sentValue[i],3)
    return block_no,minerAlias,reward,txCnt,sentValue

def index4_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    block_no = index4()[0]
    minerAlias =index4()[1]
    reward = index4()[2]
    txCnt = index4()[3]
    sentValue = index4()[4]
    sql1 = "truncate table trademassage;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    for i in range(0,10):
        sql = "insert into trademassage (block_no,minerAlias,reward,txCnt,sentValue_) values ('%d','%s','%f','%d','%f');" % (block_no[9-i],minerAlias[9-i],reward[9-i],txCnt[9-i],sentValue[9-i])
        try:
            db.begin()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

def index5():
    url = 'https://tokenview.com/api/block/latest'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    response = requests.get(url=url, headers=headers)
    text = response.text
    jsonobj = json.loads(text)
    data = jsonobj['data']
    network = [0 for _ in range(14)]
    priceUsd_ = [0 for _ in range(14)]
    changeUsd24h= [0 for _ in range(14)]
    for i in range(0, 14):
        network[i] = data[i]['network']
        priceUsd_[i] = data[i]['priceUsd']
        changeUsd24h[i] = data[i]['changeUsd24h']
    return network,priceUsd_,changeUsd24h

def index5_():
    try:
        db = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='root', db='trade', charset='utf8mb4')
        print('连接数据库成功')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    network = index5()[0]
    priceUsd_ =index5()[1]
    changeUsd24h = index5()[2]
    sql1 = "truncate table messages;"
    try:
        db.begin()
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    for i in range(0,14):
        sql = "insert into messages(network,priceUsd_,changeUsd24h) values ('%s','%s','%s');" % (network[i],priceUsd_[i],changeUsd24h[i])
        try:
            db.begin()
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
def loop_monitor():
    while True:
        index()
        index_()
        index1()
        index1_()
        index2()
        index2_()
        index3()
        index3_()
        index4()
        index4_()
        index5()
        index5_()
        time.sleep(10)
if __name__ == "__main__":
    loop_monitor()
