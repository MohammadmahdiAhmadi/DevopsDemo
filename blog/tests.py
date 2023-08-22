from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Idea

class IdeaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.idea = Idea.objects.create(
            title='Test Idea',
            content='This is a test idea content.',
            author=self.user
        )

    def test_idea_creation(self):
        self.assertEqual(self.idea.title, 'Test Idea')
        self.assertEqual(self.idea.content, 'This is a test idea content.')
        self.assertEqual(self.idea.author, self.user)
        self.assertEqual(self.idea.date_posted.date(), timezone.now().date())
        self.assertEqual(self.idea.likes.count(), 0)
        self.assertEqual(self.idea.dislikes.count(), 0)
        self.assertEqual(self.idea.views, 0)

    def test_idea_likes_and_dislikes(self):
        another_user = User.objects.create_user(username='anotheruser', password='anotherpassword')

        # Test liking and disliking the idea
        self.idea.likes.add(self.user)
        self.idea.dislikes.add(another_user)

        self.assertEqual(self.idea.likes.count(), 1)
        self.assertEqual(self.idea.dislikes.count(), 1)
        self.assertIn(self.user, self.idea.likes.all())
        self.assertIn(another_user, self.idea.dislikes.all())

    def test_idea_views(self):
        self.idea.views = 10
        self.idea.save()

        self.assertEqual(self.idea.views, 10)
