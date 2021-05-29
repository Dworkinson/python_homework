from zoo import animals


if __name__ == '__main__':
    try:
        while True:
            animals_list = ', '.join(animals.ANIMALS.keys())
            print(f'available animals: {animals_list}')

            action = input().strip().lower()

            if action == 'exit':
                print('Bye-bye!')
                exit()

            if action not in animals.ANIMALS:
                print(f'{action} is not available!')
                print()
                continue

            animals.ANIMALS[action].speak()
            print()
    except KeyboardInterrupt:
        print('Bye-bye!')