import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class asistencia(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.mis_vent = self.driver.window_handles[0]


    def test_navegador(self):
        navegador = self.driver
        navegador.get("https://www.ucundinamarca.edu.co/")
        navegador.execute_script("window.open('');")

        time.sleep(20)
        buplataforma = navegador.find_element_by_xpath("//*[@id='sppb-addon-1565022666579']/div/div/div/a[3]")
        time.sleep(5)
        buplataforma.click()

        time.sleep(5)
        usuario = navegador.find_element_by_id("usuario")
        usuario.send_Keys("jezamora")
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
