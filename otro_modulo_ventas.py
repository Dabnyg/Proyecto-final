import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import ImageTk, Image
import mysql.connector


ID_ventas_entry = None
ID_producto_entry= None
Producto_entry = None
cantidad_entry = None
fecha_de_venta_entry = None
busqueda_entry = None

def eliminar_ventas():
    
    ID_ventas = busqueda_entry.get()

   
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  
        database="grupal_10"  
    )

    cursor = conn.cursor()

   
    query = "DELETE FROM ventas WHERE ID_ventas = %s"
    values = (ID_ventas,)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de eliminar los datos
    ID_ventas_entry.delete(0, tk.END)
    ID_producto_entry.delete(0, tk.END)
    Producto_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)
    fecha_de_venta_entry.delete(0, tk.END)
    tk.messagebox.showinfo("Éxito", "venta eliminado")

def buscar_venta():
    # Acceder a las variables globales
    global ID_ventas_entry, ID_producto_entry, Producto_entry, cantidad_entry, fecha_de_venta_entry

    ID_ventas = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn =mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "SELECT * FROM ventas WHERE ID_ventas = %s"
    values = (ID_ventas,)

    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar los cuadros de entrada con los datos encontrados
        ID_ventas_entry.delete(0, tk.END)
        ID_producto_entry.delete(0, tk.END)
        Producto_entry.delete(0, tk.END)
        cantidad_entry.delete(0, tk.END)
        fecha_de_venta_entry.delete(0, tk.END)

        ID_ventas_entry.insert(0, str(resultado[0]))
        ID_producto_entry.insert(0, resultado[1])
        Producto_entry.insert(0, resultado[2])
        cantidad_entry.insert(0, str(resultado[3]))
        fecha_de_venta_entry.insert(0, str(resultado[4]))
    else:
        # Mostrar un mensaje de que el producto no se encontró
        tk.messagebox.showerror("Error", "venta no encontrado")

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

def mostrar_ventana_ventas():

    
    # Crea una nueva ventana para Ventas
    ventana_ventas = tk.Toplevel()
    ventana_ventas.title("Ventas")
    imagen = Image.open("logo.png")
    nuevo_ancho = 250
    nuevo_alto = 250
    imagen=imagen.resize((nuevo_ancho, nuevo_alto))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta=tk.Label(ventana_ventas,image=imagen_tk)        
    etiqueta.pack()
    etiqueta.config(image=imagen_tk)
    etiqueta.place(x=20, y=20)
    ventana_ventas.geometry("800x600")
    ventana_ventas.configure(bg="#384E77")

    global ID_ventas_entry, ID_producto_entry,Producto_entry,cantidad_entry,fecha_de_venta_entry, busqueda_entry
    
    # Crear campos de entrada para productos en la ventana principal
    tk.Label(ventana_ventas, text="Ingrese ID de la venta:").place(relx=0.4, rely=0.0, relwidth=0.2, relheight=0.05)
    ID_ventas_entry = tk.Entry(ventana_ventas)
    ID_ventas_entry.place(relx=0.6, rely=0.0, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_ventas, text="Ingrese ID del producto:").place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.05)
    ID_producto_entry = tk.Entry(ventana_ventas)
    ID_producto_entry.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_ventas, text="Ingrese producto:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
    Producto_entry = tk.Entry(ventana_ventas)
    Producto_entry.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.05)
   
    tk.Label(ventana_ventas, text="Ingrese cantidad:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
    cantidad_entry = tk.Entry(ventana_ventas)
    cantidad_entry.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05)
        
    tk.Label(ventana_ventas, text="Ingrese fecha de venta:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
    fecha_de_venta_entry = tk.Entry(ventana_ventas)
    fecha_de_venta_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)

    guardar_button = tk.Button(ventana_ventas, text="Guardar Ventas", command=guardar_ventas, bg="#007F00", fg="white", font=("Helvetica", 13))
    guardar_button.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.05)

    busqueda_label = tk.Label(ventana_ventas, text="Buscar venta por ID", bg="#384E77", fg="white",
                              font=("Helvetica", 12))
    busqueda_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.05)
    busqueda_entry = tk.Entry(ventana_ventas)
    busqueda_entry.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

    # Botón para buscar producto
    buscar_button = tk.Button(ventana_ventas, text="Buscar venta", command=buscar_venta, bg="#FFA500", fg="white",
                             font=("Helvetica", 16))
    buscar_button.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)

    # Botón para eliminar producto
    eliminar_button = tk.Button(ventana_ventas, text="Eliminar venta", command=eliminar_ventas, bg="#FF0000",
                                fg="white", font=("Helvetica", 16))
    eliminar_button.place(relx=0.4, rely=.8, relwidth=0.4, relheight=0.05)

    def cerrar_ventana():
     ventana_ventas.destroy()

    cerrar_button = tk.Button(ventana_ventas, text="volver al menú", command=cerrar_ventana, bg="#FF0000", fg="white", font=("Helvetica", 13))
    cerrar_button.place(relx=0.4, rely=0.9, relwidth=0.4, relheight=0.05)
    
    ventana_ventas.mainloop()







def guardar_ventas():
    # Acceder a las variables globales
    global ID_ventas_entry, ID_producto_entry,Producto_entry,cantidad_entry,fecha_de_venta_entry

    ID_ventas = ID_ventas_entry.get()
    ID_producto = ID_producto_entry.get()
    Producto = Producto_entry.get()
    cantidad = cantidad_entry.get()
    fecha_de_venta = fecha_de_venta_entry.get()

    # Configura la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realiza una inserción en la base de datos
    query = "INSERT INTO ventas (ID_ventas,ID_producto,Producto,cantidad, `fecha de venta`) VALUES (%s, %s, %s, %s,%s)"
    values = (ID_ventas,ID_producto,Producto,cantidad,fecha_de_venta)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de guardar los datos
    ID_ventas_entry.delete(0, tk.END)
    ID_producto_entry.delete(0, tk.END)
    Producto_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)
    fecha_de_venta_entry.delete(0, tk.END)