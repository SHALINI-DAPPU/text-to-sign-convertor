asl_fingerspelling = {
    'a': '👌',
    'b': '👍',
    'c': '✌',
    'd': '🤞',
    'e': '🤟',
    'f': '🖖',
    'g': '🤘',
    'h': 'hello.png',  # Map "hello" to the image file "hello.png"
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

def display_image(image_filename):
    image = Image.open(image_filename)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.photo = photo
    label.pack()

def text_to_asl(text):
    text = text.lower()
    translation = asl_fingerspelling.get(text, text)

    if translation.endswith('.png'):
        display_image(translation)
        return ""

    return translation

def main():
    print("Text-to-ASL Fingerspelling Translator")
    while True:
        user_input = input("Enter a phrase or type 'exit' to quit:")
        
        if user_input.lower() == "exit":
            break
        
        asl_translation = text_to_asl(user_input)
        if asl_translation:
            print("ASL Fingerspelling Translation:", asl_translation)

if __name__ == "__main__":
    root = Tk()
    root.title("ASL Fingerspelling Translator")
    
    main()
    root.mainloop()
