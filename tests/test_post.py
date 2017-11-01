import unittest
from app.models import User, Category, Post, Comment
from . import db


class TestPostModel(unittest.TestCase):
    def setUp(self):
        self.user_nish = User(user_id=12345, fulname="Sherry B", username="sherry", email="ndungu.virginia00@gmail.com",
                              profession="developer", quote="Peace", user_pwd="thornemelon")
        self.digital_marketing = Category(
            category_id=123, topic="Digital Marketing")
        self.new_post = Post(post_id=1234, title="It’s all about customer experience", description="In 2017, leading marketers will be taking steps towards optimizing their Customer Experience through personalized content and with new way of operating content.",
                             votes="5", user=self.user_nish, category=self.digital_marketing)

    def tearDown(self):
        User.query.delete()
        Category.query.delete()
        Post.query.delete()

    def test_check_variables(self):
        self.assertEquals(self.new_post.post_id, 1234)
        self.assertEquals(self.new_post.title,
                          "It’s all about customer experience")

        self.assertEquals(self.new_post.description,
                          "In 2017, leading marketers will be taking steps towards optimizing their Customer Experience through personalized content and with new way of operating content.")
        self.assertEquals(self.new_post.votes, 5)
        self.assertEquals(self.new_post.user, self.user_nish)
        self.assertEquals(self.new_post.category, self.digital_marketing)

     def test_save_post(self):

         self.new_post.save_post()
         self.assertTrue(len(Review.query.all()) > 0)

    def test_get_posts(self):
        self.new_post.save_post()
        all_posts = Post.get_post(12345)
        self.assertTrue(len(all_posts) == 1)
