from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # print(question_text)
    # print(question_answer)
    question_bank.append(Question(question_text, question_answer))

# print(question_bank[0].text)

sample_play = QuizBrain(question_bank)
score = 0

while sample_play.still_has_quesstions():
    print(f"Q.{sample_play.question_no + 2} {sample_play.next_question()} (True/False)")
    user_answer = input("Your answer? ")
    if user_answer.lower() == sample_play.give_answer().lower():
        score += 1
        print(f"That's correct. Your score is {score}")
    else:
        print(f"That's wrong one. Your score is {score}")
        print(f"Correct answer for this question is {sample_play.give_answer()}")
    print("\n")

print(f"Your final score is: {score} out of {sample_play.give_total_question_count()}")




