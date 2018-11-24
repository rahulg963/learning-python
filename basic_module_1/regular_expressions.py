import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other!'

for pattern in patterns:
	print("I'm searching for: " + pattern)
	if re.search(pattern, text):
		print("MATCH!")
	else:
		print("NO MATCH!")

match = re.search('term1', text)
print(type(match.start()))
print(match.start())

split_term = '@'
email = 'user@gmail.com'
split_already = email.split(split_term)
match = re.split(split_term, email)
print(match)

# returns list of all matche
print(re.findall('text', 'this text contains text twice'))


# -----------

def multi_re_find(patterns, phrase):
	for pat in patterns:
		print("Searching for pattern {}". format(pat))
		print(re.findall(pat, phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

# s followed by zero or more d's
test_patterns = ['sd*']
# s followed by one or more d's
test_patterns = ['sd+']
# s followed by zero or one d
test_patterns = ['sd?']
# s followed by three d
test_patterns = ['sd{3}']
# s followed by one or three d
test_patterns = ['sd{1,3}']
# s followed one or more(either s or d's)
test_patterns = ['s[sd]+']
multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'
# for remove use ^ means exclude one or more instances
test_patterns = ['[^!.?]+']
test_patterns = ['[A-Z]+']
multi_re_find(test_patterns, test_phrase)

test_phrase = 'TYh12asdd 1231212dd'
# returns sequence of digits
# fir white space '\s'
# not white space '\S'
# alphanumeric '\w'
# non alphanumeric '\W'
test_patterns = [r'\d+']
multi_re_find(test_patterns, test_phrase)