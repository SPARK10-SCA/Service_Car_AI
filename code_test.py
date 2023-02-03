print('앞범퍼(스틸형)하단'.find("프런트범퍼" or '앞범퍼'))

print(any('앞범퍼(스틸형)하단'.find(i) for i in ('asdg','sadf')))

my_str = 'apple, egg, avocado'
list_of_strings = ['apple', 'banana', 'kiwi']

# ✅ check if ONE of multiple strings exists in another string

if any(substring in 'apple, egg, avocado' for substring in ['saf', 'asg', 'asf']):
    # 👇️ this runs
    print('At least one of the multiple strings exists in the string')
else:
    print('None of the multiple strings exist in the string')