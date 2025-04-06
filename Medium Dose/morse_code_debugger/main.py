MORSE_CODE = {
    '.-' : 'A' , '-...' : 'B', '-.-.' : 'C', '-..' : 'D', '.' : 'E', '..-.' : 'F',
    '--.' : 'G' , '....' : 'H' , '..' : 'I' , '.---' : 'J', '-.-' : 'K', '.-..' : 'L',
    '--' : 'M' , '-.' : 'N', '---' : 'O', '.--.':'P', '--.-' : 'Q', '.-.':'R', '...':'S',
    '-':'T', '..-':'U','...-':'V', '.--' : 'W', '-..-':'X', '-.--':'Y','--..':'Z',
    '.----':'1', '..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9', '-----':'0','/':''
            } #creatin a dict

def morse_code_debugger(encrypted_msg):
    sep_words = encrypted_msg.split("   ") #separatin words from the original msg
    sep_letters = [i.split(" ") for i in sep_words] #separatin each letter from every single word
    decoded_words = ["".join(MORSE_CODE[letter] for letter in word if letter in MORSE_CODE)for word in sep_letters] #decodin each letter
    return " ".join(decoded_words) #joinin words with a space between 'em
if __name__ == "__main__":
    msg = input(".-- .... .- - .----. ... / - .... . / -- . ... ... .- --. . : ")
    print(morse_code_debugger(msg))
