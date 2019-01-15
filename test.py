class ColorWeight:
    '''颜色权重，用于显色定义权重'''
    def __init__(self):
        self.weight = 1
        self.trees = 0
        self.combos = None
    def Combos_Weeks(self, days=None):
        '''连续坚持额外奖励tree
        此处改为返回连续天数更为合适'''
        with open('trees-data.txt', 'r') as data:
            combos = data.readlines()[-1].split(',')
            if days == 7:
                combos[self.number] = str(int(combos[self.number]) + 1)
                self.combos = combos
                return int(combos[self.number])
            else:
                combos[self.number] = '0'
                self.combos = combos
                return 0
        
    def obtain_trees(self, days):
        '''calculate the number of trees'''
        tree = self.weight - (7 - days)
        if tree <= 0:
            tree = 0
        return tree
    
    def reward_trees(self, days):
        '''you must rewrite this function!'''
        return 0
    
    def calculate_tree(self, days):
        self.trees = self.obtain_trees(days) + self.reward_trees(days)
        with open('trees-data.txt', 'a') as data:
            self.combos[0] = str(int(self.combos[0]) + self.trees)
            data.writelines(','.join(self.combos))
        return self.trees

class BlueWeight(ColorWeight):
    def __init__(self, number=-2):
        super().__init__()
        self.weight = 1
        self.number = number
        self.reward_weight = [0, 1, 2, 4, 7, 11, 16]
        if number == -2:
            raise 'you must give squence number!'
    def reward_trees(self, days):
        temp = self.Combos_Weeks(days)
        if temp-1 >= 5:
            return 10
        elif temp == 0:
            return 0
        else:
            return self.reward_weight[temp-1]


class Yellow_Weiht(ColorWeight):
    def __init__(self, number=-2):
        super().__init__()
        self.weight = 4
        self.number = number
        if number == -2:
            raise 'you must give squence number!'
    def reward_trees(self, days):
        temp = self.Combos_Weeks(days)
        if temp <= 1:
            return 0
        elif 2 ** (temp - 1) >= 10:
            return 10
        else:
            return 2 ** (temp -1)

class Red_Weight(ColorWeight):
    '''Red_Weight too complex still wait to finish'''
    def __init__(self, number=-2):
        super().__init__()
        self.weight = 6
        self.number = number
        if number == -2:
            raise 'you must give squence number!'
    def reward_trees(self, days):
        pass

ge = Yellow_Weiht(1)
hb = BlueWeight(2)
bt = BlueWeight(3)
ml = BlueWeight(4)
gb = Yellow_Weiht(5)

tree1 = ge.calculate_tree(3)
tree2 = hb.calculate_tree(7)
tree3 = bt.calculate_tree(7)
tree4 = ml.calculate_tree(7)
tree5 = gb.calculate_tree(7)

all_add = [tree1,tree2,tree3,tree4,tree5]
print(all_add)
final_trees = sum(all_add) + 6 - 30
with open('trees-data.txt', 'r') as data:
    temp = data.readlines()[-1].split(',')
    temp[0] = str(int(temp[0]) + final_trees)
    print(','.join(temp))
with open('trees-data.txt', 'a') as data:
    data.writelines(','.join(temp))
