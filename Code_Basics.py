#基本规则：
#1.变量名称字母有分大小写，命令只有小写不能大写(如pirnt不能写成Print)
#2.编程基本条件：文本编辑器如NotePad++、Python命令窗口。
#3.括号内如果需要多个内容和条目，请用“，”逗号隔开，比如print输出多个值。
#4.★★任何语句的正文都需要隔开4个空格键然后书写。
#5.\t功能为插入4个空格（也就是Tab键），\n功能为插入换行。
#6.快捷键Ctrl+C:（鼠标在Console内操作）用于终止或停止程序运行，比如死循环等；
#7.str命令的使用：转换非字符串值表示为字符串。


#1_基本语句:输出print，单变量，多变量、数学计算。
Hello = 6.021
hello1 = Hello+5.04
display = "Hello World by variable"
A1, A2, A3 = 2.5, "goldwind", 28*70-30 #多个变量不要求必须一致格式
print (Hello)
print ("answer=", hello1)
print ("Hello World!")
print (display)
print ("result=", A1,A2,A3)

#2_While循环语句：当什么条件满足后执行某个运算或结果，并!!循环!!执行（对应if语句仅执行一次不循环）。
acc = 2
while acc<20: #注意条件写完后面要有个冒号，条件下面的所有行都会被依顺序执行。
    print ("init=",acc)
    acc=2+acc 
    print ("new data=", acc)
    
#3-for循环语句+列表：用于列表内容的条件选择、执行计算等。
list1=[1,3,4,6,7,8,9,2,3,45,667,23]
for inin in list1:
    print(inin+2)
    print("List1=",list1[4])#附加学习-用去提取列表中第5位元素。
	
for letter in 'Python':     # 第一个实例
    print("当前字母 :",letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print("当前水果：",fruit)
 
print("Good bye!")
	
#4-if条件语句:条件满足后执行一次，和while对比是非循环的条件判断语句（真或假），非循环。
ages = list(range(20,30))
for age in ages:
    if age > 20: 
        print(age,"你不能买酒。")
    else:
        print ("young",age,"我要买酒")
#5-if语句扩展到if-else,if-elif-else,其中elif,if都可以多次使用。
you = 16
me = 22
if you >22 :
    print("you are a good boy")
elif you>17:
    print("you can try")
elif you>6:
    print("you are lucky")
else: 
    print("you are a girl")
if me >10:
    print("My age is",me)

#6-列表的编写和应用（详见课本功能更多）。
list2=list(range(3,9))
print ("List2=",list2)
list3=[]
for bill in range(1,5):         
    list3.append(bill**2)  #给每个元素取平方：命令：列表名.append(元素平方)
print("List3=",list3)
print("The Min of list3 is:",min(list3))
print("The Max of list3 is:",max(list3))
print(list3[1])#打印该列表中第2个元素。

#7-函数的定义和调用
def fun():
    a=21
    b=22
    c=a*b
    print (c)
    return a+b+c
print(fun())
#8-列表\元组\词典的区别：
    列表用方括号或无括号，元组用小括号，字典用大括号。
	#列表内容可以修改和计算，元组内容不可更改和计算，除非生成新元组。
list_example1 = [1,2,3,3,4,5]
list_example2 = 1,2,3,4,5
demension_yuanzu = (1,2,3,4,5)
list_zidian = {"item1":22, "item2":35, "item3" = "txt_book"}
#9-input命令和数据类型格式转换int
age = input("print your age = ") # 注意input命令用户输入的信息系统默认是字符串。
age1 = input(variable)# 注意input命令内也可以套入其他变量或结果同步输出。
age=int(age) #此处将输入的age值强制转换成整数利用int命令。
if age >=20:
    print("you can vote")
else:
    print ("hello boy")
numb = 3%2 # %符号用于取整除余数（或者叫模）
print (numb)
#10-同一个变量+=命令：
    用于给原变量做叠加，可以是数字也可以说字符串，但是原变量和+变量必须同类型。
test = 2
test +=3
print(test) #结果就会输出5（2+3的结果）。
test="gold"
test +="wind"
print(test) #结果就会输出goldwind（gold+wind的结果）。