def chat_like_part():
    print("Hi! Please enter your question below")
    q = input()

    print("What table do you want to use?")
    t = input()

    print("What columns in table " + t + " do you want to use?")
    cols = input()
    cols = " ".join(cols.replace(',', '').split()).split(" ")

    print("Thanks for you input, please try this SQL query")
    return q, t, cols

if __name__ == '__main__':
    print(chat_like_part())
