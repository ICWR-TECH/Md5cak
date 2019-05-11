#!/usr/bin/python
# Md5cak MD5 Cracker
# Copyright (c)2019 - Afrizal F.A - ICWR-TECH - All Reserved

import sys, hashlib, itertools

print """
####################################
# Md5cak - MD5 Cracker             #
# Coded By Afrizal F.A - ICWR-TECH #
####################################
"""

strmd5=sys.argv[1]
mulai=int(sys.argv[2])
sampai=int(sys.argv[3])

str_kata=str(sys.argv[4])

for u in range(mulai,sampai+1) :
   if not u :
      continue

   for kata in itertools.product(str_kata,repeat=u):

      if hashlib.md5(''.join(kata)).hexdigest() == strmd5 :
         sys.stdout.write("\r[+] Success : " + ''.join(kata))
         exit()
      else :
         sys.stdout.write("\r[-] Failed : " + ''.join(kata))
