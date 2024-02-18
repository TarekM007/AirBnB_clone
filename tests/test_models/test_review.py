#!/usr/bin/env python3
"""Test model for Review class"""

import unittest
import os
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "Paris, Texas"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        Rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Rv))
        self.assertNotIn("place_id", Rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        Rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Rv))
        self.assertNotIn("user_id", Rv.__dict__)

    def test_text_is_public_class_attribute(self):
        Rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(Rv))
        self.assertNotIn("text", Rv.__dict__)

    def test_two_reviews_unique_ids(self):
        Rv_1 = Review()
        Rv_2 = Review()
        self.assertNotEqual(Rv_1.id, Rv_2.id)

    def test_two_reviews_different_created_at(self):
        Rv_1 = Review()
        sleep(0.05)
        Rv_2 = Review()
        self.assertLess(Rv_1.created_at, Rv_2.created_at)

    def test_two_reviews_different_updated_at(self):
        Rv_1 = Review()
        sleep(0.05)
        Rv_2 = Review()
        self.assertLess(Rv_1.updated_at, Rv_2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        Rv = Review()
        Rv.id = "333444"
        Rv.created_at = Rv.updated_at = my_date
        rv_str = Rv.__str__()
        self.assertIn("[Review] (333444)", rv_str)
        self.assertIn("'id': '333444'", rv_str)
        self.assertIn("'created_at': " + my_date_repr, rv_str)
        self.assertIn("'updated_at': " + my_date_repr, rv_str)

    def test_args_unused(self):
        Rv = Review(None)
        self.assertNotIn(None, Rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        date_iso = my_date.isoformat()
        Rv = Review(id="444", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Rv.id, "444")
        self.assertEqual(Rv.created_at, my_date)
        self.assertEqual(Rv.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "Paris, Texas"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.text), str)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.review))

if __name__ == "__main__":
    unittest.main()
