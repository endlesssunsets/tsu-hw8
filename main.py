import os
from client import Client


def read_csv_file(filename: str, separator: str = ',') -> list[dict[str, str]]:
    with open(filename, newline='') as file:
        res = []

        text = file.read()
        lines = text.splitlines()
        header = lines.pop(0).split(separator)
        for line in lines:
            to_append = {}
            i = 0
            for row in line.split(separator):
                to_append[header[i]] = row
                i += 1
            res.append(to_append)

        return res


def main():
    print('Обработка данных о веб-клиентах')
    print('Чтобы выйти из программы в любой момент, нажмите комбинацию CTRL+C на вашей клавиатуре.')

    while True:
        print('Пожалуйста, введите путь к CSV-таблице:')
        table_filename = str(input('[по умолчанию: web_clients_correct.csv] > '))
        if table_filename == '':
            table_filename = 'web_clients_correct.csv'
        if os.path.exists(table_filename):
            break
        print('Файла не существует.')

    while True:
        print('Теперь напишите путь к файлу, в который записать описания об веб-клиентах.')
        output_filename = str(input('[по умолчанию: web_clients.txt] > '))
        if output_filename == '':
            output_filename = 'web_clients.txt'
        try:
            open(output_filename, 'w+')
            break
        except:
            print('Не мог создать файл. Может быть не существует папка, в котором он должен находится?')

    clients_processed = 0
    with open(output_filename, 'w+') as txt:
        for client_row in read_csv_file(table_filename):
            client = Client(
                client_row['name'],
                client_row['device_type'],
                client_row['browser'],
                client_row['sex'],
                client_row['age'],
                client_row['bill'],
                client_row['region']
            )
            print(f'Обрабатываю запрос от {client.name} в {client.region}...')
            txt.write(str(client) + '\n')
            clients_processed += 1
    print(f'Обработано клиентов ВСЕГО: {clients_processed} из файла {table_filename}')
    print(f'Описания о них были записаны в файл {output_filename}')


if __name__ == '__main__':
    main()