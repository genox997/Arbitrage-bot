


import math

def twoway(p1,p2):
    stake = 100
    p1_amount = truncate((float(stake)*float(p2))/(float(p1)+float(p2)))
    p2_amount = truncate((float(stake)*float(p1))/(float(p1)+float(p2)))
    profit = truncate((float(stake)*float(p1)*float(p2))/(float(p1)+float(p2))-float(stake))
    return p1_amount, p2_amount,profit

def threeway(w,d,l):
    stake = 100
    w=(float)(w)
    d=(float)(d)
    l=(float)(l)


    w_amount = truncate((float(stake)*float(1/w))/(float(1/w)+float(1/d)+float(1/l)))
    d_amount = truncate((float(stake)*float(1/d))/(float(1/w)+float(1/d)+float(1/l)))
    l_amount = truncate((float(stake)*float(1/l))/(float(1/w)+float(1/d)+float(1/l)))
    profit = truncate((float(w)*w_amount)-100)
    return w_amount, d_amount,l_amount ,profit


def truncate(number) -> float:
    stepper = 10.0 ** 2
    return math.trunc(stepper * number) / stepper