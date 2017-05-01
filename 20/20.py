import json
import sys

filename = sys.argv[1]

with open(filename) as f:
    for line in f:
        decode_data = json.loads(line)
        if decode_data['title'] == "イギリス":
            print(decode_data['text'], "\n")

