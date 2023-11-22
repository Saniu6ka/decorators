from tests import test_1, test_2
from functions import flat_generator



if __name__ == '__main__':
    test_1()
    test_2()
    gen = flat_generator([[1, 2], [3, 4]])
    for item in gen:
        print(item)