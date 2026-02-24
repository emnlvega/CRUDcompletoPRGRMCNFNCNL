import requests
import json

BASE_URL = "http://localhost:8000/api/productos/"

def imprimir_respuesta(metodo, response):
    print(f"\n{'*'*50}")
    print(f"  {metodo}")
    print(f"{'*'*50}")
    print(f"  Status Code : {response.status_code}")
    try:
        print(f"  Respuesta   : {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception:
        print(f"  Respuesta   : {response.text}")
    print(f"{'*'*50}\n")


def obtener_todos():
    try:
        response = requests.get(BASE_URL)
        imprimir_respuesta("GET - Obtener todos", response)
    except requests.exceptions.ConnectionError:
        print("Error de conexion con el servidor")


def crear_nuevo():
    producto = {
        "nombre": "Smartphone Android",
        "precio": "599.99",
        "stock": 25,
        "descripcion": "Telefono de gama media con 128GB"
    }
    try:
        response = requests.post(BASE_URL, json=producto)
        imprimir_respuesta("POST - Crear nuevo", response)
        if response.status_code == 201:
            return response.json().get("id")
    except requests.exceptions.ConnectionError:
        print("Error de conexion con el servidor")
    return None


def reemplazar_completo(producto_id):
    datos = {
        "nombre": "Smartphone Premium",
        "precio": "899.99",
        "stock": 15,
        "descripcion": "Version Pro con mejor camara"
    }
    try:
        response = requests.put(f"{BASE_URL}{producto_id}/", json=datos)
        imprimir_respuesta(f"PUT - Reemplazar ID={producto_id}", response)
    except requests.exceptions.ConnectionError:
        print("Error de conexion con el servidor")


def modificar_parcial(producto_id):
    cambios = {
        "precio": "499.99"
    }
    try:
        response = requests.patch(f"{BASE_URL}{producto_id}/", json=cambios)
        imprimir_respuesta(f"PATCH - Modificar ID={producto_id}", response)
    except requests.exceptions.ConnectionError:
        print("Error de conexion con el servidor")


def borrar_producto(producto_id):
    try:
        response = requests.delete(f"{BASE_URL}{producto_id}/")
        imprimir_respuesta(f"DELETE - Borrar ID={producto_id}", response)
        if response.status_code == 204:
            print("  Producto eliminado correctamente")
    except requests.exceptions.ConnectionError:
        print("Error de conexion con el servidor")


if __name__ == "__main__":
    print("\nIniciando pruebas de API\n")

    print("1. Listando productos actuales...")
    obtener_todos()

    print("2. Creando producto nuevo...")
    id_nuevo = crear_nuevo()

    if id_nuevo:
        print(f"3. Reemplazando producto ID={id_nuevo}...")
        reemplazar_completo(id_nuevo)

        print(f"4. Modificando precio ID={id_nuevo}...")
        modificar_parcial(id_nuevo)

        print(f"5. Eliminando producto ID={id_nuevo}...")
        borrar_producto(id_nuevo)

        print("6. Listado final...")
        obtener_todos()
    else:
        print("No se pudo crear el producto")

    print("\nPruebas completadas\n")