string_sample_1 = 'this is also a string'
print(string_sample_1)

# double quotes allows escape strings, formats, and string manipulations
string_sample_2 = "this is a sample string"
print(string_sample_2)

# positional argument format
string_format_1 = "this is sample string {} 1".format('format')
print(string_format_1)

string_format_2 = "this is sample {} {} 2".format('string', 'format')
print(string_format_1)

args = ('sample', 'string', 'format')
string_format_3 = "this is {} {} {} 3".format(*args)

# key-word argument format
string_format_4 = "this is sample string {text} 4".format(text='format')
print(string_format_4)

string_format_5 = "this is sample {text1} {text2} 5".format(text1='string', text2='format')
print(string_format_5)

string_format_6 = "this is sample string {text} {text} 6".format(text='format')
print(string_format_6)

kwargs = {'text1': 'sample', 'text2': 'string', 'text3': 'format'}
string_format_7 = "this is {text1} {text2} {text3} 7".format(**kwargs)
print(string_format_7)

# with variable string format
text = 'format'
string_format_8 = f"this is sample string {text} 8"
print(string_format_8)

text = 'format'
string_format_9 = f"this is sample string {text} {text} 9"
print(string_format_9)

text1 = 'string'
text2 = 'format'
string_format_10 = f"this is sample {text1} {text2} 10"
print(string_format_10)

# data type positional string format
num = 11
text = 'format'

string_format_11 = "this is sample string %s %d" % (text, num)
print(string_format_11)

num = 12
text = 'string'

string_format_11 = "this is sample %s format %d" % (text, num)
print(string_format_11)
