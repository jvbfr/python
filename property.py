class Book:
    def __init__(self, book_id):
        self.book_id = book_id
        self._text = None

    @property
    def text(self):
        if self._text is None:
            print(f"Loading text for book {self.book_id} from file...")
            # Faz de conta q é uma tabela imensa
            self._text = f"Contents of file book_{self.book_id}.txt"
        return self._text


class Library:
    def __init__(self, number_of_books):
        self.books = [Book(book_id) for book_id in range(1, number_of_books + 1)] 

    def get_book_text_by_id(self, book_id):
        return self.books[book_id - 1].text


# Biblioteca com 1000 livros
library = Library(1000)

# Vai acessar apenas o texto do livro com id 5
book_text = library.get_book_text_by_id(5)

print(book_text)
