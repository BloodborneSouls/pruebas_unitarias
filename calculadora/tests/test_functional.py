import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class TestCalculadoraFunctional(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        path_to_html = os.path.abspath("calculadora/tests/calculadora.html")
        self.driver.get(f"file://{path_to_html}")

    def tearDown(self):
        self.driver.quit()

    def test_suma(self):
        driver = self.driver
        driver.find_element(By.ID, "valor1").send_keys("5.0")
        driver.find_element(By.ID, "valor2").send_keys("3.0")
        driver.find_element(By.ID, "sumar").click()
        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "8")

    '''def test_valor_invalido(self):
        driver = self.driver
        driver.find_element(By.ID, "valor1").send_keys("a")
        driver.find_element(By.ID, "valor2").send_keys("3.0")
        driver.find_element(By.ID, "sumar").click()
        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "Error: Valor inválido")

        driver.find_element(By.ID, "valor1").clear()
        driver.find_element(By.ID, "valor2").clear()

        driver.find_element(By.ID, "valor1").send_keys("5.0")
        driver.find_element(By.ID, "valor2").send_keys("b")
        driver.find_element(By.ID, "sumar").click()
        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "Error: Valor inválido")'''

    '''def test_division_por_cero(self):
        driver = self.driver
        driver.find_element(By.ID, "valor1").send_keys("5.0")
        driver.find_element(By.ID, "valor2").send_keys("0")
        driver.find_element(By.ID, "dividir").click()
        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "Error: División por cero")'''

if __name__ == "__main__":
    unittest.main()
