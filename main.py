from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """
    Calculate damage during an attack based on character class.

    Args:
        char_name (str): The character's name.
        char_class (str): Character class ('warrior', 'mage', or 'healer').

    Returns:
        str: A string indicating the damage dealt by the character.
    """
    damage: int = 5
    if char_class == 'warrior':
        damage += randint(3, 5)
    elif char_class == 'mage':
        damage += randint(5, 10)
    elif char_class == 'healer':
        damage += randint(-3, -1)
    return f'{char_name} нанёс урон {damage}'


def defence(char_name: str, char_class: str) -> str:
    """
    Calculate block strength during defense based on character class.

    Args:
        char_name (str): The character's name.
        char_class (str): Character class ('warrior', 'mage', or 'healer').

    Returns:
        str: A string indicating the block strength during defense.
    """
    block: int = 10
    if char_class == 'warrior':
        block += randint(5, 10)
    elif char_class == 'mage':
        block += randint(-2, 2)
    elif char_class == 'healer':
        block += randint(2, 5)
    return f'{char_name} блокировал {block} урона'


def special(char_name: str, char_class: str) -> str:
    """
    Use special abilities based on character class.

    Args:
        char_name (str): The character's name.
        char_class (str): Character class ('warrior', 'mage', or 'healer').

    Returns:
        str: A string indicating the special ability used by the character.
    """
    abilities: set = {
        'warrior': ('Выносливость', 80 + 25),
        'mage': ('Атака', 5 + 40),
        'healer': ('Защита', 10 + 30),
    }
    ability_name, ability_power = abilities[char_class]
    return f'{char_name} применил «{ability_name} {ability_power}»'


def start_training(char_name: str, char_class: str) -> str:
    """
    Begin character training with attack, defense, and special abilities.

    Args:
        char_name (str): The character's name.
        char_class (str): Character class ('warrior', 'mage', or 'healer').

    Returns:
        str: A string indicating the end of the training.
    """
    classes: set = {'warrior': 'Воитель', 'mage': 'Маг', 'healer': 'Лекарь'}
    class_name = classes[char_class]
    print(f'{char_name}, ты {class_name} — отличный боец!')
    print('Тренируйся: attack, defence, special, skip')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Команда: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Choose a character class for the player.

    Returns:
        str: The selected character class ('warrior', 'mage', or 'healer').
    """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))