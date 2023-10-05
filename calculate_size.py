from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_website_size(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Calculate the content length (size) of the response in bytes
            content_length = len(response.content)
            
            # Convert the size to a more human-readable format
            # size_readable = convert_bytes(content_length)
            
            return content_length
        else:
            return f"Failed to retrieve the website (Status Code: {response.status_code})"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def convert_bytes(size_bytes):
    # Convert bytes to a more human-readable format (KB, MB, GB, etc.)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0

@app.route('/get_website_size', methods=['GET'])
def calculate_website_size():
    website_url = request.args.get('url')
    
    if website_url:
        website_size = get_website_size(website_url)
        return jsonify({'website_size': website_size})
    else:
        return jsonify({'error': 'URL parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
