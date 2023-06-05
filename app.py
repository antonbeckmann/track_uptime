import time
from prometheus_client import start_http_server, Gauge
from ping3 import ping, verbose_ping

def check_ping(target):
    # Ping versuchen
    response_time = ping(target)
    
    if response_time is not None:
        # Rechner ist erreichbar
        return 1, response_time
    else:
        # Rechner ist nicht erreichbar
        return 0, None

if __name__ == '__main__':
    # Metrik initialisieren
    ping_metric = Gauge('ping_reachable', '1 if ping is reachable, 0 otherwise')
    response_time_metric = Gauge('ping_response_time', 'Response time of ping in milliseconds')
    
    # Prometheus-Server starten
    start_http_server(8000)
    
    while True:
        # Zielrechner überprüfen
        reachable, response_time = check_ping('example.com')
        
        # Metrikwerte setzen
        ping_metric.set(reachable)
        if response_time is not None:
            response_time_metric.set(response_time)
        else:
            response_time_metric.set(0)
        
        # Wartezeit
        time.sleep(1)
