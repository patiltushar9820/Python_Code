#file in python using command line
import sys
#fp=open(sys.argv[1],mode='rt',encoding='utf8')
#print(fp.read())

#2 with block file operation
def file1():
    with open(sys.argv[1],mode='rt',encoding='utf8') as f:
        print(list[int(line.strip()) for line in f])
if __name__=='__main__':
    file1()
