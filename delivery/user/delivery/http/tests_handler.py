from django.test import TestCase, Client


class HandlerTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.post('/user/create/',
                         {'name': 'Jhon',
                          'phone': '56933375029',
                          'email': 'qwerty@gmail.com',
                          'password': '9874563'
                          })

    def test_get_all(self):
        response = self.client.get('/menu/today/')
        assert response.status_code == 200

    def test_get_by_id(self):
        pass

    def test_logout(self):
        response = self.client.get('/user/logout/', follow=True)
        assert response.status_code == 200

    def test_authentication(self):
        self.client.post('/user/create/',
                         {'name': 'Jhon',
                          'phone': '56933375029',
                          'email': 'fake@gmail.com',
                          'password': 'goodpassword'
                          })
        response = self.client.post('/user/login/',
                                    {'email': 'fake@gmail.com',
                                     'password': 'goodpassword'
                                     })
        assert response.status_code == 302

    def test_create(self):
        response = self.client.post('/user/create/',
                                    {'name': 'Jhon',
                                     'phone': '56933375029',
                                     'email': 'fake@gmail.com',
                                     'password': 'goodpassword'
                                     })

        assert response.status_code == 200
