import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import csv
import os

sender_email = 'juan.ponton@forotecnoloxico.net'  # Tu dirección de correo electrónico
password = ''  # Tu contraseña de correo electrónico
asunto = 'Selección Stand Foro Tecnolóxico de Emprego'  # Asunto del correo electrónico
cc = ''  # Dirección de correo a poner en copia
carpeta_adjuntos = 'adjuntos/'  # Ruta de la carpeta donde están los archivos

def create_message(recipient_name, recipient_email, file_path=None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Cc'] = cc
    message['Subject'] = asunto

    # Leer el contenido del archivo HTML para el cuerpo del correo
    with open('cuerpo_correo.html', 'r', encoding='utf-8') as cuerpo_file:
        cuerpo_html = cuerpo_file.read()

    # Leer el contenido del archivo HTML para la firma
    with open('firma_correo.html', 'r', encoding='utf-8') as firma_file:
        firma_html = firma_file.read()

    # Agregar el saludo al inicio del mensaje HTML del cuerpo del correo
    saludo = f'Buenos días {recipient_name},'
    cuerpo_html_con_saludo = f'<p>{saludo}</p>{cuerpo_html}'

    # Combinar el cuerpo del correo y la firma
    contenido_completo = f'{cuerpo_html_con_saludo}<br>{firma_html}'

    # Agregar el contenido HTML al cuerpo del mensaje
    body = MIMEText(contenido_completo, 'html')
    message.attach(body)

    # Adjuntar el archivo al mensaje si existe
    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), Name=os.path.basename(file_path))
            attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            message.attach(attachment)

    return message

def send_emails():
    # Configuración del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    port = 587  # El puerto SMTP que estás utilizando

    # Lectura de los nombres de los destinatarios desde un archivo CSV
    with open('destinatarios.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Verificar si la línea está vacía
            if len(row) == 0:
                continue  # Saltar esta línea

            recipient_name = row[1]
            recipient_email = row[2]

            print(f'Enviando correo a {recipient_name} ({recipient_email})')

            # Path para el archivo basado en el nombre del destinatario
            file_path = os.path.join(carpeta_adjuntos, f'{recipient_email}.pdf')  # Cambiar la extensión según el tipo de archivo que estás adjuntando

            ###ESCOGER UNA DE LAS SIGUIENTES OPCIONES###
            
            # Crear el mensaje sin adjunto
            #message = create_message(recipient_name, recipient_email)
            #Crear el mensaje con adjunto
            #message = create_message(recipient_name, recipient_email, file_path)

            recipients = [recipient_email, cc]

            # Iniciar sesión en el servidor SMTP y enviar el correo
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipients, message.as_string())

            print(f'Correo enviado a {recipient_name} ({recipient_email})')

send_emails()
