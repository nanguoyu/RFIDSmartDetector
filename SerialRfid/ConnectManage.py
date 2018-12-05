import serial
from util import String2Hex, Hex2String
import time

start = 'AA28010500D3FF'
stop = 'AA28020100D4FF'


class connectmanage():
    def __init__(self, com, baud, iso):
        self.iso = iso
        self.SERIAL = serial.Serial(com, baud)

    def write(self, string):
        self.SERIAL.write(String2Hex(string))

    def ShowAllUid(self):
        self.SERIAL.write(start)

    def Stop(self):
        self.SERIAL.write(stop)

    def GetUid(self):
        raw = Hex2String(self.SERIAL.read_all())
        print "raw"+raw
        if self.iso == '14443A':
            print("Type: ISO 14443A ")
            # print raw
            return raw[raw.find('aa 28 01 05 05 02') + 18:raw.find('ff aa 28 01 05 01 bc 91 ff') - 4]
        if self.iso == '15693':
            print("Type: ISO 15693 ")
            string = raw[raw.find('aa 28 01 05 09 04') + 18:raw.find('ff aa 28 01 05 01 bc 91 ff') - 4]
            uid = string.split()[::-1]
            return " ".join(uid)
        else:
            print("125KHZ")
            string = raw[raw.find('02 0b a5')+9:raw.find('77 03')-1]
            return string

    def read_raw(self):
        self.SERIAL.read_all()

    def close(self):
        self.SERIAL.close()
