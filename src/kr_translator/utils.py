STEP = 500
MIN_CHARS = 20

def has_repeating_chars(text):
    return any(
        len(s := text[i:min(i+STEP, len(text))]) >= STEP and len(set(s)) < MIN_CHARS
        for i in range(0, len(text), STEP)
    )