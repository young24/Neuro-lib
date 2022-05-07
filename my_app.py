
import streamlit as st

import os
import openai

openai.organization = "org-wObRLA0OtN6V7bGAUPAHbjjG"
openai.api_key = "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"#st.secrets["OPENAI_API_KEY"]

response = openai.File.create(
  file=open("output.jsonl"),
  purpose='answers'
)

if st.text_input("Your question", key="question"):
  
  response = openai.Answer.create(
    search_model="ada",
    model="curie",
    question=st.session_state.question,
    file=response.id,
    examples_context="In 2017, U.S. life expectancy was 78.6 years.",
    examples=[["What is human life expectancy in the United States?","78 years."]],
    max_tokens=16,
    stop=["\n","<|endoftext|>"],
  )
  
  st.write(response)

