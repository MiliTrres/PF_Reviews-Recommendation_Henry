<h1 align="center"><b>Proyecto de Análisis y Machine Learning McDonald's</b></h1>


# INSTRUCCIONES PARA COMENZAR A TRABAJAR EN EL PROYECTO

## 1) Crear entorno virtual

Todas las dependencias y librerías van a quedar instaladas acá:

```
python -m venv pf
```

Esto nos posibilita solo trabajar con las librerías necesarias del proyecto, y no con todas las que se tengan instaladas localmente. Permite que otros usuarios o compañeros de trabajo puedan replicar e instalar sencillamente lo mismo que nosotros, y que no interfiera con las cosas que tengan también previamente descargadas. 

Recuerda activar tu entorno virtual una vez creado y cada vez que vayas a trabajar en el proyecto.

## 2) Clonar el repositorio

```
git clone https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry.git
```
**⚠️IMPORTANTE:** Recuerda crear tu rama de trabajo y nunca trabajar en la rama **Main.**
Para esto es necesario familiarizarse en como trabajar con Git y Github.

## 3) Instalar requirements.txt

Intalamos las librerías necesarias para correr el proyecto:
```
pip install -r requirements.txt
```

Si luego se necesita instalar otra librería más, se debe ejecutar este comando:
```
pip freeze > requirements.txt
```
Cualquier persona que quiera usar nuestro código, va a poder instalar lo mismo que instalamos nosotros.
