RUNTEST=python3 -m unittest -v -b

ALLMODULES=$(patsubst %.py, %, $(wildcard test_*.py))

.PHONY: tests build clean

default: clean build
upload: upload_testpypi upload_pypi

tests:
	${RUNTEST} ${ALLMODULES}

% : test_%.py
	${RUNTEST} test_$@

generate: china_cities/cities.csv
	python3 generate/generate.py

install:
	python2 setup.py install && python3 setup.py install

build:
	python2 setup.py sdist bdist_wheel && python3 setup.py sdist bdist_wheel

clean:
	rm -rf ./build ./dist ./*.egg-info ./*/__pycache__ ./*/*.pyc

upload_testpypi:
	twine upload --repository testpypi dist/*

upload_pypi:
	twine upload --repository pypi dist/*
