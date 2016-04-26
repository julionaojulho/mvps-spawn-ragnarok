import unittest

from view.Mvpview import MvpView

class MvpViewTest(unittest.TestCase):
    """Testing class for MvpView."""

    def setUp(self):
        self.view = MvpView('eddga')
        print self.view

    def test_add_entry(self):
        self.view.add_entry(['eddga'])

    def test_next_on_list(self):
        self.view.next_on_list()

if __name__ == '__main__':
    unittest.main()

    
Mvp = MvpView()
Mvp.add_entry(['eddga'])
print Mvp.time
Mvp.nextonlist()
print Mvp.queued

#in progress
