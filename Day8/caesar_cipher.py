def encode(msg, shift):
    arr = ""
    for a in msg:
        curr_val = ord(a)
        if curr_val > 122 or curr_val < 97:
            arr += a
            continue
        new_val = curr_val + shift
        if new_val > 122:
            new_val = 96 + (new_val - 122)
        arr += chr(new_val)
    print(f"Here's the encoded result: {arr}")

def decode(msg, shift):
    arr = ""
    for a in msg:
        curr_val = ord(a)
        if curr_val > 122 or curr_val < 97:
            arr += a
            continue
        new_val = curr_val - shift
        if new_val < 97:
            new_val = 123 - (97 - new_val)
        arr += chr(new_val)
    print(f"Here's the decoded result: {arr}")

from art import logo
print(logo)
start = "yes"
while start == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if choice == "encode":
        msg = input("Type your message: \n").lower()
        shift = int(input("type the shift number: \n"))
        shift = shift % 26
        encode(msg, shift)
    elif choice == "decode":
        msg = input("Type your message: \n").lower()
        shift = int(input("type the shift number: \n"))
        shift = shift % 26
        decode(msg, shift)
    else:
        print("No such option available.")
    start = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
