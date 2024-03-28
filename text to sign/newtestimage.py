asl_fingerspelling = {
    'hello':'hello.png',
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
