"""
============================
Author:柠檬班-木森
Time:2019/9/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
for 循环：迭代循环
语法格式：  
for 变量 in 遍历的数据：
    # 遍历出来一个数据时，去执行的代码
            



# 当前有10位 同学的成绩，请区分成绩的等级
小于60分：不及格

60-79：及格

80以上（包括80）：优秀


"""

li = [78, 32, 55, 77, 88, 90, 54, 24, 67, 39]

for num in li:
    print('当前的成绩是：{}'.format(num))
    if num < 60:
        print("您的成绩不及格，赶紧回去补课")
    elif num < 80:
        print("您的成绩及格了，很不错")
    else:
        print("您的成绩非常的优秀")


# 内置函数：range()
# 传一个参数：默认从0开始，参数值代表终止位置的值
# 传2个参数：第一个代表起始位置，第二个代表终止位置，（左闭右开）
# 传三个参数:第一个代表起始位置，第二个代表终止位置，（左闭右开）,第三个代表步长

# print(list(range(10)))
# print(list(range(0,10,5)))

#  for循环实现：打印100遍hello python

# for i in range(1,101):
#     print(i)
#     print('hello python')
#     print('这是第{}次'.format(i))

