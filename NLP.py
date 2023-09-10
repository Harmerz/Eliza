#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import re

rules = [
        ['(.*)h[ea]ll*o(.*)',
        ['Hallo Hai, disini dengan bot milik Haikal Hilmi']],
        ['(.*)siapa [namamu|kamu](.*)',
            ['Saya adalah bot asisten milik Haikal dengan nama BEBHUT (Bot Eliza Buatan Haikal Untuk Tugas)',
            'Saya adalah BEBHUT']
        ],
        [
            '(.*)apa itu [Bb][Ee][Bb][Hh][Uu][Tt](.*)',
            ['BEBHUT adalah akronim dari Bot Eliza Buatan Haikal Untuk Tugas']
        ],
         [
           '(.*)nama[ saya|ku](.*)',
           ['Halo, untuk saat ini saya belum bisa mengenal anda',
            'Senang telah mengenal anda',
            'Untuk sekarang itu sulit untuk diingat',
            'Nama yang bagus, serta terlalu bagus untuk disimpan di memory']
         ],
        [
           '(.*)nama[ saya|ku] BEBHUT(.*)',
           ['Nama kita ternyata mirip ya', 'Namamu keren juga']
         ],
        [
            '(.*)[Bb][Ee][Bb][Hh][Uu][Tt](.*)',
            [
                'Hallo itu saya',
                'Itu saya dengan kepanjangan Bot Eliza Buatan Haikal Untuk Tugas',
            ]
        ],
        ['(.*)so+r+y+(.*)|(.*)maa+f(.*)',
        ["Tolong jangan meminta maaf kepada saya",
         'Jangan meminta maaf kepada Bot',
         'Kenapa kamu meminta maaf?'
         ]],
             ['(.*)kabarmu(.*)',
        ["Sebagai program saya merasa baik-baik saja",
         'Baik, bagaimana denganmu?',
         'Aku merasa enakan'
         ]],
        [
            '(.*)dibuat|tujuan(.*)',
            ['Tujuan aku dibuat untuk memenuhi Tugas NLP', 'Tujuan aku dibuat untuk Tugas ELIZA']
        ],
        [
            '(.*)haikal(.*)',
            ['Haikal itu pemilik saya dengan NIU 482625',
             'Haikal orang yang telah membuat saya dengan NIU 482625',
             'Pemilik NIM 21/482625/TK/53328']
        ],
        [
            '(.*)siapa (.*)',
            ['Saya tidak tahu']
        ],
        [
            "quit",
            ['BYE BYE!!']
        ],
        [
            "(.*)cuaca(.*)",
            ["Mungkin cuaca besok cerah", "Mohon maaf saya tidak tau mengenai cuaca", "Apa kamu bisa memberitahuku?"]
        ],
        [
            "(.*)kamu lakukan(.*)",
            ["Saya bisa menjawab pertanyaan anda", "Halo ada apa?"],
        ],

        ['(.*)',
        ['Menarik ya',
         'Mohon maaf saya belum paham',
         'Tidak ada di database',
         'Lanjutkan coba',
         '\\2']]]

grammar = {
    'saya': 'anda',
    'aku': 'kamu',
    'kami': 'kita',
    }


def correction(word):
    character = word.lower().split()
    for (i, j) in enumerate(character):
        if j in grammar:
            character[i] = grammar[j]
    return ' '.join(character)


def test(sentence):
    for (pattern, message) in rules:
        match = re.match(pattern, sentence.rstrip('.!'))
        if match:
            response = random.choice(message)
            temp = ' ' + correction(match.group())
            response2 = re.sub(r"\\2", temp, response)
            return response2
    recall = random.choice(random.choice([r[1] for r in rules]))
    return recall
    
while True:
  sentence =input("You: ")
  print("BEBHUT: " + test(sentence.lower()))
  if sentence == "quit":
        break