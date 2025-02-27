# 🔐 Message Encoder & Decoder

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Security](https://img.shields.io/badge/Feature-Text%20Encryption-red.svg)](https://github.com/Naeem-360/message_encode_decode)
[![Terminal](https://img.shields.io/badge/Interface-Colorful%20Terminal-purple.svg)](https://pypi.org/project/termcolor/)

A simple yet effective Python tool that encodes and decodes text messages using character manipulation and random letter injection for basic encryption.

## 🌟 Features

- 🔒 Encode messages with a custom algorithm 
- 🔓 Decode previously encoded messages
- 🎨 Colorful terminal output for better readability
- 🔄 Option to continue encoding/decoding multiple messages
- 🛡️ Basic text scrambling for casual privacy

## 📋 Requirements

- Python 3.x
- termcolor library

## 🚀 Installation

### Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Naeem-360/message_encode_decode.git

# Navigate to the project directory
cd message_encode_decode
```

### Install Dependencies

```bash
# Install required packages
pip install termcolor
```

## 💻 Usage

Run the script using Python:

```bash
python encode_decode.py
```

## 🔐 How It Works

### Encoding Process

1. Takes each word in your message
2. For words with 3 or more characters:
   - Swaps the first and last character
   - Adds 3 random letters at the beginning
   - Adds 3 random letters at the end
3. For words with fewer than 3 characters:
   - Simply reverses the word

### Decoding Process

1. Takes each encoded word
2. For words with random letters added:
   - Removes the first 3 random characters
   - Removes the last 3 random characters
   - Swaps the first and last character back to original position
3. For short words:
   - Reverses them back to original

## 🖥️ User Interface

The application features:
- Clear menu options for encoding or decoding
- Color-coded results (encoded messages in red, decoded messages in yellow)
- Divider lines for improved readability
- Friendly welcome and exit messages with emoji

## 📝 Example

Original message:
```
Hello World
```

Encoded message (random letters will vary):
```
abc oellHxyz def orlWdghi
```

Decoded message:
```
Hello World
```

## 💡 Use Cases

- 📱 Send messages with basic privacy
- 🎮 Create simple puzzles or games
- 🎓 Educational tool for understanding basic text manipulation
- 🔍 Introduce beginners to the concept of encryption

## ⚠️ Note

This is a simple encoding algorithm for fun and is not suitable for securing sensitive information. It provides only very basic obfuscation, not true cryptographic security.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Naeem-360/message_encode_decode/issues).

## 📜 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.
