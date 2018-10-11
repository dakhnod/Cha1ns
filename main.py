#!/usr/bin/python

import pkgutil
import Chains
from Chains import *
import time

chains = []
moduleObjects = {}

def rcallback(name, *args):
	for chain in chains:
		if chain[0] == name:
			print("matching chain " + chain[-1].__module__ + " to input " + chain[0])
			chain[-1](args)
		else:
			print("no output to input " + name)

def chain(module_, modules, callback):
	chain = [modules[0].__name__]
	for module in modules:
		if module not in moduleObjects:
			name = module.__name__.split(".")[1].capitalize()
			clas = getattr(module, name)	
			object = clas()
			if hasattr(object, "setup"):
				print("module " + object.__module__ + " setting up...")
				if object.__module__.startswith("Input."):
					object.callback = rcallback
				object.setup()
			moduleObjects[module] = object
		else:
			object = moduleObjects[module]
			print("module " + module.__name__ + " already set up")
		field = object.__module__.replace(".", "_")
		setattr(module_, field, object)
		chain.append(module)
		
	chain.append(callback)
	chain.pop(1)
	chains.append(chain)

def setupChains():
	package = Chains
	for importer, modname, ispackage in pkgutil.iter_modules(package.__path__):
		module = getattr(Chains, modname)
		if hasattr(module, "setup"):
			setupFunction = getattr(module, "setup")
			print("chain " + modname + " setting up")
			args = setupFunction()
			chain(module, args, module.callback)
		else:
			print("chain " + modname + " has no setup")

def cleanupModules():
	for module, object in moduleObjects.items():
		if hasattr(object, "cleanup"):
			print("module " + module.__name__ + " cleaning up")
			object.cleanup()

try:
	setupChains()
	time.sleep(60)
finally:
	cleanupModules()
