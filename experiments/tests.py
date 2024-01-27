from unittest.mock import patch, MagicMock
from django.test import TestCase, Client
from django.urls import reverse
from mongo_db_connection import close_connection
from bson import ObjectId  # For mocking ObjectID
from django.contrib.auth.models import User


class ExperimentViewTestCase(TestCase):
    def setUp(self):
        # Mock the get_database function from your mongo_utils
        self.db_patch = patch('mongo_db_connection.get_database')
        self.mock_db = self.db_patch.start()
        self.mock_collection = MagicMock()
        self.mock_db.return_value = self.mock_collection
        self.client = Client()

# close connection after each test
    def tearDown(self):
        self.db_patch.stop()
        close_connection()
    

    # test case one
    def test_home_view(self):
        self.mock_collection.find.return_value = [
            {'_id': '1', 'title': 'Test Experiment', 'owner_name': 'Test Owner'}
        ]
        response = self.client.get(reverse('experiments:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experiments/home.html')


    # test case two
    def test_detail_view(self):
        mock_id = ObjectId('507f1f77bcf86cd799439011')  
        self.mock_collection.find_one.return_value = {
            '_id': mock_id, 'title': 'Test Experiment', 'owner_name': 'Test Owner'
        }
        response = self.client.get(reverse('experiments:detail', args=(mock_id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experiments/detail.html')


    # test case three
    def test_submit_new_entry_get(self):
        response = self.client.get(reverse('experiments:submit_new_entry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experiments/submit_new_entry.html')

    

    # test case four
    def test_submit_new_entry_post(self):
        self.mock_collection.insert_one.return_value = None
        data = {'title': 'New Experiment', 'owner_name': 'New Owner'}
        response = self.client.post(reverse('experiments:submit_new_entry'), data)
        

    # test case five
    def test_about_view(self):
        response = self.client.get(reverse('experiments:about'))
        self.assertEqual(response.status_code, 302)  # 302 is for redirection
        self.assertRedirects(response, 'https://mbjallow.com', fetch_redirect_response=False)


    # test case six     
    def test_invalid_url(self):
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)

    # test case seven
    def test_context_data_in_view(self):
        self.mock_collection.find.return_value = [{'title': 'Test Experiment', 'owner_name': 'Test Owner'}]
        response = self.client.get(reverse('experiments:home'))
        self.assertIn('experiments', response.context)

    
    # test case eight 
    def test_static_files_loading(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertIn('/static/css/style.css', response.content.decode())


    # test case nine
    def test_home_page_title(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertContains(response, "<title>Experiment Hub</title>", html=True)


    # test case ten
    def test_home_response_code(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertEqual(response.status_code, 200)


    # test case eleven
    def test_home_template_used(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertTemplateUsed(response, 'experiments/home.html')


    # test case twelve
    def test_home_static_files(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertIn('href="/static/css/style.css"', response.content.decode())


    # test case thirteen
    def test_about_page_redirection(self):
        response = self.client.get(reverse('experiments:about'))
        self.assertEqual(response.status_code, 302)


    # test case fourteen
    def test_home_navigation_links(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertIn('href="/experiments/about/"', response.content.decode())
        self.assertIn('href="/experiments/submit/"', response.content.decode())


    # test case fifteen
    def test_presence_of_element_on_page(self):
        response = self.client.get(reverse('experiments:home'))
        self.assertIn('Welcome to the Experiment Hub!', response.content.decode())







