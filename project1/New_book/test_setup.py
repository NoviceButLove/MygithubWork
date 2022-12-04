class AnonymousSurvey():
     #学习

    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('Survey results:')
        for ii in self.responses:
            print('  _'+ii+'_  ')