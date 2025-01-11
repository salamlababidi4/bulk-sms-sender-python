def get_phone_number(person):
    customers = ["Rachel Green", "Monica Geller", "Ross Geller", "Phoebe Buffay",
                "Joey Tribbiani", "Chandler Bing"]
    numbers = ["+1-813-856-3347", "+1-527-324-1403", "+1-687-801-6781",
                "+1-208-702-5161","+1-908-665-3975", "+1-444-970-5300"]
    return numbers[customers.index(person)]

def send_sms(number):
    # sends message #
    print("Message is successfully sent to " + number)
    return True

def send_bulk_sms(names):
    for people in names:
        try:
            phone = get_phone_number(people)
            send_sms(phone)
            
        except ValueError:
            print(f"Customer is not found in the phone book: {people}")

customer_list = [
    "Rachel Green",
    "Monica Geller",
    "Mariam El Mir",
    "Ross Geller"
]

send_bulk_sms(customer_list)