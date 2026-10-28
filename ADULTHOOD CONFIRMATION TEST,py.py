print("ADULTHOOD CONFIRMATION TEST 101")

questions = [
    "Does your money finish before month end?", 
    "Are you tired even after resting?" ,
    "Do you hate decideing what to eat?",
    "Does your laundry multiply overnight?",
    "Has anyone ever told you 'Please I need urgent 2k'?" ,
    "Have you ever wondered if adulthood is a scam?" ,
    "Have you ever said 'it is well' when you dont know what to say? ",
    "Have you ever shouted 'Jesus' multiple times a day?" ,
    "Have you ever said 'God abeg, omo, na wao' multiple times a day?"
] 

score = 0

for question in questions:
    answer = input(question + "(yes/no): ")
    if answer.strip().lower() == "yes":
        score += 1

print(f"\nAdulting symptoms: {score}/{len(questions)}")

if score >= 7:
    print("VERDICT: YOU ARE IN TOO DEEP")
elif score >= 4:
    print("VERDICT: ADULTHOOD IS ADULTING")
else:
    print("VERDICT: ADULTHOOD IS STILL LOADING")


