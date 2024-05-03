# Implementación  del Patrón ETL
## Team 4
**Integrantes:**
- José Jaime Dominguez Sandoval
- Carlos Tadeo Ibarra Reyes
- Oscar de Jesús Torres Rivera
- Juan Luis Dena Juárez

## Pasos para la Ejecución:
# Prerrequisitos:
-[Instalar Docker](:https://www.docker.com/)
[Instalar conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

Clonar el repositorio:
```
	git clone https://github.com/JAIMDOMINGUEZ/ETL.git
```
## Ejecutar el gestor
1. Ingresar al directorio cliente-master
	`cd gestor-master`
2.  Crear un entrono 
```
conda create --name gdd python=3.8 -y
```
3. Activar el entorno
```
	conda activate gdd
```
4. Instalar las dependencias
```
pip install -r requirements.txt
```

5. Ejecutar el contenedor
```
ocker run -d -it -p 5080:5080 -p 6080:6080 -p 8080:8080 -p 9080:9080 --name dgraph dgraph/standalone:latest
```
7. Ejecutar el gestor de datos
```
python loader.py
```
8. Desactiva el entorno
```
conda deactivate
```
## Ejecutar el Cliente
1. Ingresar al directorio cliente-master
	`cd gestor-master`
2.  Crear un entrono 
```
conda create --name client python=3.8 -y
```
3. Activar el entorno
```
	conda activate client
```
4. Instalar las dependencias
```
pip install -r requirements.txt
```
5. Ejecutar el gestor de datos
```
python main.py
```
6. Desactiva el entorno
```
conda deactivate
```
7. [Acceder al servidor](http://localhost:5000/)
	
