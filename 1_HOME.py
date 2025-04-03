"""
@file    1_HOME.py
@brief
@details

@author  nottoday <776038371@qq.com>
@version v1.0.0
@date    2025/4/3
@license MIT (See LICENSE in project root)

@history
@depends
"""
import streamlit as st

from COMMON_FUNC import clear_foot

PAGE_CONFIG = {"page_title":"Home",
           "layout":"wide",
           "initial_sidebar_state":"auto",
            "page_icon":"random"

       }
st.set_page_config(**PAGE_CONFIG)
clear_foot()