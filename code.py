import tkinter as tk
from tkinter import messagebox


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    original_text = text_entry.get().lower()
    shift_amount = int(shift_entry.get())
    encode_or_decode = direction_var.get()

    if encode_or_decode not in ["encode", "decode"]:
        messagebox.showerror("Invalid Input", "Please choose 'encode' or 'decode'.")
        return

    cipher_text = ""


    for letter in original_text:

        if letter not in alphabet:
            cipher_text += letter
            continue


        if encode_or_decode == "decode":
            shift_amount *= -1


        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)

        cipher_text += alphabet[shifted_position]


    result_label.config(text=f"Result: {cipher_text.capitalize()}")



root = tk.Tk()
root.title("Caesar Cipher")


direction_var = tk.StringVar(value="encode")


direction_label = tk.Label(root, text="Choose operation (encode/decode):")
direction_label.pack()

encode_radio = tk.Radiobutton(root, text="Encode", variable=direction_var, value="encode")
encode_radio.pack()

decode_radio = tk.Radiobutton(root, text="Decode", variable=direction_var, value="decode")
decode_radio.pack()


text_label = tk.Label(root, text="Enter your message:")
text_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()


shift_label = tk.Label(root, text="Enter shift number:")
shift_label.pack()

shift_entry = tk.Entry(root, width=10)
shift_entry.pack()


cipher_button = tk.Button(root, text="Apply Caesar Cipher", command=caesar_cipher)
cipher_button.pack()


result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14))
result_label.pack()


root.mainloop()
