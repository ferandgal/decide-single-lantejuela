import random
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.testcases import TransactionTestCase

from django.core.serializers import json
from .forms import CensusForm
from .models import Census
from base import mods
from base.tests import BaseTestCase
from voting.models import Question, Voting
from datetime import date

#Use TransactionTestCase instead of BaseTestCase
class CensusTestCase(TransactionTestCase):
    reset_sequences = True
    def setUp(self):
        super().setUp()
        question1 = Question.objects.create(desc='Question 1')
        voting1 = Voting.objects.create(id=10, name='Voting', question = question1)
        voting1.save()

        self.census = Census(voting_id=10, voter_id=1)
        self.census.save()
    
    def tearDown(self):
        super().tearDown()
        self.voting1 = None
        self.admin = None
        self.user1 = None
        self.user2 = None
        self.census = None
    
    def test_add_voter_custom_post(self):
        admin = User(username='admin2', password='qwerty')
        admin.is_staff = True
        admin.save()

        self.client.force_login(admin)
        response = self.client.post('/census/addCustom/', 
        data={'voting': ['10'], 'voter_ids': [admin.pk]})
        census = Census.objects.all()
        
        print('----------------------------------------------------------------------\n')
        print('Census: ', census)
        print(response)
        print('\n----------------------------------------------------------------------\n')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(census), 1)
    
    def test_add_voter_custom_get(self):

        admin = User(username='admin2', password='qwerty')
        admin.is_staff = True
        admin.save()
        self.client.force_login(admin)
        response = self.client.get('/census/addCustom/')
        self.assertEqual(response.status_code, 200)
