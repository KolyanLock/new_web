import uuid

# Create your models here.
from django.core import validators
from django.db.models import Model, UUIDField, CharField, PositiveSmallIntegerField, EmailField, TextField, \
    PositiveIntegerField, DateTimeField, ForeignKey, OneToOneField, CASCADE, ManyToManyField


class Author(Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']
        unique_together = ['name', 'age']

    TYPES = (
        ('a', 'foreign'),
        ('b', 'domestic'),
        ('c', 'other')
    )

    id = UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    name = CharField(
        verbose_name='Имя автора', max_length=200,
        validators=[validators.RegexValidator(regex='^.*ем$', message='Wrong')]
    )
    age = PositiveSmallIntegerField(verbose_name='Возраст автора')
    email = EmailField(verbose_name='Почта автора', null=True, blank=True)
    lit_typ = CharField(verbose_name='Тип литературы', choices=TYPES, default='a', max_length=1)

    def info(self):
        name = f'Name: {self.name}'
        age = f'Age : {self.age}'
        lit_type = f'Type: {self.get_lit_typ_display()}'
        return [name, age, lit_type]

    def __str__(self):
        return self.name


class Book(Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        get_latest_by = 'published'

    title = CharField(max_length=200)
    description = TextField()
    page_num = PositiveIntegerField()
    published = DateTimeField(auto_now_add=True)
    author = ForeignKey(Author, on_delete=CASCADE)

    def __str__(self):
        return self.title


class Review(Model):
    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

    author = CharField(max_length=200)
    text = TextField()
    published = DateTimeField(auto_now_add=True)
    book = OneToOneField(Book, on_delete=CASCADE)

    def __str__(self):
        return self.author


class Product(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Store(Model):
    name = CharField(max_length=200)
    products = ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.name
