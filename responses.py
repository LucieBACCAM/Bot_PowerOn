import random
import Start_server

def handle_response(message) -> str:
    p_message = message.lower()

    str1 = "Tu dis quoi fdp?"
    str2 = "Lalala j'entends rien"
    str3 = "Votre correspondant est injoignable"
    str4 = "Il serait peut-être temps de se taire non?"

    if p_message == "hello":
        return "Hello there!"

    if p_message == 'hello there':
        return "General Kenobi"

    if p_message == "!help":
        return "ceci est le help connard:   " \
               "Fais un **!on** pour allumer le serveur.   " \
               "Celui-ci s'éteint au bout de 5 min si il y a personne."

    if p_message == '!on':
        Start_server.Start_command()
        return "Server is on"


    return random.choices([str1, str2, str3, str4])
