import cv2
from pyzbar.pyzbar import decode

def scan_qr_from_file(image_path):
    """Escanea y decodifica un código QR desde una imagen."""
    try:
        img = cv2.imread(image_path)
        detected_qrs = decode(img)
        for qr in detected_qrs:
            data = qr.data.decode('utf-8')
            print(f"Contenido del QR: {data}")
            return data
        print("No se detectó ningún código QR.")
        return None
    except Exception as e:
        print(f"Error al escanear QR desde archivo: {e}")
        return None

def scan_qr_from_camera():
    """Escanea un código QR usando la cámara."""
    cap = cv2.VideoCapture(0)
    print("Presione 'q' para salir.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            data = obj.data.decode('utf-8')
            print(f"QR Detectado: {data}")
            cap.release()
            cv2.destroyAllWindows()
            return data
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print("No se detectó ningún código QR.")
    return None
