reinstall: cos/scripts/cosenv
	pip install -e .

fix-import: install-requires redo-imports remove-install-requires clr

install-requires:
	pip install reorder-python-imports

remove-install-requires:
	pip uninstall aspy.refactor-imports cached-property reorder-python-imports -y

redo-imports:
	reorder-python-imports cos/commands/*.py
	reorder-python-imports cos/services/*.py
	reorder-python-imports cos/*.py
	
clean:
	rm -rf dist/ build/

upload:
	python setup.py sdist bdist_wheel
	# twine upload dist/*

uc: upload clean clr

clr:
	clear