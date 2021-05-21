from translate import Translator

class Translation_Engine:

    def __init__(self, from_lang, to_lang):
        self.fromlang = from_lang
        self.tolang = to_lang
        self.translator = Translator(from_lang=from_lang, to_lang=to_lang)

    def translate(self, src):
        translation = self.translator.translate(src)
        return translation


def main():
    lang1, lang2 = input("lang1: "), input("lang2: ")
    t = Translation_Engine(lang1, lang2)
    src = input("Input text to translate: ")
    print(t.translate(src))


if __name__ == "__main__":
    main()