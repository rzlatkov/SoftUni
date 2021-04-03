from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    name = 'joe'

    def test_unit_when_courses_available(self):
        self.s = Student(self.name, {'bg': [1]})
        self.assertEqual(self.s.name, self.name)
        self.assertEqual(self.s.courses, {'bg': [1]})

    def test_init_when_courses_not_available(self):
        self.s = Student(self.name)
        self.assertEqual(self.s.name, self.name)
        self.assertEqual(self.s.courses, {})

    def test_enroll_first(self):
        self.s = Student(self.name, {'bg': [1]})
        self.s.enroll('bg', [2], '')
        self.assertEqual(self.s.courses['bg'], [1, 2])

    def test_enroll_first_output(self):
        self.s = Student(self.name, {'bg': [1]})
        output = self.s.enroll('bg', [2], '')
        self.assertEqual(output, 'Course already added. Notes have been updated.')

    def test_enroll_second_Y(self):
        self.s = Student(self.name, {'bg': [1]})
        self.s.enroll('maths', [2], 'Y')
        self.assertEqual(self.s.courses['maths'], [2])

    def test_enroll_second_Y_output(self):
        self.s = Student(self.name, {'bg': [1]})
        output = self.s.enroll('maths', [2], 'Y')
        self.assertEqual(output, "Course and course notes have been added.")

    def test_enroll_second_empty_str(self):
        self.s = Student(self.name, {'bg': [1]})
        self.s.enroll('maths', [2], '')
        self.assertEqual(self.s.courses['maths'], [2])

    def test_enroll_second_empty_str_output(self):
        self.s = Student(self.name, {'bg': [1]})
        output = self.s.enroll('maths', [2], '')
        self.assertEqual(output, "Course and course notes have been added.")

    def test_enroll_third(self):
        self.s = Student(self.name, {'bg': [1]})
        self.s.enroll('wtf', [2], 's')
        self.assertEqual(self.s.courses['wtf'], [])

    def test_enroll_third_output(self):
        self.s = Student(self.name, {'bg': [1]})
        output = self.s.enroll('wtf', [2], 's')
        self.assertEqual(output, "Course has been added.")

    def test_add_notes_when_course_in_courses(self):
        self.s = Student(self.name, {'bg': [1]})
        self.s.add_notes('bg', 3)
        self.assertEqual(self.s.courses['bg'], [1, 3])

    def test_add_notes_when_course_in_courses_output(self):
        self.s = Student(self.name, {'bg': [1]})
        output = self.s.add_notes('bg', 3)
        self.assertEqual(output, "Notes have been updated")

    def test_add_notes_when_course_not_in_courses(self):
        self.s = Student(self.name, {'bg': [1]})
        with self.assertRaises(Exception) as exc:
            self.s.add_notes('maths', [1, 2, 3])
        self.assertEqual(str(exc.exception), "Cannot add notes. Course not found.")

    def test_leave_course_when_course_not_found(self):
        self.s = Student(self.name, {'bg': [1]})
        with self.assertRaises(Exception) as exc:
            self.s.leave_course('maths')
        self.assertEqual(str(exc.exception), "Cannot remove course. Course not found.")

    def test_leave_course_when_course_found(self):
        self.s = Student(self.name, {'bg': [1], 'maths': [2, 3, 4, 5]})
        self.s.leave_course('maths')
        self.assertEqual(self.s.courses, {'bg': [1]})

    def test_leave_course_when_course_found_output(self):
        self.s = Student(self.name, {'bg': [1], 'maths': [2, 3, 4, 5]})
        output = self.s.leave_course('maths')
        self.assertEqual(output, "Course has been removed")


if __name__ == '__main__':
    unittest.main()
