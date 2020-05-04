from selenium import webdriver
import time
import unittest

class AppTest(unittest.TestCase):

    def setUp(self):
        # acrescentamos a fixture do nosso teste. No unittest 
        # é setUp. A inicialização dos estados.
        # é equivalente aos métodos anotados como @before no jUnit
        self.driver = webdriver.Firefox()
        self.driver.get("http://google.com")

    def tearDown(self):
        # acrescentamos a finalização. No unittest é via tearDown.
        # é equivalente aos métodos anotados como @after no jUnit
        self.driver.quit()


    def test_can_query_on_google(self):
        # em python o método de teste deve começar com a palavra 'test'        
        element = self.driver.find_element_by_name("q")
        element.send_keys("reinforcement learning")
        element.submit()
        time.sleep(3)

        # uso do assertIn
        # verificando se o título da página retornada contém a palavra 'software'
        self.assertIn("reinforcement learning", self.driver.title)
        # more tests...
        

    def test_another_feature(self):
        # Em python o método de teste deve começar com a palavra 'test'
        element = self.driver.find_element_by_name("q")
        element.send_keys("machine learning")
        element.submit()
        time.sleep(3)

        # uso do assertIn
        # verificando se o título da página retornada contém a palavra 'software'
        self.assertIn("machine learning", self.driver.title)
        # more tests...
        

if __name__ == "__main__":
    unittest.main()