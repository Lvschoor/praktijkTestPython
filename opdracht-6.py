from keyword import iskeyword


def contains_keywords(*words):
    is_keyword = False
    for word in words:
        if iskeyword(word):
            is_keyword = True
            break
    return is_keyword


print(contains_keywords("hello", "goodbye"))
print(contains_keywords("def", "haha", "lol", "chickens are evil", 42))
print(contains_keywords("four", "for", "if"))
print(contains_keywords("blabla", "doggo", "crab", "anchor"))
print(contains_keywords("grizzly", "ignore", "return", "False"))
