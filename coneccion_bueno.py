import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

IDproducto_entry = None
nombre_entry = None
fecha_vencimiento_entry = None
precio_entry = None
busqueda_entry = None
imagen_tk=None

def eliminar_producto():
    
    IDproducto = busqueda_entry.get()

    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456", 
        database="grupal_10"  
    )

    cursor = conn.cursor()

    
    query = "DELETE FROM productos WHERE IDproducto = %s"
    values = (IDproducto,)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de eliminar los datos
    IDproducto_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    fecha_vencimiento_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)

    tk.messagebox.showinfo("Éxito", "Producto eliminado")

def buscar_producto():
    # Acceder a las variables globales
    global IDproducto_entry, nombre_entry, fecha_vencimiento_entry, precio_entry

    IDproducto = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "SELECT * FROM productos WHERE IDproducto = %s"
    values = (IDproducto,)

    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar los cuadros de entrada con los datos encontrados
        IDproducto_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        fecha_vencimiento_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)

        IDproducto_entry.insert(0, str(resultado[0]))
        nombre_entry.insert(0, resultado[1])
        fecha_vencimiento_entry.insert(0, resultado[2])
        precio_entry.insert(0, str(resultado[3]))
    else:
        # Mostrar un mensaje de que el producto no se encontró
        tk.messagebox.showerror("Error", "Producto no encontrado")

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

def mostrar_ventana_productos():
    global imagen_tk, IDproducto_entry, nombre_entry, fecha_vencimiento_entry, precio_entry, busqueda_entry

    # Crear la ventana principal
    ventana_productos = tk.Tk() 
    
    ventana_productos.geometry("900x600")
    ventana_productos.configure(bg="#D33A1A")

    tk.Label(ventana_productos, text="Ingrese ID del producto:").place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.05)
    IDproducto_entry = tk.Entry(ventana_productos)
    IDproducto_entry.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_productos, text="Ingrese el producto:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
    nombre_entry = tk.Entry(ventana_productos)
    nombre_entry.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_productos, text="Ingrese fecha de vencimiento:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
    fecha_vencimiento_entry = tk.Entry(ventana_productos)
    fecha_vencimiento_entry.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_productos, text="Ingrese el precio:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
    precio_entry = tk.Entry(ventana_productos)
    precio_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)

    # Botón para guardar
    guardar_button = tk.Button(ventana_productos, text="Guardar", command=guardar_producto, bg="#007F00", fg="white",
                               font=("Helvetica", 16))
    guardar_button.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.05)

    # Crear campos de entrada para buscar producto en la ventana principal
    busqueda_label = tk.Label(ventana_productos, text="Buscar Producto por ID", bg="#384E77", fg="white",
                              font=("Helvetica", 12))
    busqueda_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.05)
    busqueda_entry = tk.Entry(ventana_productos)
    busqueda_entry.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

    # Botón para buscar producto
    buscar_button = tk.Button(ventana_productos, text="Buscar Producto", command=buscar_producto, bg="#FFA500", fg="white",
                             font=("Helvetica", 16))
    buscar_button.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)

    # Botón para eliminar producto
    eliminar_button = tk.Button(ventana_productos, text="Eliminar Producto", command=eliminar_producto, bg="#FF0000",
                                fg="white", font=("Helvetica", 16))
    eliminar_button.place(relx=0.4, rely=.8, relwidth=0.4, relheight=0.05)

    def cerrar_ventana():
      ventana_productos.destroy()

    cerrar_button = tk.Button(ventana_productos, text="volver al menú", command=cerrar_ventana, bg="#FF0000", fg="white", font=("Helvetica", 13))
    cerrar_button.place(relx=0.4, rely=0.9, relwidth=0.4, relheight=0.05)
    

def guardar_producto():
    # Acceder a las variables globales
    global IDproducto_entry, nombre_entry, fecha_vencimiento_entry, precio_entry

    IDproducto = IDproducto_entry.get()
    nombre = nombre_entry.get()
    fecha_de_vencimiento = fecha_vencimiento_entry.get()
    precio = precio_entry.get()

    # Configura la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realiza una inserción en la base de datos
    query = "INSERT INTO productos (IDproducto, nombre, `fecha de vencimiento`, precio) VALUES (%s, %s, %s, %s)"
    values = (IDproducto, nombre, fecha_de_vencimiento, precio)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de guardar los datos
    IDproducto_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    fecha_vencimiento_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)

   
