import request
dato = "xl3525" #Patente a consultar.
headers = {'Authorization': 'AQUI TU API KEY',} #Generar la llave para poder utilizar la api
url = requests.get('http://api.multidatachile.com/cars/jsongetowners/%s' % dato, headers=headers) #Lanzar la llamada a la api para sacar los datos
respuesta=url.text #Leer la respuesta de la llamada
data     = json.loads(respuesta) #Convertir la llamada en un json Valido para su pronta lectura.
print data['0']['Name'] #Extraer un dato de el json validado.
