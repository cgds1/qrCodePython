from qr_generator import generate_qr
from qr_scanner import scan_qr_from_file, scan_qr_from_camera
from qr_validator import validate_qr

def main_menu():
    """Menu principal para seleccionar las opciones del programa."""
    while True:
        print("\n=== QR Code Utility ===")
        print("1. Generar Código QR")
        print("2. Escanear QR desde archivo")
        print("3. Escanear QR desde cámara")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            content = input("Ingrese el contenido del QR: ")
            filename = input("Ingrese el nombre del archivo para guardar el QR: ")
            generate_qr(content, filename)
        elif choice == "2":
            filepath = input("Ingrese la ruta del archivo de imagen: ")
            qr_content = scan_qr_from_file(filepath)
            if qr_content:
                validate_qr(qr_content)
        elif choice == "3":
            scan_qr_from_camera()
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
