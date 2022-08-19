import sys, random
def main():

    print("Welcome to the Nogizaka Member Alias Generator.'\n")


    names =  ["Akimoto", "Saito", "Higuchi", "Wada", "Hoshino", "Ikuta", "Takayama",
    "Matsumura", "Shiraishi", "Nakada", "Inoue", "Sakurai", "Saito", "Eto", "Nishino", "Kawago",
    "Nojo", "Saito", "Wakatsuki", "Ikoma", "Kawamura", "Nakamoto", "Ito", "Hashimoto", "Fukagawa",
    "Nagashima", "Hatanaka", "Yamato", "Ito", "Ichiki", "Miyazawa", "Kashiwa", "Ando", "Iwase",
    "Suzuki", "Yamazaki", "Kitano", "Shinnuchi", "Terada", "Watanabe","Ito", "Hori", "Sasaki", "Ito",
    "Sagara", "Yonetoku", "Yada", "Nishikawa", "Ito", "Iwamoto", "Umezawa", "Kubo", "Sakaguchi",
    "Sato", "Nakamura", "Mukai", "Yamashita", "Yoshida", "Yoda", "Ozono", "Endo", "Kaki",
    "Kakehashi", "Kanagawa", "Kitagawa", "Kuromi", "Satou", "Shibata", "Seimiya", "Tamura",
    "Tsutsui", "Hayakawa", "Hayashi", "Matsuo", "Yakubo", "Yumiki", "Matsui", "Ioki", "Ikeda",
    "Ichinose", "Inoue", "Okamoto", "Ogawa", "Okuta", "Kawasaki", "Sugawara", "Tomisato", "Nakanishi"]

    lastnames = ["Manatsu", "Asuka", "Hina", "Maaya", "Minami", "Erika", "Kazumi",
    "Sayuri", "Mai", "Kana", "Sayuri", "Reika", "Yuri", "Misa", "Nanase", "Hina",
    "Ami", "Chiharu", "Yumi", "Rina", "Mahiro", "Himeka", "Marika", "Nanami", "Mai",
    "Seira", "Seira", "Rina", "Nene", "Rena", "Seira", "Yukina", "Mikumo", "Yumiko",
    "Ayane", "Rena", "Hinako", "Mai", "Ranze", "Miria", "Junna", "Miona", "Kotoko", "Karin",
    "Iori", "Kyouka", "Risako", "Nanami", "Riria", "Renka", "Minami", "Shiori", "Tamami",
    "Kaede", "Reno", "Hazuki", "Mizuki", "Ayano-Christie", "Yuki", "Momoko", "Sakura", "Haruka",
    "Sayaka", "Saya", "Yuri", "Haruka", "Rika", "Yuna", "Rei", "Mayu",
    "Ayame", "Seira", "Runa", "Miyu", "Mio", "Nao", "Rena", "Mao", "Teresa",
    "Miku", "Nagi", "Hina", "Aya", "Iroha", "Sakura", "Satsuki", "Nao", "Aruno"]

    middlename = ('Baby Oil', 'Bad News', 'Big Burps', "Bill Beenie­Weenie",
    "Bob Stinkbug", 'Bowel Noises', 'Boxelder', "Bud Lite",
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
    'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
    'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
    'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
    'Huggy', 'Ignatious', 'Jimbo', "Joe Pottin Soil", 'Johnny',
    'Lemongrass', 'Lil Debil', 'Longbranch', 'Lunch Money',
    'Mergatroid', 'Mr Peabody', 'Oil­Can', 'Oinks', 'Old Scratch',
    'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
    "The Squirts", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
    'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
    'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
    "Jazz Hands", 'Worms', 'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
    'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
    'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
    'Hootkins', 'Jefferson', 'Jenkins', 'Jingley­Schmidt', 'Johnson',
    'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
    'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
    'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
    'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
    'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
    'Stevens', 'Stroganoff', 'Sugar­Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
    'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
    'Woolysocks')

    while True:
        random_seed = random.randint(1,87)
        random_tuple = random.choice(middlename)
        print("\n\n")
        print(f"{names[random_seed]} '{(random_tuple)}' {lastnames[random_seed]}", file = sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break
        input("\nPress Enter to exit.")

if __name__ == "__main__":
    
    main()