#!/usr/bin/python3
def lookup(obj):
    return dir(obj)

class MyClass1(object):
    pass

    def my_meth(self):
        pass

    print(lookup(MyClass1))
    print(lookup(int))
