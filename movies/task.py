import smtplib
from django.core import management
from django.core.management import call_command
from movies import local_settings
from practica_django.celery import app


@app.task()
def search_movie(movie):
  print("when the download will finish we will send you a email")
  movies = call_command("download", movie)
  return str(movies)

@app.task()
def send_email(movie):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login(local_settings.EMAIL, local_settings.PASSWORD)
  message = f"films for {movie} have been added to the database "
  to = 'jumartinez@lsv-tech.com'
  server.sendmail(local_settings.EMAIL, to, message)
  server.quit()