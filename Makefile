reinstall: cos/scripts/cosenv
	pip install -e .

clean:
	rm -rf dist/ build/