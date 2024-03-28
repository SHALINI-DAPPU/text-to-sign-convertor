from tkinter import *

asl_fingerspelling = {
    'hello':'hello.png',
}

def display_image(image_filename):
    image = Image.open(image_filename)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.photo = photo
    label.pack()

def text_to_asl(text):
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
        print("ASL Fingerspelling Translation:", asl_translation)

if __name__ == "__main__":
    root = Tk()
    root.title("ASL Fingerspelling Translator")
    
    main()
    root.mainloop()
