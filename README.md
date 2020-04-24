# Crunpy

    python crunpy.py min max [lists | strings] [-c 'out({})']
    
    lists    =  1 2 3 4 ...
    strings  =  abcdefg ...
    
      -c     =  'command_in_python({resulte_code})'
    
    
    EX:
    
    python crunpy.py 1 1 abc
    a
    b
    c
    
    python crunpy.py 1 2 name 2000 2010 1978
    name
    2000
    2010
    1978
    namename
    name2000
    name2010
    name1978
    2000name
    20002000
    20002010
    20001978
    2010name
    20102000
    20102010
    20101978
    1978name
    19782000
    19782010
    19781978
    
    python crunpy 1 1 abc -c 'out({}.upper())'
    A
    B
    C
    
    python crunpy 1 2 $(cat wordlist.txt)
    cat
    dog
    hat
    catcat
    catdog
    cathat
    dogcat
    dogdog
    doghat
    hatcat
    hatdog
    hathat
