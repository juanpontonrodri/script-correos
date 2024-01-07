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

3. **Personalización de la Firma**
   - Modifica los campos personalizables en el archivo `firma_correo.html` para adaptar la firma del correo.

4. **Lista de Destinatarios**
   - Copia en el archivo `destinatarios.csv` la lista de nombres y correos electrónicos a utilizar.
   - El formato predeterminado es el resultado de exportar un archivo de Excel con los datos de "Empresa", "Nombre de contacto", "Correo" y "Teléfono", tomando los datos de las columnas 1 y 2.
