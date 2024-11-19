from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title("Comprar entradas")

root.iconbitmap("img.ico")

def mostrar():
    respuesta = askquestion(title="Comprar entrada?",
    message="Quieres comprar?")
    
    if respuesta == "yes":
        venta_producto = showinfo(title="Comprado!!", message="Bien hecho")
        if venta_producto:
            viaje_extranjero = askquestion(title="Venta productos", message="Quieres comprar otro producto?")
            if viaje_extranjero == "yes":
                alta_banco = askokcancel(title="Seguro", message="Pero seguro que lo quieres")
                if alta_banco:
                    try_cancelar = showerror(title="Confirmación", message="Estas apunto de comprarlo")
                    if try_cancelar:
                        confirmado = askyesnocancel(title="Otra confirmación", message="Pero seguro?")
                        if confirmado is True:
                            showinfo(title="Vuelo comprado", message="Esta hecho")
                        if confirmado is False:
                            showerror(title="Vuelo cancelado", message="Cancelado")
            else:
                showerror(title="En verdad no", message="No lo quieres")            
    else:
        showerror(title="Vaya..", message="Te quedastes sin ella")                    
boton = Button(root, text="Iniciar", command=mostrar, width=75).pack()

root.mainloop()

# mostrar distintas ventanas
# al cancelar volver al principio