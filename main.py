import random
import networkx as nx
import matplotlib.pyplot as plt

def choose_word():
    words = ["klavye", "python", "program", "balina", "gitar"]
    return random.choice(words)

def create_graph(word):
    G = nx.DiGraph()

    for i in range(len(word) + 1):
        G.add_node(i, label=word[:i])

    for node in G.nodes():
        for letter in set(word):
            if letter not in G.nodes[node]['label']:
                next_label = G.nodes[node]['label'] + letter
                next_node = word.find(next_label) + 1
                G.add_edge(node, next_node, label=letter)

    return G

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def draw_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    labels = {node: graph.nodes[node]['label'] for node in graph.nodes()}
    nx.draw(graph, pos, labels=labels, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray')
    plt.show()

def hangman():
    while True:
        word_to_guess = choose_word()
        graph = create_graph(word_to_guess)
        guessed_letters = set()
        incorrect_guesses = 0
        max_incorrect_guesses = 6

        print("Welcome to Hangman!")

        while incorrect_guesses < max_incorrect_guesses:
            print("\nCurrent Word:", display_word(word_to_guess, guessed_letters))
            print("Guessed Letters:", ", ".join(guessed_letters))
            print("Incorrect Guesses:", incorrect_guesses)

            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            if guess not in word_to_guess:
                incorrect_guesses += 1
                print("Incorrect guess. Attempts left:", max_incorrect_guesses - incorrect_guesses)
            else:
                print("Good guess!")

            draw_graph(graph)

            if "_" not in display_word(word_to_guess, guessed_letters):
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break

        if "_" in display_word(word_to_guess, guessed_letters):
            print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
