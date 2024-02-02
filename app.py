from flask import Flask, jsonify, request
from datetime import datetime,timedelta
app = Flask(__name__)


@app.route('/v1/', methods=['GET'])
def handle_jlogin___():
   return  ({'token':'encoded_jwt'})

if __name__ == '__main__':
   print("+++++++++++++++++++++++++++++++++++ main")
   app.run(debug=True, port=4000)
