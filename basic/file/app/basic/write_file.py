# core mode:
# 'w' - write mode(if not exist, create a new file; if exist, overwrite the file)
# 'a' - append mode
# 'r' - read mode (default)
# 'r+' - read and write mode
from pathlib import Path

filename = Path(__file__).with_name('article.txt')

# w = 写入模式
with open(filename, 'w', encoding='utf-8') as file_object:
    # write() 不会自动换行，需要手动加 \n
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# a = 追加模式
with open(filename, 'a', encoding='utf-8') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
