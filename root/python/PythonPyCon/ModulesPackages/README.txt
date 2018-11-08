Any Python source file is a module 
	# spam.py
	def grok(x):
		...
	
	def blah(x):
		...

Import to execute and access it
	import spam 
	a = spam.grok('hello')

	from spam import grok 
	a = grok('hello')

Each module is its own isolated world 

Global variables bind inside the same module 

Functions record their definition environment 
__module__
__globals__

When a module is imported, all of the statements in the module execute one 
after another until the end of the file is reached

from module import *
	Takes all symbols from a module and places them into local scope 

It is standard practire for package and module names to be concise and lowercase 

Use a leading underscore for modules that are meant to be private or internal 

Module Search Path 
	If a isn't on the path, it won't import 
		>>> import sys 
		>>> sys.path 
	Sometimes you might hack it 
		>>> import sys 
		>>> sys.path.append("/project/foo/myfiles")

Model Cache
	Modules only get loaded once 
	There's cache behind the scenes 
	Consequence: If you make a change to the source and repeat the import, 
	nothing happens.

