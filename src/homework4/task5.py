"""# 5 task:  languages in school """

n = int(input('Enter numbers of pupils ='))
pupils_langs = {}
current_pupil_lang = {}
all_languages = []
repeat_langs = []
common_lang = []
uniq_lang = []
for i in range(0, n):
    num_lang = int(input(f'Enter number of languages for pupils number № {i + 1}:'))
    mass_lang = []
    for j in range(0, num_lang):
        language = input('Enter language')
        mass_lang.append(language)
        all_languages.append(language)
    current_pupil_lang = {i: mass_lang}
    pupils_langs.update(current_pupil_lang)
for g in all_languages:
    if all_languages.count(g) > 1:
        if g not in repeat_langs:
            repeat_langs.append(g)
for key, values in pupils_langs.items():
    for val in values:
        if val in repeat_langs and val not in common_lang:
            common_lang.append(val)
        elif val not in uniq_lang:
            uniq_lang.append(val)
print('number of common languages', len(common_lang))
print('common languages', common_lang)
print('number of other languages', len(uniq_lang))
print('other languages', uniq_lang)
