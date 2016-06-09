import sys 
from tkinter import *

def suma():
	try:
	 _valor=int (entrada_texto.get())
	 _valor2=int (entrada_texto2.get())
	 _valor=(_valor + _valor2)
	 etiqueta.config(text=_valor)
	 etiqueta2.config(text=_valor)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	except ValueError:
	 etiqueta2.config(text="INGRESE UN NUMERO: ")

def resta():
	try:
	 _valor=int (entrada_texto.get())
	 _valor2=int (entrada_texto2.get())
	 _valor=(_valor - _valor2)
	 etiqueta.config(text=_valor)
	 etiqueta2.config(text=_valor2)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	except ValueError:
	 etiqueta2.config(text="INGRESE UN NUMERO: ")

def multi():
	try:
	 _valor=int (entrada_texto.get())
	 _valor2=int (entrada_texto2.get())
	 _valor=(_valor * _valor2)
	 etiqueta.config(text=_valor)
	 etiqueta2.config(text=_valor2)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	except ValueError:
	 etiqueta2.config(text="INGRESE UN NUMERO: ")

def div():
	try:
	 _valor=int (entrada_texto.get())
	 _valor2=int (entrada_texto2.get())
	 _valor=(_valor / _valor2)
	 etiqueta.config(text=_valor)
	 etiqueta2.config(text=_valor2)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	except ValueError:
	 etiqueta2.config(text="INGRESE UN NUMERO: ")

def modulo():
	try:
	 _valor=int (entrada_texto.get())
	 _valor2=int (entrada_texto2.get())
	 _valor=(_valor % _valor2)
	 etiqueta.config(text=_valor)
	 etiqueta2.config(text=_valor2)
	except ValueError:
	 etiqueta.config(text="INGRESE UN NUMERO: ")
	except ValueError:
	 etiqueta2.config(text="INGRESE UN NUMERO: ")

app=Tk()
app.title("CALCULADORA SIMPLE")

 #VENTANA PRINCIPAL 
vp=Frame(app)
vp.grid(column=0, row=0, padx=(80,80), pady=(10,10))
vp.columnconfigure(0, weight=1)

etiqueta=Label(vp, text="valor")
etiqueta.grid(column=3, row=6, sticky=(W,E))

boton=Button(vp, text="SUMA", command=suma)
boton.grid(column=1, row=1)
boton2=Button(vp, text="RESTA", command=resta)
boton2.grid(column=1, row=2)
boton3=Button(vp, text="MULTIPLICACION", command=multi)
boton3.grid(column=1, row=3)
boton4=Button(vp, text="DIVISION", command=div)
boton4.grid(column=1, row=4)
boton5=Button(vp, text="MODULO", command=modulo)
boton5.grid(column=1, row=5)

valor= ""
entrada_texto=Entry(vp, width=20, textvariable=valor)
entrada_texto.grid(column=4, row=2)
valor2= ""
entrada_texto2=Entry(vp, width=20, textvariable=valor2)
entrada_texto2.grid(column=4, row=3)

app.mainloop()