# Emojiswitch
Emoji switch (supporting Chinese and English by set parameter lang)

# Example
~~~
from emojiswitch import emojize, demojize

# word switch to emoji
print(emojize('This animal is :tiger:', delimiters=(":", ":"), lang="en"))                                  # This animal is 🐅
print(emojize('这个动物是__老虎__', delimiters=("__", "__"), lang="zh"))                           # 这个动物是🐅

# emoji swith to word
print(demojize('我喜欢吃🍏', delimiters=("__", "__"), lang="zh"))                                           # 我喜欢吃__青苹果__
print(emojiswitch.demojize('I like eating 🍏', delimiters=("__", "__"), lang="en"))         # I like eating __green_apple__
~~~

# Two modes:
demojize   ：Parsing Emoji into a specific language (currently only Chinese (zh) and English (en) are supported)  
(delimiters: distinguish the text to be translated)

emojize      ：Translate text to Emoji  
(delimiters: distinguish the text to be translated)

# Installation
~~~
$ pip install emojiswitch
~~~

# Authors
mieqihezi(梅妻鹤子)
