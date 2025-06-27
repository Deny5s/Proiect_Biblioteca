# Smart Management of Books in a Virtual Library

The application will allow the management of a collection of books in a virtual library. The user can add, search, filter, sort, and save books to files. OOP will be used for modeling, and map, filter, reduce, and comprehensions for data processing. Decorators will be used for validation/logging, and exceptions for error handling.

1. OOP Modeling

  - Create the classes: Book, Author, and Library
  
  - Book: should include title, genre, year of publication, author, and rating

  - Author: should include first name, last name, and nationality
  
  - Library: manages a list of books

2. Book Add/Search/Delete Functionality

  - Methods for adding, deleting by title, and searching by author or title

3. Decorators

  - Create a decorator for logging actions to a file (log.txt)

  - Create a decorator for validating input data (e.g., rating between 1 and 10)

4. Using map

  - Display all book titles in uppercase using map

5. Using filter

  - Display all books published after the year 2000 and with a rating > 4

6. Using reduce

  - Calculate the average rating of the books in the library

7. Comprehension

  - Create a list of book titles written by authors of a specific nationality using list comprehension

8. Exception Handling

  - Use try-except blocks to handle file errors or invalid data

9 File Reading and Writing

  - Allow saving the library to a .json file and loading it when the application starts

10. Minimal CLI Interface (Menu)

  - A simple console menu that allows the user to interact with the application

BONUS:

1. Allow sorting books by multiple criteria (e.g., descending rating, then alphabetically by title)

2. Display statistics such as: total number of books, most popular genres, author with the most books
