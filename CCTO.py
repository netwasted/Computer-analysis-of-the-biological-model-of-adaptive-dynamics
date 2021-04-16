import os
import numpy
import string

plot1 = open('plot1.txt', 'a')
plot1.truncate(0)
plot2 = open('plot2.txt', 'a')
plot2.truncate(0)
for sm2 in numpy.linspace(0, 0.2, num=500):
    for d12 in numpy.linspace(0, 0.001, num=50):
        cmd = './a point -t test1 -dim 1 -al 0.400000 -points 512 -a 2.000000 -b 0.4 0.4 -dvec 0.2 0.2 -dmat 0.001 ' + str(d12) + ' 0.001 0.001 -sw 0.04 0.04 0.04 0.04 -sm 0.04 ' + str(sm2)
        os.system(cmd)
        n = open('test1.N', 'r')
        s = (n.readline()).split(' ')
        if s[0] != '-nan' and s[1] != '-nan':
            plot1.write(str(sm2) + ' ' + str(d12) + ' ')
            plot2.write(str(sm2) + ' ' + str(d12) + ' ')
            plot1.write(s[0]+'\n')
            plot2.write(s[1]+'\n')
        n.close()
plot1.close()
plot2.close()
