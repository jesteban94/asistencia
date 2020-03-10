import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class asistencia(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navegador(self):
        navegador = self.driver
        navegador.get("https://www.ucundinamarca.edu.co/")
        time.sleep(20)
        buplataforma = navegador.find_element_by_xpath("//*[@id='sp-header']/div/div/div/div[2]/div[2]/a")
        buplataforma.click()
        time.sleep(3)







if __name__ == "__main__":
    unittest.main()