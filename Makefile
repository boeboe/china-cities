RUNTEST=python3 -m unittest -v -b
RUNGENERATE=python3 generate/generate.py

ALLMODULES=$(patsubst %.py, %, $(wildcard test_*.py))

default: tests

tests:
	${RUNTEST} ${ALLMODULES}

% : test_%.py
	${RUNTEST} test_$@

generate: china_cities/cities.csv
	${RUNGENERATE}
