ALL = .

help: ## Show this help message.
	@echo 'Usage:'
	@echo
	@grep --no-filename -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "------------------------------------"

install-pyenv: ## Install pyenv on bash shell
	curl https://pyenv.run | bash
	export PATH="$HOME/.pyenv/bin:$PATH"
	eval "$(pyenv init --path)"
	eval "$(pyenv init -)"
	source ~/.bashrc
	pyenv install 3.8.12
	pyenv local 3.8.12

install-requirements: ## Install only requirements
	pip install poetry
	poetry install

start-db: ## Start database for first time
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

create-venv: ## Create the virtual environment
	python3 -m venv venv

run: ## Start the repository
	python3 manage.py run

test: ## Run the tests for the project
	python3 manage.py test

test-coverage: ## Run the tests for the project with coverage
	pytest --cache-clear --cov=app ./app/test/ > pytest-coverage.txt

lints: ##Run the lints  to check the project
	flake8 app/ --exclude __init__.py
