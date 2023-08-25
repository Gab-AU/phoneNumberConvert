import re
import pyperclip

def format_phone_number(phone_number):
    formatted_number = '-'.join([phone_number[:3], phone_number[3:6], phone_number[6:]])
    return formatted_number

def main():
    while True:
        user_input = input("Enter a phone number: ")
        digits = re.findall(r'\d', user_input)
        caller_phone = ''.join(digits)

        # Format 1
        clipboard_text = f"The phone number is {caller_phone}"
        pyperclip.copy(clipboard_text)
        print("Clipboard contains:", clipboard_text)

        input("Press enter to try another format")

        # Format 2
        formatted_phone = format_phone_number(caller_phone)
        clipboard_text = f"The phone number is {formatted_phone}"
        pyperclip.copy(clipboard_text)
        print("Clipboard contains:", clipboard_text)

        input("Press enter to close")
        break

if __name__ == "__main__":
    main()