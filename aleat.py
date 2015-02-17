import webapp
import socket
import random


class miServidor(webapp.webApp):

    def process(self, parsedRequest):
        return("200 OK", "<html>"
                         "<body><h1>" +
                         "Solicita tu pagina aleatoria</h1>" +
                         "<a href='" + str(random.randrange(1000000)) +
                         "'>Dame otra</a>" +
                         "<BODY BGCOLOR='#F5A9F2'>" +
                         "</body></html>")

if __name__ == "__main__":
    serv = miServidor(socket.gethostname(), 1234)
