import random


def make():
    global nodes
    nodes = [i for i in range(30)]
    nodes[0] = {2: 1, 7: 5}
    nodes[1] = {1: 1, 3: 1, 8: 3}
    nodes[2] = {2: 1, 4: 1, 9: 10}
    nodes[3] = {3: 1, 5: 1, 10: 4}
    nodes[4] = {4: 1, 6: 1, 11: 5}
    nodes[5] = {5: 1, 12: 9}
    nodes[6] = {1: 5, 8: 1, 13: 12}
    nodes[7] = {7: 1, 9: 1, 14: 10, 2: 3}
    nodes[8] = {8: 1, 10: 1, 15: 9, 3: 10}
    nodes[9] = {9: 1, 11: 1, 16: 8, 4: 4}
    nodes[10] = {10: 1, 12: 1, 17: 11}
    nodes[11] = {11: 1, 6: 9, 18: 10}
    nodes[12] = {7: 12, 14: 1, 19: 6}
    nodes[13] = {13: 1, 15: 1, 20: 3, 8: 10}
    nodes[14] = {14: 1, 16: 1, 21: 5}
    nodes[15] = {15: 1, 17: 1, 22: 4}
    nodes[16] = {16: 1, 18: 1, 23: 2}
    nodes[17] = {17: 1, 12: 10, 24: 3}
    nodes[18] = {13: 6, 20: 1, 25: 4}
    nodes[19] = {19: 1, 21: 1, 26: 4}
    nodes[20] = {20: 1, 22: 1, 27: 3}
    nodes[21] = {21: 1, 23: 1, 28: 2}
    nodes[22] = {22: 1, 24: 1, 29: 2}
    nodes[23] = {23: 1, 18: 3, 30: 3}
    nodes[24] = {19: 4, 26: 1}
    nodes[25] = {25: 1, 27: 1, 20: 4}
    nodes[26] = {26: 1, 28: 1, 21: 3}
    nodes[27] = {27: 1, 29: 1, 22: 2}
    nodes[28] = {28: 1, 30: 1, 23: 2}
    nodes[29] = {29: 1, 24: 3}

def update(index):
    index -= 1
    for neighbors, dist in nodes[index].items():
        print("Neighbor: %d | Distance: %d" % (neighbors, dist))
        get_neighbors(neighbors -1)
        for destinations, dist2 in nodes[index].items():
            if(neighbors - 1 != destinations):
                try:
                    if nodes[neighbors-1][destinations] > dist2 + dist:
                        nodes[neighbors-1][destinations] = dist2 + dist
                except KeyError:
                    nodes[neighbors-1][destinations] = dist + dist2



def get_neighbors(index):
    for neighbors, dist in nodes[index].items():
        print("---- Neighbor: %d | Distance: %d" % (neighbors, dist))


def pullDistances(index, num):
    cur_node = node[index]
    try:
        print("Distance is %d" % nodes[index][num])
    except IndexError:
        print("Distance: 1000")



make()

while(1):
    update(random.randint(1, 30))
    print("***** 1 to 30 *****")
    try:
        print(nodes[0][30])
    except KeyError:
        print(1000)
