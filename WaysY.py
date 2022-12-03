import os
from progress.bar import IncrementalBar
import time
file_name = ''
def by_chars(chars, length, filename):
    os.system('touch ' + filename + '.txt')
    ch = list(chars)
    w = ''
    t = ''
    quantity = len(ch)**length
    bar = IncrementalBar('Bar', max = quantity)
    with open(filename + '.txt', 'a') as wl:
        for i in range(quantity):
            for r in range(length):
                t += ' ' + str((i//len(chars)**r)%len(chars))
            y = t.split()
            for k in range(length):
                w += ch[int(y[k])]
            wl.write(w + '\n')
            t = ''
            w = ''
            bar.next()
            
def by_charstest(chars, length):
    ch = list(chars)
    os.system('touch test.txt')
    w = ''
    t = ''
    quantity = len(ch)**length
    bar = IncrementalBar('Bar', max = quantity)
    with open('test.txt', 'a') as wl:
        for i in range(quantity):
            for r in range(length):
                t += ' ' + str((i//len(chars)**r)%len(chars))
                y = t.split()
            for k in range(length):
                w += ch[int(y[k])]
            wl.write(w + '\n')
            t = ''
            w = ''
            bar.next()
    os.system('rm test.txt')

name = '         __      __           __   __\n         \ \    / /_ _ _  _ __\ \ / /\n          \ \/\/ / _` | || (_-<\ V /\n           \_/\_/\__,_|\_, /__/ |_|\n                       |__/'
print(name + '\n by Évariste Galois\n')

inp = input('[_] Type a set of symbols, without spaces(for example: 1234567890-./abc):  ')
inp1 = int(input('[_] Type the length of "words" you need:  '))
file_name = input('[_] Type name of file  where wordlist will be generated:   ')
test = input('[_] Test speed?(y/n): ')
while test != 'y' and test != 'n':
    print('[!] Error')
    test = input('[_] Test a speed?(y/n): ') 
if test == 'y':
    print('[~] You chose option y')
    t1 = time.time()
    by_charstest(inp, 5)
    t2 = time.time()
    print('\n[~] Your result is(sec per word):  ')
    result = (t2-t1)/(len(inp)**5)
    print(result)
    print('[~] The task will be done approximately n(sec):    ')
    print(result*(len(inp)**inp1))
else:
    print('[~] You chose option n')
check = input('[~] Your choices were:    \n1.Symbols: %s \n2.Length:  %s \n3.Filename: %s \n[_] Continue?(y/n): ' %(inp, str(inp1), file_name)) 
while check != 'y' and check != 'n':
    print('[!] Error')
    check = input('[_] Continue?(y/n)')
if check == 'y':
    by_chars(inp, inp1, file_name)
    print('[done]')
elif check == 'n':
    print('[bye]')
    quit
