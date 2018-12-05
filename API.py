# coding=utf-8
import time
from flask import request
from flask import Flask, session
from SerialRfid.ConnectManage import connectmanage
from kNN import rfid


app = Flask(__name__)


@app.route('/API', methods=['GET', 'POST'])
def hello_world():
    return '您读到的RFID的UID是：'


@app.route('/API/UID/', methods=['GET', 'POST'])
def getalluid():
    serial3 = connectmanage(com='com13', baud=38400, iso='t5557')
    S = time.time()
    serial3.write('0204A510B103')
    C1 = time.time()
    time.sleep(1)
    C2 = time.time()

    serial3.write('AA28010500D3FF')
    T13 = time.time()
    # serial3.write('AA28040500D6FF')
    # # AA 28 04 05 00 D6 FF
    # # 15693
    uid = serial3.GetUid()
    E = time.time()
    staus = rfid(T13 - S + (C2 - C1))
    serial3.close()
    print(uid)
    return "读取到的标签UID"+str(uid)+"目前"+staus


if __name__ == '__main__':
    app.debug = True
    app.run()
