import unittest
# TODO Импорт нужно поправить.
#  У вас возможно жт ои работаетЮ но только лишь потому что вы промаркировали директорию"mark directory as sources root"
from bowling import get_score


class GetScoreTest(unittest.TestCase):
    # TODO Текстов должно быть минимум  8-10
    def test_strike(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, [20, 20, 20, 20, 20, 20, 20, 20, 20, 20], 'не работает подсчёт strike')

    def test_spare(self):
        result = get_score('4/3/2/5/9/1/8/5/5/3/')
        self.assertEqual(result, [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], 'не работает подсчёт spare')

    def test_points(self):
        result = get_score('443322517-188154533-')
        self.assertEqual(result, [8, 6, 4, 6, 7, 9, 9, 9, 8, 3], 'не работает подсчёт две попытки с очками')

    def test_0first(self):
        result = get_score('-4-3-2-1---8-1-4-3--')
        self.assertEqual(result, [4, 3, 2, 1, 0, 8, 1, 4, 3, 0], 'не работает подсчёт первая 0 очков')


if __name__ == '__main__':
    unittest.main()
