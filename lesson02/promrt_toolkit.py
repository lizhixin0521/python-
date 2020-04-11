#!/usr/bin/env python3
from prompt_toolkit import prompt
from prompt_toolkit.history  import FileHistory#按向上的按键，可以查看输入的历史
from prompt_toolkit.auto_suggest  import AutoSuggestFromHistory#输入内容时会提示之前的输过的内容
#from prompt_toolkit.contrib.completers import WordCompleter
#SQLCompleter=WordCompleter(['select','from','insert','update','delete','drop'],ignore_case=True)
while True:
	user_input=prompt('>',
				history=FileHistory('history.txt'),
				auto_suggest=AutoSuggestFromHistory(),
				#completer=SQLCompleter,
				)
	print(user_input)
	
