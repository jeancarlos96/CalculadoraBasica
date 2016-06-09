# -*- coding: utf-8 -*-
from tkinter import *
import TkMessageBox

def sumar():
	n1=float(txtn1.get())
	en2=float(txtn2.get())
	suma=n1+n2
	lblresp=Label(text=suma).place(x=180, y=45)	

def restar():
	n1=float(txtn1.get())
	n2=float(txtn2.get())
	rest=n1-n2
	lblresp=Label(text=resta).place(x=180, y=45)	

def multi():
	n1=float(txtn1.get())
	n2=float(txtn2.get())
	mult=n1*n2
	lblresp=Label(text=multi).place(x=180, y=45)	

def div():
	n1=float(txtn1.get())
	n2=float(txtn2.get())
	divi=n1/n2
	lblresp=Label(text=div).place(x=180, y=45)	

ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("CALCULADORA")

lblN1=Label(text="Ingrese un n1: ", font=("Times New Roman",12)).place(x=10,y=30)
lblN2=Label(text="Ingrese un n2: ", font=("Times New Roman",12)).place(x=10,y=60)
#lblrep=Label(text="la suma es: ",tot).place(x=200, y=45)


entrada=StringVar()
txtn1=Entry(ventana, textvariable=entrada).place(x=150, y=35)
#n1=parseFloat(txtN1.get())
entrada2=StringVar()
txtn2=Entry(ventana, textvariable=entrada2).place(x=150, y=70)
#n2=parseFloat(txtN2.get())
#BOTONES
btnSuma=Button(ventana, text="sumar", command=sumar).place(x=100, y=100)
btnResta=Button(ventana, text="restar", command=restar).place(x=150, y=100)
btnMulti=Button(ventana, text="multiplicar", command=multi).place(x=200, y=100)
btnDiv=Button(ventana, text="dividir", command=div).place(x=280, y=100)
ventana.mainloop()