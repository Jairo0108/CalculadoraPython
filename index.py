from tkinter import *
from tkinter import ttk
from modulos_de_operacion.division import division as dv
from modulos_de_operacion.multiplicacion import multiplicacion as mp 
from modulos_de_operacion.suma import suma as sum
from modulos_de_operacion.resta import resta as res

# Creamos la intancia que contendra toda la aplicacion de la calculadora:
entorno = Tk()

# Seccion de configuracion:
entorno.title("Calculadora")

display = Entry(entorno)
display.grid(row = 0, columnspan=5, sticky="nsew")

i = 0

valor1 = 0
valor2 = 0
operador = ""

def resultado(a, b, c):
    global valor1
    global operador
    global valor2
    
    valor1 = a
    valor2 = b
    operador = c
    
    if operador == "/":
        dv.division(valor1, valor2)
    elif operador == "*":
        mp.multiplicacion(valor1, valor2)
    elif operador == "+":
        sum.suma(valor1, valor2)
    elif operador == "-":
        res.resta(valor1, valor2)

def asignaciones(n, op):
    global valor1
    global operador
    valor1 = n
    operador = op

def obtenerNumeros(n):
    global i
    display.insert(i, n)
    i+=1

# Botones
Button(entorno, text="1", command=lambda:obtenerNumeros(1)).grid(row=4, column=0, sticky=W+E+S+N)
Button(entorno, text="2", command=lambda:obtenerNumeros(2)).grid(row=4, column=1, sticky=W+E+S+N)
Button(entorno, text="3", command=lambda:obtenerNumeros(3)).grid(row=4, column=2, sticky=W+E+S+N)

Button(entorno, text="4", command=lambda:obtenerNumeros(4)).grid(row=3, column=0, sticky=W+E+S+N)
Button(entorno, text="5", command=lambda:obtenerNumeros(5)).grid(row=3, column=1, sticky=W+E+S+N)
Button(entorno, text="6", command=lambda:obtenerNumeros(6)).grid(row=3, column=2, sticky=W+E+S+N)

Button(entorno, text="7", command=lambda:obtenerNumeros(7)).grid(row=2, column=0, sticky=W+E+S+N)
Button(entorno, text="8", command=lambda:obtenerNumeros(8)).grid(row=2, column=1, sticky=W+E+S+N)
Button(entorno, text="9", command=lambda:obtenerNumeros(9)).grid(row=2, column=2, sticky=W+E+S+N)

Button(entorno, text="0", command=lambda:obtenerNumeros(0)).grid(row=5, column=0, sticky=W+E+S+N)
Button(entorno, text="00", command=lambda:obtenerNumeros("00")).grid(row=5, column=1, sticky=W+E+S+N)
Button(entorno, text=".", command=lambda:obtenerNumeros(".")).grid(row=5, column=2, sticky=W+E+S+N)

Button(entorno, text="ON").grid(row=1, column=0, sticky=W+E+S+N)
Button(entorno, text="M+").grid(row=1, column=1, sticky=W+E+S+N)
Button(entorno, text="MC").grid(row=1, column=2, sticky=W+E+S+N)
Button(entorno, text="MR").grid(row=1, column=3, sticky=W+E+S+N)
Button(entorno, text="OFF").grid(row=1, column=4, sticky=W+E+S+N)

Button(entorno, text="%").grid(row=2, column=3, sticky=W+E+S+N)
Button(entorno, text="CE").grid(row=2, column=4, sticky=W+E+S+N)
Button(entorno, text="X").grid(row=3, column=3, sticky=W+E+S+N)
Button(entorno, text="/", command=lambda:asignaciones(float(display.get()), "/")).grid(row=3, column=4, sticky=W+E+S+N)
Button(entorno, text="+").grid(row=4, rowspan= 5, column=3, sticky="nsew")
Button(entorno, text="-").grid(row=4, column=4, sticky=W+E+S+N)
Button(entorno, text="=", command=lambda:resultado(valor1, valor2, operador)).grid(row=5, column=4, sticky=W+E+S+N)



# Mantiene la aplicacion en un loop infinito, para que se mantenga corriendo.
entorno.mainloop()
