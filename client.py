class Client:
    def __init__(self,
                 name: str,
                 device_type: str,
                 browser: str,
                 sex: str,
                 age: str,
                 bill: str,
                 region: str | None = None):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.sex = sex
        self.age = age
        self.bill = bill
        self.region = region

        if self.name.startswith('"'):
            self.name = self.name[1:]
        if self.name.endswith('"'):
            self.name = self.name[:-1]
        self.name = self.name.replace('""', '"')

    def __str__(self) -> str:
        def device_type_to_str(device_type: str) -> str:
            if device_type == 'mobile':
                return 'мобильного'
            elif device_type == 'desktop':
                return 'компьютерного'
            elif device_type == 'laptop':
                return 'ноутбучного'
            else:
                return 'планшетного'

        string = ''

        string += f'Пользователь {self.name} '
        string += f'{'женского' if self.sex == 'female' else 'мужского'} пола, '
        string += f'{self.age} лет '
        string += f'совершил{'а' if self.sex == 'female' else ''} покупку на {self.bill} у.е. '
        string += f'с {device_type_to_str(self.device_type)} браузера {self.browser}.'
        if self.region != '-':
            string += f' Регион, из которого совершалась покупка: {self.region}.'

        return string