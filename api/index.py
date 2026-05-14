from flask import Flask, request, Response
from flask_cors import CORS
import requests

application = Flask(__name__)
CORS(application)

@application.route('/proxy-products')
def proxy_products():
    store_id = request.args.get('storeId', '').upper()
    rack = request.args.get('rack', '').upper()
    
    # Kuncinya ada di URL ini, API ini punya data harga yang lebih stabil
    if rack:
        url = f"https://app.alfastore.co.id/prd/api/mob/tablet/productinfo/CheckPerRack/?storeId={store_id}&rack={rack}"
    else:
        # Gunakan API cex product list tapi pastikan field harga tertangkap
        url = f"https://app.alfastore.co.id/prd/api/cex/get_product_list/?storeId={store_id}"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=30)
        return Response(resp.content, content_type='application/json')
    except:
        return {'error': 'failed'}, 502

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
