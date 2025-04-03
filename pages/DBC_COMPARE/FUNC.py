"""
@file    FUNC.py
@brief
@details

@author  nottoday <776038371@qq.com>
@version v1.0.0
@date    2025/4/3
@license MIT (See LICENSE in project root)

@history
@depends
"""


def return_messages_from_dbc(test):
    return_dict = {}
    for message in test.messages:
        return_dict[hex(message.frame_id)] =  message.signal_tree
    return return_dict

def compare_lists(old_list, new_list):
    # 使用集合来获取差异
    old_set = set(old_list)
    new_set = set(new_list)

    # 旧列表有但新列表没有的元素
    old_diff = sorted(list(old_set - new_set))

    # 新列表有但旧列表没有的元素
    new_diff = sorted(list(new_set - old_set))

    # 两个列表都有的元素
    common_elements = sorted(list(old_set & new_set))
    # if old_diff != []:
    #     print("旧列表有但新列表没有的元素:", old_diff)
    # if new_diff != []:
    #     print("新列表有但旧列表没有的元素:", new_diff)
    # print("两个列表都有的元素:", common_elements)

    return old_diff, new_diff, common_elements