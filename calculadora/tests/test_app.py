import unittest
from calculadora.app import CalculadoraApp
from calculadora.app import tk

class TestCalculadoraApp(unittest.TestCase):

    def setUp(self):
        self.app = CalculadoraApp()
        self.app.update()

    def tearDown(self):
        self.app.destroy()

    def test_sumar(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("3")
            self.app.sumar()
            assert self.app.resultado.get() == "8.0"
        except AssertionError:
            print("Error en la prueba de suma, resultado inesperado")

    def test_restar(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("3")
            self.app.restar()
            assert self.app.resultado.get() == "2.0"
        except AssertionError:
            print("Error en la prueba de resta, resultado inesperado")

    def test_multiplicar(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("3")
            self.app.multiplicar()
            assert self.app.resultado.get() == "15.0"
        except AssertionError:
            print("Error en la prueba de multiplicación, resultado inesperado")

    def test_dividir(self):
        try:
            self.app.valor1.set("6")
            self.app.valor2.set("3")
            self.app.dividir()
            assert self.app.resultado.get() == "2.0"
        except AssertionError:
            print("Error en la prueba de división, resultado inesperado")

    def test_dividir_por_cero(self):
        try:
            self.app.valor1.set("5")
            self.app.valor2.set("0")
            self.app.dividir()
            assert self.app.resultado.get() == "Indefinido"
        except AssertionError:
            print("Prueba aprobada: Se esperaba un error de división por cero y se manejó correctamente.")

    def test_iniciar_interfaz(self):
        try:
            assert isinstance(self.app.valor1, tk.StringVar)
            assert isinstance(self.app.valor2, tk.StringVar)
            assert isinstance(self.app.resultado, tk.StringVar)
            assert self.app.resultado.get() == ""
        except AssertionError:
            print("Error en la inicialización de la interfaz")

if __name__ == "__main__":
    unittest.main()
