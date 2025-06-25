import tkinter as tk
from math import sin, cos, tan, log, radians

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simple")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.entrada = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="groove", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15, pady=10, padx=10, sticky="we")

        self.crear_botones()

    def agregar(self, valor):
        self.entrada.insert(tk.END, str(valor))

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.limpiar()
            self.agregar(resultado)
        except:
            self.limpiar()
            self.agregar("Error")

    def funcion_cientifica(self, func):
        try:
            valor = float(self.entrada.get())
            resultado = {
                'sin': sin(radians(valor)),
                'cos': cos(radians(valor)),
                'tan': tan(radians(valor)),
                'log': log(valor)
            }[func]
            self.limpiar()
            self.agregar(round(resultado, 6))
        except:
            self.limpiar()
            self.agregar("Error")

    def crear_botones(self):
        # Sección básica
        botones_basicos = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (texto, fila, columna) in botones_basicos:
            comando = self.limpiar if texto == 'C' else (
                self.calcular if texto == '=' else lambda t=texto: self.agregar(t)
            )
            tk.Button(self.root, text=texto, width=5, height=2, font=("Arial", 16),
                      command=comando, bg="#ffffff", fg="#000000").grid(row=fila, column=columna, padx=5, pady=5)

        # Sección científica
        funciones = [('sin', 1), ('cos', 2), ('tan', 3), ('log', 4)]
        for (nombre, fila) in funciones:
            tk.Button(self.root, text=nombre, width=5, height=2, font=("Arial", 16),
                      command=lambda f=nombre: self.funcion_cientifica(f),
                      bg="#d0e0f0", fg="#000000").grid(row=fila, column=4, padx=5, pady=5)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()