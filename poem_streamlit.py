import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# import os
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

st.title("_AI 시인_ :sunglasses:")
title = st.text_input("시의 주제를 입력하세요", "봄비")
st.write("시의 주제는", title)

if st.button("시 작성"):
    with st.spinner("시를 짓는 중..."):
        model = init_chat_model(
            "gpt-4o-mini",
            temperature=0.7,    # 0~1 : 딱딱/정확 ~ 창의/다양
            timeout=30,         # 응답 대기 시간(초)
            max_tokens=1000,    # 답변 길이 제한
            max_retries=6,      # 재시도 횟수
            api_key=api_key,
        )
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'You are a master of poem'),
            ('user', "{input}"),
        ])
        chain = prompt | model | StrOutputParser()
        response = chain.invoke({"input": f"{title}에 대한 시를 작성해줘"})

    st.write(response)
