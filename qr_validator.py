import re

def validate_qr(content):
    """Valida el contenido de un código QR."""
    url_pattern = re.compile(
        r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)
    if url_pattern.match(content):
        print("El código QR es válido: Es una URL.")
        return True
    else:
        print("El código QR no es válido.")
        return False
