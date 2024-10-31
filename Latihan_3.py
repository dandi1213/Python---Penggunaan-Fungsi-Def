# (222443015) M Dandi Al Idrus 2AEC

import random

salam = ["Selamat datang di XL Center", "Wilujeng sumping di XL Center", "Welcome to XL Center"]
keywords = ["pulsa", "internet"]
response = ['Sisa pulsa anda Rp.15.000', 'Anda memiliki paket data sebesar 500GB']

print("====================Chatbot=========================")
print(random.choice(salam))

while True:
    user = input('Ketik apa yang ingin anda ketahui: ').lower()

    keyword_found = False

    for index in range(len(keywords)):
        if keywords[index] in user:
            print('Bot XL: ' + response[index])
            keyword_found = True

    if not keyword_found:
        print('Maaf, saya tidak mengerti pertanyaan Anda atau informasi tersebut tidak tersedia.')

    another_question = input('Apakah ada yang ingin kamu tanyakan kembali? (ya/tidak): ').lower()
    if another_question != 'ya':
        break
