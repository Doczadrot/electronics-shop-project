# language_mixin.py
class LanguageMixin:
    _keyboard_language = 'EN'
    SUPPORTED_LANGUAGES = ('EN', 'RU')

    @property
    def language(self):
        return self._keyboard_language

    def change_lang(self):
        self._keyboard_language = 'RU' if self._keyboard_language == 'EN' else 'EN'