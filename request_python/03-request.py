import requests

def main():

    prima_valuta = input("inserisci la prima valuta:")
    seconda_valuta = input("inserisci la seconda valuta:")


    payload = {'base': prima_valuta, 'symbols':seconda_valuta}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("La richiesta non è andata a buon fine")
    
    response_data = response.json()
    tasso_di_cambio = response_data["rates"][seconda_valuta]
    print("Data: ", response_data["date"])
    print(f"1{prima_valuta} corrisponde a {tasso_di_cambio} {seconda_valuta}")



if __name__=="__main__":
    main()