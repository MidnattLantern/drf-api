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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        evee = User.objects.create_user(
            username='evee', password='evyy_passy'
        )
        stevee = User.objects.create_user(
            username='stevee', password='stevyy_passy'
        )
        Post.objects.create(
            owner=evee, title='evees title', content='evees content'
        )
        Post.objects.create(
            owner=stevee, title='stevees title', content='stevees content'
        )


    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'evees title')
        self.assertEqual(response.data['content'], 'evees content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/invalid/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='stevee', password='stevyy_passy')
        response = self.client.put('/posts/2/', {'title': 'some new title'})
        post = Post.objects.filter(pk=2).first()
        self.assertEqual(post.title, 'some new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tes_user_cant_update_another_users_post(self):
        self.client.login(username='evee', password='evyy_passy')
        response = self.client.put('posts/2/', {'title': 'some new title'})
        post = Post.objects.filter(pk=2).first()
        self.assertEqual(post.title, 'some new title')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)