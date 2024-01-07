## Automatización de Correos para el Foro Tecnológico

### Descripción
Este script proporciona una automatización para el envío masivo de correos electrónicos para el Foro Tecnológico de Empleo. Permite personalizar los mensajes y enviarlos a múltiples destinatarios utilizando plantillas HTML.

### Instrucciones de Uso
1. **Configuración Inicial**
   - Introduce tu dirección de correo, contraseña y asunto para los correos a enviar.
   - Opcionalmente, introduce la dirección de correo para la copia (CC).
  
2. **Personalización del Mensaje**
   - Modifica la variable `saludo` para agregar un saludo personalizado si es necesario.
   - Escribe el cuerpo del correo en el archivo `cuerpo_correo.html`.
   - La variable saludo se introducirá donde ponga <!--SALUDO--> en el `cuerpo_correo.html` por lo que esa parte no se debe eliminar.

3. **Personalización de la Firma**
   - Modifica los campos personalizables en el archivo `firma_correo.html` para adaptar la firma del correo.

4. **Lista de Destinatarios**
   - Copia en el archivo `destinatarios.csv` la lista de nombres y correos electrónicos a utilizar.
   - El formato predeterminado es el resultado de exportar un archivo de Excel con los datos de "Empresa", "Nombre de contacto", "Correo" y "Teléfono", tomando los datos de las columnas 1 y 2.

5. **Archivos adjuntos**
   - Se debe de escoger una de las opciones (con arhivos o sin ellos) y descomentar la linea adecuada en la linea 70 del script.
   - Si se adjuntan archivos se deben de introducir en la carpeta adjuntos y deben de llevar como nombre el correo electrónico de la persona de destino. 
   - También se debe de configurar la extensión de los archivos a enviar.


**Posibles errores**
   - Si da error de autentificación de gmail debemos deshabilitar la autentificacion en dos pasos o crear una contraseña de aplicacion. Además hay que habilitar el acceso de aplicaciones menos seguras en el panel de seguridad de la cuenta de google.