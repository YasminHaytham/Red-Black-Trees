from RedBlackTree import RedBlackTree
import os

# Colors
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

if not os.path.exists("dictionary.txt"):
    with open("dictionary.txt", "w", encoding="utf-8") as f:
        f.write("")

tree = RedBlackTree()
try:
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                tree.insert(word)
except UnicodeDecodeError:
    with open("dictionary.txt", "w", encoding="utf-8") as f:
        f.write("")
    print(RED + "dictionary.txt was corrupted and has been reset." + RESET)

print(GREEN + "Dictionary loaded!" + RESET)
while True:
    print(CYAN + "\n1. Insert a Word")
    print("2. Search a Word")
    print("3. Print Stats")
    print("4. Exit" + RESET)

    choice = input("Choose Wisely: ")

    if choice == "1":
        word = input("Enter the word: ").strip().lower()
        if tree.SearchWord(word):
            print(RED + "ERROR: Word already in the dictionary!" + RESET)
        else:
            tree.insert(word)
            with open("dictionary.txt", "a", encoding="utf-8") as f:
                f.write(word + "\n")
            print(GREEN + f"'{word}' inserted." + RESET)
            print(YELLOW + "Size:"         + RESET, tree.TreeSize(tree.root))
            print(YELLOW + "Height:"       + RESET, tree.TreeHight(tree.root))
            print(YELLOW + "Black-Height:" + RESET, tree.BlackHeight(tree.root))

    elif choice == "2":
        word = input("Enter the word: ").strip().lower()
        if tree.SearchWord(word):
            print(GREEN + "YES it's in the dictionary!" + RESET)
        else:
            print(RED + "NO it's not in the dictionary." + RESET)

    elif choice == "3":
        print(YELLOW + "Size:"         + RESET, tree.TreeSize(tree.root))
        print(YELLOW + "Height:"       + RESET, tree.TreeHight(tree.root))
        print(YELLOW + "Black-Height:" + RESET, tree.BlackHeight(tree.root))

    elif choice == "4":
        print(GREEN + "Dont come back!" + RESET)
        break
