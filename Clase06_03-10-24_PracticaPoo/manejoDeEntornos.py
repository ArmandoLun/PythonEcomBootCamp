# ejemplo con colorama en un entorno virtual

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")

#crear un nuevo entorno
#python -m venv ve_nuevo

#Este comando guarda una lista de librerias en un txt
#pip freeze > requeriments.txt

#Este comando instala las librerias tomando los nombre de una lista
#pip install -r requeriments.txt