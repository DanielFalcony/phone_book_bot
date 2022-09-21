# добавление фильтра матерных слов из cenz.txt (слова в исходном файле добавляются через \n)
import json

words_list = []

with open('cenz.txt', encoding='utf-8') as file:
    for string in file:
        word = string.lower().split('\n')[0]
        if word != '':
            words_list.append(word)

with open('cenz.json', 'w', encoding='utf-8') as file_json:
    json.dump(words_list, file_json)
