n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for word in words:
        for i in word:
            print i
    return result


print join_strings(n)
