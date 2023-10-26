''' clipboard template '''
# $ pip install pyperclip

import pyperclip

# copy to clipboard
pyperclip.copy('Hello')

# get string from clipboard
string_from_clipboard = pyperclip.paste()

# クリップボードに中身があればそれを返す
# 中身が空の場合は待つ
string_from_clipboard = pyperclip.waitForPaste()

# 中身が新しくなったら返す
string_from_clipboard = pyperclip.waitForNewPaste()

# 待ち時間を設定することができる。待ち時間を過ぎてもクリップボードから
# 文字列が取得できない場合は PyperclipTimeoutException
