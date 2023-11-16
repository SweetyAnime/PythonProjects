import random

names_3_star = ["Amber Catalyst", "Black Tassel", "Bloodtainted Greatsword",
    "Cool Steel", "Dark Iron Sword", "Debate Club", "Ebony Bow",
    "Emerald Orb", "Ferrous Shadow", "Fillet Blade", "Halberd",
    "Harbinger of Dawn", "Magic Guide", "Messenger", "Otherworldly Story",
    "Quartz", "Raven Bow", "Recurve Bow", "Sharpshooter's Oath",
    "Skyrider Greatsword", "Skyrider Sword", "Slingshot",
    "Thrilling Tales of Dragon Slayers", "Traveler's Handy Sword",
    "Twin Nephrite", "White Iron Greatsword", "White Tassel"]

names_4_star = ["Amber", "Barbara", "Beidou", "Bennett", "Candace", "Charlotte",
    "Chongyun", "Collei", "Diona", "Dori", "Faruzan", "Fischl",
    "Freminet", "Gorou", "Kaeya", "Kaveh", "Kirara", "Kujou Sara",
    "Kuki Shinobu", "Layla", "Lisa", "Lynette", "Mika", "Ningguang",
    "Noelle", "Razor", "Rosaria", "Sayu", "Shikanoin Heizou", "Sucrose",
    "Thoma", "Xiangling", "Xingqiu", "Xinyan", "Yanfei", "Yaoyao", "Yun Jin"]
    
good_5_star = ["Albedo", "Alhaitham", "Aloy", "Ayaka", "Ayato", "Baizhu", "Childe",
    "Cyno", "Eula", "Furina", "Ganyu", "Hu Tao", "Itto", "Kazuha", "Klee",
    "Kokomi", "Lyney", "Nahida", "Neuvillette", "Nilou", "Raiden Shogun",
    "Shenhe", "Venti", "Wanderer", "Wriothesley", "Xiao", "Yae Miko",
    "Yelan", "Yoimiya", "Zhongli"]

bad_5_star = ["Dehya", "Diluc", "Jean", "Keqing", "Mona", "Qiqi", "Tighnari"]

def spin_and_print(spin_count, guarantee_5_star_count, last_5_star_category, used_names, printed_4_star, coins):
    result = ""

    if guarantee_5_star_count > 0:
        if last_5_star_category == "good":
            result = f"5-star (Good): {random.choice(good_5_star)}"
        else:
            result = f"5-star (Bad): {random.choice(bad_5_star)}"

        print(f"Spin {spin_count}: {result}")
        guarantee_5_star_count -= 1
        if guarantee_5_star_count == 0:
            print("Congratulations! You got a 5-star! Gacha reset.")
            return 0, 0, None, used_names, False, coins  # Reset spin count, guarantee count, and last category
        else:
            print(f"Congratulations! You got a 5-star ({last_5_star_category} category)!")
            return spin_count + 1, guarantee_5_star_count, last_5_star_category, used_names, printed_4_star, coins
    elif spin_count % 10 == 0 and spin_count >= 50 and spin_count <= 90:
        if random.randint(1, 2) == 1:
            result = f"5-star (Good): {random.choice(good_5_star)}"
            last_5_star_category = "good"
        else:
            result = f"5-star (Bad): {random.choice(bad_5_star)}"
            last_5_star_category = "bad"

        print(f"Spin {spin_count}: {result}")
        guarantee_5_star_count = 1  # Set guarantee count for the next spin
    elif spin_count % 10 == 0:
        result = f"4-star (Epic): {random.choice(names_4_star)}"
        if not printed_4_star:
            print(f"Spin {spin_count}: {result}")
            printed_4_star = True  # Set flag to indicate that 4-star is printed
        else:
            print(f"Spin {spin_count}: {result} (Already printed 4-star for this set of wishes)")
    else:
        star = random.choices([3, 4], weights=[90, 10])[0]
        if star == 3:
            name = random.choice(names_3_star)
            while name in used_names:
                name = random.choice(names_3_star)
            used_names.append(name)
            result = f"{star}-star: {name}"
        else:
            name = random.choice(names_4_star)
            while name in used_names:
                name = random.choice(names_4_star)
            used_names.append(name)
            result = f"{star}-star: {name}"

    print(f"Spin {spin_count}: {result}")
    print(f"Current Coins: {coins}")
    return spin_count + 1, guarantee_5_star_count, last_5_star_category, used_names, printed_4_star, coins

def guess_head_or_tail(coins):
    print("\nGuess the outcome: Head or Tail?")
    user_guess = input("Enter your choice: ").lower()

    if user_guess in ["head", "tail"]:
        coin_outcome = random.choice(["head", "tail"])

        print(f"The coin landed on: {coin_outcome}")

        if user_guess == coin_outcome:
            print("Congratulations! You guessed it right!")
            coins += 160  # Earn 160 coins for winning the game
        else:
            print("Sorry, better luck next time!")

        print(f"Current Coins: {coins}")
    else:
        print("Invalid choice. Please enter 'head' or 'tail'.")

    return coins

def continue_head_or_tail(coins):
    while True:
        print("\nDo you want to continue the Head or Tail game?")
        print("1. Yes")
        print("2. No and go back to Gacha game")
        choice = input("Enter your choice: ")

        if choice == "1":
            coins = guess_head_or_tail(coins)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    return coins
    
def gacha_game():
    coins = 0
    spin_count = 1
    guarantee_5_star_count = 0  # Initialize guarantee_5_star_count
    last_5_star_category = None
    used_names = []
    printed_4_star = False

    while True:
        print("\nChoose an option:")
        print("1. Spin once")
        print("2. Wish 10 times")
        print("3. Guess Head or Tail")
        print("0. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == "0":
            break
        elif user_choice == "1" and coins >= 160:
            coins -= 160
            print("You made a wish! Good luck!")
            spin_count, guarantee_5_star_count, last_5_star_category, used_names, printed_4_star, coins = spin_and_print(
                spin_count, guarantee_5_star_count, last_5_star_category, used_names, printed_4_star, coins
            )
        elif user_choice == "1" and coins < 160:
            print("Not enough coins. Earn more by winning the Gacha game!")
        elif user_choice == "2" and coins >= 1600:
            coins -= 1600
            print("You made 10 wishes! Good luck!")
            # Add the code to make 10 wishes or perform the corresponding action
        elif user_choice == "2" and coins < 1600:
            print("Not enough coins. Earn more by winning the Gacha game!")
        elif user_choice == "3":
            coins = continue_head_or_tail(coins)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    gacha_game()
    