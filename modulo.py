import tkinter as tk
import mysql.connector
from otro_modulo import id_producto_entry, nombre_entry, fecha_de_vencimiento_entry, precio_entry

# Función para guardar los datos en MySQL
def guardar_producto():
    id_producto = id_producto_entry.get()
    nombre = nombre_entry.get()
    fecha_de_vencimiento = fecha_de_vencimiento_entry.get()
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
    query = "INSERT INTO productos (ID_producto, nombre, fecha_de_vencimiento, precio) VALUES (%s, %s, %s, %s)"
    values = (id_producto, nombre, fecha_de_vencimiento, precio)
    
    cursor.execute(query, values)
    conn.commit()
    
    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()
    
    # Limpiar los campos después de guardar los datos
    id_producto_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    fecha_de_vencimiento_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ingreso de Producto")

# Crear campos de entrada
id_producto_label = tk.Label(ventana, text="ID Producto")
id_producto_label.pack()
id_producto_entry = tk.Entry(ventana)
id_producto_entry.pack()

nombre_label = tk.Label(ventana, text="Nombre")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

fecha_vencimiento_label = tk.Label(ventana, text="Fecha de Vencimiento")
fecha_vencimiento_label.pack()
fecha_de_vencimiento_entry = tk.Entry(ventana)
fecha_de_vencimiento_entry.pack()

precio_label = tk.Label(ventana, text="Precio")
precio_label.pack()
precio_entry = tk.Entry(ventana)
precio_entry.pack()

# Botón para guardar
guardar_button = tk.Button(ventana, text="Guardar", command=guardar_producto)
guardar_button.pack()

# Resto del código para la ventana tkinter
ventana.mainloop()