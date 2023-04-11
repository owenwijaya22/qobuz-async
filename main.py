import logging
import threading
from qobuz_dl.core import QobuzDL
import json

logging.basicConfig(level=logging.INFO)
with open('config.json', 'r') as f:
    data = json.load(f)

def download(url):
    qobuz.handle_url(url)
    
qobuz = QobuzDL(quality=27)
qobuz.get_tokens()
qobuz.initialize_client(data["email"], data["password"], qobuz.app_id, qobuz.secrets)

urls = [input("Enter URL: ") for _ in range(input("How many songs:"))]
threads = [threading.Thread(target=download, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()   