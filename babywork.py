import random

str0 = '♥'
str1 = '●'
str2 = '▲'
str3 = '☆'
str4 = '△'
str5 = '○'

def kenengxing(x,y,res):
    #计算 x 到 y 加法、减法 res结果以内有几种可能性
    set1 = set()
    for a in range(x,y):
        for b in range(x,y):
            if (a + b <= res):
                set1.add(str(a) + ' + ' + str(b) + ' = ' + str(a+b))

    set2 = set()
    for a in range(x,y):
        for b in range(x,y):
            if (x <= a - b < y):
                set2.add(str(a) + ' - ' + str(b) + ' = ' + str(a-b))

    print(len(set1))
    print(set1)
    print(len(set2))
    print(set2)

#kenengxing(1,10,10)

#10内加减法
def add10(NumOfTime):
    for each in range(NumOfTime):
        ret3 = random.randint (0,1) #0减法，1加法
        if ret3 :
            ret  = random.randint (1,9)
            ret2 = (random.randint (1,10-ret))
            print("%d + %d = " % (ret,ret2) ,end="          ")
        else :
            ret  = random.randint (1,10)
            ret2  = random.randint (ret+1,10)
            print("%d - %d = " % (ret2,ret) ,end="          ")
        if each % 4 == 0:
            print('\r')

#20内加减法
def add20(NumOfTime):
    for each in range(NumOfTime):
        if each % 4 == 0 and each != 0:
            print('\r')
        ret3 = random.randint (0,1) #0减法，1加法
        if ret3 :   #加法
            ret  = random.randint (1,19)
            ret2 = (random.randint (1,20-ret))  #被加数
            print("%d + %d = " % (ret,ret2) ,end="        ")
        else :      #减法
            ret  = random.randint (1,20)
            ret2  = random.randint (ret+1,20)   #被减数
            print("%d - %d = " % (ret2,ret) ,end="        ")








def getAddRandom():
    x  = random.randint (1,9)       #加数
    y = (random.randint (1,10-x))  #被加数
    return (x,y)

def getSubRandom():
    x  = random.randint (2,10)      #减数
    try:
        y = (random.randint (1,x-1))  #被减数
        return (x,y)
    except :
        print('*************************************************')
        return (x,2)


#加法
def addMid(x,y):
    print("%d + (  ) = %d" % (x,x+y) ,end="     ")

def addLeft(x,y):
    print("(  ) + %d = %d" % (x,x+y) ,end="     ")

def addRight(x,y):
    print("%d + %d = (  )" % (x,y) ,end="     ")


#减法
def subLeft(x,y):
    print("(  ) - %d = %d" % (y,x-y) ,end='     ')

def subMid(x,y):
    print("%d - (  ) = %d" % (x,y) ,end='     ')

def subRight(x,y):
    print("%d - %d = (  )" % (x,y) ,end='     ')


AddOrSubLMR = {0:addLeft ,1:addMid,2:addRight,3:subLeft ,4:subMid ,5:subRight}

def exercises(o):
    if o < 3:
        x,y = getAddRandom()
    elif o >= 3:
        x,y = getSubRandom()
    AddOrSubLMR.get(o)(x,y)



def get10(NumOfTime = 10,type = 6):
    '''
    函数解释：出10以内加减题目；
    参数一，出题数目；
    参数二，出题模式：
    0、加法，括号在左边
    1、加法，括号在中间
    2、加法，括号在右边
    3、减法，括号在左边
    4、减法，括号在中间
    5、减法，括号在右边
    6、随机加减法 and 随机括号位置；
    '''
    for each in range(NumOfTime):
        if each % 4 == 0 and each != 0:
                print('\r')
        if 0 <=  type < 5:
            exercises(type)
        else :
            AddOrSub = random.randint (0,5)
            exercises(AddOrSub)

def getadd10(NumOfTime = 10):
    '''
    函数解释：出10以内加题目；
    参数一，出题数目；
    '''
    for each in range(NumOfTime):
        if each % 4 == 0 and each != 0:
            print('\r')
        AddOrSub = random.randint (0,2)
        exercises(AddOrSub)
    print('\n\n')

def getsub10(NumOfTime = 10,type = 6):
    '''
    函数解释：出10以内减题目；
    参数一，出题数目；
    '''
    for each in range(NumOfTime):
        if each % 4 == 0 and each != 0:
            print('\r')
        AddOrSub = random.randint (3,5)
        exercises(AddOrSub)
    print('\n\n')

def morethenit(NumOfTime = 1):
    #教育孩子哪个比哪个多的概念。多多少。

    for each in range(NumOfTime):
        star,trigon = random.sample(range(11),2)
        #star = random.randint(1,10)
        #trigon = random.randint(1,10)


        if star > trigon :
            strx = str('%s 比 %s 多几个？' % (str1 * star, str2 * trigon))
        elif star < trigon :
            strx = str('%s 比 %s 多几个？' % (str3 * trigon ,str4 * star))
        else:
            strx = str( '%s 比 %s 多几个？' % (str0 * trigon ,str5 * star) )
        print(strx,end='  ' * (20-star-trigon))
        print('(   )   ( )   (   )  =  (   )')
    print('\n\n')

#getsub10(32)
#getadd10(32)
#morethenit(100)
def test():
    morethenit(10)
    getsub10(32)
    getadd10(32)

if __name__ == '__main__':
    test()


