# coding=utf-8
def Hex2String(argv):
    result = ''
    hLen = len(argv)
    for i in xrange(hLen):
        hvol = ord(argv[i])
        hhex = '%02x' % hvol
        result += hhex + ' '
    return result[:-1]


def String2Hex(string):
    print "input string"+Hex2String(string.decode('hex'))
    return string.decode('HEX')
