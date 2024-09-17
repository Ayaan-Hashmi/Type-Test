import time
import random
def get_random_sentence():
    sentences = [
        "In the vast expanse of the universe, galaxies collide and stars are born, creating breathtaking celestial tapestries.",
        "As the sun sets on the horizon, casting a warm glow over the tranquil ocean, the world is painted in hues of orange and pink.",
        "The intricate dance of nature unfolds in the heart of the rainforest, where diverse species coexist in a delicate balance of life.",
        "Exploring the depths of the ocean reveals a mesmerizing world filled with mysterious creatures and stunning underwater landscapes.",
        "On the journey of self-discovery, one must navigate the twists and turns of introspection to unlock the secrets of personal growth.",
        "Amidst the hustle and bustle of city life, there lies a hidden oasis of calm, where time seems to slow down, inviting peaceful reflection.",
        "The symphony of laughter and joy echoes through the playground as children embrace the simple pleasures of friendship and play.",
        "In the realm of technology, innovation prop"
    ]
    return random.choice(sentences)
def calculate_typing_speed(start_time, end_time, typed_text):
    words_per_minute = (len(typed_text.split()) / (end_time - start_time)) * 60
    return words_per_minute

def calculate_accuracy(original_text, typed_text):
    correct_words = sum(a == b for a, b in zip(original_text.split(), typed_text.split()))
    accuracy = (correct_words / len(original_text.split())) * 100
    return accuracy

def display_results(start_time, end_time, original_text, typed_text):
    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(original_text, typed_text)
    print("\nTyping Speed: {:.2f} words per minute".format(typing_speed))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("")

def typing_test():
    sentence = get_random_sentence()
    print("Type the following sentence:")
    print("{}".format(sentence))
    input("\nPress Enter when you are ready to start typing...")
    start_time = time.time()
    typed_text = input("Type the sentence here: ")
    end_time = time.time()
    display_results(start_time, end_time, sentence, typed_text)

def custom_typing_test():
    custom_sentence = input("\nEnter a sentence for typing test: ")
    print("\nType the following sentence:")
    print("{}".format(custom_sentence))
    input("\nPress Enter when you are ready to start typing...")
    start_time = time.time()
    typed_text = input("Type the sentence here: ")
    end_time = time.time()
    display_results(start_time, end_time, custom_sentence, typed_text)
if __name__ == "__main__":
    print("\nWelcome to the Type Test!")
    while True:
        print("")
        print("1. Typing Test (Random Sentence)")
        print("2. Custom Typing Test")
        print("3. Exit")
        print("")
        choice = input("Choose an option (1, 2, or 3): ")
        if choice == "1":
            typing_test()
        elif choice == "2":
            custom_typing_test()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        another_test = input("Wanna do another test? (Yes/No): ").lower()
        if another_test != "yes" or "y":
            print("Exiting the program. Goodbye!")
            break
