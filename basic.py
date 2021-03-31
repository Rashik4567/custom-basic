import os
import basic

os.system("clear")
while True:
    text = input("basic> ")
    if text.lower() == "clear":
        os.system("clear")
        continue
    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    else:
        print(result)
