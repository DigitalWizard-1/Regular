import csv
import re

def ModifityPhone(tele):
  result = re.sub(
    r"(\+7|8)?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\(]*([а-я.]*)\s*(\d{4})*[\s)]*",
    r"+7(\2)\3-\4-\5 \6\7", tele)
  return result.strip()

def Optimization(new_contact_list):
  n = 0
  for num in contacts_list:
    new_string = num
    tmp_fio_1 = re.findall(r"\w+", num[0])
    len_1 = len(tmp_fio_1)
    tmp_fio_2 = re.findall(r"\w+", num[1])
    len_2 = len(tmp_fio_2)
    new_string[0] = tmp_fio_1[0]
    if new_string[1] == '' and len_1 > 1:
      new_string[1] = tmp_fio_1[1]
    if new_string[2] == '' and len_1 > 2:
      new_string[2] = tmp_fio_1[2]
    elif new_string[2] == '' and len_2 > 1:
      new_string[2] = tmp_fio_2[1]
    if len_2 > 1:
      new_string[1] = tmp_fio_2[0]

    new_string[5] = ModifityPhone(num[5])

    flag = 0
    for id in range(len(new_contact_list)):
      if new_string[0] == new_contact_list[id][0]:
        flag += 1
        for id2 in range(7):
          if new_contact_list[id][id2] == '':
            new_contact_list[id][id2] = new_string[id2]
    if n == 0 or flag == 0:
      new_contact_list.append(new_string)
      n += 1

if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  # TODO 1: выполните пункты 1-3 ДЗ

  contact_list_new = []
  Optimization(contact_list_new)

  # TODO 2: сохраните получившиеся данные в другой файл

  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list_new)
