from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\\firefox.exe')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        inputbox.send_keys('공작깃털 사기')

        inputbox.send_keys(Keys.ENTER)

        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), '공작깃털 사기'
            )
        )

        self.check_for_row_in_list_table('1: 공작깃털 사기')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: 공작깃털 사기', [row.text for row in rows])

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        self.cehck_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.cehck_for_row_in_list_table('1: 공작깃털 사기')

        self.fail('Finish the Test')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')