# coding=utf-8
tag = [10110101, 10110100, 11110101, 11010101]
boy = []
output = []


def int2list(Inter):
    inter = Inter
    listA = []
    w = range(9)[1:]
    list.reverse(w)
    for x in w:
        shang = inter / 10 ** (x - 1)
        inter %= 10 ** (x - 1)
        listA.append(shang)
    return listA


def list2int(List):
    list.reverse(List)
    Int = 0
    for w in range(len(List)):
        Int += List[w] * 10 ** w
    list.reverse(List)
    return Int


def list2tag(llist):
    listA = []
    for x in llist:
        listA.append(list2int(x))
    return listA


def tag2list(ttag):
    listB = []
    for x in ttag:
        listB.append(int2list(x))
    return listB


def split(INTER, LISTONE):
    A = []  # INTER>LISTINE{X]
    B = []
    for x in range(len(LISTONE)):
        if INTER > LISTONE[x]:
            print str(INTER) + "大于" + str(LISTONE[x])
            A.append(LISTONE[x])
        elif INTER < LISTONE[x]:
            print str(INTER) + "小于" + str(LISTONE[x])
            B.append(LISTONE[x])
        if INTER == LISTONE[x]:
            output.append(LISTONE[x])
    print "我们把" + str(LISTONE) + "划分为比" + str(INTER) + "小的" + str(A)
    print "和比" + str(INTER) + "大的" + str(B)
    return A, B


def divide(lista, Data):
    data = Data
    llist = lista
    # print "lista "+str(lista)
    # print "data "+str(data)
    print "len" + str(len(llist))
    print "我们使用新的请求序列号" + str(llist[0])
    a, b = split(llist[0], data)
    print "处理比" + str(llist[0]) + "小的" + str(a)
    # print "b"+str(b)
    if len(a) == 1:
        print("we find" + str(a[0]))
        output.append(a[0])
    elif len(a) != 0:
        # print "llist"+str(llist)
        llist.remove(llist[0])
        # print "after remove"+str(llist)
        divide(llist, a)
    print "处理比" + str(llist[0]) + "大的" + str(b)
    if len(b) == 1:
        print("we find" + str(b[0]))
        output.append(b[0])
    elif len(b) != 0:
        print "我该如何处理" + str(b)


def anti(listC):
    put = []
    temp = list2tag(listC)
    TAG = []
    tt = []
    index = []
    e0 = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(len(listC)):
        e0[0] += listC[x][0]
        e0[1] += listC[x][1]
        e0[2] += listC[x][2]
        e0[3] += listC[x][3]
        e0[4] += listC[x][4]
        e0[5] += listC[x][5]
        e0[6] += listC[x][6]
        e0[7] += listC[x][7]

    for x in range(len(e0)):
        if e0[x] == len(listC):
            tt.append(1)
        elif e0[x] == 0:
            tt.append(0)
        else:
            tt.append(1)
            index.append(x)
    print "这些位发生碰撞"
    print index
    print "开始处理碰撞包"
    # 生成一个包
    print "初次"
    # tt = [1, 1, 1, 1, 1, 1, 1, 1]
    print tt
    TAG.append(list2int(tt))
    for x in index:
        print "原始tt为"
        print tt
        print "把初次的第%d位置零得到" % x
        tt[x] = 0
        print tt
        TAG.append(list2int(tt))
        # tt[x] = 1
    # TAG.sort(reverse = True)
    print "向标签群发送以下请求序列号" + str(TAG)
    #
    ttag = temp
    print "要处理的tag" + str(ttag)
    divide(TAG, ttag)
    print "ok"
    ret_list = list(set(temp) ^ set(output))
    print "这些还没有找到" + str(ret_list)
    return ret_list, output


if __name__ == '__main__':
    print tag
    # print int2list(tag[0])
    print tag2list(tag)
    print "asa"
    # for x in range(4):
    #     temp = []
    #     for y in range(8):
    #         temp.append(int(raw_input("请按位输入一个标签的一位")))
    #     boy.append(temp)
    #     temp = []
    #     print ("请输入一个标签")

    print list2tag(tag2list(tag))
    # tag2list(tag)
    ret, ouuu = anti(tag2list(tag))

    print "output" + str(output)
