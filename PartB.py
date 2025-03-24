import unittest
from PartA import Staff, TeachingStaff

class TestStaffClasses(unittest.TestCase):
    def setUp(self):
        # Create test objects
        self.staff1 = Staff("John Smith", "01/01/1990", "M", "123", "123 Street")
        self.staff2 = Staff("John Smith", "01/01/1990", "M", "123", "123 Street")
        self.teacher1 = TeachingStaff("Jane Doe", "05/05/1985", "F", "456", "789 Road", "Maths", "Higher")

    # B2. Test if object is instance of class
    def test_instance_of(self):
        self.assertIsInstance(self.staff1, Staff)
        self.assertIsInstance(self.teacher1, TeachingStaff)
        self.assertIsInstance(self.teacher1, Staff)  # Parent class

    # B3. Test if object is NOT instance of class
    def test_not_instance_of(self):
        self.assertNotIsInstance(self.staff1, TeachingStaff)
        self.assertNotIsInstance("test", Staff)
        self.assertNotIsInstance(123, Staff)

    # B4. Test if 2 objects are identical
    def test_objects_identical(self):
        self.assertEqual(self.staff1.name, self.staff2.name)
        self.assertEqual(self.staff1.DoB, self.staff2.DoB)
        self.assertEqual(self.staff1.sex, self.staff2.sex)
        self.assertEqual(self.staff1.staffID, self.staff2.staffID)
        self.assertEqual(self.staff1.address, self.staff2.address)

    # B5. Test update methods
    def test_update_methods(self):
        # Test Staff update methods
        self.staff1.update_name("Jane Smith")
        self.assertEqual(self.staff1.name, "Jane Smith")

        self.staff1.update_address("456 New Street")
        self.assertEqual(self.staff1.address, "456 New Street")

        # Test invalid updates
        self.staff1.update_name(123)  # Should not update
        self.assertNotEqual(self.staff1.name, 123)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
