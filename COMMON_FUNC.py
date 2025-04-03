"""
@file    COMMON_FUNC.py
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

def clear_foot():
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)