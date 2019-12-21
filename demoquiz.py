#question

class Question:
    def __init__(self,text,choices, answer):
        self.choies = choices
        self.text = text
        self.answer = answer
    def check(self, answer):
        return self.answer == answer



#quiz

class Quiz:
    def __init__(self,question):
        self.question = question
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def display(self):
        question = self.getQuestion()
        print(f"soru: {self.questionIndex+1}: {question.text}")
        for a in question.choies:
            print("-" + a)
        answer = input("cevap: ")
        question.

q = Question('en iyi programlama dili? ', ['c#', 'python','java','javascript'],'python')
q2 = Question('en poüler programlama dili? ', ['c#', 'python','java','javascript'],'python')
q3 = Question('en çok kazandıran programlama dili? ', ['c#', 'python','java','javascript'],'python')
questions = [q,q2,q3]

quiz = Quiz(questions)

