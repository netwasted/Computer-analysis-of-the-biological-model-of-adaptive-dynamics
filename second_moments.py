import os
import numpy
import string

plot = open('second_moments.txt', 'a')
plot.truncate(0)
for sm2 in numpy.linspace(0, 0.2, num=50):
    for d12 in numpy.linspace(0, 0.001, num=10):
        cmd = './a point -t test1 -dim 1 -al 0.400000 -points 16384 -a 4.0 -b 0.4 0.4 -dvec 0.2 0.2 -dmat 0.001 ' + str(d12) + ' 0.001 0.001 -sw 0.04 0.04 0.04 0.04 -sm 0.04 ' + str(sm2)
        os.system(cmd)
        n = open('test1.data', 'r')
        s = (n.readline()).split(' ')
        s = (n.readline()).split(' ')
        if s[-5] != '-nan':
            plot.write(str(sm2) + ' ' + str(d12) + ' ')
            plot.write(s[-5] + '\n')
        n.close()
plot.close()
