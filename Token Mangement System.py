import random

# Dictionary to store event details
events = {}

def create_event():
    event = input("Enter the purpose of the Token (events, camps, etc): ").strip()
    print("Enter some needed data: ")
    event_place = input(f"Enter the exact location of {event}: ").strip()
    event_date = input(f"Enter the date of the {event} (DD/MM/YYYY): ").strip()
    event_time = input(f"Enter the time schedule of {event} (HH:MM): ").strip()
    tokens = int(input(f"Enter the number of Token allocation for the {event}: "))
    event_id = int(''.join(random.choices('0123456789', k=4)))

    # Storing event details
    events[event_id] = {
        'event': event,
        'place': event_place,
        'date': event_date,
        'time': event_time,
        'total_tokens': tokens,
        'allocated_tokens': set()
    }

    print("Tokens created successfully!")
    print("Please note the event ID: ", event_id)

def get_token():
    event_id = int(input("Enter event ID: "))
    name = input("Enter your name: ").strip()
    phono = input("Enter your mobile number: ").strip()
    email = input("Enter your email id: ").strip()

    if event_id in events:
        event = events[event_id]
        if len(event['allocated_tokens']) < event['total_tokens']:
            # Generating unique token number for the user
            while True:
                token_number = random.randint(1, event['total_tokens'])
                if token_number not in event['allocated_tokens']:
                    event['allocated_tokens'].add(token_number)
                    break
            print(f"Hello {name}, your token number for the event is: {token_number}")
        else:
            print("Sorry, all tokens for this event have been allocated.")
    else:
        print("Invalid event ID. Please check and try again.")

def main():
    while True:
        who = input("Let us know who you are, Client or User (or 'exit' to quit): ").strip().lower()

        if who == 'client':
            create_event()
        elif who == 'user':
            get_token()
        elif who == 'exit':
            break
        else:
            print("Invalid role. Please enter either 'Client' or 'User'.")

if __name__ == "__main__":
    main()
