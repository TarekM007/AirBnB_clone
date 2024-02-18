#!/usr/bin/python3
""" Defines unittests for models/user.py. """

import unittest
import uuid
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from time import sleep


class TestUser_instantiation(unittest.TestCase):
    """ test case for User model class """

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.user = User()
        cls.user.email = "abc@example.com"
        cls.user.password = "123456"
        cls.user.first_name = "Ahmed"
        cls.user.last_name = "Ali"

    def test_for_instantiation(self):
        """Tests instantiation of User class."""
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.u.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_has_attributes(self):
        u = user()
        self.assertTrue('id' in self.u.__dict__)
        self.assertTrue('created_at' in self.u.__dict__)
        self.assertTrue('updated_at' in self.u.__dict__)
        self.assertTrue('email' in self.u.__dict__)
        self.assertTrue('password' in self.u.__dict__)
        self.assertTrue('first_name' in self.u.__dict__)
        self.assertTrue('last_name' in self.u.__dict__)

    def test_attributes_are_string(self):
        u = user()
        self.assertIs(type(self.u.email), str)
        self.assertIs(type(self.u.password), str)
        self.assertIs(type(self.u.first_name), str)
        self.assertIs(type(self.u.last_name), str)

    def test_is_subclass(self):
        """Test to check if User is a subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")

    def test_str(self):
        """test that the str method has the correct output"""
        u = User()
        string = "[User] ({}) {}".format(u.id, user.__dict__)
        self.assertEqual(string, str(u))

    def test_is_subclass(self):
        u = user()
        self.assertTrue(issubclass(self.u.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        u = user()
        self.u.save()
        self.assertNotEqual(self.u.created_at, self.u.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.u))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_dict = u.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        _dict = u.to_dict()
        self.assertEqual(_dict["__class__"], "User")
        self.assertEqual(type(_dict["created_at"]), str)
        self.assertEqual(type(_dict["updated_at"]), str)
        self.assertEqual(_dict["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(_dict["updated_at"], u.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
