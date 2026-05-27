import sys
import string

word_count = 0
letter_count = 0
line_count = 0


if len(sys.argv) != 2:
    print("請附上正確的檔案喔")
    sys.exit()
else:
    try:
        with open(sys.argv[1], encoding="utf-8") as txt:
            lines = txt.read()

    except FileNotFoundError:
        print("找不到檔案，請確認檔案名稱或路徑是否正確")
        sys.exit()


lines_s = lines.split()
clean_words = [word.strip(string.punctuation) for word in lines_s]
clean_words = [word for word in clean_words if word]
for word in clean_words:
    letter_count += len(word)

line_count = len(lines.splitlines())

word_count = len(clean_words)

print(f"文件中的總行數是:{line_count}| 總字數是:{word_count}| 總字母數是:{letter_count}")
