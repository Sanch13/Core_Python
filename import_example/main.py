import os
import sys
from pathlib import Path


def main():
    # project_path = os.getcwd()  # Получаем текущую директорию
    project_path = Path(__file__).parent.resolve()

    print(project_path)

    if project_path not in sys.path:
        sys.path.insert(0, project_path)  # Добавляем путь проекта в sys.path


if __name__ == '__main__':
    main()
    from pack_1.sub_pack_a.sub_pack_a import func_sub_pack_a, sub_pack_a
    from pack_1.pack_1 import func_pack_1

    func_sub_pack_a()
    print(sub_pack_a)
    print("-------------")
    func_pack_1()


# home/sanch/.cache/pypoetry/virtualenvs/core-python-WIY_8JP6-py3.12/bin/python /home/sanch/PycharmProjects/projects_from_stepik/Core_Python/import_example/main.py
# /home/sanch/PycharmProjects/projects_from_stepik/Core_Python/import_example
# /home/sanch/PycharmProjects/projects_from_stepik/Core_Python
# /snap/pycharm-professional/395/plugins/python/helpers/pycharm_display
# /usr/local/lib/python312.zip
# /usr/local/lib/python3.12
# /usr/local/lib/python3.12/lib-dynload
# /home/sanch/.cache/pypoetry/virtualenvs/core-python-WIY_8JP6-py3.12/lib/python3.12/site-packages
# /snap/pycharm-professional/395/plugins/python/helpers/pycharm_matplotlib_backend
