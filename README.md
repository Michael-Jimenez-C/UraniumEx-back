# UraniumEx-back

Version de python:3.11.9

# Requerimientos

Se requiere wheel para instalar los modulos y librerias.

```sh
sudo apt-get install python3.11-pip python3.11-dev libmysqlclient-dev
```
o
```sh
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

# Instalación
## Linux
```sh
sudo apt install python3.11-venv
```

```sh
python3.11 -m venv venv
source venv/bin/activate
pip install -r requeriments.txt
```
## Windows
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requeriments.txt
```

# Inicialización
```sh
uvicorn main:app --reload
```
o
```sh
fastapi dev main.py
```
