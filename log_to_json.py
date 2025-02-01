import re
import json

# Caminho do log falso
log_file = "fake_access.log"

# Expressão Regular para capturar dados
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>GET|POST|PUT|DELETE) (?P<url>\S+) HTTP/\d\.\d" (?P<status>\d+)')

# Lista para armazenar os logs em JSON
log_json = []

# Ler os logs e transformar em JSON
with open(log_file, "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            log_entry = {
                "ip": match.group("ip"),
                "timestamp": match.group("timestamp"),
                "method": match.group("method"),
                "url": match.group("url"),
                "status": match.group("status")
            }
            log_json.append(log_entry)

# Salvar em JSON
with open("logs.json", "w") as json_file:
    json.dump(log_json, json_file, indent=4)

print("✅ Logs convertidos para JSON: logs.json")
