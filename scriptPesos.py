import os

def get_file_size(file_path):
    """Obtiene el tamaño de un archivo."""
    return os.path.getsize(file_path)

def get_folder_size(folder_path):
    """Calcula el tamaño total de una carpeta, incluyendo todos los archivos dentro."""
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            try:
                total_size += get_file_size(file_path)
            except OSError:
                print(f"No se pudo acceder a: {file_path}")
    return total_size

def list_files_and_folders(path):
    """Lista archivos sueltos y carpetas con el tamaño total de su contenido."""
    files_info = []
    folders_info = []

    # Recorrer los archivos y carpetas en la ruta especificada
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        if os.path.isfile(item_path):
            # Si es archivo, agregar a la lista de archivos
            try:
                file_size = get_file_size(item_path)
                files_info.append((item_path, file_size))
            except OSError:
                print(f"No se pudo acceder a: {item_path}")
        
        elif os.path.isdir(item_path):
            # Si es carpeta, calcular su tamaño total
            folder_size = get_folder_size(item_path)
            folders_info.append((item_path, folder_size))

    # Ordenar ambos por tamaño de mayor a menor
    files_info.sort(key=lambda x: x[1], reverse=True)
    folders_info.sort(key=lambda x: x[1], reverse=True)

    # Mostrar archivos ordenados
    print("Archivos sueltos:")
    for file_path, file_size in files_info:
        print(f"{os.path.basename(file_path)} {file_size / (1024 * 1024):.2f} MB")

    # Mostrar carpetas con su tamaño total
    print("\nCarpetas:")
    for folder_path, folder_size in folders_info:
        print(f"{folder_path} {folder_size / (1024 * 1024):.2f} MB")

# Ruta de ejemplo
path = r"E:\SteamLibrary\steamapps\common"
list_files_and_folders(path)