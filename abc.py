import socket

def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Failed to resolve the IP address for '{domain_name}': {str(e)}"

# Replace 'example.com' with the website's domain name you want to look up
website_domain = 'example.com'
ip_address = get_ip_address(website_domain)

if not ip_address.startswith("Failed"):
    print(f"The IP address of {website_domain} is: {ip_address}")
else:
    print(ip_address)
