def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    split_s = s.split(' ')
    whiout_space = []
    stri = '#'
    for i in range(len(split_s)):
        if split_s[i] != '':
            whiout_space.append(split_s[i])
    for i in whiout_space:
        stri += i.capitalize()

    return stri



