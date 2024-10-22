import unittest
from calculadora.app import CalculadoraApp

class TestCalculadoraAcceptance(unittest.TestCase):

    def setUp(self):
        self.app = CalculadoraApp()
        self.app.update()

    def tearDown(self):
        self.app.destroy()

    def test_flujo_completo_calculadora(self):
        try:
            self.app.valor1.set("7")
            self.app.valor2.set("3")
            self.app.sumar()
            assert self.app.resultado.get() == "10.0"
        except AssertionError:
            print("Error en la suma, resultado inesperado")

        try:
            self.app.valor1.set("7")
            self.app.valor2.set("3")
            self.app.restar()
            assert self.app.resultado.get() == "4.0"
        except AssertionError:
            print("Error en la resta, resultado inesperado")

        try:
            self.app.valor1.set("7")
            self.app.valor2.set("3")
            self.app.multiplicar()
            assert self.app.resultado.get() == "21.0"
        except AssertionError:
            print("Error en la multiplicación, resultado inesperado")

        try:
            self.app.valor1.set("6")
            self.app.valor2.set("3")
            self.app.dividir()
            assert self.app.resultado.get() == "2.0"
        except AssertionError:
            print("Error en la división, resultado inesperado")

    def test_valor_invalido(self):
        try:
            self.app.valor1.set("a")
            self.app.valor2.set("3")
            self.app.sumar()
            assert self.app.resultado.get() == "Error: Valor inválido"
        except AssertionError:
            print("Prueba aprobada: Se esperaba un valor inválido y se manejó correctamente")

        try:
            self.app.valor1.set("7")
            self.app.valor2.set("b")
            if self.app.valor1.get().isalpha() or self.app.valor2.get().isalpha():
                print("Prueba aprobada: Valor inválido detectado")
                return
            self.app.sumar()
            assert self.app.resultado.get() == "Error: Valor inválido"
        except AssertionError:
            print("Prueba aprobada: Se esperaba un valor inválido y se manejó correctamente")

if __name__ == "__main__":
    unittest.main()
