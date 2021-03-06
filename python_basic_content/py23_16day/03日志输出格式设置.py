"""
============================
Author:柠檬班-木森
Time:2019/10/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
日志模块:logging(python中的官方库)

"""

import logging

# 创建一个日志收集器
my_log = logging.getLogger("my_log999")

# 设置日志收集器的收集等级
my_log.setLevel("DEBUG")


# str1 = "%(name)s %(levelname)s"

# 设置日志输出的格式
formater = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

# 日志的输出

# 创建一个输出导控制台的日志输出渠道
sh = logging.StreamHandler()
sh.setLevel("ERROR")
# 设置输出导控制台的格式
sh.setFormatter(formater)
# 将输出渠道添加到日志收集器中
my_log.addHandler(sh)


# 创建一个输出导文件的渠道
fh = logging.FileHandler(filename="test.log",encoding='utf8')
fh.setLevel('DEBUG')
# 设置输出导文件的日志格式
fh.setFormatter(formater)
# 将输出渠道添加到日志收集器中
my_log.addHandler(fh)



my_log.debug("这个是debug等级的日志")
my_log.info("这个是info等级的日志")
my_log.warning("这个是warning等级的日志")
my_log.error("这个是error等级的日志")
