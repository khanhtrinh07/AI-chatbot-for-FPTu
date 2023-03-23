from underthesea import text_normalize
from underthesea import ner

InputText = input("Để có thể dễ dàng giao tiếp xin mời bạn giới thiệu về bản thân (Tên, ngày tháng năm sinh, địa chỉ,...): ")
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

print(name)
print(dob)
print(loc)
