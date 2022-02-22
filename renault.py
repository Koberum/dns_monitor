# Obiettivo
#   Lo script dovrà testare periodicamente un DNS server per verificare se esegue correttamente le query
#   Questo script poi sarà implementato come demone di Linux per testare di continuo lo stato e per cambiare i DNS
#   nel caso il DNS principale non risolve piu
#   All'inizio, lo script se nota qualche problema, deve avviare il medoto azione(), poi si implementerà la funzione azione.

# Analisi
#   Lo script avrà due stati:
#       1. Stato filtro attivo
#           Questo è lo stato in cui lo script rileva che il server sta rispondendo
#       2. Stato filtro disattivato
#           Questo stato si verificherà quando lo script nota che il server non è raggiungibile
#           in questo caso, triggera l'azione e cambia Stato

# Requisiti
#   1. Tutti i parametri devono essere presi a caldo da file config
#   2. Lo script deve essere stabile, con tutte le eccezioni gestite
#   3. Loggin totale di errori e warning, e dei passaggi di stato e di switch di azioni
#   4. Valutare anche tempi di risposta del server (può succedere che un server sia lento a causa dell'alto carico, e può metterci piu tempo a rispondere)
#   4. Rendere lo script demone Linux

# NOTE
#   Per ogni stato, lo script avrà diversi parametri:
#       1. Numero di tentativi
#           Corrisponde al numero di volte che verrà inviata la query
#       2. Tempo di retry
#           Corrisponde al tempo tra un tentativo e l'altro
# TUTTI i parametri devono essere caricati da file config, e editabili in run-time.

# Steps
#   1. Testare periodicamente un server DNS (si consiglia di creare classi o metodi per la gestione)
#   2. Se il server non risponde dopo X tentativi, trigger di azione(True)
#   3. Se il server torna Online dopo X tentativi confermati, trigger di azione(False)


import re
from unittest import result
from dnspython.dns import query, message, rdatatype

# Carico la configurazione da file
config = configparser.ConfigParser()
config.read("config.ini")

# Ottengo i parametri
parametro1 = config['SEZIONE_PARAMETRI']['parametro1']


def send_query(domain): # Invia una query DNS ad uno specifico server
    server = '1.1.1.1' # Server a cui verrà inviata la query
    q_timeout = 5 # Aspetta 5 secondi per ottenere il risultato della query in caso di failure
    port = 53 # Porta DNS
    request = message.make_query(domain, rdatatype.DNSKEY, want_dnssec=True)
    r = query.udp(request, server, q_timeout, port)
    return r

def azione(valore):
    if valore==True:
        print("Azione attivata")
    else
        print("Azione disattivata")

#############################
#        Main Logic         #
#############################

# Speech is silver, silence is golden...
