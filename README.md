# MyWeight

**MyWeight** - консольное приложение для хранения и систематизации периодических данных о вашем весе в Google таблице.

## Подготовка

* [How to Use Google Sheets With Python](https://youtu.be/bu5wXjz2KvU)
* [Работаем с Google Sheets API на Python](https://youtu.be/Bf8KHZtcxnA)

1. Создайте новую Google таблицу <https://sheet.new/> и сохраните ее название в переменную `SHEET` файла `.env`. По умолчанию используется значение `myweight`
2. Зайдите в настройки доступа таблицы и добавьте email пользователя указанного в `client_email` файла `service_account.json`
3. Установите зависимости python

   ```sh
   pip install -r requirements.txt
   ```

## Использование

```sh
/bin/python /path/to/script/ <<< 85.3
```

### Для быстрого вызова команды можно создать alias в shell

Создайте файл с алиасами, если еще не создан

```sh
touch ~/.bash_aliases
```

Добавьте алиас в файл

```sh
alias weight='/bin/python /path/to/script/myweight'
```

Подключите файл с алиасами в shell (.bashrc, .zshrc и т.д.)

```sh
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Обновить данные файла настроек shell

```sh
source .zshrc
```
