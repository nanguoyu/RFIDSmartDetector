# coding=utf-8
from SerialRfid.ConnectManage import connectmanage
import time
from kNN import rfid

if __name__ == '__main__':
    serial3 = connectmanage(com='com13', baud=38400, iso='15693')
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
    print(rfid(T13-S+(C2-C1)))
    print(uid)

    serial3.close()
