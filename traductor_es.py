#!/usr/bin/python3

#AUTOR i-100-user

from googletrans import Translator

# Definir colores y estilos
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
SUBRAYADO = "\033[4m"
CIAN = "\033[36m"
RESET = "\033[0m"
FONDO_AZUL = "\033[44m"
FONDO_MAGENTA = "\033[45m"
FONDO_CIAN = "\033[46m"
FONDO_BLANCO = "\033[47m"
NEGRITA = "\033[1m"

def traducir_texto(texto, src='en', dest='es'):
    traductor = Translator()
    # Dividir el texto en fragmentos  caracteres
    fragmentos = [texto[i:i + 10000000] for i in range(0, len(texto), 10000000)]
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
