import re

# Caminho do log falso
log_file = "fake_access.log"

# Expressão Regular para capturar dados
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>GET|POST|PUT|DELETE) (?P<url>\S+) HTTP/\d\.\d" (?P<status>\d+)')

# Dicionário para contar requisições por IP
ip_counts = {}

# Ler e processar os logs
with open(log_file, "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            status = match.group("status")
            url = match.group("url")

            # Identificar tentativas de ataque
            if status in ["403", "404", "500"] or "/admin" in url or "/wp-login.php" in url:
                print(f"🚨 POSSÍVEL ATAQUE: IP {ip} tentou acessar {url} (Status: {status})")

            # Contar acessos por IP
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

# Mostrar os IPs mais ativos
print("\n📌 IPs mais ativos:")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip}: {count} requisições")
