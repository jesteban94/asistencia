import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class asistencia(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navegador(self):
        navegador = self.driver
        navegador.get("https://www.ucundinamarca.edu.co/")
        main_page = navegador.current_window_handle
        pag=navegador.title
        time.sleep(10)

        print(pag)


        buplataforma = navegador.find_element_by_xpath("//*[@id='sppb-addon-1565022666579']/div/div/div/a[3]")
        time.sleep(3)

        buplataforma.click()
        time.sleep(5)

        print(main_page)

        for handle in navegador.window_handles:
            if handle != main_page:
                login_page = handle

        pagi = navegador.title
        time.sleep(2)

        print(pagi)

        navegador.switch_to.window(login_page)
        venta= navegador.window_handles
        pagina= navegador.title
        time.sleep(5)

        print(venta)
        print(pagina)

        usuario = navegador.find_element_by_xpath("//*[@id='usuario']")
        usuario.send_Keys("jezamora")
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
