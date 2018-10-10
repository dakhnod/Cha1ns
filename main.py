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
			print("matching output " + chain[1].__name__ + " to input " + chain[0])
			chain[-1](args)
		else:
			print("no output to input " + name)

def chain(inputModule, *outputModules, callback):
	chain = [inputModule.__name__]
	if inputModule not in moduleObjects:
		name = inputModule.__name__.split(".")[1].capitalize()
		clas = getattr(inputModule, name)
		object = clas()
		if hasattr(object, "setup"):
			object.setup(rcallback)
		moduleObjects[inputModule] = object
	for outputModule in outputModules:
		if outputModule not in moduleObjects:
			name = outputModule.__name__.split(".")[1].capitalize()
			clas = getattr(outputModule, name)	
			moduleObjects[outputModule] = clas
			object = clas()
			if hasattr(object, "setup"):
				object.setup()
			moduleObjects[outputModule] = object
		chain.append(outputModule)
	chain.append(callback)
	chains.append(chain)

def setupChains():
	package = Chains
	for importer, modname, ispackage in pkgutil.iter_modules(package.__path__):
		module = getattr(Chains, modname)
		if hasattr(module, "setup"):
			setupFunction = getattr(module, "setup")
			print("setting up chain " + modname)
			setupFunction(chain, moduleObjects)
		else:
			print("chain " + modname + " has no setup")
	#print(moduleObjects)
	#print(chains)


setupChains()
time.sleep(60)
