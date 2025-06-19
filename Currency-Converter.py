def currency_converter(amount, from_currency, to_currency):
    conversion_rates = {
        'USD': {'USD': 1, 'EUR': 0.85, 'GBP': 0.75, 'INR': 74.50},
        'EUR': {'USD': 1.18, 'EUR': 1, 'GBP': 0.88, 'INR': 88.20},
        'GBP': {'USD': 1.33, 'EUR': 1.13, 'GBP': 1, 'INR': 100.45},
        'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010, 'INR': 1}
    }
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        converted_amount = amount * conversion_rates[from_currency][to_currency]
        return converted_amount
    else:
        return None
    
def main():
    print("Welcome to the currency converter! ")

    currencies = ['USD', 'EUR', 'GBP', 'INR']

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    from_currency = input(f"Enter the source currency ({', '.join(currencies)}): ").upper()
    to_currency = input(f"Enter the target currency ({', '.join(currencies)}): ").upper()

    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currency. Please enter one of the supported currencies.")
        return
    
    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion error. Please check your input.")

if __name__ == "__main__":
    main()
