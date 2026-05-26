import sys
import string
from sys import argv


word_count = 0
char_count = 0
line_count = 0


if len(argv) != 2:
    print("請附上正確的檔案喔")
    sys.exit()
else:
    try:
        txt = open(argv[1])
        lines = txt.read()
    except FileNotFoundError:
        print("找不到檔案，請確認檔案名稱或路徑是否正確")
        sys.exit()


lines_s = lines.split()
clean_words = [word.strip(string.punctuation) for word in lines_s]
for word in clean_words:
    char_count += len(word)

line_count = len(lines.splitlines())

word_count = len(lines.split())

print(f"文件中的總行數是:{line_count}| 總字數是:{word_count}| 總字母數是:{char_count}")
