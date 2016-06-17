#!/usr/bin/env python
"""
Autocompletion example with cursor position not at the end of the completion.

Press [Tab] to complete the current word.
- The first Tab press fills in the common part of all completions
    and shows all the completions. (In the menu)
- Any following tab press cycles through all the possible completions.
"""
from __future__ import unicode_literals

from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit import prompt

completions = [
    ('upper_case()', 1),
    ('lower_case()', 1),
    ('list_add(list:=, element:=)', len(', element:=)')),
    ('<html></html>', len('</html>'))
]
words, cursor_positions = zip(*completions)
comp = WordCompleter(words, ignore_case=True, cursor_positions=cursor_positions)

def main():
    text = prompt('Input: ', completer=comp,
                  complete_while_typing=False)
    print('You said: %s' % text)


if __name__ == '__main__':
    main()
