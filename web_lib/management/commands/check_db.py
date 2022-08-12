from django.core.management import BaseCommand

from web_lib.models import Book


class Command(BaseCommand):
    help = 'Проверяет БД'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', help='book id', type=int, nargs='+')

    def handle(self, *args, **options):
        book_ids = options['book_ids']

        for book_id in book_ids:
            try:
                Book.objects.get(pk=book_id)
                self.stdout.write(self.style.SUCCESS(f'Book with pk = {book_id} is found'))
            except Book.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Book with pk = {book_id} is not found'))
