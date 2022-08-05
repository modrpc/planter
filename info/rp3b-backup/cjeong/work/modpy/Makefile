run:
	@python3 -m modpy.shell.main --name shell

node:
	@python3 -m mods.node.main --name `hostname` --rpcport 12346 

upload:
	python setup.py sdist upload -r pypitest
	python setup.py sdist upload -r pypi
