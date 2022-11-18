#! /usr/bin/env python3

def random_ayah_picker():
    import random
    import webbrowser

    official_surahs_and_ayahs = []

    with open("/Users/abdulrahmanateya/Downloads/SurahInfoSheet1.csv", "r") as surahinfo:
        # print(surahinfo.readlines())
        for x in surahinfo.readlines():
            # print(x)
            b = list(x.split(","))[0], list(x.split(","))[2]
            official_surahs_and_ayahs.append(tuple(b))
    for x in official_surahs_and_ayahs:
        pass
        # print(x)
    ayahs_requested = int(input("How many ayahs do you want? "))
    
    i = 0
    while i < ayahs_requested:
        surah = random.choice(official_surahs_and_ayahs[1:])
        print(surah)
        i += 1
        surah_number = surah[0]
        ayah_number = random.randint(1, int(surah[1]))
        print(f'http://quran.com/{surah_number}/{ayah_number}/')
        webbrowser.open(f'http://quran.com/{surah_number}/{ayah_number}/', new=2)
    
random_ayah_picker()