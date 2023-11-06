import tkinter as tk
from tkinter import Tk, Label
from PIL import ImageTk, Image
import mysql.connector

producto_entry = None
tamaño_de_porción_entry = None
carbohidratos_entry = None
vencimiento_entry = None
busqueda_entry = None

def eliminar_producto():
    # Acceder a las variables globales
    producto = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "DELETE FROM información_nutricional WHERE producto = %s"
    values = (producto,)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de eliminar los datos
    producto_entry.delete(0, tk.END)
    tamaño_de_porción_entry.delete(0, tk.END)
    carbohidratos_entry.delete(0, tk.END)
    vencimiento_entry.delete(0, tk.END)
    busqueda_entry.delete(0, tk.END)

    tk.messagebox.showinfo("Éxito", "Producto eliminado")

def buscar_producto():
    # Acceder a las variables globales
    global producto_entry, tamaño_de_porción_entry, carbohidratos_entry, vencimiento_entry, busqueda_entry

    producto = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "SELECT * FROM información_nutricional WHERE producto = %s"
    values = (producto,)

    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar los cuadros de entrada con los datos encontrados
        producto_entry.delete(0, tk.END)
        tamaño_de_porción_entry.delete(0, tk.END)
        carbohidratos_entry.delete(0, tk.END)
        vencimiento_entry.delete(0, tk.END)

        producto_entry.insert(0, str(resultado[0]))
        tamaño_de_porción_entry.insert(0, resultado[1])
        carbohidratos_entry.insert(0, resultado[2])
        vencimiento_entry.insert(0, str(resultado[3]))
    else:
        # Mostrar un mensaje de que el producto no se encontró
        tk.messagebox.showerror("Error", "Producto no encontrado")

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()



def mostrar_ventana_infonutricional():
    # Crea una nueva ventana para Ventas
    ventana_infonutricional = tk.Toplevel()
    ventana_infonutricional.title("Informacion nutricional")
    imagen = Image.open("logo.png")
    nuevo_ancho = 250
    nuevo_alto = 250
    imagen=imagen.resize((nuevo_ancho, nuevo_alto))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta=tk.Label(ventana_infonutricional,image=imagen_tk)        
    etiqueta.pack()
    etiqueta.config(image=imagen_tk)
    etiqueta.place(x=20, y=20)
    ventana_infonutricional.geometry("800x600")
    ventana_infonutricional.configure(bg="#8539A4")

    global producto_entry, tamaño_de_porción_entry, carbohidratos_entry, vencimiento_entry, busqueda_entry
    
    # Etiquetas de ingreso de información
    tk.Label(ventana_infonutricional, text="Ingrese producto:").place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.05)
    producto_entry = tk.Entry(ventana_infonutricional)
    producto_entry.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_infonutricional, text="Ingrese el tamaño de porción:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
    tamaño_de_porción_entry = tk.Entry(ventana_infonutricional)
    tamaño_de_porción_entry.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_infonutricional, text="Ingrese los carbohidratos:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
    carbohidratos_entry = tk.Entry(ventana_infonutricional)
    carbohidratos_entry.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_infonutricional, text="Ingrese Vencimiento:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
    vencimiento_entry = tk.Entry(ventana_infonutricional)
    vencimiento_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)


    guardar_button = tk.Button(ventana_infonutricional, text="Guardar información", command=guardar_informacion, bg="#007F00", fg="white", font=("Helvetica", 13))
    guardar_button.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.05)


    busqueda_label = tk.Label(ventana_infonutricional, text="Buscar Producto:", bg="#384E77", fg="white",
                              font=("Helvetica", 12))
    busqueda_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.05)
    busqueda_entry = tk.Entry(ventana_infonutricional)
    busqueda_entry.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

    # Botón para buscar producto
    buscar_button = tk.Button(ventana_infonutricional, text="Buscar Producto", command=buscar_producto, bg="#FFA500", fg="white",
                             font=("Helvetica", 16))
    buscar_button.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)

    # Botón para eliminar producto
    eliminar_button = tk.Button(ventana_infonutricional, text="Eliminar Producto", command=eliminar_producto, bg="#FF0000",
                                fg="white", font=("Helvetica", 16))
    eliminar_button.place(relx=0.4, rely=.8, relwidth=0.4, relheight=0.05)

    def cerrar_ventana():
     ventana_infonutricional.destroy()

    cerrar_button = tk.Button(ventana_infonutricional, text="volver al menú", command=cerrar_ventana, bg="#FF0000", fg="white", font=("Helvetica", 13))
    cerrar_button.place(relx=0.4, rely=0.9, relwidth=0.4, relheight=0.05)



    ventana_infonutricional.mainloop()

def guardar_informacion():
    producto =producto_entry.get()
    tamaño_de_porción = tamaño_de_porción_entry.get()
    carbohidratos = carbohidratos_entry.get()
    vencimiento = vencimiento_entry.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()
    
    query = "INSERT INTO información_nutricional (producto, `tamaño de porción`, carbohidratos, vencimiento) VALUES (%s, %s, %s, %s)"
    values = (producto, tamaño_de_porción, carbohidratos, vencimiento)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de guardar los datos
    producto_entry.delete(0, tk.END)
    tamaño_de_porción_entry.delete(0, tk.END)
    carbohidratos_entry.delete(0, tk.END)
    vencimiento_entry.delete(0, tk.END)
    # Aquí puedes realizar la lógica para guardar la información en tu base de datos o donde desees
    # Por ahora, simplemente mostramos la información
    