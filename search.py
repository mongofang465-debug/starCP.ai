import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# 读取 .env
load_dotenv()

client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"], 
    base_url="https://openrouter.ai/api/v1"
)


def search_person(name):

    prompt = f"""
你是一个信息整理助手。

请根据公开网络信息，整理该人物资料：

{name}

输出结构：

# 基本信息
- 姓名
- 年龄（如未知写未知）
- 学历

# 职业信息
- 职业
- 代表作品或经历

# 公开感情信息
- 如有公开报道则整理
- 无则写：未公开

# 家庭背景（公开信息）
- 未知则写未知

# 公众形象评价（基于媒体/采访）

# 性格特点（基于公开采访或报道）

# 公开采访观点摘要

要求：
- 不要编造
- 不确定写未知
- 仅基于公开信息
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
