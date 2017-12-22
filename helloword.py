#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print ("hello,word")
#
# dic={'key1':123,'key2':456,'key3':111}
# 需求  key1   key2     默认值都是123
# n=dict.fromkeys(['key1','key2','key3'],[])
# n['key1'].append('x');
# # 找到和没找到  效果一
# n1={'key1': [], 'key2': [], 'key3': []}
# n1['key1'].append('x')
# print(n1);
# print(n);
# # @staticmethod   静态方法；是类调用的
#
# {'key1': ['x'], 'key2': [], 'key3': []}
# {'key1': ['x'], 'key2': ['x'], 'key3': ['x']}


# li=[11,22,33,44];
# for item in li:
#     print(item);
# 11
# 22
# 33
# 44
# for k,v in enumerate(li,2):
#
#     print(k,v)

# 2 11
# 3 22
# 4 33
# 5 44

# r=range(1,20);  # 1<=r<20
# print(r);
# for item in r:
#     print(item);

    # range(1, 20)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19


# r=range(1,20,2);
# # print(r); range(1, 3, 20)
# for item in r:
#     print(item);
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# r=range(30,0,-3);
# for item in r:
#     print(item);
    # 30
    # 27
    # 24
    # 21
    # 18
    # 15
    # 12
    # 9
    # 6
    # 3


# ASCII   美国信息交换标准代码  主要用于英文
# unicode 万国码

# 详情见  博客  计算
# 我=0;
# while 我< 10:
#     我+= 1;
#     print(我);
#
#
# else:
#     print("我=10  break");


# 一、回顾
#     1顶部
#         解释器
#         编码
#     2 print"";
#       print()；
#     3编码
#         ascii(1个字节（8位）来表示)->unicode->(最少占用2个字节，用两个字节来表示一个字节，浪费，所以对其压缩  出现了gbk,utf-8,gb2312，); 用一个字节

      # 4变量
      #       首字母不能是数字，
      #       变量名不能是关键字
      #       数字，字母，下划线
      #       py3.6  可以是汉子
      # 5流程控制
      #    5.1 条件
      #           if 条件:
      #               pass
      #           elif 条件:
      #               pass
      #           else:
      #               pass
      #           --缩进
      #    5.2 循环
      #
      #        while 条件
      #            while 条件:
      #                 pass
      #            continue (结束当前循环 继续进行下一步循环)
      #            break （所有循环全部终止）
    #

    # 第二天
    # 1
        # 运算符:
        # *=
        # +=
        # c+=2   (c=c+2)
        # num=123;
        # ret=num % 2 ;
        # if ret==0:
        #     #偶数
        # else:
        #     奇数
      # 判  一个字符串 在不在列表里面
      # li=['alex','jason'];
      # num='alex';
      # if num in li and  num.startswith('a'):
      #     print("zai");
      # else:
      #     print('buzai')
      # 2 基本的数据类型；
#       1   int ，整形
#         n=123;
#         n=int(123); #执行int的——init——
#         s="123";
#         m=int(s);

        # 不能转换的在  py里面
        # a='123sd';
        # b=int(a);
        # print(b);
#           (2.7  才有长度，  32位系统    2的31   次方       64位  2的63次方   py3  没长度限制)
#     2  str，字符串
#         s="sbc";
#         s=str("abc");
#         a=123;
#         m=str(a);
#    3 bytes，字节类型
        # 目的是   字节转换成字符串；
        # b='字节类型的对象';(不知道  utf-8还是  gbk)
        # m=str(b,encoding="utf-8");
        # 首字母大写   变大小写；
        # 去空格
        # 替换
        # 是否是  字母  数字
        # 以什么开头，结尾
        # 查找
        # 查找个数
        # 格式化=============
        # 编码，解码
        # 居中，  左右
        # 填充
        # 链接 li=['alex','jason']  l1='_'.join(li);
        # 截取
      # 4 list,列表；
      # i=[11,22,33,44];
      # i1=list([11,22,33,44]); 一个元素一个元素循环后加到里面

# # # # # # # # # # # # # # # # # #  写列表 都要加一个，[11,22,33,]
#        t=(11,22,33);
#        i=list(t);

            # 列表公共功能
            # 索引
            # 切片
            # for
            # 长度
            # enumerate
            # in
            # del  del li[0]
            #
            # 特有功能：
            # 翻转
            # 排序
            # append  追加
            # insert  插入
            # 索引位置
            # 删除
            # 个数  count
            # 扩展
            # 清除

            # 元组
            # t=(11,22,33);
            # t=tuple(可迭代对象);
            #  列表转元祖
            #  li=[11,22,33,];
            #  m=tuple(li);  # 列表公共功能
            # 索引
            # 切片
            # for
            # 长度
            # enumerate
            # in
            # 特有功能：

            # 索引位置
            # 个数  count
            # 元组 特性
            #   儿子不能被修改，孙子可能被修改
            # 字典：
            # d={
            #     "k1":123,
            #     "k2":456
            # };
            # 列表转字典
            #     需求  列表转字典，转字典时候，key 从10 往后递加 value  是列表的元素
            #
            # li=[11,22,33,44];
            # dic={};
            # for i,j in enumerate(li,10):
            #     dic[i]=j;
            #
            #
            #     等价下面；
            # new_dict=dict(enumerate(li,10));


            # 增加
            #   d.update({
            #       "k3":234
            #   });
            #  d['k1']=123;




            # 公共的功能
            # 索引
            # 增加 dic[key]=value
            # 删除 del
            # for
            # 长度
            # in
            # 特有功能：
            #     项
            #     所有的key
            #     所有的值
            #     get
            #
            #     has_key=> py3 没了
            #       代替
            #       xxx in dic.keys();
            #     update
            #     clear
            #     formkeys

# 字符串和字节之间转换
# a="李杰";
# 把李杰 变成gbk编码的字节；
# b=bytes(a,encoding="gbk");   //  type(b)=>bytes
# c=str(b,encoding="gbk")

# int  优化机制；
# a=123;
# b=123;
# id(a);  查看内存地址
# 相同因为  有优化 -5 ~~257；
# a=123;
# b=a;
#
# 查看内存地址   id();
# 类似  a=1234444;
#       b=a;
#

# set   就是 无序的 不重复的集合
# 列表   是有序的  可以重复  允许修改 l=list()
# 元祖   是有序的 可以重复  不允许修改
# 字典是  无序列的
# set   不允许重复的集合 （列表）
#  创建
 # s=set([可迭代的对象]);

# myset=set=([11,22])
# print(myset);
#1创建集合 只能创建空的
# s=set();
#或{11，22，33}


# l=[1,2,3,4];
# l=(1,2,3,4)
#2转换
# s1=set(l);


se=set();
# se.add(88)
# print(se);
# se.clear();
# print(se);
# {88}
# set()
# se={11,22,33}
# be={22,55}
# ret=se.difference(be)  #此函数不会改变原来的值 要赋值给新的变量
# #找到se 存在  be 不存在的  se 值  不会改变原来的值 要赋值给新的变量
# ret2=be.difference(se)
#
# #找到be 存在  se 不存在的  be 值
# print(ret2)
# print(ret)
# # {55}
# # {33, 11}
#
# se.difference_update(be)
#
# #找到se 存在  be 不存在的  se 值  跟新自己 {33, 11}
# print(se)

# se={11,22,33}
# se.discard(44) # 不报错
# se.remove(44)# 报错
# se.discard(11)# 移除有两个   discard  不报错   remove  报错
# ret=se.pop();# 顺序不一定
# #移除后有返回值

#交集
# se={11,22,33}
# be={22,66,77}
# # intert=se.intersection(be)
# # se.intersection_update(be)
# # print(se)
# # print(intert)
#
#
# # 是否有交集  有交集  返回  false  没 返回 true
# se={11,22,33}
# be={22,66,77}
# ret=se.isdisjoint(be)
# print(ret)



se={11,22,33,44,55}
be={11,33}

#子序列
# ret1=se.issubset(be);
# ret2=be.issubset(se);
# print(ret1)
# print(ret2)
# False
# True
#父序列
ret=se.issuperset(be)
print(ret); #



# se={11,22,33,44}
# be={11,22,77,55}
# # s1存在  be  不 存在
# r1=se.difference(be)
# #be 存在  se  不存在
# r2=be.difference(se)
# se.difference_update(be)
#
#
#
# ret=se.union(be)
#
#
# se.update(be)
# se.update([33,44,55])


# 3 yuan   yun  suan
name='ddddd'  if 1==1 else 'ggggg';
print(name)




# str  一次性创建，不能被修改，只要修改  就在创建
# list  链表  下一个元素的位置，上一个元素的位置。

# 0   alex
# 1   ldm
# 2   kwl
# 4   gaopang

# 深浅copy
#对于数字和字符串而言，赋值，拷贝，深浅拷贝 无意义，因为指向同一个内存地址。
#对于数字和字符串而言，赋值，拷贝，深浅拷贝 无意义，因为指向同一个内存地址。

