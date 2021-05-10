import unittest
#  Импорт нужно поправить.
#  У вас возможно жт ои работаетЮ но только лишь потому что вы промаркировали директорию"mark directory as sources root"
from lesson_014.bowling import get_score


class GetScoreTest(unittest.TestCase):
    #  Тестов должно быть минимум  8-10
    def test_strike(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200, 'не работает подсчёт strike')

    def test_spare(self):
        result = get_score('4/3/2/5/9/1/8/5/5/3/')
        self.assertEqual(result, 150, 'не работает подсчёт spare')

    def test_0first(self):
        result = get_score('-4-3-2-1---8-1-4-3--')
        self.assertEqual(result, 26, 'не работает подсчёт первая 0 очков')

    def test_points69(self):
        result = get_score('443322517-188154533-')
        self.assertEqual(result, 69, 'не работает подсчёт две попытки с очками')

    def test_points63(self):
        result = get_score('81716151414333221154')
        self.assertEqual(result, 63, 'не работает подсчёт две попытки с очками')

    def test_points122(self):
        result = get_score('Х4/34-48/45173/X18')
        self.assertEqual(result, 122, 'не работает подсчёт разные результаты')

    def test_points114(self):
        result = get_score('Х4/34-48/45173/X1-')
        self.assertEqual(result, 114, 'не работает подсчёт разные результаты')

    def test_points0(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0, 'не работает подсчёт все промахи')


if __name__ == '__main__':
    unittest.main()
