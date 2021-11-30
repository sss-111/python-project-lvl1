# makefile

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
	poetry run flake8 brain_calc
	poetry run flake8 brain_even
	poetry run flake8 brain_gcd
	poetry run flake8 brain_prime
	poetry run flake8 brain_progression
	
.PHONY: brain-games
