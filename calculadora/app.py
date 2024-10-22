import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x500")
        self.configure(bg="lightblue")
        
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.resultado = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        style = ttk.Style()
        style.configure("TLabel", padding=6, relief="flat", background="lightblue")
        style.configure("TButton", padding=6, relief="raised", background="white")

        ttk.Label(self, text="Valor 1:").pack(pady=10)
        ttk.Entry(self, textvariable=self.valor1).pack(pady=10)

        ttk.Label(self, text="Valor 2:").pack(pady=10)
        ttk.Entry(self, textvariable=self.valor2).pack(pady=10)

        ttk.Button(self, text="Sumar", command=self.sumar).pack(pady=10)
        ttk.Button(self, text="Restar", command=self.restar).pack(pady=10)
        ttk.Button(self, text="Multiplicar", command=self.multiplicar).pack(pady=10)
        ttk.Button(self, text="Dividir", command=self.dividir).pack(pady=10)

        ttk.Label(self, text="Resultado:").pack(pady=10)
        ttk.Label(self, textvariable=self.resultado, width=20, relief="solid", background="white").pack(pady=10)

    def sumar(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get())
            self.resultado.set(num1 + num2)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def restar(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get())
            self.resultado.set(num1 - num2)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get())
            self.resultado.set(num1 * num2)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def dividir(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get())
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                self.resultado.set("")  # Limpiar el resultado en caso de error
            else:
                self.resultado.set(num1 / num2)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")
