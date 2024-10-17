import os
print(f"Sistema operativo: {os.name}")

if os.name == "nt":
    print("es windows")
    os.system("cls")

