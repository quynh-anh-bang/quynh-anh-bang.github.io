def get_FUV_email_class_code(email):
    result = 0
    at_index = email.index('@')

    if 'fulbright.edu.vn' in email:
        if '.' in email[:at_index] and '@student' in email:
            result = 1
        if ('.' in email[:at_index]) and ('@student' not in email):
            result = 2
        if ('.' not in email[:at_index]):
            result = 3
    else:
        result = 4
    print (email, result)
    return result

def get_vnd(input_money):
    if input_money[-3:] == 'VND':
        vnd_value = float(input_money[:-3])
    elif input_money[-3:] == 'CAD':
        vnd_value = float(input_money[:-3]) * 18063
    elif input_money[-3:] == 'USD':
        vnd_value = float(input_money[:-3]) * 24372
    else:
        vnd_value = 0.0
    print(input_money, vnd_value)
    return vnd_value

get_FUV_email_class_code('phuong.le.220041@student.fulbright.edu.vn')
get_FUV_email_class_code('linh.huynh@fulbright.edu.vn')
get_vnd('37.6CAD')
get_vnd('abc')