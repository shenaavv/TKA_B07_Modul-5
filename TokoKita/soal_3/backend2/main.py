from flask import Flask, jsonify, request
import socket
import hashlib

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 12000000},
    {"id": 2, "name": "Mouse", "price": 150000},
    {"id": 3, "name": "Keyboard", "price": 350000}
]


@app.route('/')
def home():
    hostname = socket.gethostname()
    return f"Server 2 - TokoKita | Hostname: {hostname}"


@app.route('/products')
def get_products():
    return jsonify(products)


@app.route('/catalogue')
def catalogue():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 2 - TokoKita",
        "hostname": hostname,
        "products": products
    })


@app.route('/checkout', methods=['POST'])
def checkout():
    hostname = socket.gethostname()

    # Simulasi beban CPU nyata: iterative hashing sebanyak 300.000 iterasi
    # Tidak menggunakan time.sleep() - beban murni dari komputasi CPU
    data = "tokokita-checkout-payload"
    for i in range(300000):
        data = hashlib.sha256(f"{data}{i}".encode()).hexdigest()

    return jsonify({
        "status": "success",
        "message": "Checkout berhasil diproses",
        "server": "Server 2 - TokoKita",
        "hostname": hostname,
        "transaction_id": data[:16]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
