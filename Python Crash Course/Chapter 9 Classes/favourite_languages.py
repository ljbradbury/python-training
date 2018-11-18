

from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages["Jen"] = "Python"
favourite_languages["Bob"] = "Perl"
favourite_languages["Sarah"] = "C#"
favourite_languages["Tim"] = "Java"

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")
