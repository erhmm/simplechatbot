import streamlit as st
from openai import OpenAI

client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key="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"
)

st.title("NVIDIA Chatbot (Qwen Model)")
user_input = st.text_input("You:", key="input")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="qwen/qwen3-235b-a22b",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            extra_body={"chat_template_kwargs": {"thinking": True}},
            stream=True
        )

        full_reply = ""
        for chunk in response:
            content = getattr(chunk.choices[0].delta, "content", "")
            full_reply += content
            st.write(full_reply)
