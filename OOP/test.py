import unittest
from email import Email

from email import inbox
from email import populate_inbox

class TestEmail(unittest.TestCase):

    def setUp(self):
        # Clear the inbox before each test
        inbox.clear()
        populate_inbox()

    def test_mark_as_read(self):
        email = Email("test@example.com", "Test Subject", "Test Content")
        self.assertFalse(email.has_been_read)  # Initially should be False
        email.mark_as_read()
        self.assertTrue(email.has_been_read)  # Should be True after marking as read

    def test_populate_inbox(self):
        self.assertEqual(len(inbox), 3)  # Should have 3 emails after populating

    def test_unread_count(self):
        unread_count = sum(not email.has_been_read for email in inbox)
        self.assertEqual(unread_count, 3)  # Initially all emails should be unread

        # Mark one email as read and check the count again
        inbox[0].mark_as_read()
        unread_count = sum(not email.has_been_read for email in inbox)
        self.assertEqual(unread_count, 2)  # Now there should be 2 unread emails

if __name__ == "__main__":
    unittest.main()
