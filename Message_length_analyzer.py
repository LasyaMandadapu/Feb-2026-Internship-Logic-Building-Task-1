messages = ["Hi", "Welcome to the platform", "Ok" ]
for message in messages:
    length = len(message)
    print("Message:" , message)
    print("Length:", length)

    # check if message is longer than 10 characters
    if length > 10:
        print("Flag: Message is longer than 10 charcaters")
    print() # blank line for the clear output
    