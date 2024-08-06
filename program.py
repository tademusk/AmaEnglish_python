import json

try:
    with open('amharic.json', 'r', encoding='utf-8') as file:
        amharic_to_english = json.load(file)
except FileNotFoundError:
    print("The file 'amharic.json' was not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")
    exit(1)

def transliterate(text):
    result = []
    for char in text:
        if char in amharic_to_english:
            result.append(amharic_to_english[char])
        else:
            result.append(char)
    return ''.join(result)

def main():
    while True:
        user_input = input("Please enter Amharic text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        transliterated_text = transliterate(user_input)
        print(transliterated_text)

if __name__ == "__main__":
    main()
