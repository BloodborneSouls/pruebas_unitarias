import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TestCalculadoraFunctional(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        path_to_html = os.path.abspath("calculadora/tests/calculadora.html")
        print(f"Cargando archivo HTML desde: file://{path_to_html}")
        self.driver.get(f"file://{path_to_html}")
        self.driver.maximize_window() 

    def tearDown(self):
        self.driver.quit()

    def test_suma(self):
        driver = self.driver
        valor1_input = driver.find_element(By.ID, "valor1")
        valor2_input = driver.find_element(By.ID, "valor2")

        valor1_input.send_keys("5")
        valor2_input.send_keys("3")
        driver.find_element(By.ID, "sumar").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "resultado"), "8")
        )

        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "8")

    '''def test_valor_invalido(self):
        driver = self.driver
        valor1_input = driver.find_element(By.ID, "valor1")
        valor2_input = driver.find_element(By.ID, "valor2")


        valor1_input.send_keys("a")
        valor2_input.send_keys("3")
        driver.find_element(By.ID, "sumar").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "resultado"), "Error: Valor inválido")
        )

        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "Error: Valor inválido")'''

    '''def test_division_por_cero(self):
        driver = self.driver
        valor1_input = driver.find_element(By.ID, "valor1")
        valor2_input = driver.find_element(By.ID, "valor2")

        valor1_input.send_keys("5")
        valor2_input.send_keys("0")
        driver.find_element(By.ID, "dividir").click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "resultado"), "Error: División por cero")
        )

        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "Error: División por cero")'''

    def test_limpiar_campos(self):
     
        driver = self.driver
        valor1_input = driver.find_element(By.ID, "valor1")
        valor2_input = driver.find_element(By.ID, "valor2")

       
        valor1_input.send_keys("5")
        valor2_input.send_keys("3")
        driver.find_element(By.ID, "sumar").click()

      
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "resultado"), "8")
        )

        
        resultado = driver.find_element(By.ID, "resultado").text
        self.assertEqual(resultado, "8")

       
        valor1_input.clear()
        valor2_input.clear()

    
        self.assertEqual(valor1_input.get_attribute("value"), "")
        self.assertEqual(valor2_input.get_attribute("value"), "")

if __name__ == "__main__":
    unittest.main()
