# -*- coding: utf-8 -*-
#copy
#python ex17.py test16.txt copied17.txt
#convert to ansi

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "\n>>>>>>>>>>>>>>>>>>\nװ�Ƴ�����ճ����\n����Ϊ��װ��\n��%s �� %s" %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long "%len(indata)

print "Does the output file exist? %r"%exists(to_file)
print "READY,return to continue,hit the screen to abort\n kiding again CTRL-C you knew it"

raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "ALL DONE"
out_file.close()
in_file.close()

