import math
import numpy
import os
import string

plot1 = open('plot1.txt', 'a')
plot1.truncate(0)
plot2 = open('plot2.txt', 'a')
plot2.truncate(0)
for sw11 in numpy.linspace(0, 0.15, num=50): # change num
    for sw12 in numpy.linspace(0, 0.15, num=50): #change num
        cmd = './a point -t test1 -dim 3 -al 0.400000 -points 512 -a 2.000000 -b 0.4 0.4 -dvec 0.2 0.2 -dmat 0.001 0.001 0.001 0.001 -sw ' + str(sw11) + ' ' + str(sw12) + ' ' + str(sw12) + ' ' + str(sw11) + ' -sm 0.06 0.06'
        os.system(cmd)
        n = open('test1.N', 'r')
        s = (n.readline()).split(' ')
        if s[0] != '-nan' and s[1] != '-nan':
            plot1.write(str(sw11) + ' ' + str(sw12) + ' ')
            plot2.write(str(sw11) + ' ' + str(sw12) + ' ')
            plot1.write(s[0]+'\n')
            plot2.write(s[1]+'\n')
        n.close()
plot1.close()
plot2.close()
