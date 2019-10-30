#! /usr/bin/env python3
class ColorWeight:
    '''颜色权重，用于显色定义权重'''

    def __init__(self):
        self.weight = 1
        self.trees = 0
        self.combos = None

    def Combos_Weeks(self, preCombos, days=None):
        '''传入历史数据preCombos和days，输出新的Combos数
        此处改为返回连续天数更为合适'''
        if days == 7:
            self.combos = str(int(preCombos) + 1)
            return int(self.combos)
        else:
            self.combos = '0'
            return 0

    def reward_trees(self, days):
        '''you must rewrite this function!'''
        return 0

    def obtain_trees(self, days, preCombos):
        '''calculate the number of trees'''
        tree = self.weight - (7 - days)
        if tree <= 0:
            tree = 0
        tree += self.reward_trees(days, preCombos)
        return tree


class BlueWeight(ColorWeight):
    def __init__(self):
        super().__init__()
        self.weight = 1
        self.reward_weight = [0, 1, 2, 4, 7, 11, 16]

    def reward_trees(self, days, preCombos):
        temp = self.Combos_Weeks(preCombos, days)
        if temp-1 >= 5:
            return 10
        elif temp == 0:
            return 0
        else:
            return self.reward_weight[temp-1]


class Yellow_Weiht(ColorWeight):
    def __init__(self):
        super().__init__()
        self.weight = 4

    def reward_trees(self, days, preCombos):
        temp = self.Combos_Weeks(preCombos, days)
        if temp <= 1:
            return 0
        elif 2 ** (temp - 1) >= 10:
            return 10
        else:
            return 2 ** (temp - 1)


class Red_Weight(ColorWeight):
    '''Red_Weight too complex still wait to finish'''

    def __init__(self):
        super().__init__()
        self.weight = 6

    def reward_trees(self, days):
        pass


ge = Yellow_Weiht()
hb = BlueWeight()
bt_ml = BlueWeight()
Lew = Yellow_Weiht()
Reading = Yellow_Weiht()
Intro = Yellow_Weiht()
gb = Yellow_Weiht()

all_color = [ge, hb, bt_ml, Lew, Reading, Intro, gb]
all_add = 0
with open('trees-data.txt', 'r') as data:
    last_combos = data.readlines()[-1].split(',')
    days = input(
        "please input days({} values) split by space: ".format(len(all_color)))
    obtainDay = input(
        "please input obtain days and red color split by space: ")
    days = [int(i) for i in days.split()]
    obtainDay = [int(i) for i in obtainDay.split()]
    for i, colori in enumerate(all_color):
        # if length of last_combos not enough then append new value
        if i > len(last_combos) - 2:
            last_combos.append('0')
        all_add += colori.obtain_trees(days[i], last_combos[i+1])
    last_combos[0] = str(int(last_combos[0]) + all_add +
                         obtainDay[0] - obtainDay[1] - 60)

with open('trees-data.txt', 'a') as data:
    for i, colori in enumerate(all_color):
        # print(colori.combos)
        last_combos[i+1] = colori.combos
    addData = ','.join(last_combos)
    print(addData)
    data.writelines('\n'+addData)
