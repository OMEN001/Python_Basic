"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字符串拼接


"""

s1 = "python"

s2 = "java"

# 第一种方式：+
s3 = s1 + s2
print(s3)

# 第二种方式：format()字符串格式化输出的方法
s4 = '{}{}'.format(s1, s2)

# print(s4)

# 第三种 F表达式(了解)
print('--------s5-----------')
s5 = F"{s1}{s2}"
print(s5)

print('--------s6-----------')
# 第四种 %s占位（传统格式化输出的方式）
s6 = "%s%s" % (s1, s2)
print(s6)

# 第五种：字符串拼接方法
s7 = ' '.join((s1, s2))  # s1+666+s2
print(s7)

a = ("hello", "你好", "18")
a1 = a[0]
a2 = a[1]
a3 = a[2]
a4 = "  ".join((a1, a2, a3))
print(a4)
