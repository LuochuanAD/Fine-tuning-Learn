import json
import random

def load_data():
    with open('alpaca_data.json','r',encoding='utf-8') as f:
        data=json.load(f)
    return data

def conversion_to_jsonl(data):

    random.shuffle(data)

    split=int(len(data)*0.7)

    train=data[:split]
    valid=data[split:]

    def convert(item):
        return {
            "messages":[
                {
                    "role":"user",
                    "content":item["instruction"]+"\n"+item.get("input","")
                },
                {
                    "role":"assistant",
                    "content":item["output"]
                }
            ]
        }

    with open("train.jsonl","w",encoding="utf-8") as f:
        for item in train:
            f.write(json.dumps(convert(item),ensure_ascii=False)+"\n")

    with open("valid.jsonl","w",encoding="utf-8") as f:
        for item in valid:
            f.write(json.dumps(convert(item),ensure_ascii=False)+"\n")

if __name__ == "__main__":
    original_data = load_data()
    conversion_to_jsonl(original_data)