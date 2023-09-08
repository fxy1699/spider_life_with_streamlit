import streamlit as st
from streamlit_chat import message
import requests
import json


 

API_KEY = "9N2AfHbW7mT6fl1dmqBLsGcb"
SECRET_KEY = "DvqDEYDt5PjGWSFErbXOLGymR3qujDxV"
 
 
# 如果没有 prompts 这个 session_state，就初始化
if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [
        {"role":"user","content":"很好，请继续以蜘蛛侠为主人公进行人生重开模拟，可以参考《蜘蛛侠：纵横宇宙》中的角色"},
        {"role":"assistant","content":"1岁：你出生了，是个男孩。\
2岁：你的父母带你去看了电影《蜘蛛侠》，你被蜘蛛侠的英勇事迹所吸引。\
3岁：你开始模仿蜘蛛侠的动作和姿势，你的父母为你购买了一些蜘蛛侠的玩具。\
4岁：你开始对科技和机械产生兴趣，你尝试制作一些简单的道具和装备。\
5岁：你参加了学校的科技竞赛，你用你的道具和装备制作了一个简单的蜘蛛机器人，赢得了比赛的冠军.\
6岁：你开始学习编程和机械设计，你想成为一名像蜘蛛侠一样的超级英雄。\
7岁：你的父母给你买了一台电脑，你开始自学编程和机械设计。\
8岁：你用你的电脑和机械技术制作了一个简单的蜘蛛机器人，它能够爬墙和发射蜘蛛丝。\
9岁：你在学校的科技竞赛中展示了你的蜘蛛机器人，引起了学校老师的注意。\
10岁：你开始在学校的科学实验室里进行研究和实验，探索更多关于蜘蛛和机械的技术。\
11岁：你在学校的科技竞赛中获得了更多的奖项和荣誉，你的蜘蛛机器人也变得更加先进和复杂。\
12岁：你在互联网上发现了更多的关于超级英雄和机械技术的信息，你开始探索更多新的技术和创意。\
13岁：你用你的技术和创意制作了一个全新的蜘蛛机器人，它拥有更加强大的功能和技能。\
14岁：你在学校的科技实验室里进行了一次实验，你不小心被一只辐射蜘蛛咬伤了。你在学校的科技实验室里进行了一次实验，你不小心被一只辐射蜘蛛咬伤了。\
15岁：在辐射蜘蛛的毒素影响下，你的身体开始发生变异。你开始出现一些奇怪的症状，比如夜间的蜘蛛爬行感觉、超强的力量和敏捷性等。你决定利用你的能力帮助别人，并使用你的技能和机械技术成为了一名超级英雄，被称为“蜘蛛侠”。\
16岁：你继续完善你的技能和装备，学习更多的武术和机械技术。你开始在城市中阻止一些小规模的犯罪行为，并逐渐得到了人们的认可和尊敬。\
17岁：你遇到了一个神秘的导师，他教会了你更多关于超级英雄的事情，并帮助你提高你的技能和战斗策略。\
18岁：你在一次阻止犯罪的行动中，暴露了自己的真实身份。你的家人和支持者们开始意识到你是一名超级英雄，这也让你面临着更多的挑战和危险。"},
        {"role":"user","content":"请仿照上面从一岁开始生成一段新的蜘蛛侠的人生，到35岁为止，每生成一岁请换行"},
        ]
# 如果没有 generated 这个 session_state，就初始化
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
# 如果没有 past 这个 session_state，就初始化
if 'past' not in st.session_state:
    st.session_state['past'] = []
 


 
#生成鉴权信息
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 
# 生成的回答
def generate_response():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    headers = {
        'Content-Type': 'application/json'
    }
    # 把用户输入的消息加入到 prompts 中
    #st.session_state['prompts'].append({"role": "user", "content":prompt})
    question = {
        "messages":st.session_state.prompts
    }
    payload = json.dumps(question)
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
 
 
# 重置聊天界面
def end_click():
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state['user'] = ""
 
 
# 处理聊天按钮点击事件
def chat_click():
    output=generate_response()
    # 把生成的回答和用户输入的消息存储到 session_state 中
    st.session_state['generated'].append(output)
    #st.session_state['prompts'].append({"role": "assistant", "content": output})
    st.session_state['user'] = ""
 
 

 
# 显示 ChatBot 界面
#st.image("logo.png", width=80)
st.title("Spider Life")
 
 
# 显示用户输入框
#user_input=st.text_input("You:", key="user")
 
 
# 显示聊天和重置按钮
col1, col2, col3 , col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    pass
with col2:
    pass
with col3:
    pass
with col4:
    chat_button=st.button("Go", on_click=chat_click)
with col5:
    end_button=st.button("Reset", on_click=end_click)
with col6 :
    pass
with col7:
    pass
with col8:
    pass


 
 
## 显示 ChatBot 的回答和用户的输入
#if st.session_state['generated']:
#    # 倒序遍历已经生成的回答和用户的输入
#    for i in range(len(st.session_state['generated'])-1, -1, -1):
#        # 分别使用两种方式显示 ChatBot 的回答
#        tab1, tab2 = st.tabs(["normal", "rich"])
#        with tab1:
#            message(st.session_state['generated'][i], key=str(i) + '_generated')
#        with tab2:
#            st.markdown(st.session_state['generated'][i])
#        # 显示用户的输入
#        message(st.session_state['past'][i], is_user=True, key=str(i) + '_past')
        
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        answer_json = json.loads(st.session_state['generated'][i])
        st.markdown(answer_json["result"])
        