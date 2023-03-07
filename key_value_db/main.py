def main():
    storage = dict()

    while True:
        command: str = input('db >> ')

        if command == 'exit':
            break
        if command.startswith('set'):
            args = command.split()

            if len(args) < 3:
                print('key and value not provided')
                continue

            key, value = args[1], args[2]

            storage[key] = value

            continue
        if command.startswith('get'):
            args = command.split()

            if len(args) < 2:
                print('key not provided')
                continue

            key = args[1]

            if key not in storage.keys():
                print('NULL')
            else:
                print(storage[key])

            continue

        print('you can only use set, get and exit commands')


if __name__ == '__main__':
    main()
