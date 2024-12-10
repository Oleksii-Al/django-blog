from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.
class TestCollaborateForm(TestCase):
    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg = "Form is not valid")

        def email_field_is_valid(self):
            """Test email field"""
            form = CollaborateForm({
            'name': 'Alex',
            'email': '',
            'message': 'Hello!'
            })
            self.assertFalse(form.is_valid(), msg = "Email isn't provided, form is valid")

        def email_field_is_invalid(self):
            form = CollaborateForm({
                'name': 'Max',
                'email': 'max',
                'message': 'Max is here'
            })
            self.assertTrue(form.is_valid(), msg = "Email is not valid, form is valid")
