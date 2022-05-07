import jsonlines
import io

fileName = "myDoc.txt"

with open(fileName) as fh:
    lines = fh.readlines()
    aString = ''.join(lines)

# A record cannot be more than 2048 tokens
with jsonlines.open('output.jsonl', mode='w') as writer:
    writer.write({"text": aString})
