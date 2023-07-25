from django.test import TestCase, SimpleTestCase
from .models import Catalog
from django.urls import reverse
from django.urls.base import resolve
from .views import home
from .forms import AddBookForm


class CatalogueViewTests(TestCase):

    def test_book_list_view(self):
        ''' Тестовый метод, позволяющий показать, что созданные нами книги корректно отображаются в нашем шаблоне. '''
        Book_1 = Catalog.objects.create(
            title='Django for Beginners (2018)',
            ISBN='978-1-60309-0',
            author='John Doe',
            price=9.99,
            availability='true'
        )

        Book_2 = Catalog.objects.create(
            title='Django for Professionals (2020)',
            ISBN='978-1-60309-3',
            author='Mary Doe',
            price=11.99,
            availability='false'
        )

        response = self.client.get(reverse('home'))

        self.assertIn('Django for Professionals (2020)', response.content.decode())
        self.assertIn('Samuel Torimiro', response.content.decode())
        self.assertIn('978-1-60309-3', response.content.decode())

class CatalogTemplateTests(TestCase):

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'E-library Application')

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hello World')


class CatalogFormTests(TestCase):
    "Test the form"

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_book_form(self):
        form = self.response.context.get('add_book_form')
        self.assertIsInstance(form, AddBookForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('add_book_form')
        self.assertIn('class="form-control"', form.as_p())

    def test_book_form_validation_for_blank_items(self):
        add_book_form = AddBookForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability': ''}
        )
        self.assertFalse(add_book_form.is_valid())


class ElibraryURLsTest(TestCase):
    "Test the catalog URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resloves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home)


class CatalogModelTests(TestCase):
    "Test the catalog model"

    def setUp(self):
        self.book = Catalog(
            title='First Django Book',
            ISBN='978-3-16-148410-0',
            author='Ilya Perminov',
            price='9.99',
            availability='True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalog)

    def test_str_representation(self):
        self.assertEquals(str(self.book), "First Django Book")

    def test_saving_and_retrieving_book(self):
        first_book = Catalog()
        first_book.title = 'First Django Book'
        first_book.ISBN = '978-3-16-148410-0'
        first_book.author = 'Ilya Perminov'
        first_book.price = '9.99'
        first_book.availability = 'True'
        first_book.save()

        second_book = Catalog()
        second_book.title = 'Second Django Book'
        second_book.ISBN = '978-3-16-148410-1'
        second_book.author = 'Dmitry Seleznev'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()

        saved_books = Catalog.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'First Django Book')
        self.assertEqual(second_saved_book.author, 'Dmitry Seleznev')
