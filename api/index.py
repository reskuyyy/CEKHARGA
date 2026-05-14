from flask import Flask, request, Response
from flask_cors import CORS
import requests
import os

application = Flask(__name__)
CORS(application)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
}

@application.route('/')
def index():
    return "Planogram API Proxy Running"

@application.route('/proxy-products')
def proxy_products():
    store_id = request.args.get('storeId', '')
    # Kita buat fleksibel, bisa terima rak atau tidak
    rack = request.args.get('rack', '')
    
    if not store_id:
        return {'error': 'storeId wajib diisi'}, 400
    
    # Menggunakan URL API yang kamu berikan
    url = f"https://app.alfastore.co.id/prd/api/mob/tablet/productinfo/CheckPerRack/?storeId={store_id}&rack={rack}"
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        return Response(resp.content, status=resp.status_code,
                        content_type=resp.headers.get('Content-Type', 'application/json'))
    except Exception as e:
        return {'error': str(e)}, 502

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    application.run(host='0.0.0.0', port=port)
