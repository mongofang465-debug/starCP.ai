import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# 读取 .env
load_dotenv()

# OpenRouter Key
client = OpenAI(
    api_key=st.secrets("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_single(profile):

    prompt = f"""
你是一个娱乐向AI情感分析师。

以下信息来自公开资料整理：

{profile}

请输出：

# 人物画像
# 性格特点
# 公开资料体现的择偶倾向（娱乐推测）
# 可能偏好的伴侣类型
# 家庭观分析（基于公开信息）
# 娱乐向婚姻/家庭模式推测
# 情感建议

要求：
- 只做娱乐分析
- 不要当作事实
- 不要断言未来
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
    
def analyze_cp(profile1, profile2):

    prompt = f"""
你是一个娱乐向明星CP分析师。

人物A资料：
{profile1}

人物B资料：
{profile2}

请输出：

# CP匹配度（0-100）
# 性格契合度
# 事业观匹配度
# 家庭观匹配度
# 潜在矛盾点
# 相处挑战
# 娱乐向关系建议
# 综合评价

要求：
- 仅娱乐分析
- 不要预测真实未来
- 不要当作事实
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content    
