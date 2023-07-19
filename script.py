from myDict import ascii_code

user_text_input = input("Entrez votre texte : ")

def encode(input : str):
    ascii_output : list = []
    for i in input:
        inv_item = {v: k for k, v in ascii_code.items()}
        text = inv_item.get(i)
        ascii_output.append(text)
    print(*ascii_output, sep=":")

encode(user_text_input)