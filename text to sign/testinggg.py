
asl_fingerspelling = {
    'a': '👌',
    'b': '👍',
    'c': '✌',
    'd': '🤞',
    'e': '🤟',
    'f': '🖖',
    'g': '🤘',
    'h': '🖕',
    'i': '🤙',
    'j': '👈',
    'k': '👉',
    'l': '👆',
    'm': '👇',
    'n': '☝',
    'o': '👊',
    'p': '✊',
    'q': '🤛',
    'r': '🤜',
    's': '👋',
    't': '🤚',
    'u': '🖐',
    'v': '✋',
    'w': '👐',
    'x': '🙌',
    'y': '🙏',
    'z': '🤝',
    ' ': ' ',
}

def text_to_asl(text):
    text = text.lower()  # Convert text to lowercase
    asl_translation = ''.join([asl_fingerspelling.get(char, char) for char in text])
    return asl_translation

def main():
    print("Text-to-ASL Fingerspelling Translator")
    while True:
        user_input = input("Enter a phrase or type 'exit' to quit:")
        
        if user_input.lower() == "exit":
            break
        
        asl_translation = text_to_asl(user_input)
        print("ASL Fingerspelling Translation:", asl_translation)

if __name__ == "__main__":
    main()
