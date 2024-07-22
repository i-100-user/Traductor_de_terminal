# Traductor de Texto para la Terminal

Este es un script de Python que traduce texto de inglés a español (u otros idiomas) usando la API de Google Translate. Está diseñado para ejecutarse en la terminal de Linux y manejar textos largos dividiéndolos en fragmentos para evitar problemas de límite de longitud de consulta.

## Requisitos

- Python 3
- La biblioteca `googletrans` (4.0.0-rc1 o superior)

## Instalación

1. **Instalar Python 3**: Asegúrate de tener Python 3 instalado. Puedes verificarlo con:

    ```sh
    python3 --version
    ```

2. **Instalar la biblioteca `googletrans`**: Instala la biblioteca necesaria con pip:

    ```sh
    pip install googletrans==4.0.0-rc1
    ```

## Uso

1. **Guardar el script**: Guarda el siguiente código como `traductor.py` en un directorio de tu elección:

    ```python
    from googletrans import Translator

    # Definir colores y estilos
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AZUL = "\033[34m"
    SUBRAYADO = "\033[4m"
    RESET = "\033[0m"
    FONDO_AZUL = "\033[44m"
    FONDO_MAGENTA = "\033[45m"
    FONDO_CIAN = "\033[46m"
    FONDO_BLANCO = "\033[47m"
    NEGRITA = "\033[1m"

    def traducir_texto(texto, src='en', dest='es'):
        traductor = Translator()
        # Dividir el texto en fragmentos de hasta 500 caracteres
        fragmentos = [texto[i:i + 500] for i in range(0, len(texto), 500)]
        traducciones = []
        for fragmento in fragmentos:
            traduccion = traductor.translate(fragmento, src=src, dest=dest)
            traducciones.append(traduccion.text)
        return ''.join(traducciones)

    def traducir_archivo(ruta_archivo, src='en', dest='es'):
        # Abrir y leer el archivo de texto
        with open(ruta_archivo, 'r') as archivo:
            texto = archivo.read()
        
        # Traducir el texto leído del archivo
        return traducir_texto(texto, src, dest)

    if __name__ == "__main__":
        import sys
        
        # Verificar que se haya pasado un argumento (la ruta del archivo)
        if len(sys.argv) < 2:
            print(f"\n{NEGRITA}[{RESET}{VERDE}*{RESET}{NEGRITA}] Uso: traductor{RESET} {CIAN}+{RESET} {NEGRITA}archivo.txt{RESET}")
        else:
            # Obtener la ruta del archivo del primer argumento
            ruta_archivo = sys.argv[1]
            
            try:
                # Llamar a la función para traducir el archivo
                resultado = traducir_archivo(ruta_archivo)
                
                # Imprimir la traducción
                print(f"{FONDO_AZUL}Traducción:{RESET}")
                print(f"\n{resultado}")
            
            except Exception as e:
                print(f"{ROJO}Error: {RESET}{e}")
    ```

2. **Ejecutar el script**: Usa el siguiente comando para ejecutar el script desde la terminal, proporcionando el archivo de texto que deseas traducir:

    ```sh
    python3 traductor.py archivo.txt
    ```

## Notas

- **Límites de Consulta**: El script maneja textos largos dividiéndolos en fragmentos de hasta 500 caracteres para evitar problemas de límite de longitud de consulta.

- **Colores y Estilos**: El script utiliza códigos de escape ANSI para darle formato y color a la salida en la terminal. Puedes ajustar estos códigos según tus preferencias.

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de hacer un fork del repositorio y enviar pull requests. Asegúrate de seguir las buenas prácticas de desarrollo y pruebas antes de enviar cambios.



---


---
¡Gracias por usar nuestro traductor de texto! Si tienes alguna pregunta o encuentras problemas, no dudes en abrir un issue en el repositorio.
