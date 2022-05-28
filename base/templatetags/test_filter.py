# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 21:31
# @Author  : daibeisi
# @FileName: test_filter.py
# @Blog    ：https://blog.bookhub.com.cn
from django import template

register = template.Library()


@register.filter(name="coderstatus")
def coderstatus(value, arg):
    """返回coder的状态"""
    if value == "morehair":
        return '{}是”菜鸟“程序员'.format(arg)
    if value == "middlehair":
        return '{}是工程师级程序员'.format(arg)
    if value == "fewhair":
        return '{}是资深程序员'.format(arg)
