#import os
#for module in os.listdir(os.path.dirname(__file__)):
#	if module == '__init__.py' or module[-3:] != '.py':
#		continue
#	print("importing " + module)
#	mod = __import__(module[:-3], locals(), globals(), ["setup"])
#del module
