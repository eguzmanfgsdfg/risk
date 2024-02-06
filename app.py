from flask import Flask, jsonify, request
from datetime import datetime,timedelta
app = Flask(__name__)
from Modelo import *
from flask import Flask, request,json
from db import *
import jwt

def get(data,nombre,str1=True) -> str:
   try:
      dat= data[nombre] #if str1 else f'{}'
      print ('val ',nombre,' = ',dat)
      return    f'{dat}'
   except KeyError:
      return ''
def getToken(username,id) -> str:
   fecha = datetime.today()
   print(fecha)
   dias_a_sumar = timedelta(days=30)
   print(dias_a_sumar)
   fecha_nueva = (fecha + dias_a_sumar).strftime('%Y-%m-%d')
   print(fecha_nueva)
   resp ={"username": username,"id":id,"date": fecha_nueva}
   print(resp)
   encoded_jwt = jwt.encode(resp, "secret", algorithm="HS256")
   print(encoded_jwt)
   return encoded_jwt

def setToken(encoded_jwt) -> str:
   dencoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
  # dencoded_jwt = jwt.decode (encoded_jwt, "secret1", algorithm=["HS256"])
   print(dencoded_jwt)
   return dencoded_jwt

@app.route('/v1/', methods=['GET'])
def handle_jlogin___():
   return  ({'status':'ok'})

@app.route('/v1/token', methods=['GET'])
def handle_jlogin():
   content_type = request.headers.get('Content-Type')
   print (request.headers.get('username'))  
   print (request.headers.get('password'))  
   resp = sp(request.headers.get('username'),request.headers.get('password'))
  
   print ('+++++++++++++++++el sp devolvio  [',resp,']')
   if resp=='' :
      return  ({'error':'Datos Invalidos'})
   encoded_jwt =getToken(request.headers.get('username'),resp)
   return  ({'token':encoded_jwt})

if __name__ == '__main__':
   print("+++++++++++++++++++++++++++++++++++ main")
   app.run(debug=False, port=4000)
