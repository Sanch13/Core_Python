class AttrDisplay:
    def gather_attributes(self):
        attr = []
        for k, v in sorted(self.__dict__.items()):
            attr.append(f"{k}={v}")
        return ', '.join(attr)

    def __repr__(self):
        return f'[{self.__class__.__name__}: {self.gather_attributes()}]'


if __name__ == '__main__':
    class Top(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = Top.count
            self.attr2 = Top.count
            Top.count += 1


    class SubTop(Top):
        pass

    x, y = Top(), SubTop()
    print(x)
    print(y)
