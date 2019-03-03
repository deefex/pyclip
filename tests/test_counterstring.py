from pyclip.counterstring import generate_counterstring


def test_counterstring_negative():
    assert generate_counterstring('*', -10) == ''


def test_counterstring_length_0():
    assert generate_counterstring('*', 0) == ''


def test_counterstring_length_1():
    assert generate_counterstring('*', 1) == '*'


def test_counterstring_length_2():
    assert generate_counterstring('*', 2) == '2*'


def test_counterstring_length_3():
    assert generate_counterstring('*', 3) == '*3*'


def test_counterstring_length_4():
    assert generate_counterstring('*', 4) == '2*4*'


def test_counterstring_length_5():
    assert generate_counterstring('*', 5) == '*3*5*'


def test_counterstring_length_10():
    assert generate_counterstring('*', 10) == '*3*5*7*10*'


def test_counterstring_length_35():
    assert generate_counterstring('*', 35) == '2*4*6*8*11*14*17*20*23*26*29*32*35*'


def test_counterstring_length_57():
    assert generate_counterstring('*', 57) == '*3*5*7*9*12*15*18*21*24*27*30*33*36*39*42*45*48*51*54*57*'


def test_counterstring_length_100():
    assert generate_counterstring('*', 100) == '*3*5*7*9*12*15*18*21*24*27*30*33*36*39*42*45*48*51*54*57*60*63*66*69*72*75*78*81*84*87*90*93*96*100*'
