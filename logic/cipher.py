import hashlib

def hash_text(text, algorithm):
    if algorithm == "sha256":
        hashed_text = hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "sha512":
        hashed_text = hashlib.sha512(text.encode()).hexdigest()
    elif algorithm == "sha1":
        hashed_text = hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "sha384":
        hashed_text = hashlib.sha384(text.encode()).hexdigest()
    elif algorithm == "BumBar":
        result = ''
        text1 = text.lower().replace(' ', '`')

        for x in text1:
            if 97 <= ord(x) <= 122 or x == '`':
                result += str(ord(x) - 96)
            else:
                result += x

        result = ' '.join(result)
        return result
    else:
        hashed_text = "Unknown algorithm"
    return hashed_text
