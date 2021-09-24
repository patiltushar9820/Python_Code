#file in python 
#1 Open a file 
#fp=open("abc.txt",mode='rt',encoding='utf8')

#2 write to abc.txt file
#str=input('enter file text that you want written in file\n')
#fp.write(str )

#3 read the file
#print(fp.read())

#4 read the file line by line
#print(fp.readline())

#5 read the all lines of the file and print on single line 
#print(fp.readlines())

#6 close the file
#fp.close()

fp=open("abc.txt",mode='at',encoding='utf8')
str=input('enter multiple lines')
fp.writelines(str)



