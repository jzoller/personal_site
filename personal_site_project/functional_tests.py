from selenium import webdriver
import unittest

class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page_has_correct_content(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Jaosn Zoller', self.browser.title)

        # Next, test basic content

if __name__ == '__main__':
    unittest.main(warnings='ignore')

