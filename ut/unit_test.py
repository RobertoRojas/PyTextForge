import sys

EXPECTED=\
"""This is a list:

- CONTENT_FROM_DATA
- CONTENT_FROM_JSON
- CONTENT_FROM_FILE
- CONTENT_FROM_JSON_FILE
- OVER1
- OVER2"""

def main() -> None:
    with open('./output.txt', 'r') as f:
        content = f.read()
        if content == EXPECTED:
            print('The content is as expected')
            sys.exit(0)
        else:
            print('The content is not the same:')
            print('-' * 15)
            print(EXPECTED)
            print('-' * 15)
            print(f'Len: {len(EXPECTED)}; Expected content;')
            print('-' * 15)
            print(content)
            print('-' * 15)
            print(f'Len: {len(content)}; File=output.txt;')
            sys.exit(1)

if __name__ == '__main__':
    main()