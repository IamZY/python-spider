# -*- coding:utf-8 -*-

import re

# pattern = re.compile(r"\d+")
# pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I)
pattern = re.compile(r"(\w+) (\w+)")

# m = pattern.match("aaa123bbb456")
# m = pattern.match("aaa123bbb456",3,5)  # 12
# m = pattern.match("Hello World hello Python")
# m = pattern.search(r"Hello 123 World hello Python")
# m = pattern.findall(r"Hello 123 World hello Python")

str = "hello 123 hello 456"

m = pattern.sub(r"\2 \1",str)


# 取对象中的使用group
# print m.group()
# print m[0]
print m
# m.span()
# mm = "123;123"
#
# mm = mm.split(";")
#
# print mm
