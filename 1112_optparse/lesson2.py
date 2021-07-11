"""
コンソールで 
python lesson2.py --help
python lesson2.py -f test.txt a b 
python lesson2.py --file=test.txt a b 
python lesson2.py -n 10 a b 
python lesson2.py --num=10 a b 
python lesson2.py -v
python lesson2.py -q
python lesson2.py -r
python lesson2.py
python lesson2.py --release
python lesson2.py -e prd --release
python lesson2.py -e dev --release
と入力してみる
"""
from optparse import OptionParser

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string', 
    dest='filename', help='File name')

    parser.add_option('-n', '--num', action='store', type='int', 
    dest='num', help='Enter num')

    parser.set_defaults(verbose=True)
    #parser.add_option('-v', action='store_true', dest='verbose')
    parser.add_option('-v', action='store_true', dest='verbose')
    #parser.add_option('-v', action='store_false', dest='verbose', default=True)
    parser.add_option('-q', action='store_false', dest='verbose')

    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    parser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't relase")
        setattr(parser.values, option.dest, True)

    parser.add_option('--release', action='callback', callback=is_relase, dest='release')

    options, args = parser.parse_args()
    print(options)
    print(options.filename)
    print(args)

if __name__ == '__main__':
    main()

