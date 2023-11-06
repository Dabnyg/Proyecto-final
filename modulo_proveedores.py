import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import ImageTk, Image
import mysql.connector

# Definir las variables de entrada
idproducto_entry = None
idproveedores_entry= None
Telefono_entry = None
Dirección_entry = None
busqueda_entry = None

def eliminar_producto():
    # Acceder a las variables globales
    idproducto = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "DELETE FROM proveedores WHERE idproducto = %s"
    values = (idproducto,)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de eliminar los datos
    idproducto_entry.delete(0, tk.END)
    idproveedores_entry.delete(0, tk.END)
    Telefono_entry.delete(0, tk.END)
    Dirección_entry.delete(0, tk.END)

    tk.messagebox.showinfo("Éxito", "Producto eliminado")

def buscar_producto():
    # Acceder a las variables globales
    global idproducto_entry, idproveedores_entry, Telefono_entry, Dirección_entry, busqueda_entry

    idproducto = busqueda_entry.get()

    # Configurar la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realizar una consulta para buscar el producto
    query = "SELECT * FROM proveedores WHERE idproducto = %s"
    values = (idproducto,)

    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # Actualizar los cuadros de entrada con los datos encontrados
        idproducto_entry.delete(0, tk.END)
        idproveedores_entry.delete(0, tk.END)
        Telefono_entry.delete(0, tk.END)
        Dirección_entry.delete(0, tk.END)

        idproducto_entry.insert(0, str(resultado[0]))
        idproveedores_entry.insert(0, resultado[1])
        Telefono_entry.insert(0, resultado[2])
        Dirección_entry.insert(0, str(resultado[3]))
    else:
        # Mostrar un mensaje de que el producto no se encontró
        tk.messagebox.showerror("Error", "Producto no encontrado")

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()


def mostrar_ventana_proveedores():
    # Crea una nueva ventana para Ventas
    ventana_proveedores = tk.Toplevel()
    ventana_proveedores.title("proveedores")
    imagen = Image.open("logo.png")
    nuevo_ancho = 250
    nuevo_alto = 250
    imagen=imagen.resize((nuevo_ancho, nuevo_alto))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta=tk.Label(ventana_proveedores,image=imagen_tk)        
    etiqueta.pack()
    etiqueta.config(image=imagen_tk)
    etiqueta.place(x=20, y=20)
    ventana_proveedores.geometry("800x600")
    ventana_proveedores.configure(bg="#ABEB2A")

    global idproducto_entry, idproveedores_entry,Telefono_entry,Dirección_entry, busqueda_entry
    
    # Crear campos de entrada para productos en la ventana principal
           
    tk.Label(ventana_proveedores, text="Ingrese ID del producto:").place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.05)
    idproducto_entry = tk.Entry(ventana_proveedores)
    idproducto_entry.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_proveedores, text="Ingrese ID del proveedor:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
    idproveedores_entry = tk.Entry(ventana_proveedores)
    idproveedores_entry.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.05)

    tk.Label(ventana_proveedores, text="Ingrese el telefono:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
    Telefono_entry = tk.Entry(ventana_proveedores)
    Telefono_entry.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05)
   
    tk.Label(ventana_proveedores, text="Ingrese la dirección:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
    Dirección_entry = tk.Entry(ventana_proveedores)
    Dirección_entry.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)
        
  
    

    guardar_button = tk.Button(ventana_proveedores, text="Guardar proveedores", command=guardar_proveedores, bg="#007F00", fg="white", font=("Helvetica", 13))
    guardar_button.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.05)

    busqueda_label = tk.Label(ventana_proveedores, text="Buscar Producto por ID", bg="#384E77", fg="white",
                              font=("Helvetica", 12))
    busqueda_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.05)
    busqueda_entry = tk.Entry(ventana_proveedores)
    busqueda_entry.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

    # Botón para buscar producto
    buscar_button = tk.Button(ventana_proveedores, text="Buscar Producto", command=buscar_producto, bg="#FFA500", fg="white",
                             font=("Helvetica", 16))
    buscar_button.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.05)

    # Botón para eliminar producto
    eliminar_button = tk.Button(ventana_proveedores, text="Eliminar Producto", command=eliminar_producto, bg="#FF0000",
                                fg="white", font=("Helvetica", 16))
    eliminar_button.place(relx=0.4, rely=.8, relwidth=0.4, relheight=0.05)

    def cerrar_ventana():
     ventana_proveedores.destroy()

    cerrar_button = tk.Button(ventana_proveedores, text="volver al menú", command=cerrar_ventana, bg="#FF0000", fg="white", font=("Helvetica", 13))
    cerrar_button.place(relx=0.4, rely=0.9, relwidth=0.4, relheight=0.05)
    


    ventana_proveedores.mainloop()







def guardar_proveedores():
    # Acceder a las variables globales
    global idproducto_entry, idproveedores_entry, Telefono_entry, Dirección_entry

    idproducto = idproducto_entry.get()
    idproveedores = idproveedores_entry.get()
    Telefono = Telefono_entry.get()
    Dirección = Dirección_entry.get()
    

    # Configura la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cambia esto a tu contraseña de MySQL
        database="grupal_10"  # Cambia esto a tu base de datos
    )

    cursor = conn.cursor()

    # Realiza una inserción en la base de datos
    query = "INSERT INTO proveedores (idproducto,idproveedores,telefono,dirección) VALUES (%s, %s, %s, %s)"
    values = (idproducto,idproveedores,Telefono,Dirección)

    cursor.execute(query, values)
    conn.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    # Limpiar los campos después de guardar los datos
    idproducto_entry.delete(0, tk.END)
    idproveedores_entry.delete(0, tk.END)
    Telefono_entry.delete(0, tk.END)
    Dirección_entry.delete(0, tk.END)
    