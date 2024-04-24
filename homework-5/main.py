import sys
import os
from src.item import Item
from src.keyboard import Keyboard
from src.language_mixin import LanguageMixin  # Импортируем LanguageMixin из нужного места

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

    try:
        kb.language = 'CH'
    except AttributeError:
        pass
    else:
        assert False, "Должно выбросить AttributeError"

    print("Все тесты пройдены успешно!")
