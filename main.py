import numpy
import random
from preProcessEnglish import preprocess_data
from preprocessVi import preprocess_data as pd
from bagOfWord import bag_of_words
from model import call_model
from testContinueLearning import collectData, saveNoRe
from nerT import nerText, normalizeText
from tensorflow.python.framework import ops

words, labels, training, output, data = preprocess_data("D:\Code\Project\ProjectDone_MINZUT CHATBOT\data.json")
ops.reset_default_graph()
callModel = call_model(training, output)

def chat():
    InputText = input("Để có thể dễ dàng giao tiếp xin mời bạn giới thiệu về bản thân (Tên, ngày tháng năm sinh, địa chỉ,...): ")
    name, dob, loc = nerText(InputText)
    print("Bắt đầu trò chuyện cùng MinzuT (nhập 'quit' để dừng chương trình)!")
    while True:
        text = input("Bạn: ")
        inp = normalizeText(text)
        if inp.lower() == "quit":
            break
        results = callModel.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        # kiểm tra xem kết quả có đạt ngưỡng xác định trước hay không
        if results[0][results_index] < 0.6:
            saveNoRe(inp)
            print("Xin lỗi, tôi không hiểu ý của bạn, bạn có thể diễn đạt bằng cách khác!")
        else:
            tag = labels[results_index]
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    for i in range(len(responses)):
                        if "{name}" in responses[i]:
                            responses[i] = responses[i].replace("{name}", name)
                        if "{dob}" in responses[i]:
                            responses[i] = responses[i].replace("{dob}", dob)
                        if "{loc}" in responses[i]:
                            responses[i] = responses[i].replace("{loc}", loc)
                    break
            print(random.choice(responses))
            print("Predict "+ str(results[0][results_index]))
    collectData()


chat()


