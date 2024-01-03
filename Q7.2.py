import requests

api_id = ""  # Your API key goes here

while True:
    coin = input("Enter cryptocoin: ")
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr&x_cg_demo_api_key={api_id}")
    data = response.json()

    if coin in data:
        print("\nCrypto:", coin)
        print("Price in USD:", data[coin]['usd'], "USD")
        print("Price in INR:", data[coin]['inr'], "INR")
    else:
        print("Invalid cryptocoin!")

    choice = input("Want to see more cryptocoins? (y/n): ")
    if choice.lower() == "n":
        break
