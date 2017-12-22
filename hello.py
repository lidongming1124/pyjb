# /usr/bin/env python
# -*-  coding:utf -8 -*-

#李东
#iter  迭代
# i1=type('dfdfdfd');
# i2=cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
# int16=hex(33)   #将数字换行为16进制并以字符串形式返回  0x21
# int8=oct(33)   #将数字换行为8进制并以字符串形式返回    041
# bin2=bin(33);   #将数字换行为2进制并以字符串形式返回  0b100001
# myacii=chr(58) #将ASCII的数字换行为ASCII的字符，范围只能是0<=num<=255   :
# myord=ord(':');   #58
# int1=int('0x21 ',16);#
# int1=long('33',10)
# a=float(3) #3.0
# import decimal
# a1=decimal.Decimal("%.2f" % float(3)) #3.00
# a3=round(float(3), 6)#3.0\
# b1=bool(3);#True
# c1=complex('88') #不懂
# abs5=abs(-55);#55
# yz=coerce(22,33)#不懂
# mod1=divmod(8,2)
# mod2=divmod(10,3)#(3,1) 返回一个包含商和余数的元组
# rounds=round(3.49999,1)#3.5
# pows=pow(2,3,5)#3
# pows=pow(2,3)#8
#
# #print ("hello"[::-1]);#olleh
# c='bcdefghij'
# print(c[1:10:1])#cdefghij  X[I:J:K]:这标识索引X对象的元素，从偏移为I直到J-1，每隔K元素索引一次。第三个限制值，K，默认为1
#
#
# if( 'ss' in  'dfdfdfgfsdfs'):
#     print ('111111111111');
# else:
#     print ('222222222');
#
# if( 'ss' not in   'dfdfdfgfsdfs'):
#     print ('111111111111');
# else:
#     print ('222222222');

# jason='name' +'jason';
# print (jason); #namejason


# format1="%d"% 33
# format1="%s %s"% ('name','jason')#name jason
# print (format1);
# leng=len('dsfsdfs');

# str1= '11'
# str2=str1.join(('jason','minty'))#jason11minty
# str2=str1.join(['jason','minty'])#jason11minty
# del str2;
# print (str2); #NameError: name 'str2' is not defined

# print (leng);
#seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# seasons1=list(enumerate(seasons))
# print(seasons1);
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# seasons1=list(enumerate(seasons, start=1))
# print(seasons1);
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# for i, v in enumerate(seasons):
#     print (v,i);
#     print (i);
# max1=max('424328')
# print(max1);
# 8
# max1=max([4,8,9,88])
# max1=max((4,8,9,88))
# print(max1);
# 88
# max1=min([4,8,9,88])
# max1=min((4,8,9,88))
# print(max1);
# 4

# a = [1,2,3]
# c = [4,5,6,7,8]
# b = [4, 5, 6]
# zipped = zip(a,b)
# [(1, 4), (2, 5), (3, 6)]
# zipped = zip(a,c)
# [(1, 4), (2, 5), (3, 6)]元素个数与最短的列表一致
# zipped = zip(a,c)
# zipped=zip(*zipped)
# #与 zip 相反，可理解为解压，返回二维矩阵式
# print (zipped);
# reversed 返回一个反转的迭代器。
# seqString = 'Runoob'
# str1=reversed(seqString);<reversed object at 0x0258B250>
# print (str1);

# range(5, 9)  #  <=5 <9
# 字符串
# seqString = 'Runoob'
# print(list(reversed(seqString)))
#
# # 元组
# seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
# print(list(reversed(seqTuple)))
#
# # range
# seqRange = range(5, 9)
# print(list(reversed(seqRange)))
#
# # 列表
# seqList = [1, 2, 4, 3, 5]
# print(list(reversed(seqList)))
# ['b', 'o', 'o', 'n', 'u', 'R']
# ['b', 'o', 'o', 'n', 'u', 'R']
# [8, 7, 6, 5]
# [5, 3, 4, 2, 1]


# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

# a = [5,7,6,3,4,1,2]
# b = list(reversed(sorted(a )));
# [7, 6, 5, 4, 3, 2, 1]
# sorted(a )
# [1, 2, 3, 4, 5, 6, 7] reverse=True
# L = [('b', 2,5), ('a', 1,6), ('c', 3,8), ('d', 4,9)]
# #
# # ls=sorted(L, cmp=lambda x,y:cmp(x[2],y[2]))
# # [('b', 2, 5), ('a', 1, 6), ('c', 3, 8), ('d', 4, 9)]
# # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# ls=sorted(L, key=lambda x:x[1], reverse=True)
# [('d', 4, 9), ('c', 3, 8), ('b', 2, 5), ('a', 1, 6)]
#
# sum([0,1,2])
# sum((2, 3, 4), 1)
# sum([0,1,2,3,4], 2)
# user_input = raw_input("Enter your name: ")
# print user_input;是啥
# string='我的'
# string1=unicode(string,"utf -8")
#
# #print unicode(string,"utf -8").encode('base64','strict')#错1
#
# s1=string.encode('base64','strict')#ok
#s1=str.encode('gbk')  #错1
# print type(string1);
# format1="%d"% 33
# format1="%s %s"% ('name','jason')#name jason
# print (format1);
# leng=len('dsfsdfs');
# %c 转换成字符(ASCII 码值，或者长度为一的字符串)
# %ub 转成无符号十进制数
# %ob 转成无符号八进制数
# %s 优先用str()函数进行字符串转换
# %d / %i 转成有符号十进制数
# %ub 转成无符号十进制数
# format1="%ob %s"% (321,'jason')#name jason
# print (format1);
# s='sssss ';
# b=s.strip('dddd')
# print b;


# str.partition(str) 返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
# str = "http://www.w3cschool.cc/"
#
# print str.partition("://")
# ('http', '://', 'www.w3cschool.cc/')


# unicode是：
#
# 一种不用字节的形式来表示文本；就是说是变长的，len就是个数。
#
# 每次中语言的每一个字符都有唯一的数字来表示。
#
# 支持所有主流的语言；
#
# 可以表示超过100万的符号；


# str2 = 'ab c\n\nde fg\rkl\r\n'
# print str2.splitlines(True)

# str1 = 'ab c\n\nde fg\rkl\r\n'
# print str1.splitlines();

# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print str.split( );
# print str.split(' ',3);

# 3、变形
# lower(),#全部小写
# upper(),#全部小写
# capitalize(),#首字母大写
# swapcase(),#大小写交换
# title()#每个单词第一个大写,其他小写

# str1 = 'ab c,\n\nde fg,\rkl\r\n'
# print str1.splitlines(True); // 只有 一个参数，按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。




# str = "this is string example....wow!!!";
#
# sub = "i";
# print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
# sub = "wow";
# print "str.count(sub) : ", str.count(sub)
#
# str.count(sub, 4, 40) :  2
# str.count(sub, 4, 40) :  1

#Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
# str = "Lin,e1-abcdef \nLi,ne2-abc \nLine4-a,bcd";
# str1=str.split(',');
# title()#每个单词第一个大写,其他小写
# str1=' hello   world!'.title()
# str1=' hello   world!'
# str2=str1.lower()  upper()
# print  str1;

# str.count(sub, start= 0,end=len(string))
#
# 参数
#
#     sub -- 搜索的子字符串
#     start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
#     end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

# count( sub[, start[, end]]),#计算substr在S中出现的次数

# find( sub[, start[, end]]),#返回S中出现sub的第一个字母的标号，如果S中没有sub则返回-1。start和end作用就相当于在S[start:end]中搜索
# find()方法语法：
#
# str.find(str, beg=0, end=len(string))
#
# 参数
#
#     str -- 指定检索的字符串
#     beg -- 开始索引，默认为0。
#     end -- 结束索引，默认为字符串的长度。
# str1 = "this is string example....wow!!!";
# str2 = "exam";
#
# print str1.find(str2);
# print str1.find(str2, 10);
# print str1.find(str2, 40);
#
#
# 15
# 15
# -1


# index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# str.index(str, beg=0, end=len(string))
#
# 参数
#
#     str -- 指定检索的字符串
#     beg -- 开始索引，默认为0。
#     end -- 结束索引，默认为字符串的长度。

# str1 = "this is string example....wow!!!";
# str2 = "exam";
#find()函数族找不到时返回-1，index()函数族则抛出ValueError异常。
# print str1.index(str2);15
# print str1.index(str2, 10);15
# print str1.index(str2, 40);#报错

# rfind( sub[, start[,end]]),#返回S中最后出现的substr的第一个字母的标号，如果S中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号
# rindex( sub[, start[, end]])
# T2.find('ie') 字符串方法调用：搜索
# find()----找到的第一个符合字符的index
# rfind()-----找到最后一个符合的字符的index
# 备注：
# find()函数族找不到时返回-1，index()函数族则抛出ValueError异常。
# 另，也可以用 in 和 not in 操作符来判断字符串中是否存在某个模板

#  Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替 max-1 次。
# str.replace(old, new[, max])
#
# 参数
#
#     old -- 将被替换的子字符串。
#     new -- 新字符串，用于替换old子字符串。
#     max -- 可选字符串, 替换不超过 max 次
# str = "this is string example....wow!!! this is really string";
# print str.replace("is", "was");
# print str.replace("is", "was", 3);

#  Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。


# translate()对 unicode 对象的支持并不完备，建议不要使用  from string import maketrans   # 引用 maketrans 函数。
#
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print str.translate(trantab);
#
# 以上实例输出结果如下：
#
# th3s 3s str3ng 2x1mpl2....w4w!!!
#
# 以上实例去除字符串中的 'x' 和 'm' 字符：
#
# #!/usr/bin/python
#
# from string import maketrans   # Required to call maketrans function.
#
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print str.translate(trantab, 'xm');
#
# 以上实例输出结果：
#
# th3s 3s str3ng 21pl2....w4w!!!




# isalnum(),#是否全是字母和数字，并至少有一个字符
# str = "this2009";  # 字符中没有空格
# print str.isalnum();
# str = "this is string example....wow!!!";
# print str.isalnum();
# True
# False


# isalpha(),是否全是字母，并至少有一个字符
# str = "this";  # No space & digit in this string
# print str.isalpha();
# str = "this is string example....wow!!!";
# print str.isalpha();
# True
# False
# isdigit(),是否全是数字，并至少有一个字符 ，如果是全数字返回True,否则返回False


# str = "123456";  # Only digit in this string
# print str.isdigit();
#
# str = "3333this is string example....wow!!!";
# print str.isdigit();
# True
# False

# islower(),#S中的字母是否全是小写
# str = "THIS is string example....wow!!!";
# print str.islower();
#
# str = "this is string example....wow!!!";
# print str.islower();
# False
# True
# isupper(),#S中的字母是否是大写
# str = "THIS IS STRING EXAMPLE....WOW!!!";
# print str.isupper();
#
# str = "THIS is string example....wow!!!";
# print str.isupper();
# True
# False
# # isspace(),#是否全是空白字符，并至少有一个字符
# str = "       ";
# print str.isspace();
#
# str = "This is string example....wow!!!";
# print str.isspace();
# True
# False
# istitle(),S是否是首字母大写的
# str = "This Is String Example...Wow!!!";
# print str.istitle();
#
# str = "This is string example....wow!!!";
# print str.istitle();
# True
# False
# startswith(prefix[, start[, end]]), #startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

# str = "this is string example....wow!!!";
# print str.startswith( 'this' );
# print str.startswith( 'is', 2, 4 );
# print str.startswith( 'this', 2, 4 );
# True
# True
# False
# endswith(suffix[,start[, end]]),#方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
# str = "this is string example....wow!!!";
#
# suffix = "wow!!!";
# print str.endswith(suffix);
# print str.endswith(suffix,20);
#
# suffix = "is";
# print str.endswith(suffix, 2, 4);
# print str.endswith(suffix, 2, 6);


# center(width[, fillchar]), 字符串中间对齐
# str = "[www.runoob.com]"
#
# print ("str.center(40, '*') : ", str.center(40, '*'))
# ("str.center(40, '*') : ", '************[www.runoob.com]************')
# ljust(width[, fillchar]), 字符串左对齐，不足部分用fillchar填充，默认的为空格
# str = "Runoob example....wow!!!"
# print (str.ljust(50, '*'))
# Runoob example....wow!!!**************************


# rjust(width[, fillchar]), 字符串右对齐，不足部分用fillchar填充，默认的为空格
# str = "this is string example....wow!!!";
# print str.rjust(50, '0');
# 000000000000000000this is string example....wow!!!
# zfill(width), 把字符串变成width长，并在右对齐，不足部分用0补足
# str = "this is string example....wow!!!";
#
# print str.zfill(40);
# print str.zfill(50);
# 00000000this is string example....wow!!!
# 000000000000000000this is string example....wow!!!00000000this is string example....wow!!!
# 000000000000000000this is string example....wow!!!
# expandtabs([tabsize])expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# str = "this is\tstring example....wow!!!"
#
# print ("原始字符串: " + str)
# print ("替换 \\t 符号: " +  str.expandtabs())
# print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))

# encode([encoding[,errors]]),
# decode([encoding[,errors]])
# 这是一对互逆操作的方法，用以编码和解码字符串。因为str是平台相关的，它使用的内码依赖于操作系统环境，
# 而unicode是平台无关的，是Python内部的字符串存储方式。
# unicode可以通过编码（encode）成为特定编码的str，而str也可以通过解码（decode）成为unicode。
# # 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。errors默认值为"strict"，意思是UnicodeError。
# 可能的值还有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 和所有的通过

# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
#
# print(str)
#
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
#
# print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
# print("GBK 解码：", str_gbk.decode('GBK','strict'))
# 菜鸟教程
# UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
# GBK 编码： b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
# UTF-8 解码： 菜鸟教程
# GBK 解码： 菜鸟教程
# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
#
# print(str)
#
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
#
# print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
# print("GBK 解码：", str_gbk.decode('GBK','strict'))
# 菜鸟教程
# UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
# GBK 编码： b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
# UTF-8 解码： 菜鸟教程
# GBK 解码： 菜鸟教程


# (三)、序列类型函数[不是对象的方法是函数]
# 1)列表求长：len(L)
# 2)列表中的最大值最小值： max(L)和min(L)
# max()和min()函数在字符串操作里面用处不大,因为它们能对字符串做的只能是找出
# 串中"最大"和"最小"的字符(按词典序),而对列表和元组来说,它们被定义了更多的用处.比如
# 对只包含数字和字符串对象的列表,max()和min()函数就非常有用,重申一遍,混合对象的结构
# 越复杂返回的结构准确性就越差
# 3)正向排序和反向排序：sorted(L) reversed(L)
# 4)zip() 对多个列表内容进行组合
# 返回一个列表，其第一个元素是it0,it1,...这些元素的第一个元素组成的一个元组，第二个...,类推.
# 6)sum() 列表求和
# 7）enumerate(iter)   ：接受一个可迭代对象作为参数，返回一个enumerate 对象(同时也是一个迭代器),该对象生成由iter 每个元素的index 值和item值组成的元组(PEP 279)

# L=['1', 'a']
# L[0] = 2
# print L;
# # name=list('hello')
# print  name;
# ['h', 'e', 'l', 'l', 'o']
# num = [1, 5]

# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print '这是 pass 块'
#    else:
#
#      print '当前字母 :', letter
#
# print "Good bye!"
# import time
#
# localtime = time.localtime(time.time())
# print "本地时间为 :", localtime

# num=10;
# while (num):
#     num=num-1;
#     if num ==5:
#        continue;
#     else:
#         print  num;
# 1--100
# number =list(range(0,101));
# sum=0;
# for i in  number:
#     sum =sum +i;
# print sum;
# number =list(range(0,101));
# sum =0;
# for i in number:
#     if i%2==0:
#         sum=sum+i;
# print sum;

# "{"infoCode":1,"message":"操作成功！","data":{"id":36926,"siteId":"abf41211-df8c-49eb-b443-e0c25a1145be","siteName":"北京西站瑞海大厦B4充电站","orderStatus":1,"enCharging":1,"pileType":1,"chargingTime":0,"chargingTimeStr":"0分","orderAmount":0.0,"startTime":1512443774000,"charge":0.0,"service":0.0,"parking":0.0,"chargingDegree":0.0,"orderNo":"10201509080010471712051116143204","terminalCode":"1020150908001047","createTime":1512443774000,"updateTime":1512443774000,"couponNum":0.0,"payMoney":0.0,"isOpen":0,"collected":0,"cardType":100,"merchantName":"小易充电"}}"
# n = 1
# name = 'hahaha'
# pwd = 'hehehe'
# while True:
#     username = input('请输入用户名： ')
#     password = input('请输入密码： ')
#     if username == name and password == pwd:
#         print ('hello,%s'%username)
#         exit()
#     else:
#         n = n + 1
#         if n > 3:
#             print "密码超过3次";
#             exit
# import os
#
#
# os.system('ls -l');

a={1,2,3,4,5}
b={3,4,5,6,7}
# a 和b 的交集
# c=a.intersection(b)
# print(c)  {3, 4, 5}


# a 和 b 的 (对称差集) 差集
# c=a.symmetric_difference(b)
# print(c);  {1, 2, 6, 7}
# c=b.symmetric_difference(a)
# print( c) {1, 2, 6, 7}


# a 和 b 的 (a 的) 差集
# c=a.difference(b)
# print(c) {1, 2}


# a 和 b 的并集
# c=a.union(b)
# print(c) {1, 2, 3, 4, 5, 6, 7}

s={4,5}
t={3,4,5,6,7}
# 测试是否 s 中的每一个元素都在 t 中
# mark=s.issubset(t)
# print(mark)  True


# 测试是否 t 中的每一个元素都在 s 中
# mark=s.issuperset(t)
# print(mark) False


#  可变元祖  参数
# def f1(a):
#     print(a,type(a));
# f1(99);
# def f2(*a):
#     print(a,type(a));
# f2(11,22,33); #(11, 22, 33) <class 'tuple'>

#可变  字典参数
def f3(**a):
    print(a,type(a));
# f3(11,22);  TypeError: f3() takes 0 positional arguments but 2 were given
# f3(k1=22,k2=33);  {'k1': 22, 'k2': 33} <class 'dict'>


#可变  万能参数
# def f4 (a0,*a1,**a2):
#      print(a0,type(a0));
#      print(a1,type(a1));
#      print(a2, type(a2));
# f4(1111,22,33,44,55,66,k1=123,k2=234);
# 1111 <class 'int'>
# (22, 33, 44, 55, 66) <class 'tuple'>
# {'k1': 123, 'k2': 234} <class 'dict'>
# def f1(*a):
#     print(a,type(a));
# li=(11,22,33);
# f1(li,123)
# f1(*li,123)
# f1(11,22,33)
#  ((11, 22, 33), 123) <class 'tuple'>
# d(11, 22, 33, 123) <class 'tuple'>ic={k1}
# d(11, 22, 33) <class 'tuple'>ef f1(**  ('k1', 'k2') <class 'tuple'>a):
# dic={"k1":123,"k2":234}
# def f2(**b):
#     print(b,type(b));
# f2(k1=dic);  {'k1': {'k1': 123, 'k2': 234}} <class 'dict'>
# f2(**dic);   {'k1': 123, 'k2': 234} <class 'dict'>











