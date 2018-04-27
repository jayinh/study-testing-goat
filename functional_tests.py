from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 작업 목록 온라인 앱 사이트 접속
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'로 표시됨 
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # 작업 추가
        
        # "책상정리" 라고 텍스트 상자에 입력하기
        
        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 "1: 책상정리" 아이템이 표시됨
        
        # 추가 아이템 입력이 가능한 텍스트 상자가 있음
        
        # "서랍정리"라고 텍스트 입력
        
        # 페이지 갱신 후 두개의 아이템을 확인 가능
        
        # 사이트는 개인별로 특정 URL을 생성해 준다
        
        # URL에 대한 설명도 같이 표시
        
        # 해당 URL에 접속하면 개인의 작업목록을 확인 가능
       

if __name__ == '__main__':
    unittest.main(warnings='ignore')
