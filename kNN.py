# coding=utf-8
cent_node = [2.0086, 2.0241, 2.0115]
label = ["无人", "非人物体通过", "一个人通过"]


def rfid(rssi):
    distance = []
    for x in range(len(label)):
        distance.append((rssi - cent_node[x]) ** 2)
    for x in range(len(label)):
        if min(distance) - distance[x] == 0:
            return label[x]







































