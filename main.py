from random import randint


def attack(char_name, char_class):
    damage = 5
    if char_class == 'warrior':
        damage += randint(3, 5)
    elif char_class == 'mage':
        damage += randint(5, 10)
    elif char_class == 'healer':
        damage += randint(-3, -1)
    return f'{char_name} нанёс урон {damage}'


def defence(char_name, char_class):
    block = 10
    if char_class == 'warrior':
        block += randint(5, 10)
    elif char_class == 'mage':
        block += randint(-2, 2)
    elif char_class == 'healer':
        block += randint(2, 5)
    return f'{char_name} блокировал {block} урона'


def special(char_name, char_class):
    abilities = {
        'warrior': ('Выносливость', 80 + 25),
        'mage': ('Атака', 5 + 40),
        'healer': ('Защита', 10 + 30)
    }
    ability_name, ability_power = abilities[char_class]
    return f'{char_name} применил «{ability_name} {ability_power}»'


def start_training(char_name, char_class):
    classes = {
        'warrior': 'Воитель',
        'mage': 'Маг',
        'healer': 'Лекарь'
    }
    class_name = classes[char_class]
    print(f'{char_name}, ты {class_name} — отличный боец!')
    print('Тренируйся: attack, defence, special, skip')
    cmd = None
    while cmd != 'skip':
        cmd = input('Команда: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    descriptions = {
        'warrior': 'дерзкий воин ближнего боя',
        'mage': 'находчивый маг дальнего боя',
        'healer': 'могущественный лекарь и заклинатель'
    }
    while True:
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: ').lower()
        if char_class in descriptions:
            print(f'{char_class.capitalize()} — {descriptions[char_class]}.')
            return char_class
        else:
            print('Неправильный выбор. Попробуйте снова.')


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель - warrior, Маг - mage, Лекарь - healer')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == "__main__":
    main()