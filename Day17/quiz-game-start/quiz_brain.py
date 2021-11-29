
class QuizBrain:
    def __init__(self, list_of_questions):
        self.question_no = -1
        self.question_list = list_of_questions

    def next_question(self):
        self.question_no += 1
        return self.question_list[self.question_no].text

    def give_answer(self):
        return self.question_list[self.question_no].answer

    def still_has_quesstions(self):
        total_questions = len(self.question_list)

        if self.question_no == total_questions - 1:
            print("------End of Game------")
            return False
        else:
            return True

    def give_total_question_count(self):
        return len(self.question_list)
