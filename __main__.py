#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
MyWeight - консольное приложение для хранения и систематизации периодических
данных о вашем весе в Google таблице.
"""


import os
from datetime import datetime

import gspread
from dotenv import load_dotenv


def main(args):
    load_dotenv()

    sheet_name = os.getenv("SHEET", "myweight")
    dir = os.path.dirname(args[0])
    weight = input("Ваш вес: ").strip().replace(".", ",")
    service_account = gspread.service_account(
        filename=f"{dir}/service_account.json"
    )
    sheet = service_account.open(sheet_name)
    worksheet = sheet.sheet1
    curdate = datetime.now().strftime("%d.%m.%Y")
    curdate = str(curdate)

    print([curdate, weight])

    cell = worksheet.find(curdate)
    if cell:
        try:
            confirm = (
                input(
                    "Данные на сегодня уже заполнены. "
                    "Перезаписать? (y/n|д/н): "
                )
                .strip()
                .lower()
            )

            match confirm:
                case "y" | "д":
                    worksheet.update(
                        f"B{cell.row}",
                        weight,
                        value_input_option="USER_ENTERED",
                    )
                    print("Данные перезаписаны.")
                case _:
                    print("Действия отменены.")
                    sys.exit(0)
        except Exception:
            print(
                "Перезапись данных невозможна в данном режиме. Для перезаписи "
                "используйте команду `myweight` без дополнительных параметров."
            )
    else:
        worksheet.append_row(
            [curdate, weight], value_input_option="USER_ENTERED"
        )


if "__main__" == __name__:
    import sys

    main(sys.argv)
