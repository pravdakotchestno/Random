
#создание двух списков: с числами и с символами
listofletters = [chr(x) for x in range(32, 127)]
listofnums = [x for x in range(1, len(listofletters) + 1)]

#склейка этих списков в словарь
alf = dict(zip(listofnums, listofletters))

#создание перевернутого словаря, где ключи - значения, а значения - ключи
ralf = dict(zip(alf.values(), alf.keys()))

#функция для зашифровки одного символа
def encryptChar(position, char, key, mainkey):
    return (char + (position * key) + mainkey) % len(listofletters) + 1

#функция для расшифровки одного символа
def decryptChar(position, char, key, mainkey):
    return (char - (position * key) - mainkey - 2) % len(listofletters) + 1

#функция для зашифровки строки два раза
#строка шифруется, переворачивается и шифруется еще раз
def encryptString(str, key):
    str = encryptStringOnce(str, key)[:: -1]
    return encryptStringOnce(str, key)

#метод для двойной расшифровки строки
#строка расшифровывается, переворачивается и расшифровывается еще раз
def decryptString(str, key):
    str = decryptStringOnce(str, key)[:: -1]
    return decryptStringOnce(str, key)

#метод для зашифровки строки единожды
def encryptStringOnce(str, key):
    #инициализация ключа, который будет применятся ко всем символам в сообщении
    mainkey = key
    #переменная для зашифрованного сообщения
    result = ""
    #переменная, уменьшающаяся с каждой иттерацией цикла на 1
    # и изначальное значение которой равно длине соообщения (позиция с конца)
    pos = len(str)
    #цикл для обработки каждого символа
    for i in str:
        #проверка i на валидность
        validateChar(i)
        #зашифровка текущего символа в соответствии с его позицией,
        # текущего ключа и главного ключа
        i = encryptChar(pos, ralf[i], key, mainkey)

        #добавление зашифрованного символа в строку
        result = result + alf[i]
        #переопределение текущего ключа в соответствии с символами шифруемого текста от 0 до len(str)-pos+1
        # и его укорачивание путем нахождения остатка от деления на 65536
        key = sumAll( str[: len(str) - pos + 1 ] ) % 65536
        #уменьшение позиции на 1
        pos -= 1
    #возврат зашифрованного текста
    return result


#метод для расшифровки строки единожды
def decryptStringOnce(str, key):
    #инициализация ключа, который будет применятся ко всем символам в сообщении
    mainkey = key
    #переменная для расшифрованного сообщения
    result = ""
    #переменная, уменьшающаяся с каждой иттерацией цикла на 1
    # и изначальное значение которой равно длине соообщения (позиция с конца)
    pos = len(str)
    #цикл для обработки каждого символа
    for i in str:
        #проверка i на валидность
        validateChar(i)
        #расшифровка текущего символа в соответствии с его позицией,
        # текущего ключа и главного ключа
        i = decryptChar(pos, ralf[i], key, mainkey)
        #добавление зашифрованного символа в строку
        result = result + alf[i]

        #переопределение текущего ключа в соответствии с символами расшифруемого текста от 0 до len(str)-pos+1
        # и его укорачивание путем нахождения остатка от деления на 65536
        key = sumAll(result) % 65536
        #уменьшение позиции на 1
        pos -= 1
    #возврат расшифрованного текста
    return result


#проверяет, есть ли символ в шифроалфавите
def validateChar(char):
    if char not in listofletters:
        throwError("message contains unsupported chars");raise SystemExit

#метод для печати ошибок в консоль
def throwError(errorMessage):
    print("Error:",errorMessage,"!")

#метод для суммации кодов всех букв в строке
def sumAll(str):
    sum = 0
    for i in str:
        sum += ralf[i]
    return sum

# главный метод
def main():
    #ввод режима
    mode = input("Select mode [E,D]\n>").upper()
    #обработка правильности режима
    if mode not in ('E', 'D'):
        throwError("unknown mode"); raise SystemExit
    #ввод сообщения
    str = input("Enter your message:\n>")
    #ввод ключа
    key = int(input("Enter your key:\n>"))



    #шифровка или расшифровка в соответствии с режимом
    finalmessage = ""
    if mode == 'E':
        finalmessage = encryptString(str,key)
    else:
        finalmessage = decryptString(str,key)
    #вывод финального сообщения
    print("--------------Final message--------------\n")
    print(finalmessage)
    print("\n-----------End of final message----------")


if __name__ == __main__:
    main()
