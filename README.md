# Python wc Practice 🐾

這是一個 Python 小練習專案，功能類似簡易版的 `wc` 工具。

它可以讀取一個文字檔，並統計：

- 總行數
- 總字數
- 總字母數 / 字元數
- 基本的檔案錯誤處理

雖然它還不是完美版本，但它記錄了我練習 Python 檔案讀取、命令列參數、字串處理和錯誤處理的過程。

---

## Features ✨

- 使用命令列參數讀取檔案
- 檢查是否正確輸入檔案名稱
- 如果找不到檔案，會顯示錯誤提示
- 使用 `.split()` 計算文字中的單字
- 使用 `.splitlines()` 計算行數
- 使用 `string.punctuation` 嘗試清理英文標點符號
- 使用迴圈計算清理後的字母數

---
## What I Practiced 📚

這個小專案主要練習了：

sys.argv
sys.exit()
open()
try / except
FileNotFoundError
.read()
.split()
.splitlines()
list comprehension
string.punctuation
for 迴圈累加計算

---

## Why I Made This 🌱

我正在學習 Python，這個專案是為了練習把基礎語法變成一個可以實際執行的小工具。

小小的程式也是進步的證明。
今天先讓它跑起來，之後再慢慢讓它變得更好。owo

## How to Use 🚀

在終端機輸入：

```bash
python wc_practice.py example.txt