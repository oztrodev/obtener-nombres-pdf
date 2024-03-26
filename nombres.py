import os
import fitz

def get_pdf_page_count(file_path):
    try:
        pdf_document = fitz.open(file_path)
        if len(pdf_document) > 0:
            return pdf_document.page_count
        else:
            return 0
    except Exception as e:
        print(f"Error al abrir el archivo '{file_path}': {e}")
        return -1

def get_file_size(file_path):
    return os.path.getsize(file_path) / (1024 * 1024) 

carpeta = 'PACK N°21 RELIGION\PACK N°21 RELIGION - PDF PARTE VI'
ruta = 'M:/Oztroteka/' + carpeta
ruta_salida = 'M:/Oztroteka/CONTENIDO PACKS/resultado.txt'

print("Obteniendo nombres...")

archivos_vacios = []

with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_completa) and archivo.lower().endswith('.pdf'):
            paginas = get_pdf_page_count(ruta_completa)
            if paginas == -1:
                archivos_vacios.append(archivo)
            else:
                nombre_archivo = os.path.basename(ruta_completa)
                peso_archivo_mb = get_file_size(ruta_completa)
                archivo_salida.write(f"{nombre_archivo} | {paginas} páginas | {peso_archivo_mb:.2f} MB\n")

print("Los resultados han sido guardados en", ruta_salida)
print("CARPETA", carpeta)

if archivos_vacios:
    print("Los siguientes archivos están vacíos y han sido eliminados:")
    for archivo in archivos_vacios:
        ruta_completa = os.path.join(ruta, archivo)
        os.remove(ruta_completa)
        print(archivo)
else:
    print("No se encontraron archivos vacíos en la carpeta.")
