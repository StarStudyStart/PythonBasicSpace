class AnonymousSurvey():
    '''手机匿调查问卷'''
    def __init__(self,question):
        '''存储一个问题，并为存储答案做准备'''
        self.question = question
        self.responses = []
        
    def show_questions():
        '''显示调查问题'''
        print(self.question)
        
    def store_reponse(self,reponse):
        '''存储单份调查问卷'''
        self.responses.append(reponse)
        
    def show_survey():
        '''显示调查结果'''
        print('Survey Results!')
        for reponse in reponses:
            print(' - '+reponse)
