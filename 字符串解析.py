import json


def character_parsing(long_text):
    """
    解析字符串
    :param long_text: 字符串
    :return: 字典数据表
    """
    flag = False
    data_dict = dict(sub_fund=[])
    temp_list = list()
    temp_dict = dict()
    text_list = long_text.strip().split('\n')
    for index in range(len(text_list)):

        if index == 0:
            data_dict['name'] = text_list[index]
            continue

        if index == 1:
            data_dict['lei'] = text_list[index]
            continue

        if 'FUND' in text_list[index] and '.' in text_list[index] and isinstance(int(text_list[index].split('.')[0]), int):
            if flag:
                temp_dict['isin'] = temp_list
                data_dict['sub_fund'].append(temp_dict)
                flag = False
                temp_list = []
                temp_dict = {}
            temp_dict['title'] = text_list[index].split('.')[1].strip()
        else:
            temp_list.append(text_list[index].strip())
            flag = True

    return data_dict


if __name__ == '__main__':
    long_text = \
    """Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
    dict_data = character_parsing(long_text)
    print(json.dumps(dict_data, indent=4, ensure_ascii=False))
