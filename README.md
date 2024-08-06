# Amharic to English Transliteration Tool

This tool is designed to transliterate Amharic characters to their corresponding English phonetic representations. The transliteration is based on a predefined mapping of Amharic characters to English letters.

## Features

- **Amharic to English Transliteration**: Convert Amharic text into its English phonetic equivalent.
- **Interactive Command Line Interface**: Enter Amharic text and receive the transliterated English text in real-time.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/tademusk/AmaEnglish_python.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd amharic-transliterator
    ```
3. **Ensure Python is Installed**:
    Ensure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Prepare the JSON File**:
   Ensure you have a JSON file named `amharic.json` in the project directory. This file should contain the mappings of Amharic characters to their English transliterations.

2. **Run the Script**:
    ```bash
    python program.py
    ```

3. **Transliterate Text**:
    - Enter Amharic text when prompted.
    - The script will output the transliterated English text.
    - Type `exit` to quit the program.

## Example

```bash
Please enter Amharic text: አማርኛ
amarigna
```

## Error Handling

- The program will handle missing or improperly formatted JSON files and notify the user accordingly.