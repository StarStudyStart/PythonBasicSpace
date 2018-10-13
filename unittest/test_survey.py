import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''测试匿名调查类能否准确的输出属性'''
    def setUp(self):
        '''创建一次对象，在后续每个单元测试都可以使用'''
        question = " What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanlish','Chinese']
        
    def test_single_reponse(self):
        '''单个答案测试是否被存储'''
        self.my_survey.store_reponse("English")
        self.assertIn('English',self.my_survey.responses)
        
    def test_three_response(self):
        '''三个答案测试是否存储'''
        for response in self.responses:
            self.my_survey.store_reponse(response)
        
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
        
unittest.main()
        
