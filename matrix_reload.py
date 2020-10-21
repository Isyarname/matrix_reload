import random, copy

class Matrix:
    def __init__(self, width=0, height=0, homogeneous=False, value=7, ls=[]):
        self.body = []
        self.maxValLen = len(str(value))
        if len(ls) == 0:
            if homogeneous == True:
                for i in range(height):
                    temp = []
                    for j in range(width):
                        temp.append(value)
                    self.body.append(temp)
            else:
                n = 0
                for i in range(height):
                    temp = []
                    for j in range(width):
                        n += 1
                        temp.append(n)
                    self.body.append(temp)
        else:
            self.body.extend(ls)
            

    def matrixToString(self):
        if type(self.body[0]) == int:
                for i in self.body:
                    lenght = len(str(i))
                    if lenght > self.maxValLen:
                        self.maxValLen = lenght
        else:    
            for i in self.body:
                for j in i:
                    lenght = len(str(j))
                    if lenght > self.maxValLen:
                        self.maxValLen = lenght
        s = ""
        if type(self.body[0]) != int:
            for i, o in enumerate(self.body):
                for j, oo in enumerate(o):
                    val = str(oo)
                    s += val + " "
                    if len(val) < self.maxValLen:
                        for i in range(self.maxValLen - len(val)):
                            s += " "
                s += "\n"
        else:
            for i in self.body:
                s += str(i) + " "
        return s

    def transpose(self):
        ls = []
        if type(self.body[0]) != int:
            for i in range(len(self.body[0])):
                ls.append([])

            for i in self.body:
                for j in range(len(i)):
                    ls[j].append(i[j])
            self.body = ls
        else:
            print("одномерный список не подходит")

    def fill(self, value):
        if type(self.body[0]) == int:
            for i in range(len(self.body)):
                self.body[i] = value
        else:
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    self.body[i][j] = value

    def flatten(self):
        ls = []
        for i in range(len(self.body)):
            ls.extend(self.body[i])
        self.body = ls

    def shuffle(self):
        lenX = len(self.body)
        lenY = len(self.body[0])
        if type(self.body[0]) == int:
            random.shuffle(self.body)
        else:
            for i in range(lenX):
                for j in range(lenY):
                    x = random.randint(0, lenX-1)
                    y = random.randint(0, lenY-1)
                    self.body[i][j], self.body[x][y] = self.body[x][y], self.body[i][j]        

    def reshape(self, width, height):
        if type(self.body[0]) == int:
            lenght = len(self.body)
        else:
            lenght = len(self.body) * len(self.body[0])

        if width*height != lenght:
            print("неподходящий размер матрицы")
        else:
            if type(self.body[0]) != int:
                self.flatten()
            ls = []
            n = 0
            for i in range(height):
                ls.append([])
                for j in range(width):
                    if n < lenght:
                        ls[i].append(self.body[n])
                        n += 1
                    else:
                        break
            self.body = ls
        
    def copy(self):
        return copy.deepcopy(self.body)

    def __str__(self):
        return self.matrixToString()

    def __add__(self, other):
        for i,o in enumerate(self.body):
            for j,oo in enumerate(o):
                self.body[i][j] = oo + other
        return Matrix(ls=self.body)

    def __radd__(self, other):
        for i,o in enumerate(self.body):
            for j,oo in enumerate(o):
                self.body[i][j] = other + oo
        return Matrix(ls=self.body)

    def __sub__(self, other):
        for i,o in enumerate(self.body):
            for j,oo in enumerate(o):
                self.body[i][j] = oo - other
        return Matrix(ls=self.body)

    def __rsub__(self, other):
        for i,o in enumerate(self.body):
            for j,oo in enumerate(o):
                self.body[i][j] = other - oo
        return Matrix(ls=self.body)
    
    def __len__(self):
        return len(self.body)
    
    def __getitem__(self, key):
        return self.body[key]
    
    def __setitem__(self, key, value):
        self.body[key] = item
        
    #def __iter__(self):
        #return iter(self.body)


def concantenate(t, axis=0):
    ls = []
    if axis == 0:
        for i in t:
            ls.extend(i.body)

    elif axis == 1:
        for i in range(len(t[0].body)):
            ls.append([])

        for i in range(len(t[0].body)):
            for j in t:
                ls[i].extend(j.body[i])
    return Matrix(ls=ls)

a = Matrix(5,6)
print(a)
type(len(a))
b = Matrix(ls=a.copy())
b.reshape(6,5)
print(b)

def Summatorz(la, lb, a=1):
    t = Matrix(ls=lb.copy())
    l = min(len(la), len(la[0]), len(lb), len(lb[0]))
    if a == 1:
        for i in range(0, l):
            t[i][i] += la[i][i]
    elif a == 2:
        k = len(t[0])-1
        for i in range(0, l):
            t[i][k-i] += la[i][l-1-i]
    return t

def Subtractorz(la, lb, a=1):
    t = Matrix(ls=lb.copy())
    l = min(len(la), len(la[0]), len(lb), len(lb[0]))
    if a == 1:
        for i in range(0, l):
            t[i][i] -= la[i][i]
    elif a == 2:
        k = len(t[0])-1
        for i in range(0, l):
            t[i][k-i] -= la[i][l-1-i]
    return t

def Multiplierz(la, lb, a=1):
    t = Matrix(ls=lb.copy())
    l = min(len(la), len(la[0]), len(lb), len(lb[0]))
    if a == 1:
        for i in range(0, l):
            t[i][i] *= la[i][i]
    elif a == 2:
        k = len(t[0])-1
        for i in range(0, l):
            print(i, k-i)
            print(t[i][k-i])
            t[i][k-i] *= la[i][l-1-i]
    return t

def Dividerz(la, lb, a=1):
    t = Matrix(ls=lb.copy())
    l = min(len(la), len(la[0]), len(lb), len(lb[0]))
    if a == 1:
        for i in range(0, l):
            t[i][i] //= la[i][i]
    elif a == 2:
        k = len(t[0])-1
        for i in range(0, l):
            t[i][k-i] //= la[i][l-1-i]
    return t

def Exponentiatorz(la, lb, a=1):
    tmat = Matrix(ls=lb.copy())
    l = min(len(la), len(la[0]), len(lb), len(lb[0]))     
    if a == 1:
        for i in range(0, l):
            t = tmat[i][i]
            for j in range(la[i][i] - 1):
                tmat[i][i] *= t
    elif a == 2:
        k = len(t[0])-1
        for i in range(0, l):
            t = tmat[i][k-i]
            for j in range(la[i][l-1-i] - 1):
                tmat[i][k-i] *= t
    return tmat

c = Subtractorz(a, b, a=2)
print(c)