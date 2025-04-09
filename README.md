
# Proyecto: Creación de Hábitos

Este proyecto es una aplicación web para la gestión de hábitos, donde puedes crear y ver tus hábitos, con la posibilidad de editarlos y eliminarlos.

## Requisitos

- Python 3.x
- Django 3.x o superior
- (Opcional) Entorno virtual para gestionar las dependencias

## Instalación

1. Clona este repositorio en tu máquina local:

   ```
   git clone https://github.com/Vania-0731/examen_01.git
   ```

2. Accede al directorio del proyecto:

   ```
   cd nombre_del_directorio
   ```

3. (Opcional) Crea un entorno virtual para aislar las dependencias del proyecto:

   ```
   python -m venv venv
   ```

4. Activa el entorno virtual:

   - En Windows:

     ```
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Instala las dependencias del proyecto:

   ```
   pip install -r requirements.txt
   ```

   Si no tienes el archivo `requirements.txt`, puedes instalar Django manualmente:

   ```
   pip install django
   ```

6. Realiza las migraciones de la base de datos:

   ```
   python manage.py migrate
   ```

7. Ejecuta el servidor de desarrollo de Django:

   ```
   python manage.py runserver
   ```

8. Accede a la aplicación desde tu navegador en `http://127.0.0.1:8000/`.

## Archivos principales

- **index.html**: Página principal donde se muestran los hábitos.
- **habit_form.html**: Página para crear un nuevo hábito.
- **views.py**: Controladores para manejar las vistas de la aplicación.
- **models.py**: Definición del modelo de datos para los hábitos.
- **static/css/styles.css**: Estilos para la interfaz de usuario.

## Uso

- Puedes crear nuevos hábitos en la página "Crear un nuevo hábito".
- Verás una lista de hábitos en la página principal.
- Puedes editar y eliminar hábitos de la lista.

## Notas

- Si no tienes un archivo `requirements.txt`, crea uno con el siguiente comando para guardar las dependencias:

  ```
  pip freeze > requirements.txt
  ```

## Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo LICENSE para más detalles.
