import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import ImageTk, Image
from otro_modulo_ventas import mostrar_ventana_ventas
from coneccion_bueno import mostrar_ventana_productos
from modulo_info_nutricional import mostrar_ventana_infonutricional
from modulo_proveedores import mostrar_ventana_proveedores
from modulo_control import mostrar_ventana_estado_produccion
from graficas import mostrar_ventana_graficas
from grafica_ventas import mostrar_ventana_grafica_ventas
from grafica_info import mostrar_ventana_grafica_infonutri
from grafica_control import mostrar_ventana_control 

def validar_login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    contrasena_usuario = contrasena_entry.get()



   
    usuarios_validos = ["empleado1", "empleado2", "empleado3", "usuario"]
    if usuario in usuarios_validos and contrasena == "123456":
        abrir_ventana_acceso_permitido()

    if usuario in usuarios_validos and contrasena_usuario =="usuario":
        abrir_ventana_usuario()
    else:
        acceso_denegado_label.config(text="Acceso denegado", fg="red")
        acceso_denegado_label.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)


def abrir_ventana_usuario():

     ventana.withdraw()
     
     ventana_usuario = tk.Toplevel(ventana)
     ventana_usuario.title("Acceso Permitido")

     ventana_usuario.geometry("1300x200")

    
    
     fondo_label = tk.Label(ventana_usuario, bg="#0D9C13")
     fondo_label.place(relwidth=1, relheight=1)

    
     opciones_frame = tk.Frame(ventana_usuario, bg="#0D9C13")
     opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

     graficas_button = tk.Button(opciones_frame, text="Grafica Productos", command=abrir_ventana_graficas, bg="#384E77", fg="white", font=("Helvetica", 12))
     graficas_button.pack(side="left", padx=10)
     graficas_button = tk.Button(opciones_frame, text="Grafica Ventas", command=abrir_ventana_grafica_ventas, bg="#384E77", fg="white", font=("Helvetica", 12))
     graficas_button.pack(side="left", padx=10)
     graficas_button = tk.Button(opciones_frame, text="Grafica info nutricional", command=abrir_ventana_grafica_infonutri, bg="#384E77", fg="white", font=("Helvetica", 12))
     graficas_button.pack(side="left", padx=10)
     graficas_button = tk.Button(opciones_frame, text="grafica de control produccion", command=abrir_ventana_control, bg="#384E77", fg="white", font=("Helvetica", 12))
     graficas_button.pack(side="left", padx=10)

def abrir_ventana_acceso_permitido():
    
    ventana.withdraw()

   
    

    ventana_acceso_permitido = tk.Toplevel(ventana)
    ventana_acceso_permitido.title("Acceso Permitido")

    ventana_acceso_permitido.geometry("1300x200")

    
   
    fondo_label = tk.Label(ventana_acceso_permitido, bg="#384E77")
    fondo_label.place(relwidth=1, relheight=1)

    
    opciones_frame = tk.Frame(ventana_acceso_permitido, bg="#384E77")
    opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    
    productos_button = tk.Button(opciones_frame, text="Productos", command=mostrar_ventana_productos, bg="#384E77", fg="white", font=("Helvetica", 12))
    productos_button.pack(side="left", padx=10)
    ventas_button = tk.Button(opciones_frame, text="Ventas", command=mostrar_ventana_ventas, bg="#384E77", fg="white", font=("Helvetica", 12))
    ventas_button.pack(side="left", padx=10)
    informacion_button = tk.Button(opciones_frame, text="Información Nutricional", command=mostrar_ventana_infonutricional, bg="#384E77", fg="white", font=("Helvetica", 12))
    informacion_button.pack(side="left", padx=10)
    proveedores_button = tk.Button(opciones_frame, text="Proveedores", command=mostrar_ventana_proveedores, bg="#384E77", fg="white", font=("Helvetica", 12))
    proveedores_button.pack(side="left", padx=10)
    estado_produccion_button = tk.Button(opciones_frame, text="control de producción", command=mostrar_ventana_estado_produccion, bg="#384E77", fg="white", font=("Helvetica", 12))
    estado_produccion_button.pack(side="left", padx=10)

    graficas_button = tk.Button(opciones_frame, text="Grafica Productos", command=abrir_ventana_graficas, bg="#384E77", fg="white", font=("Helvetica", 12))
    graficas_button.pack(side="left", padx=10)
    graficas_button = tk.Button(opciones_frame, text="Grafica Ventas", command=abrir_ventana_grafica_ventas, bg="#384E77", fg="white", font=("Helvetica", 12))
    graficas_button.pack(side="left", padx=10)
    graficas_button = tk.Button(opciones_frame, text="Grafica info nutricional", command=abrir_ventana_grafica_infonutri, bg="#384E77", fg="white", font=("Helvetica", 12))
    graficas_button.pack(side="left", padx=10)
    graficas_button = tk.Button(opciones_frame, text="grafica de control produccion", command=abrir_ventana_control, bg="#384E77", fg="white", font=("Helvetica", 12))
    graficas_button.pack(side="left", padx=10)

def abrir_ventana_productos():
    mostrar_ventana_productos()

def abrir_ventana_ventas():
    mostrar_ventana_ventas()

def abrir_ventana_infonutricional():
    mostrar_ventana_infonutricional()

def abrir_ventana_proveedores():
    mostrar_ventana_proveedores()

def abrir_ventana_estado_produccion():
    mostrar_ventana_estado_produccion()

def abrir_ventana_graficas():
    mostrar_ventana_graficas()   

def abrir_ventana_grafica_ventas():
    mostrar_ventana_grafica_ventas()   

def abrir_ventana_grafica_infonutri():
    mostrar_ventana_grafica_infonutri() 

def abrir_ventana_control():
    mostrar_ventana_control()

def mostrar_mensaje(mensaje):
    messagebox.showinfo("Mensaje", mensaje)


ventana = tk.Tk()
ventana.title("Inicio de Sesión Empresarial")
imagen = Image.open("logo.png")
nuevo_ancho = 250
nuevo_alto = 250
imagen=imagen.resize((nuevo_ancho, nuevo_alto))
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta=tk.Label(ventana,image=imagen_tk)        
etiqueta.pack()
etiqueta.config(image=imagen_tk)
etiqueta.place(x=20, y=20)
ventana.geometry("750x600")
ventana.configure(bg="#384E77")


usuario_label = tk.Label(ventana, text="Usuario:", bg="#384E77", fg="white", font=("Helvetica", 16))
usuario_label.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
usuario_entry = tk.Entry(ventana)
usuario_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)

contrasena_label = tk.Label(ventana, text="Contraseña:", bg="#384E77", fg="white", font=("Helvetica", 16))
contrasena_label.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.05)
contrasena_entry = tk.Entry(ventana, show="*")
contrasena_entry.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05)


login_button = tk.Button(ventana, text="Iniciar Sesión", command=validar_login, bg="#007F00", fg="white", font=("Helvetica", 16))
login_button.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.05)


acceso_denegado_label = tk.Label(ventana, text="", fg="red", font=("Helvetica", 16))


ventana.mainloop()