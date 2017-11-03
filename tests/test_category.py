import unittest
from app.models import Category


class TestCategoryModel(unittest.TestCase):
    def setUp(self):
        self.new_category = Category(id=600, topic="scientology")

    def test_category_variables(self):
        self.assertEqual(self.new_category.id, 600)
        self.assertEqual(self.new_category.topic, "scientology")

    def tearDown(self):
        Category.query.delete()

    def test_save_category(self):
        self.new_category.save_category()
        self.assertTrue(len(Category.query.all()) > 0)

    def test_get_category(self):
        self.new_category.save_category()
        all_category = Category.get_category(600)
        self.assertTrue(len(all_category) == 1)
