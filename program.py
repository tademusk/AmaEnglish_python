import json
with open('amharic.json', 'r', encoding='utf-8') as file:
    amharic_to_english = json.load(file)

def transliterate(text):
    result = []
    for char in text:
        if char in amharic_to_english:
            result.append(amharic_to_english[char])
        elif char.isspace():
            result.append(char)
        else:
            return "Please use Amharic letters only."
    return ''.join(result)

def main():
    while True:
        user_input = input("Please enter Amharic text: ")
        transliterated_text = transliterate(user_input)
        print(transliterated_text)

if __name__ == "__main__":
    main()
