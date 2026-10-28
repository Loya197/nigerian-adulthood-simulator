import streamlit as st

st.set_page_config(
page_title="Adulthood Confirmation Test 101",
page_icon="🇳🇬"
)

st.title("🇳🇬 ADULTHOOD CONFIRMATION TEST 101")
st.write("Let's investigate your symptoms of adulthood. 😂")

questions = [
"Does your money finish before month end?",
"Are you tired even after resting?",
"Do you hate deciding what to eat?",
"Does your laundry multiply overnight?",
"Has anyone ever told you 'Please I need urgent 2k'?",
"Have you ever wondered if adulthood is a scam?",
"Have you ever said 'it is well' when you don't know what to say?",
"Have you ever shouted 'Jesus' multiple times a day?",
"Have you ever said 'God abeg, omo, na wao' multiple times a day?"
]

with st.form("adulthood_test"):
answers = []

for question in questions:
answer = st.radio(
question,
["No", "Yes"],
horizontal=True
)
answers.append(answer)

submitted = st.form_submit_button("Reveal my symptoms 😂")

if submitted:
score = answers.count("Yes")

st.subheader(
f"Adulting symptoms: {score}/{len(questions)}"
)

if score >= 7:
st.error("VERDICT: YOU ARE IN TOO DEEP")
elif score >= 4:
st.warning("VERDICT: ADULTHOOD IS ADULTING")
else:
st.success("VERDICT: ADULTHOOD IS STILL LOADING")
