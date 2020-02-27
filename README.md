# Crunpy

Usage: python crunpy.py min max [lists | strings] [-c 'out({})']
<br>
<br>lists    =  1 2 3 4 ...
<br>strings  =  abcdefg ...
<br>
<br>  -c     =  'command_in_python({resulte_code})'
<br>
<br>
<br>EX:
<br>
<br>python crunpy.py 1 1 abc
<br>a
<br>b
<br>c
<br>
<br>python crunpy.py 1 2 name 2000 2010 1978
<br>name
<br>2000
<br>2010
<br>1978
<br>namename
<br>name2000
<br>name2010
<br>name1978
<br>2000name
<br>20002000
<br>20002010
<br>20001978
<br>2010name
<br>20102000
<br>20102010
<br>20101978
<br>1978name
<br>19782000
<br>19782010
<br>19781978
<br>
<br>python crunpy 1 1 abc -c 'out({}.upper())'
<br>A
<br>B
<br>C
<br>
<br>python crunpy 1 2 $(cat wordlist.txt)
<br>cat
<br>dog
<br>hat
<br>catcat
<br>catdog
<br>cathat
<br>dogcat
<br>dogdog
<br>doghat
<br>hatcat
<br>hatdog
<br>hathat
