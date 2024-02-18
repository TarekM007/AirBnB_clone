#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models import storage
from models.base_model import BaseModel


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        _st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(_st))
        self.assertNotIn("name", _st.__dict__)

    def test_two_states_unique_ids(self):
        st_1 = State()
        st_2 = State()
        self.assertNotEqual(st_1.id, st_2.id)

    def test_two_states_different_created_at(self):
        st_1 = State()
        sleep(0.05)
        st_2 = State()
        self.assertLess(st_1.created_at, st_2.created_at)

    def test_two_states_different_updated_at(self):
        st_1 = State()
        sleep(0.05)
        st_2 = State()
        self.assertLess(st_1.updated_at, st_2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        _st = State()
        _st.id = "333444"
        _st.created_at = _st.updated_at = my_date
        ststr = _st.__str__()
        self.assertIn("[State] (333444)", ststr)
        self.assertIn("'id': '333444'", ststr)
        self.assertIn("'created_at': " + my_date_repr, ststr)
        self.assertIn("'updated_at': " + my_date_repr, ststr)

    def test_args_unused(self):
        _st = State(None)
        self.assertNotIn(None, _st.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        _st = State(id="444", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(_st.id, "444")
        self.assertEqual(_st.created_at, my_date)
        self.assertEqual(_st.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_8_instantiation(self):
        """Tests instantiation of State class."""

        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))
    

if __name__ == "__main__":
    unittest.main()
