from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    website_url = request.args.get('url')

    if website_url:
        try:
            ip_address = socket.gethostbyname(website_url)
            return jsonify({'ip_address': ip_address})
        except socket.gaierror as e:
            return jsonify({'error': f"Failed to resolve the IP address for '{website_url}': {str(e)}"}), 400
    else:
        return jsonify({'error': 'URL parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
