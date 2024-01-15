from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='evee', password='evyy_passy')
    
    def test_can_list_posts(self):
        evee = User.objects.get(username='evee')
        Post.objects.create(owner=evee, title='a titile')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='evee', password='evyy_passy')
        response = self.client.post('/posts/', {'title': 'any title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'some title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)