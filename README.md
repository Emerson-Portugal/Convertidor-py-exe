# Convertidor de .py a .exe

Aqui te estare enseñando a convertir tu archivos de Python <b> .py</b> a un ejecutable <b>.exe</b>, esto te permitira ejecutar tu archivo en cualquiere maquina de Windows 

---
## Requisitos

- Instalado Python 3.10.10 o verciones anteriores
- Instalado vitualenv

```
pip install virtualenv
```

# Proceso de Instalacion 



## Creacion del Entorno Virtual 


> creamos el entorno virtual
```
python -m virtualenv venv
```

> Ejecutamos virtualenv
```python
.\venv\Scripts\activate
```

> Detemos virtualenv
```python
deactivate
```

## Instalacion de Librerias

> Vamos a instalar las librerias necesarias para poder ejecutar nuestro programa

```python
pip install zstandard
```

```python
pip install Nuitka
```


```python
pip install ordered-set
```

## Comando para Convertir de .py a .exe

```
 py -m nuitka --mingw64 --onefile "nombreArchivo.py"
```


