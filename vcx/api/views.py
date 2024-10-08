# views.py
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer
import json


# Class-based view for listing and creating books
class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        name = request.GET.get("nome")
        edition = request.GET.get("edição")
        year_published = request.GET.get("ano de publicação")
        authorsid = request.GET.get("autores")
        if name:
            books = books.filter(name__icontains=name)
        if edition:
            books = books.filter(edition__icontains=edition)
        if year_published:
            books = books.filter(year_published=year_published)
        if authorsid:
            books = books.filter(authors__id=authorsid)

        if not books.exists():
            return JsonResponse({"message": "No books found"}, status=404)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):  # por que fizeram em portugues?? com espaço e ç
        try:
            # Load the data from request.body
            data = json.loads(request.body)

            # pego os dados do post em portugues, transformo em ingles, e passo pro serializer
            mapped_data = {
                "name": data.get("nome"),
                "edition": data.get("edição"),
                "year_published": data.get("ano de publicação"),
                "authors": data.get("autores"),
            }

            # Serialize the data
            serializer = BookSerializer(data=mapped_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


# Class-based view for retrieving a book by its ID
class BookByIdView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        book = get_object_or_404(Book, id=id)
        data = json.loads(request.body)
        mapped_data = {
            "name": data.get("nome"),
            "edition": data.get("edição"),
            "year_published": data.get("ano de publicação"),
            "authors": data.get("autores"),
        }

        serializer = BookSerializer(book, data=mapped_data)  # atualizando o atual
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # deleta livro especifico
    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return JsonResponse({"message": "Book deleted successfully"}, status=200)


# ver todos os autores / adicionar
class AuthorsView(View):
    def get(self, request):
        name = request.GET.get("nome")
        authors = Author.objects.all()
        if name:  # se tiver nome nos paramentros, filtra
            authors = authors.filter(name__icontains=name)
            serializer = AuthorSerializer(authors, many=True)
            return JsonResponse(serializer.data, safe=False)
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        # pego os dados do post em portugues, transformo em ingles, e passo pro serializer
        mapped_data = {
            "name": data.get("nome"),
        }

        serializer = AuthorSerializer(data=mapped_data)
        if serializer.is_valid():  # se tiver todos os campos no formato correto
            serializer.save()  # salva
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# classe para retornar todos os livros feitos por um author
class AuthorBooksView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)  # try catch basicamente
        books_made_by_author = author.books.all()
        serializer = BookSerializer(books_made_by_author, many=True)
        return JsonResponse(serializer.data, safe=False)


# mostra informacao pessoal do autor
class AuthorByIdView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    def delete(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        for book in author.books.all():
            if book.authors.count() == 1:  # verfica se autor eh o unico
                return JsonResponse(
                    {
                        "response": f"You need to delete or update the book with id {book.id} "
                        "first, as this author is the only one in it."
                    },
                    status=400,  # Use a 400 status for client error
                )

        author.delete()
        return JsonResponse({"status": "Author deleted"}, status=200)

    def put(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        data = json.loads(request.body)
        mapped_data = {
            "name": data.get("nome"),
        }
        serializer = AuthorSerializer(author, data=mapped_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
