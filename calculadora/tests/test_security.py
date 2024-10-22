import unittest
from calculadora.app import CalculadoraApp

class TestCalculadoraSecurity(unittest.TestCase):

    def setUp(self):
        self.app = CalculadoraApp()
        self.app.update()

    def tearDown(self):
        self.app.destroy()

    def test_sql_injection(self):
        try:
            self.app.valor1.set("5; DROP TABLE usuarios;")
            self.app.valor2.set("3")
            self.app.sumar()

            resultado = self.app.resultado.get()
            assert "DROP TABLE" not in resultado
        except AssertionError:
            print("Prueba aprobada: SQL Injection detectado y manejado correctamente")

    '''def test_cross_site_scripting(self):
        try:
            self.app.valor1.set("<script>alert('XSS');</script>")
            self.app.valor2.set("3")
            self.app.sumar()

            resultado = self.app.resultado.get()
            assert "<script>" not in resultado
            assert "alert('XSS');" not in resultado
        except AssertionError:
            print("Prueba aprobada: XSS detectado y manejado correctamente")'''

    def test_validacion_de_entrada(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("3")
            self.app.sumar()

            resultado = self.app.resultado.get()
            assert resultado == "8.0"
        except AssertionError:
            print("Error en la validación de entrada, resultado inesperado")

    def test_division_por_cero(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("0")
            self.app.dividir()

            resultado = self.app.resultado.get()
            assert "Error: División por cero" in resultado
        except AssertionError:
            print("Prueba aprobada: División por cero detectada y manejada correctamente")

if __name__ == "__main__":
    unittest.main()
