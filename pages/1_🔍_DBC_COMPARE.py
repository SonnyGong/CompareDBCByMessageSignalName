"""
@file    1_🔍_DBC_COMPARE.py
@brief
@details

@author  nottoday <776038371@qq.com>
@version v1.0.0
@date    2025/4/3
@license MIT (See LICENSE in project root)

@history
@depends
"""

import cantools
import streamlit as st
import os
from COMMON_FUNC import clear_foot
from pages.DBC_COMPARE.FUNC import *
version = "DBC_COMPARE"
st.title(f'当前功能：{str(version)}')
st.caption("上传旧dbc文件和新dbc文件，列出这两个dbc的区别，主要从ID、以及Signal的名称方面进行比对！")
uploaded_file_OLD = st.file_uploader("选择旧版本DBC文件，最大支持200M",type='dbc',help='请上传需要dbc文件')
uploaded_file_NEW = st.file_uploader("选择新版本DBC文件，最大支持200M",type='dbc',help='请上传需要dbc文件')
IS_NG = 0
if uploaded_file_OLD is not None and uploaded_file_NEW is not None:
    name_old,ext_old = os.path.splitext(uploaded_file_OLD.name)
    name_new, ext_new = os.path.splitext(uploaded_file_NEW.name)
    if ext_old == ".dbc" and ext_new == ".dbc":
        #
        data_old = uploaded_file_OLD.read().decode('utf-8', "ignore")
        data_new = uploaded_file_NEW.read().decode('utf-8', "ignore")
        # st.write(uploaded_file.name)
        try:
            test_1 = cantools.database.load_string(data_old)
            # st.write(uploaded_file_OLD.name)
            st.write("老版本DBC正常")
        except Exception as e:
            IS_NG = 1
            st.write(uploaded_file_OLD.name)
            st.write(" :red[**老版本DBC存在问题： "+str(e)+"**]")
        try:
            test_2 = cantools.database.load_string(data_new)
            # st.write(uploaded_file_NEW.name)
            st.write("新版本DBC正常")
        except Exception as e:
            IS_NG = 1
            st.write(uploaded_file_OLD.name)
            st.write(" :red[**新版本DBC存在问题： "+str(e)+"**]")
        if not IS_NG:
            old_diff_dict = {}
            new_diff_dict = {}
            old_dbc_dict = return_messages_from_dbc(test_1)
            new_dbc_dict = return_messages_from_dbc(test_2)
            old_diff, new_diff, common_elements = compare_lists(list(old_dbc_dict.keys()), list(new_dbc_dict.keys()))
            st.caption("============================================================================================")
            if old_diff != []:
                st.write("新版本删除 的报文ID:", old_diff)
            if new_diff != []:
                st.write("新版本新增 的报文ID:", new_diff)
            st.caption("============================================================================================")
            for to_compare_id in common_elements:

                old_diff, new_diff, common_elements = compare_lists(old_dbc_dict[to_compare_id],
                                                                    new_dbc_dict[to_compare_id])
                if old_diff != [] or new_diff != []:
                    # st.write("\n", to_compare_id)
                    if old_diff != []:
                        old_diff_dict[to_compare_id] = old_diff
                    if new_diff != []:
                        new_diff_dict[to_compare_id] = new_diff
            if old_diff_dict != {}:
                st.write("新版本删除 的Signal:",old_diff_dict)
            st.caption("============================================================================================")
            if new_diff_dict != {}:
                st.write("新版本新增 的Signal:",new_diff_dict)


    else:
        st.write("上传的文件种类不正确，请检查！")




clear_foot()