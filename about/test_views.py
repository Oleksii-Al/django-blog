from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):
    def setUp(self):
        self.about_content = About(
            title = "About", content = "About me"
        )
        self.about_content.save()
    
    def render_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About", response.content)
        self.assertIsInstance(response.context['collaborate_form', CollaborateForm])

    def collaboration_submussion(self):
        post_data = {
            'name': 'Alex',
            'email': 'alex@test.com',
            'message': "This is the message"
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Collaboration request received! I endeavour to respond within 2 working days.", response.content)


