import requests

def consultar_ip(api_key, ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "x-apikey": api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        resultado = response.json()
        return resultado
    else:
        print(f"Error al consultar la IP {ip}. Código de estado: {response.status_code}")
        return None

# Reemplaza "TU_API_KEY" con tu propia clave de API de VirusTotal
api_key = "1e7cf2bb83480fddcba32c3a7d3b1fb9991d7a3bf72c2617360dc576b46750aa"

# IP a analizar
ip ="18.154.48.115"

# Lista para almacenar los resultados
resultados = []

resultados = consultar_ip(api_key, ip)

print('--------------------------------------------------------------------')
print('  Resultado de consultar en VirusTotal: ', ip)
print('--------------------------------------------------------------------')
#print(resultados)
print(resultados["data"]["attributes"]["last_analysis_stats"])
#for i in resultados["data"]:
#   print(i)