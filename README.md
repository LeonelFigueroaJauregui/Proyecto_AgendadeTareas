## Proyecto_AgendadeTareas 💻
### Creado por: Leonel Figueroa Jauregui
![Agenda](https://static.vecteezy.com/system/resources/thumbnails/007/059/682/small/to-do-list-concept-illustration-free-vector.jpg)

-Creado en Python🐍

NOMBRE: Leonel Figueroa Jauregui

FECHA: 13 de Mayo de 2025

PROGRAMA: Agenda_de_tareas.py

CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA

PROFESOR: Francisco Javier Ulloa Cortez

DESCRIPCION: Agenda de tareas, permite agregar tareas y verlas en una lista.
_________________________________________________________________________________________________________________________________________________________________________________

# 🗓️ Agenda de Tareas

Proyecto final desarrollado por **Leonel Figueroa Jauregui** para la materia de programación en el **Centro Universitario de los Altos, Universidad de Guadalajara**.

## 📋 Descripción

La **Agenda de Tareas** es una aplicación de consola que permite al usuario gestionar sus tareas diarias para cada día de la semana. A través de un menú interactivo, se pueden agregar, eliminar, modificar, visualizar y borrar todas las tareas.

## 🎯 Funcionalidades principales

- Agregar tareas por día de la semana.
- Eliminar tareas específicas.
- Modificar tareas ya registradas.
- Ver todas las tareas organizadas por día.
- Borrar todas las tareas.
- Salir del programa.

## 🛠️ Estructura y Funciones del Código

El programa está compuesto por las siguientes funciones:

### `mostrar_menu()`
Muestra un menú artístico con opciones numeradas para interactuar con la agenda. Es la guía principal del usuario.

### `agregar_tarea()`
Solicita al usuario un día de la semana y una tarea, luego la guarda en la lista correspondiente. Si el día es inválido, muestra un mensaje de error.

### `eliminar_tarea()`
Solicita el día y la tarea a eliminar. Verifica si la tarea existe y la borra. Si no se encuentra, lo notifica al usuario.

### `modificar_tarea()`
Permite cambiar el texto de una tarea existente. Solicita el nombre actual y el nuevo nombre, luego actualiza la lista correspondiente.

### `ver_lista_tareas()`
Muestra en pantalla todas las listas de tareas separadas por día.

### `borrar_todas_las_tareas()`
Limpia completamente todas las listas de tareas de la semana.

### `salir()`
Termina la ejecución del programa con un mensaje de despedida.

### `ejecutar_programa()`
Es la función principal que ejecuta el bucle del menú y permite al usuario seleccionar opciones entre 1 y 6. Es la última función del código, que se llama automáticamente al final para iniciar el programa.

## ▶️ Ejecución

Para ejecutar el programa:

```bash
python Agenda_de_tareas.py
```
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
## 📦 Requisitos

- Python 3.6 o superior  
- Editor o entorno para correr código Python (como VS Code, IDLE o terminal)  
- Sistema operativo con soporte para consola (Windows, macOS o Linux)  

## 🧠 Notas adicionales

- El programa está diseñado para usarse en español.  
- Utiliza listas separadas para cada día de la semana.  
- No guarda los datos una vez que se cierra el programa (no hay almacenamiento persistente).  
- Las entradas deben escribirse en minúsculas (por ejemplo, `lunes`).  
- El código es ideal como base para proyectos más avanzados (por ejemplo, con interfaz gráfica o almacenamiento en archivos).  
- Incluye arte ASCII para una experiencia más visual y divertida.  
  ____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
  ##### Thank you for reading! :))


