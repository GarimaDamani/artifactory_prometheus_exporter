import socket
import time
from prometheus_client import Enum, start_http_server, Gauge

start_http_server(9091)


def artifactory_status(art_states):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex(('127.0.0.1',8081))
    if result == 0:
        art_states.set(1)
        print("running")
    else:
        art_states.set(0)
        print("stopped")


def logs_metrics(g_2xx, g_4xx, g_5xx, g_get, g_put):
    with open("/var/opt/scripts/parse.out.log", 'r') as file:
        last_line = file.read()
        last_line = last_line.split(' ')
        g_2xx.set(last_line[0])
        g_4xx.set(last_line[1])
        g_5xx.set(last_line[2])
        g_get.set(last_line[3])
        g_put.set(last_line[4])

g_2xx = Gauge('Artifactory_logs_2xx', 'Artifactory_logs_2xx')
g_4xx = Gauge('Artifactory_logs_4xx', 'Artifactory_logs_4xx')
g_5xx = Gauge('Artifactory_logs_5xx', 'Artifactory_logs_5xx')
g_get = Gauge('Artifactory_logs_get', 'Artifactory_logs_get')
g_put = Gauge('Artifactory_logs_put', 'Artifactory_logs_put')
art_states = Gauge('Artifactory_status', 'Artifactory_status')

while True:
    artifactory_status(art_states)
    logs_metrics(g_2xx, g_4xx, g_5xx, g_get, g_put)
    time.sleep(60)
    
