def solve_runes(runes):
    avaible_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if '*' in runes:
        sign = '*'
    elif "+" in runes:
        sign = "+"
    else:
        sign = '-'
    for i in runes:
        if i in avaible_digit:
            avaible_digit.remove(i)
    for j in avaible_digit:
        puns = runes.replace('?', j)
        before = puns.split('=')[0]
        before_sign = before.split(sign)[0]
        after = before.split(sign)[1]
        result = puns.split('=')[1]
        count = before[1::].count('-')
        if before.split(sign)[0] == '':
            before_sign = f'-{before.split(sign)[1]}'
            if count == 2:
                after = f'{before.split(sign)[3]}'
            else:
                after = before.split(sign)[2]
        if after == '':
            after = before.split(sign)[2]
        if (before_sign[0] == '0' or after[0] == '0') and result[0] != '0' and sign == '*':
            pass
        elif len(before_sign) > 1 and before_sign[0] == '0':
            pass
        elif j == '0' and (before_sign == '00' or after == '00' or result == '00'):
            pass
        else:
            if sign == '*':
                if int(before_sign) * int(after) == int(result):
                    return int(j)
            elif sign == '+':
                if int(before_sign) + int(after) == int(result):
                    return int(j)
            else:
                if count == 2:
                    if int(before_sign) + int(after) == int(result):
                        return int(j)
                if int(before_sign) - int(after) == int(result):
                    return int(j)

    return -1
