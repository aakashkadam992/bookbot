def count_words(words):
    return words.split()

def get_character_count(words):
    c_dict = {}
    for i in words.split():
        for c in i:
            if c.lower() in c_dict:
                c_dict[c.lower()] += 1
            else:
                c_dict[c.lower()] = 1
    return c_dict

def sort_on(items):
    return items["num"]
def get_dict_sorted(c_dict):
    o_list = []
    for k in c_dict.keys():
        o_list.append({"char": k, "num": c_dict[k]})
    o_list.sort(reverse=True, key=sort_on)
    return o_list
    




