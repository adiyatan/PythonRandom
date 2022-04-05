data = "ini adalah string"
print(data)
print(type(data))

#1 ''/""
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"halo, apakabar?"')
print("'halo, apakabar?'")
print("ini adalah hari jum'at")

#2 \
print('mari shalat jum\'at')
print('g\'day,isn\'t it?')

# backslash
print("c:\\user\\ucup")

#tab
print("ucup\tgilang,jauhan")
print("ucup\t\t\tgilang,jauhan")

#backspace
print("ucup \bgilang,deketan")

#newline
print("baris pertama.\nbaris kedua.") # line feed > UNIX,LINUX
print("baris pertama.\rbaris kedua.") # carriage return > ACORN
print("baris pertama.\r\nbaris kedua.") # line feed carriage return > WINDOWNS

# 3
print('c:\\new folder')
# raw string
print(r'c:\new \t\r\b\\folder')
#multi literal raw
print("""
nama : ucup
kelas : 3 sd
""")
#literal dan raw string
print(r"""
nama : ucup
kelas : 3 sd\new normal
website : www.kei.com\newId
""")