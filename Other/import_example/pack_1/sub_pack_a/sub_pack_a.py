from pack_2.sub_pack_b.sub_pack_b import func_sub_pack_b, sub_pack_b

sub_pack_a: str = "asdfasdf"


def func_sub_pack_a():
    print('sub_pack_a')
    func_sub_pack_b()
    print(sub_pack_b)
