# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 22:24
# @Author  : daibeisi
# @FileName: test_tag.py
# @Blog    ：https://blog.bookhub.com.cn
from django import template

register = template.Library()


@register.simple_tag(name="test_simpletag")
def test_simpletag(*args):
    agr_str = "".join(args)
    return "这是一个simpletag示例，它接收的参数是:{}".format(agr_str)

