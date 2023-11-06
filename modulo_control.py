import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import ImageTk, Image
import mysql.connector

# Definir las variables de entrada
id_ventas_entry = None
productoid_entry= None
producto_entry = None
estado_de_produccion_entry = None
Cantidad_entry = None
busqueda_entry = None

def eliminar_producto():
    # Acceder a las variables globales
    productoid = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "DELETE FROM estado_de_produccion WHERE productoid = %s"
    values = (productoid,)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de eliminar los datos
    id_ventas_entry.delete(0, tk.END)
    productoid_entry.delete(0, tk.END)
    producto_entry.delete(0, tk.END)
    estado_de_produccion_entry.delete(0, tk.END)
    Cantidad_entry.delete(0, tk.END)

    tk.messagebox.showinfo("Éxito", "Producto eliminado")

def buscar_producto():
    # Acceder a las variables globales
    global id_ventas_entry, productoid_entry, producto_entry, estado_de_produccion_entry, Cantidad_entry

    productoid = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "SELECT * FROM estado_de_produccion WHERE productoid = %s"
    values = (productoid,)

    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar los cuadros de entrada con los datos encontrados
        id_ventas_entry.delete(0, tk.END)
        productoid_entry.delete(0, tk.END)
        producto_entry.delete(0, tk.END)
        estado_de_produccion_entry.delete(0, tk.END)
        Cantidad_entry.delete(0, tk.END)

        id_ventas_entry.insert(0, str(resultado[0]))
        productoid_entry.insert(0, resultado[1])
        producto_entry.insert(0, resultado[2])
        estado_de_produccion_entry.insert(0, str(resultado[3]))
        Cantidad_entry.insert(0, str(resultado[4]))
    else:
        # Mostrar un mensaje de que el producto no se encontró
        tk.messagebox.showerror("Error", "Producto no encontrado")

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()


def mostrar_ventana_estado_produccion():
    # Crea una nueva ventana para Ventas
    ventana_estado_produccion = tk.Toplevel()
    
    ventana_estado_produccion.geometry("800x600")
    ventana_estado_produccion.configure(bg="#389A52")

    global id_ventas_entry, productoid_entry,producto_entry,estado_de_produccion_entry, Cantidad_entry, busqueda_entry
    
    # Crear campos de entrada para productos en la ventana principal
    tk.Label(ventana_estado_produccion, text="Ingrese id de la venta:").place(relx=0.4, rely=0.0, relwidth=0.2, relheight=0.05)
    id_ventas_entry = tk.Entry(ventana_estado_produccion)
    id_ventas_entry.place(relx=0.6, rely=0.0, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_estado_produccion, text="Ingrese ID del producto:").place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.05)
    productoid_entry = tk.Entry(ventana_estado_produccion)
    productoid_entry.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_estado_produccion, text="Ingrese producto:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
    producto_entry = tk.Entry(ventana_estado_produccion)
    producto_entry.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.05)
   
    tk.Label(ventana_estado_produccion, text="Ingrese el estado de producción:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
    estado_de_produccion_entry = tk.Entry(ventana_estado_produccion)
    estado_de_produccion_entry.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05)
        
    tk.Label(ventana_estado_produccion, text="Ingrese la cantidad:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
    Cantidad_entry = tk.Entry(ventana_estado_produccion)
    Cantidad_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)

    guardar_button = tk.Button(ventana_estado_produccion, text="Guardar información", command=guardar_info, bg="#007F00", fg="white", font=("Helvetica", 13))
    guardar_button.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.05)

    busqueda_label = tk.Label(ventana_estado_produccion, text="Buscar Producto por ID", bg="#384E77", fg="white",
                              font=("Helvetica", 12))
    busqueda_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.05)
    busqueda_entry = tk.Entry(ventana_estado_produccion)
    busqueda_entry.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

    # Botón para buscar producto
    buscar_button = tk.Button(ventana_estado_produccion, text="Buscar Producto", command=buscar_producto, bg="#FFA500", fg="white",
                             font=("Helvetica", 16))
    buscar_button.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)

    # Botón para eliminar producto
    eliminar_button = tk.Button(ventana_estado_produccion, text="Eliminar Producto", command=eliminar_producto, bg="#FF0000",
                                fg="white", font=("Helvetica", 16))
    eliminar_button.place(relx=0.4, rely=0.8, relwidth=0.4, relheight=0.05)




    def cerrar_ventana():
     ventana_estado_produccion.destroy()

    cerrar_button = tk.Button(ventana_estado_produccion, text="volver al menú", command=cerrar_ventana, bg="#FF0000", fg="white", font=("Helvetica", 13))
    cerrar_button.place(relx=0.4, rely=0.9, relwidth=0.4, relheight=0.05)
    
    







def guardar_info():
    # Acceder a las variables globales
    global id_ventas_entry, productoid_entry, producto_entry,estado_de_produccion_entry, Cantidad_entry, busqueda_entry

    id_ventas = id_ventas_entry.get()
    productoid = productoid_entry.get()
    producto = producto_entry.get()
    estado_de_produccion = estado_de_produccion_entry.get()
    Cantidad = Cantidad_entry.get()

    # Configura la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realiza una inserción en la base de datos
    query = "INSERT INTO estado_de_produccion (id_ventas, productoid, producto, estado_de_produccion, Cantidad) VALUES (%s, %s, %s, %s,%s)"
    values = (id_ventas, productoid, producto, estado_de_produccion, Cantidad)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de guardar los datos
    id_ventas_entry.delete(0, tk.END)
    productoid_entry.delete(0, tk.END)
    producto_entry.delete(0, tk.END)
    estado_de_produccion_entry.delete(0, tk.END)
    Cantidad_entry.delete(0, tk.END)