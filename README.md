# DirScannerX #

**DirScannerX** es una herramienta de enumeración de directorios en servidores web desarrollada en Python. Utiliza un diccionario de palabras para encontrar rutas comunes y potencialmente sensibles en aplicaciones web. La herramienta está diseñada para usarse en sistemas de seguridad y con permisos adecuados.

## Características
- Escaneo de directorios y archivos comunes en servidores web.
- Elección de diccionario personalizado o uno por defecto.
- Simulación de solicitudes como un navegador de iPhone.
- Guarda resultados en un archivo de texto.

## Disclaimer

**DirScannerX** fue desarrollado con fines educativos y para realizar auditorías de seguridad en tus propios sistemas o en sistemas donde tengas autorización explícita para realizar pruebas de penetración. El uso de esta herramienta en sistemas sin el consentimiento adecuado es ilegal y contrario a la ética profesional en ciberseguridad.

Los desarrolladores no se responsabilizan de ningún uso indebido de **DirScannerX**. Al utilizar esta herramienta, aceptas que es únicamente bajo tu responsabilidad y para fines legales y éticos.

## Instalación

### Clonar el Repositorio

1. Abre una terminal y clona el repositorio:
    ```bash
    git clone https://github.com/tuusuario/DirScannerX.git
    ```

2. Navega al directorio de la herramienta:
    ```bash
    cd DirScannerX
    ```

3. Instala las dependencias necesarias (asegúrate de tener Python 3 instalado):
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución de la Herramienta

Para ejecutar la herramienta, simplemente utiliza el siguiente comando:
```bash
python3 DirScannerX.py
