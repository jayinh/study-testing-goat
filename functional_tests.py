from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 작업 목록 온라인 앱 사이트 접속
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'로 표시됨
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # "책상정리" 라고 텍스트 상자에 입력하기
        inputbox.send_keys('책상정리')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 "1: 책상정리" 아이템이 표시됨
        inputbox.send_keys(Keys.ENTER)

        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: 책상정리')

        # 추가 아이템 입력이 가능한 텍스트 상자가 있음
        # "서랍정리"라고 텍스트 입력
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('서랍정리')
        inputbox.send_keys(Keys.ENTER)

        # 페이지 갱신 후 두개의 아이템을 확인 가능
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: 책상정리')
            self.check_for_row_in_list_table('2: 서랍정리')

        # 사이트는 개인별로 특정 URL을 생성해 준다

        # URL에 대한 설명도 같이 표시

        # 해당 URL에 접속하면 개인의 작업목록을 확인 가능


if __name__ == '__main__':
    unittest.main(warnings='ignore')

