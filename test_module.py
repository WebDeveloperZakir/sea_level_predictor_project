# test_module.py

import unittest
import matplotlib
matplotlib.use('Agg')
import sea_level_predictor

class SeaLevelTestCase(unittest.TestCase):
    def test_draw_plot(self):
        fig = sea_level_predictor.draw_plot()
        self.assertIsNotNone(fig, "Expected a plot object returned from draw_plot()")

def test_draw_plot():
    suite = unittest.TestLoader().loadTestsFromTestCase(SeaLevelTestCase)
    unittest.TextTestRunner().run(suite)
# Unit tests
