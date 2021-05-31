import os
from string import ascii_lowercase
import random

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))
ANIMALS_PATH = os.path.join(MODULE_PATH, 'animals.py')


def deliver(animal):
    sound_template = ''.join([random.choice(ascii_lowercase) for _ in range(4)])
    class_template = (
        '@animal_in_zoo\n'
        'class {class_name}(Animal):\n'
        '    @classmethod\n'
        '    def speak(cls):\n'
        '        print(f\'{{cls.get_title()}} say {sound}-{sound}\')\n\n'
    )

    with open(ANIMALS_PATH, 'r') as source:
        source_code = source.read()

    tpl = class_template.format(
        class_name=animal.capitalize(),
        sound=sound_template
    )

    with open(ANIMALS_PATH, 'w') as destination:
        destination.write(f'{source_code}\n{tpl}')
