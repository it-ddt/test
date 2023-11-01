from django import forms

"""
ширина вк
высота вк
файл с текстом
количество слов
части речи
цвет
"""

pos_texts = [
    'имя существительное',
    'имя прилагательное (полное)',
    'имя прилагательное (краткое)',
    'компаратив',
    'глагол (личная форма)',
    'глагол (инфинитив)',
    'причастие (полное)',
    'причастие (краткое)',
    'деепричастие',
    'числительное',
    'наречие',
    'местоимение-существительное',
    'предикатив',
    'предлог',
    'союз',
    'частица',
    'междометие',
]
pos_values = [
    'NOUN',
    'ADJF',
    'ADJS',
    'COMP',
    'VERB',
    'INFN',
    'PRTF',
    'PRTS',
    'GRND',
    'NUMR',
    'ADVB',
    'NPRO',
    'PRED',
    'PREP',
    'CONJ',
    'PRCL',
    'INTJ',
]

POS = []
for i in range(len(pos_texts)):
    new = (pos_values[i], pos_texts[i])
    POS.append(new)


class ColorPickerWidget(forms.widgets.TextInput):
    input_type = 'color'


class UserForm(forms.Form):
    wc_width = forms.IntegerField(
        max_value=1920,
        min_value=640,
        label='ширина картинки'
    )

    wc_height = forms.IntegerField(
        max_value=1080,
        min_value=480,
        label='высота картинки'
    )

    wc_words = forms.IntegerField(
        max_value=1000,
        min_value=1,
        label='количество слов на картинке'
    )

    file = forms.FileField(label='файл с текстом')

    pos = forms.MultipleChoiceField(
        label='часть речи',
        widget=forms.CheckboxSelectMultiple,
        choices=POS,
        initial=['NOUN'],
    )

    color = forms.CharField(
        label='цвет фона картинки',
        widget=ColorPickerWidget(attrs={'type': 'color'}),
    )

    
