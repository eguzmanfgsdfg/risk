from flask import Flask, jsonify, request
from datetime import datetime,timedelta
app = Flask(__name__)


@app.route('/v1/', methods=['GET'])
def handle_jlogin___():
   return  ({'token':'encoded_jwt'})

@app.route('/v1/token', methods=['GET'])
def handle_jlogin():
   content_type = request.headers.get('Content-Type')
   print (request.headers.get('username'))  
   print (request.headers.get('password'))  
   #resp = sp(request.headers.get('username'),request.headers.get('password'))
   resp =''
   print ('+++++++++++++++++el sp devolvio  [',resp,']')
   if resp=='' :
      return  ({'error':'Datos Invalidos','name':request.headers.get('username')})
   encoded_jwt =getToken(request.headers.get('username'),resp)
   return  ({'token':encoded_jwt})

if __name__ == '__main__':
   print("+++++++++++++++++++++++++++++++++++ main")
   app.run(debug=False, port=4000)
