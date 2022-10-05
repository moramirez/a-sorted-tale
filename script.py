import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
  print(book['title'])
  print(ord("a"))
  print(ord(" "))
  print(ord("A"))
  print(ord("z"))
  print(ord("Z"))

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower'] 

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print(bookshelf_v2)

for book in bookshelf_v2:
  print(book['author_lower'])

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

long_bookshelf = utils.load_books('books_large.csv')

#print(long_bookshelf)
