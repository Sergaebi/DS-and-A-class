import json

favorite_books = [
    {
        "name": "The Trial",
        "year": 1914,
        "author": "Franz Kafka"
    },

    {
        "name": "1985",
        "year": 1978,
        "author": "Anthony Burgess"
    },

    {
        "name": "The Man from Mars",
        "year": 1946,
        "author": "Stanislaw Lem"
    }
]


def bubble_sort_books(list_of_books):
    for iteration_number in range(len(list_of_books) - 1, 0, -1):
        for index in range(iteration_number):
            if list_of_books[index]["year"] > list_of_books[index + 1]["year"]:
                temporary = list_of_books[index]
                list_of_books[index] = list_of_books[index + 1]
                list_of_books[index + 1] = temporary


bubble_sort_books(favorite_books)
print(json.dumps(favorite_books, indent=1))
