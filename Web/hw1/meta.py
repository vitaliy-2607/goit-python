class Meta(type):
    class_number = 0

    def __new__(mcs, *args, **kwargs):
        instance = super().__new__(mcs, *args, **kwargs)
        instance.class_number = mcs.class_number
        mcs.class_number = mcs.class_number + 1
        return instance


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
