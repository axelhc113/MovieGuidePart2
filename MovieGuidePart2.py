# Axel Hidrovo Cordova
# CIS261
# Lab title: Movie Guide Part 2

from pathlib import Path


FILENAME = "movies.txt"


def ensure_movies_file():
    path = Path(FILENAME)
    if not path.exists():
        default_movies = [
            "Cat on a Hot Tin Roof",
            "On the Waterfront",
            "Monty Python and the Holy Grail",
        ]
        path.write_text("\n".join(default_movies) + "\n", encoding="utf-8")


def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list  - List all movies")
    print("add   - Add a movie")
    print("del   - Delete a movie")
    print("exit  - Exit program")
    print()


def load_movies():
    movies = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            title = line.strip()
            if title:
                movies.append(title)
    return movies


def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for title in movies:
            file.write(title + "\n")


def list_movies(movies):
    for i, title in enumerate(movies, start=1):
        print(f"{i}. {title}")
    print()


def add_movie(movies):
    title = input("Movie: ").strip()
    if title:
        movies.append(title)
        save_movies(movies)
        print(f"{title} was added.")
        print()
        list_movies(movies)


def delete_movie(movies):
    user_input = input("Number: ").strip()
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid movie number.")
        print()
        return

    if number < 1 or number > len(movies):
        print("Invalid movie number.")
        print()
        return

    title = movies.pop(number - 1)
    save_movies(movies)
    print(f"{title} was deleted.")
    print()
    list_movies(movies)


def main():
    ensure_movies_file()
    movies = load_movies()

    display_menu()
    while True:
        command = input("Command: ").strip().lower()

        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            input("Press any key to continue . . .")
            break
    else:
        print("Not a valid command. Please try again.")
        print()

if __name__ == "__main__":
    main()