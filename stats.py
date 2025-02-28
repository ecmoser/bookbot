def get_num_words(f):
    f_words = f.split()
    return len(f_words)

def count_characters(f):
    char_dict = dict()
    for char in f:
        char = char.lower()
        if char_dict.get(char) is None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict['count']
    

def sorted_list_of_chars(d):
    l = []
    for key in d:
        l.append({'char':key, 'count':d[key]})
    l.sort(reverse = True, key = sort_on)
    s = ''
    for mini_d in l:
        if mini_d['char'].isalpha():
            s += f"{mini_d['char']}: {mini_d['count']}\n"
    s = s.strip()
    return s