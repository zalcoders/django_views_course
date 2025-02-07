BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Don't Change
OFFSET = 526

def generate_shortened_url_from_number(num):
    num += OFFSET

    if num == 0:
        return 0
    
    result = []

    while num:
        num, reminder = divmod(num, 62)
        result.append(BASE62_ALPHABET[reminder])

    return ''.join(result[::-1])