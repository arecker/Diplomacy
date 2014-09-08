from django.test import TestCase
from models import Update, Player
from django.utils import timezone


class TestUpdate(TestCase):
    def setUp(self):
        update = Update()
        update.date = timezone.now()
        update.title = 'Test Update'
        update.season = 'Test Season'
        update.body = '**This should be bold**'
        update.save()

        update2 = Update()
        update2.date = timezone.now()
        update2.title = 'Latest Update'
        update2.season = 'Test Season'
        update2.body = 'Test body'
        update2.save()

        self.update = update


    def test_to_html(self):
        expected = '<p><strong>This should be bold</strong></p>\n'
        self.update.body = '**This should be bold**'
        self.update.save()
        actual = self.update.body
        self.assertEqual(actual, expected)


    def test_get_latest(self):
        update = Update.objects.get_latest()
        self.assertEqual(update.title, 'Latest Update')


    def test_get_by_id(self):
        update = Update.objects.get_by_id(1)
        self.assertEqual(update.title, 'Test Update')
        update = Update.objects.get_by_id(2)
        self.assertEqual(update.title, 'Latest Update')


class TestPlayer(TestCase):
    def setUp(self):
        p1 = Player()
        p1.name = 'Jordan Snyder'
        p1.country = 'Serbia'
        p1.description = 'This is Jordans description'
        p1.email = 'TestJordanEmail@yahoo.com'
        p1.save()
        self.p1 = p1

        p2 = Player()
        p2.name = 'Chi Won'
        p2.country = 'South Korea'
        p2.description = 'Test Description'
        p2.save()
        self.p2 = p2


    def test_default_waiting_true(self):
        self.assertTrue(self.p1.waiting)
        self.assertTrue(self.p2.waiting)


    def test_get_waiting(self):
        waiting = Player.objects.get_players_waiting()
        self.assertEqual(len(waiting), 2)

        self.p1.waiting = False
        self.p1.save()
        waiting = Player.objects.get_players_waiting()
        self.assertEqual(len(waiting), 1)
        self.assertEqual(waiting[0].name, 'Chi Won')


    def test_get_percentage_moved(self):
        self.p1.waiting = False
        self.p1.save()
        self.p2.waiting = False
        self.p2.save()
        percentage = Player.objects.get_percentage_moved()
        self.assertEqual(percentage, 100)

        self.p1.waiting = True
        self.p1.save()
        self.p2.waiting = True
        self.p2.save()
        percentage = Player.objects.get_percentage_moved()
        self.assertEqual(percentage, 0)

        self.p1.waiting = False
        self.p1.save()
        percentage = Player.objects.get_percentage_moved()
        self.assertEqual(percentage, 50)