words = ["gin", "zen", "gig", "msg"]
morse_dict = { 'a':'.-', 'b':'-...', 
            'c':'-.-.', 'd':'-..', 'e':'.', 
            'f':'..-.', 'g':'--.', 'h':'....', 
            'i':'..', 'j':'.---', 'k':'-.-', 
            'l':'.-..', 'm':'--', 'n':'-.', 
            'o':'---', 'p':'.--.', 'q':'--.-', 
            'r':'.-.', 's':'...', 't':'-', 
            'u':'..-', 'v':'...-', 'w':'.--', 
            'x':'-..-', 'y':'-.--', 'z':'--..', 
            } 
unique = set()
for word in words:
    unique.add(''.join([ morse_dict.get(letter) for letter in word]))
print(unique)


