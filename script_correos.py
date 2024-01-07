import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

sender_email = 'juan.ponton@forotecnoloxico.net'  # Tu dirección de correo electrónico
password = ''  # Tu contraseña de correo electrónico
asunto = 'Selección Stand Foro Tecnolóxico de Emprego'  # Asunto del correo electrónico
cc = 'foro@forotecnoloxico.net'  # Dirección de correo a poner en copia


def create_message(recipient_name, recipient_email):
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

    return message


def send_emails():
    # Configuración del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    port = 587  # El puerto SMTP que estás utilizando

    # Lectura de los nombres de los destinatarios desde un archivo CSV
    with open('destinatarios.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            recipient_name = row[1]
            recipient_email = row[2]
            print(f'Enviando correo a {recipient_name} ({recipient_email})')

            message = create_message(recipient_name, recipient_email)

            # Iniciar sesión en el servidor SMTP y enviar el correo
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())

            print(f'Correo enviado a {recipient_name} ({recipient_email})')


# Programar la ejecución del envío de correos para el 8 de enero de 2023 a las 9:00 AM
# schedule.every().day.at('09:00').do(send_emails)
send_emails()

# Ejecutar el programa indefinidamente para comprobar si se ha alcanzado la fecha programada
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Esperar 60 segundos antes de volver a verificar la programación
