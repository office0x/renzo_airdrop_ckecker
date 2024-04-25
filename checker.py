import requests

def get_whitelisted_status(address):
    url = f"https://app.renzoprotocol.com/api/points/{address}"
    response = requests.get(url)
    data = response.json()
    renzo_points = data.get('data').get('totals').get('renzoPoints')
    return renzo_points

def main():
    # Load addresses from wallets.txt
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    # Iterate over addresses and print results
    for address in addresses:
        result = get_whitelisted_status(address)
        if float(result) > 360:
            print(f"{address} {result} ELIGIBLE")
        else:
            print(f"{address} {result} NOT ELIGIBLE")


if __name__ == "__main__":
    main()