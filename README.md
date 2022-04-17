# MyWeight

**MyWeight** - консольное приложение для хранения и систематизации периодических данных о вашем весе в Google таблице.

## Подготовка

* [How to Use Google Sheets With Python](https://youtu.be/bu5wXjz2KvU)
* [Работаем с Google Sheets API на Python](https://youtu.be/Bf8KHZtcxnA)

1. Создайте новую Google таблицу <https://sheet.new/> и сохраните ее название в переменную `SHEET` файла `.env`
2. Зайдите в настройки доступа таблицы и добавьте email пользователя указанного в `client_email` файла `service_account.json`

## Как использовать

```sh
/bin/python /path/to/script/ <<< 85.3
```
