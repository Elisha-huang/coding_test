import itertools

dic1 = {
    0: [None], 1: [None], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
    }

while True:
    input_str = input("Input:")

    # 去掉中括号
    str1 = input_str[1:-1]

    if str1 == '0' or str1 == '1':
        print('0 or 1 do not map any letter!')
        print('')

        # 判断是否继续输入列表
        con = input('continue or quit:(y/n)')
        if con == 'y' or con == 'Y':
            pass
        elif con == 'n' or con == 'N':
            break
        else:
            print('please input y or n')

    elif '1' in str1 or '0' in str1:
        print('0 or 1 do not map any letter!')
        print('')

        # 判断是否继续输入列表
        con = input('continue or quit:(y/n)')
        if con == 'y' or con == 'Y':
            pass
        elif con == 'n' or con == 'N':
            break
        else:
            print('please input y or n')
            continue

    else:
        # list_digit 用与将输入的数字转换为一个列表
        list_digit = str1.split(',')

        # 将列表的元素转换为整型
        list_digit = [int(list_digit[i]) for i in range(len(list_digit))]

        # 将数字对应的字母放进列表内
        list_map = []
        for j in list_digit:
            list_map.append(dic1[j])

        # 判断用户输入了几个数字，并进行组合
        num = len(list_map)
        
        if num == 1:
            result = list_map[0]
        else:
            def value(number):

                new_list = []
                for n in range(number):
                    r = list_map[n]
                    new_list.append(r)

                for result in new_list:
                    yield result

            r = value(num)
            result =  itertools.product(*r)

        # 遍历组合并打印
        str_total = ''

        for i in result:
            str2 = "".join(i)
            str_total += str2 + ' '
            
        print('output:', str_total)
        print('')

        # 判断是否继续输入列表
        con = input('continue or quit:(y/n)')
        if con == 'y' or con == 'Y':
            pass
        elif con == 'n' or con == 'N':
            break
        else:
            print('please input y or n')
