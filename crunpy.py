import sys

out = sys.stdout.write

args = sys.argv[1:]

help_text = '''
Usage: python crunpy.py min max [lists | strings] [-c 'out({})']

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
'''

def crunch(min, max, lists, command='out({})'):
    min = int(min)
    max = int(max)

    if type(lists) == str:
        lists = '"{}"'.format(lists)
    elif len(lists) == 1:
        lists = '"{}"'.format(lists[0])

    max += 2

    for a in range(2, max):

        if a <= min:
            continue

        fors = cmd = ''

        for a0 in range(1, a):
            fors += 'for a{} in {}:\n{}'.format(a0, lists, '\t' * a0)

            cmd += 'a{} + '.format(a0)
            if a0 >= a - 1:
                cmd += r'"\n"'

        cmd = '({})'.format(cmd)
        output = fors + command.format(cmd)
        #print(output)
        exec(output)

lists = 'abcdefghijklmnopqrstuvwxyz'
command = 'out({})'


try:

    if '-c' in args:
        i = args.index('-c')
        lists = args[2:i]
        command = args[i + 1]

    elif len(args[2:]) > 1:
        lists = args[2:]
    elif len(args[2:]) == 1:
        lists = args[2]

    crunch(args[0], args[1], lists, command)

except KeyboardInterrupt:
    print('\n\n ^C Interrupted')
except IOError:
    print('\n\n IOError received, exiting\n\n')
    sys.exit(0)

except:
    if args[0] == '-h' or args[0] == '--help':
        print(help_text)
