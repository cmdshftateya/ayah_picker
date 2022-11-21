#! /usr/bin/env python3

def random_ayah_picker():
    import random
    import webbrowser

    # create a data structure to put info that we will randomize from
    official_surahs_and_ayahs = []

    with open("SurahInfoSheet1.csv", "r") as surahinfo:
        # print(surahinfo.readlines())
        # loop through surah info csv document to strip information about surahs
        # index to second line in order to skip the header
        for x in surahinfo.readlines()[1:]:
            # print(x)
            # turn each line into a list so we can use index to parse through
            individual_info = x.split(",")
            # use index to get the surah order in quran
            surah_index = individual_info[0]
            # use index to get the number of ayahs in said surah
            surah_ayah_count = individual_info[2]
            # put those things into a structure for a tuple
            b = surah_index, surah_ayah_count
            # append them to the list as a tuple
            official_surahs_and_ayahs.append(tuple(b))

    # for x in official_surahs_and_ayahs:
    #     # print(x)
    ayahs_requested = int(input("How many ayahs do you want? "))
    
    i = 0
    while i < ayahs_requested:
        # pick a random tuple from the list
        surah = random.choice(official_surahs_and_ayahs)
        # print(surah)
        surah_number = surah[0]
        # pick a random ayah from the surah
        ayah_number = random.randint(1, int(surah[1]))

        # open it in the default browser
        print(f'http://quran.com/{surah_number}/{ayah_number}/')
        webbrowser.open(f'http://quran.com/{surah_number}/{ayah_number}/', new=2)
        i += 1
    
random_ayah_picker()