import requests

def main():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {
        "number": 10
    }
    
    payload = requests.post('http://127.0.0.1:2000', headers=headers, json=data)
    
    print('Request:', payload.json)
    
main()