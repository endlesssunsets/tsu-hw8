def read_csv_file(filename: str) -> list[dict[str, str]]:
    with open(filename, newline='') as file:
        res = []

        text = file.read()
        lines = text.splitlines()
        header = lines.pop(0).split(',')
        for line in lines:
            to_append = {}
            i = 0
            for row in line.split(','):
                to_append[header[i]] = row
                i += 1
            res.append(to_append)

        return res

def device_type_to_str(device_type: str) -> str | None:
    if device_type == 'mobile':
        return 'мобильного'
    elif device_type == 'desktop':
        return 'компьютерного'
    elif device_type == 'laptop':
        return 'ноутбучного'
    elif device_type == 'tablet':
        return 'планшетного'
    return None

def sex_to_str(sex: str) -> str | None:
    if sex == 'female':
        return 'женского'
    elif sex == 'male':
        return 'мужского'
    return None

def main():
    with open("./web_clients.txt", "w+") as txt:
        for client in read_csv_file("./web_clients_correct.csv"):
            gender = sex_to_str(client['sex'])
            device = device_type_to_str(client['device_type'])

            txt.write(f"Пользователь {client['name']} ")
            txt.write(f"{gender} пола, ")
            txt.write(f"{client['age']} лет ")
            txt.write(f"совершил{"а" if client['sex'] == "female" else ""} покупку на {client['bill']} у.е. ")
            txt.write(f"с {device} браузера {client['browser']}.")
            if client['region'] != '-':
                txt.write(f" Регион, из которого совершалась покупка: {client['region']}.")
            txt.write("\n")

if __name__ == '__main__':
    main()