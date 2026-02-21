from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

zap_kniga = []

for znach in contacts_list:
    fio = znach[0]
    if znach[1] != "":
        fio = fio + " " + znach[1]
    if znach[2] != "":
        fio = fio + " " + znach[2]
    fio_list = fio.split(" ")
    if len(fio_list) == 2:
        fio_list.append('')
    fio_list.append(znach[3])
    if znach[4] != "":
        fio_list.append(znach[4])
    else:
        fio_list.append('')
    phone_pattern = r"(\+7|8)\s*[(]?(\d{3})[)]?\s*[-]?(\d{3})[-]?(\d{2})[-]?(\d{2})\s*[(]?[а-я.]?[а-я.]?[а-я.]?[а-я.]?\s*(\d{4})?[)]?"
    if znach[5].find('доб') != -1:
        replacement_pattern = r"+7(\2)\3-\4-\5 доб.\6"
    else:
        replacement_pattern = r"+7(\2)\3-\4-\5"
    cleaned_phones = re.sub(phone_pattern, replacement_pattern, znach[5])
    if znach[5] != "":
        fio_list.append(cleaned_phones)
    else:
        fio_list.append('')
    print(cleaned_phones)
    if znach[6] != "":
        fio_list.append(znach[6])
    else:
        fio_list.append('')
    print(fio_list)
    if len(zap_kniga) == 0:
        zap_kniga.append(fio_list)
    else:
        count = 0
        for id in zap_kniga:
            #print(id)
            #print(zap_kniga[count][0])
            if id[0] == fio_list[0] and id[1] == fio_list[1]:
                if id[4] == '':
                    zap_kniga[count][4] = fio_list[4]
                if id[5] == '':
                    zap_kniga[count][5] = fio_list[5]
                if id[6] == '':
                    zap_kniga[count][6] = fio_list[6]
                break
            count += 1
            if len(zap_kniga) ==  count:
                zap_kniga.append(fio_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(zap_kniga)