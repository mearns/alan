#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

from alan.models import Task
from django.test import TestCase

class TaskTestCase(TestCase):

    def setUp(self):
        pass

    def test_ceate_task(self):
        task = Task.objects.create(name='My test task')
        task.save()

        self.assertEqual(len(Task.objects.all()), 1)

