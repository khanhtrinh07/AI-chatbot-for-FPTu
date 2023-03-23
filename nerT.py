from underthesea import text_normalize
from underthesea import ner

def nerText(InputText):
    text = text_normalize(InputText)
    nerT = ner(text)
    LnerT = list(nerT)
    name = ""
    dob = ""
    loc = ""
    for i, item in enumerate(LnerT):
        if "B-PER" in item[3] and "Np" in item[1]:
            name = item[0]
        elif "I-LOC" in item[3] and "M" in item[1]:
            dob = item[0]
        elif "B-LOC" in item[3] and "Np" in item[1]:
            loc = item[0]

    return name, dob, loc

def normalizeText(inputText):
    text = text_normalize(inputText)
    return text
