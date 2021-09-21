import string


def okay_name_emoji(name: str):
    OKAYLIST = [num_ for num_ in range(65, 91)] + [num_ for num_ in range(97, 123)] + [32]
    name_list = [ord(char_) for char_ in name]
    if set(name_list).difference(OKAYLIST):
        return False
    return True


def okay_name_word(name: str):
    alphabet_string = string.ascii_lowercase
    bad_words = [char_ * 3 for char_ in alphabet_string] + ["test", "fuck", "contract"]
    for bad_word in bad_words:
        if bad_word.lower() in name.lower():
            return False
    return True


async def okay_name(name: str):
    okay_name_emoji_ = okay_name_emoji(name)
    if not okay_name_emoji_:
        return False
    okay_name_word_ = okay_name_word(name)
    if not okay_name_word_:
        return False
    print("okay name/symbol")
    return True


"""
has_emoji = bool(emoji.get_emoji_regexp().search(text))
"""
