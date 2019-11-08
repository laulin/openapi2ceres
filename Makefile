build:
	rm -rf dist/ build/
	python3 setup.py sdist bdist_wheel

install: build 
	pip3 install dist/openapi2ceres*.whl

build_docker: build
	docker build -t openapi2ceres .

run: build
	docker run -it --rm --name openapi2ceres openapi2aceres /bin/bash

test: build
	docker run -it --rm --name openapi2ceres openapi2ceres /usr/bin/python3 -m openapi2ceres -i example/petstore.yaml -o example/

unittest:
	docker run -it --rm --name openapi2ceres openapi2ceres /usr/bin/python3 -m unittest discover "tests/" -p "test_*.py"

clean:
	rm -rf dist/ build/
	rm example/*.yml
	docker images | grep "<none>" | grep -o -E "[0-9a-f]{12,12}" |xargs docker rmi -f