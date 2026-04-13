from pathlib import Path

filename = Path(__file__).with_name('article.txt')

# use with statement to open the file, which ensures that the file is properly closed after its suite finishes, even if an exception is raised on the way.
with open(filename, encoding='utf-8') as file_object:
    # Read the contents of the file and print it
    contents = file_object.read()
    print(contents.strip())

    # Read the file line by line and print each line
    file_object.seek(0)  # Move the file pointer back to the beginning of the file
    for line in file_object:
        print(line.strip())

# Read the file into a list and print the list
with open(filename, encoding='utf-8') as file_object:
    # readlines() 把每一行作为元素，存入列表
    lines = file_object.readlines()

# 拼接所有行
content_string = ''
for line in lines:
    content_string += line.strip()

print(content_string)
print(len(content_string))
