import requests

def consultar_url(api_key, objetivo):
    url = f"https://www.virustotal.com/api/v3/urls"
    headers = {
        'x-apikey': api_key,
        'url': objetivo
    }
    
    data = {
        'url': objetivo
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        resultado = response.json()
        return resultado
    else:
        print(f"Error al consultar la URL {objetivo}. Código de estado: {response.status_code}")
        return None

# Reemplaza "TU_API_KEY" con tu propia clave de API de VirusTotal
api_key = "1e7cf2bb83480fddcba32c3a7d3b1fb9991d7a3bf72c2617360dc576b46750aa"

# IP a analizar
url_objetivo ="https://www.google.com"

# Lista para almacenar los resultados
resultados = []

resultados = consultar_url(api_key, url_objetivo)


print('--------------------------------------------------------------------')
print('  Resultado de consultar en VirusTotal: ', url_objetivo)
print('--------------------------------------------------------------------')
#print(resultados)
print(resultados["data"]["links"]["self"])
#for i in resultados["data"]:
#   print(i)