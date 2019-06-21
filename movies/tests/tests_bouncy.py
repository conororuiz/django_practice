from unittest import TestCase
import time

def list_number(num):
    num=str(num)
    list = []
    for i in num:
        list.append(i)
    return list

def is_bouncy(num):
    lista = list_number(num)
    creci = True
    for pos in range(0, len(str(num)) - 1):
        if lista[pos + 1] < lista[pos]:
            creci = False
            break
    decre = True
    for pos in range(0, len(str(num)) - 1):
        if lista[pos + 1] > lista[pos]:
            decre = False
            break
    if not creci and not decre:
        return True
    else:
        return False

def bouncy_numbers(porc: float):
    if porc>=1.0 or porc<=0.0:
        return 0
    num = 0
    i = 0
    j = 0

    while num != porc:
      i += 1
      if is_bouncy(i):
          j += 1
          num = j/i

    return i




class TestListNumber(TestCase):

   def test_if_get_str_return_str_list(self):
       assert list_number('121') == ['1','2','1']

   def test_if_get_int_return_str_list(self):
       assert list_number(121) == ['1','2','1']

class TestIsBouncy(TestCase):

    def test_if_get_538_return_true(self):
        assert is_bouncy(538) is True

    def test_if_get_21780_return_true(self):
        assert is_bouncy(21780) is True

    def test_if_get_100_return_true(self):
        assert is_bouncy(100) is False

class TestBouncyNumber(TestCase):

    def test_the_percentage_99_is_1587000(self):
        assert bouncy_numbers(0.99) == 1587000

    def test_the_percentage_100_return_0(self):
        assert bouncy_numbers(1) == 0

    def test_the_percentage_50_is_538(self):
        assert bouncy_numbers(0.5) == 538

    def test_the_percentage_is_negative_return_0(self):
        assert bouncy_numbers(-1) == 0