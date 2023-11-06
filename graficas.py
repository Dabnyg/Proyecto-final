import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana_graficas = None  # Declarar ventana_graficas en el ámbito de nivel superior
opciones_frame = None

def cerrar_ventana_graficas():
    global ventana_graficas
    if ventana_graficas is not None:
        ventana_graficas.destroy()

def mostrar_ventana_graficas():
    global ventana_graficas  # Acceder a la variable ventana_graficas en el ámbito global
    if ventana_graficas is None:
        # Configura la conexión a la base de datos MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  # Cambia esto a tu contraseña de MySQL
            database="grupal_10"  # Cambia esto a tu base de datos
        )
        
        if ventana_graficas is None:
         ventana_graficas = tk.Tk()
        ventana_graficas.title("Gráfica de Productos")
        ventana_graficas.geometry("800x600")
        ventana_graficas.configure(bg="#CCB0F4")
        
        
        # Realiza una consulta SQL
        cursor = mydb.cursor()
        cursor.execute("SELECT precio,nombre  FROM productos")  # Ajusta la consulta según tus necesidades
        result = cursor.fetchall()
        
        data = [row[0] for row in result]
        labels = [row[1] for row in result]

        # Crear un gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(labels, data)
        ax.set_xlabel("Productos")
        ax.set_ylabel("Precio")
        ax.set_title("Gráfico de Precios")
        
        # Crear un contenedor para el gráfico en la ventana de Tkinter
        container = tk.Frame(ventana_graficas, bg="#CCB0F4")
        container.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        
        # Colocar el gráfico en el contenedor
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        boton_volver = tk.Button(ventana_graficas, text="Volver al menú", command=cerrar_ventana_graficas, bg="#CCB0F4", fg="#0B0B0B", font=("Helvetica", 12))
        boton_volver.place(relx=0.5, rely=0.02, anchor='n')

def abrir_ventana_graficas():
    global ventana_graficas
    ventana_graficas = tk.Tk()
    ventana_graficas.title("Grafica Productos")
    ventana_graficas.geometry("800x600")
    ventana_graficas.configure(bg="#CCB0F4")
    
    opciones_frame = tk.Frame(ventana_graficas, bg="#CCB0F4")
    opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    productos_button = tk.Button(opciones_frame, text="Grafica Productos", command=mostrar_ventana_graficas, bg="#CCB0F4", fg="white", font=("Helvetica", 12))
    productos_button.pack(side="left", padx=10)