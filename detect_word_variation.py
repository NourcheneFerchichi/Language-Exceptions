def remove_duplicates(word: str) -> str:
    """ Delete duplicates characters from a string
        
    Args:
        word (str): A word with duplicated characters.

    Returns:
      Output (str): The word after deleting its duplicated characters.
    """
    chars = []
    prev = ""
    for char in word:
        if prev != char:
            chars.append(char)
            prev = char
    output = ''.join(chars)
    return output

def check_obfuscation(original_word: str, variation_word: str) -> bool:
    """ Verifies if an is variation_word the variation of the original_word

    Args:
        original_word (str): An original word.
        variation_word (str): A possible obfuscation of the original one.

    Returns:
      same_word (bool): True if original_word and variation_word are similar,
      False else.
    """
    same_word = False
    variation_word = variation_word.replace("@", "a")
    new_word = "".join(char for char in variation_word if char.isalpha())
    new_word = remove_duplicates(new_word)
    if original_word == new_word:
        same_word = True
    return same_word


### Test Solution ###
words = ["blackkkhat", "bl@khat", "b__la-c_k_hat", "abcd"]
check_obfuscation(original_word="blackhat", variation_word=words[0])
