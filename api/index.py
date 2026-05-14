from flask import Flask, request, Response
from flask_cors import CORS
import requests

application = Flask(__name__)
CORS(application)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
}

@application.route('/proxy-products')
def proxy_products():
    store_id = request.args.get('storeId', '').upper()
    rack = request.args.get('rack', '').upper()
    
    # URL dinamis: Kalau rak diisi pakai CheckPerRack, kalau kosong pakai list umum
    if rack:
        url = f"https://app.alfastore.co.id/prd/api/mob/tablet/productinfo/CheckPerRack/?storeId={store_id}&rack={rack}"
    else:
        url = f"https://app.alfastore.co.id/prd/api/cex/get_product_list/?storeId={store_id}"
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        return Response(resp.content, status=resp.status_code, content_type='application/json')
    except Exception as e:
        return {'error': str(e)}, 502

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
