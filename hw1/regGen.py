import random
import string
import sys
import re


regLen = 50
strLen = 100
strNum = 20

def regGen(n, nostar):
    max = 5 + n if n > 0 else 5
    seed = random.randrange(0, max)
    strings = [''] * strNum

    if seed == 0 or seed == 1:
        (preg1, reg1, strings1) = regGen(n + 1, False)
        (preg2, reg2, strings2) = regGen(n + 1, False)
        reg = '({}.{})'.format(reg1, reg2)
        preg = '({}{})'.format(preg1, preg2)
        for i in range(strNum):
            strings[i] = strings1[i] + strings2[i]
        return (preg, reg, strings)
    elif seed == 2 or seed == 3:
        (preg1, reg1, strings1) = regGen(n + 1, False)
        (preg2, reg2, strings2) = regGen(n + 1, False)
        reg = '({}+{})'.format(reg1, reg2)
        preg = '({}|{})'.format(preg1, preg2)
        for i in range(strNum):
            rand = random.randrange(0, 2)
            if rand == 0:
                strings[i] = strings1[i]
            else:
                strings[i] = strings2[i]
        return (preg, reg, strings)
    elif seed == 4 and nostar == False:
        (preg1, reg1, strings1) = regGen(n + 1, True)
        reg = '({}*)'.format(reg1)
        preg = '({}*)'.format(preg1)
        for i in range(strNum):
            strings[i] = ''
            n = random.randrange(0, 3)
            m = random.randrange(20, 25)
            get = random.randrange(n, m)
            for _ in range(get):
                k = random.randrange(0, strNum)
                strings[i] += strings1[k]

        return (preg, reg, strings)
    elif (seed == 4 and nostar) or (5 <= seed and seed <= 4 + n/2):
        return ('0', '0', ['0'] * strNum)
    else:
        return ('1', '1', ['1'] * strNum)

def strGen(n, m):
    n = random.randrange(n, m)
    letters = '01'
    return ''.join(random.choice(letters) for i in range(n))

if __name__ == "__main__":
    n = sys.argv[1]
    fin = open("testcases/test{}.in".format(n), "w")
    fans = open("testcases/test{}.ans".format(n), "w")
    lengthFactor = 0
    while True:
        pregex, regex, strings = regGen(lengthFactor, False)
        if len(regex) > 30 and len(regex) <= 50:
            break
    save = 0
    pregex = "^{}$".format(pregex)
    
    for string in strings:
        if len(string) < strLen and len(string) > 0:
            save += 1

    fin.write(regex + '\n')
    fin.write(str(save + 10) + '\n')

    for string in strings:
        if len(string) < strLen and len(string) > 0:
            fin.write(string + '\n')
            fans.write("Yes\n")

    for i in range(10):
        n = random.randrange(1, i * 9 + 2)
        string = ''.join(random.choice('01') for j in range(n))
        fin.write(string + '\n')
        if re.search(pregex, string) == None:
            fans.write("No\n")
        else:
            fans.write("Yes\n")

    fans.close()
    fin.close()


#    for i in range(30):
#        n = random.randrange(1, 200)
#        print(strGen(n, n + 20))
