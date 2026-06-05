import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            print(f"Порт {port} открыт")
        else:
            print(f"Порт {port} закрыт")
    except:
        print(f"Ошибка при проверке порта {port}")

# Сканируем популярные порты на учебном сервере
host = "scanme.nmap.org"
ports = [21, 22, 25, 80, 443, 3306, 8080]

for port in ports:
    scan_port(host, port)
