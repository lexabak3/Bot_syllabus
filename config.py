# -*- coding: utf-8 -*-
from datetime import *
from data import *


def check_day():
    data = datetime.today()
    return data


def check_num_week(n=0):
    data = datetime.today()
    if n != 1:
        return data.isocalendar()[1] - first_week
    else:
        return data.isocalendar()[1]
    #return ret_num_week


def check_type_week():
    data = datetime.today()
    num_of_week = data.isocalendar()[1]
    if (num_of_week - first_week) % 2 != 0:
        type_week = 'Нечётная (н/н)'
    else:
        type_week = 'Чётная (ч/н)'
    return type_week


def give_syllabus(text='', n=0):
    day = datetime.isoweekday(datetime.today())
    if n != 0:
        if day == 7:
            n = -6
    if text != '':
        return_week = week[text]
    else:
        return_week = week[day + n]
    return return_week


def give_syllabus_full_week():
    full_week = '\n'
    for i in range(len(week)-1):
        full_week = full_week + week[i+1] + '\n'
    return full_week
