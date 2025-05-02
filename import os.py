import os
import subprocess

# Configura el nombre del repositorio
repo_dir = "mi_repositorio_python"
os.makedirs(repo_dir, exist_ok=True)
os.chdir(repo_dir)

# Inicializa repositorio git
subprocess.run(["git", "init"])

# Crea archivo JSON inicial
with open("datos.json", "w") as f:
    f.write('{ "nombre": "Ejemplo", "valor": 1 }\n')

subprocess.run(["git", "add", "datos.json"])
subprocess.run(["git", "commit", "-m", "Primer commit: archivo JSON inicial"])

# Modifica el archivo JSON
with open("datos.json", "w") as f:
    f.write('{ "nombre": "Ejemplo", "valor": 2 }\n')

subprocess.run(["git", "add", "datos.json"])
subprocess.run(["git", "commit", "-m", "Segundo commit: actualiza valor a 2"])

# Crea archivo TXT adicional
with open("notas.txt", "w") as f:
    f.write("Este es un archivo de texto con notas.\n")

subprocess.run(["git", "add", "notas.txt"])
subprocess.run(["git", "commit", "-m", "Tercer commit: se añade archivo de texto con notas"])

print("\n✅ Repositorio creado con tres commits.")
