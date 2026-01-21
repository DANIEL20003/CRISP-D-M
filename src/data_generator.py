
import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for Spanish (Ecuador)
fake = Faker('es_ES')

# --- Data based on Research ---
APELLIDOS_RIOBAMBA = ['Guamán', 'Lema', 'Morocho', 'Daquilema', 'Pilco', 'Cabrera', 'García', 'Rodríguez', 'Zambrano', 'Sánchez']
NOMBRES_COMUNES = ['José', 'Luis', 'Carlos', 'Juan', 'David', 'María', 'Ana', 'Carmen', 'Sofía', 'Verónica']

MARCAS_ELECTRODOMESTICOS = {
    'Refrigeradoras': ['Indurama', 'Mabe', 'LG', 'Samsung', 'Whirlpool'],
    'Lavadoras': ['Whirlpool', 'LG', 'Samsung', 'Mabe', 'Electrolux'],
    'Televisores': ['LG', 'Samsung', 'TCL', 'Hyundai', 'Rivera'],
    'Pequeños Electrodomésticos': ['Oster', 'Umco', 'Black+Decker', 'Taurus'],
    'Cocinas': ['Indurama', 'Mabe', 'Electrolux', 'Whirlpool']
}

# --- Configuration ---
NUM_CLIENTES = 500
NUM_PRODUCTOS = 150
NUM_EMPLEADOS = 25
NUM_VENTAS = 1200
DATA_PATH = 'data/raw/'
FECHA_INICIO = datetime.now() - timedelta(days=3*365) # Last 3 years
FECHA_FIN = datetime.now()

# --- Helper Functions ---
def generar_nombre_completo():
    nombre = random.choice(NOMBRES_COMUNES)
    apellido1 = random.choice(APELLIDOS_RIOBAMBA)
    apellido2 = random.choice(APELLIDOS_RIOBAMBA)
    return f"{nombre} {apellido1} {apellido2}"

# --- Data Generation Functions ---

def generar_clientes(n):
    clientes = []
    for i in range(1, n + 1):
        nombre_completo = generar_nombre_completo()
        clientes.append({
            'cliente_id': i,
            'nombre': nombre_completo.split(' ')[0],
            'apellido': ' '.join(nombre_completo.split(' ')[1:]),
            'email': f"{nombre_completo.replace(' ', '.').lower()}@example.com",
            'telefono': fake.phone_number(),
            'direccion': fake.address().replace('\n', ', ')
        })
    return clientes

def generar_productos(n):
    productos = []
    for i in range(1, n + 1):
        categoria = random.choice(list(MARCAS_ELECTRODOMESTICOS.keys()))
        marca = random.choice(MARCAS_ELECTRODOMESTICOS[categoria])
        
        if categoria == 'Refrigeradoras':
            precio = round(random.uniform(400.0, 1500.0), 2)
            nombre_producto = f"Refrigeradora {marca} {random.randint(250, 400)}L"
        elif categoria == 'Lavadoras':
            precio = round(random.uniform(350.0, 1200.0), 2)
            nombre_producto = f"Lavadora {marca} {random.randint(10, 22)}kg"
        elif categoria == 'Televisores':
            precio = round(random.uniform(300.0, 2000.0), 2)
            nombre_producto = f"TV {marca} {random.choice([32, 43, 50, 55, 65])}\" 4K"
        elif categoria == 'Cocinas':
            precio = round(random.uniform(300.0, 900.0), 2)
            nombre_producto = f"Cocina {marca} {random.randint(4, 6)} quemadores"
        else: # Pequeños Electrodomésticos
            precio = round(random.uniform(25.0, 250.0), 2)
            nombre_producto = f"{random.choice(['Licuadora', 'Cafetera', 'Freidora de Aire'])} {marca}"

        productos.append({
            'producto_id': i,
            'nombre': nombre_producto,
            'categoria': categoria,
            'marca': marca,
            'precio_unitario': precio,
            'stock': random.randint(5, 50)
        })
    return productos

def generar_empleados(n):
    empleados = []
    roles = ['Vendedor', 'Cajero', 'Gerente de Tienda', 'Bodeguero']
    for i in range(1, n + 1):
        empleados.append({
            'empleado_id': i,
            'nombre_completo': generar_nombre_completo(),
            'rol': random.choice(roles)
        })
    return empleados

def generar_ventas(n_ventas, clientes, empleados, productos):
    ventas = []
    detalle_ventas = []
    
    for i in range(1, n_ventas + 1):
        fecha_venta = fake.date_time_between(start_date=FECHA_INICIO, end_date=FECHA_FIN)
        
        venta = {
            'venta_id': i,
            'fecha': fecha_venta.strftime('%Y-%m-%d %H:%M:%S'),
            'cliente_id': random.choice(clientes)['cliente_id'],
            'empleado_id': random.choice(empleados)['empleado_id']
        }
        ventas.append(venta)
        
        # Generar detalle de la venta
        num_productos_en_venta = random.randint(1, 4)
        productos_en_venta = random.sample(productos, num_productos_en_venta)
        
        for producto in productos_en_venta:
            cantidad = random.randint(1, 2)
            precio_unitario = producto['precio_unitario']
            detalle_ventas.append({
                'detalle_id': len(detalle_ventas) + 1,
                'venta_id': i,
                'producto_id': producto['producto_id'],
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'total_linea': round(cantidad * precio_unitario, 2)
            })
            
    return ventas, detalle_ventas

def guardar_csv(data, filename):
    if not data:
        print(f"No data to write for {filename}")
        return
        
    filepath = f"{DATA_PATH}{filename}"
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully generated {filepath}")


if __name__ == '__main__':
    print("Iniciando la generación de datos simulados...")
    
    clientes_data = generar_clientes(NUM_CLIENTES)
    productos_data = generar_productos(NUM_PRODUCTOS)
    empleados_data = generar_empleados(NUM_EMPLEADOS)
    ventas_data, detalle_ventas_data = generar_ventas(NUM_VENTAS, clientes_data, empleados_data, productos_data)
    
    guardar_csv(clientes_data, 'clientes.csv')
    guardar_csv(productos_data, 'productos.csv')
    guardar_csv(empleados_data, 'empleados.csv')
    guardar_csv(ventas_data, 'ventas.csv')
    guardar_csv(detalle_ventas_data, 'detalle_ventas.csv')
    
    print("Proceso de generación de datos finalizado.")
