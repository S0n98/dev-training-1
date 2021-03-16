import requests

if __name__ == '__main__':
    re = requests.get("https://90a9cbd658be991fa74a86e9876a3a91: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@obamababby.myshopify.com/admin/api/2021-01/customers.json")
    count = 1
    for cus in re.json()["customers"]:
        print('Customer', count)
        print(cus, end='\n\n')
        count += 1
    
