# Define variables
VENV_DIR := venv
PYTHON := python3
PIP := $(VENV_DIR)/bin/pip
PYTHON_BIN := $(VENV_DIR)/bin/python

# Default target
.DEFAULT_GOAL := help

# Help text
help:
	@echo "Usage:"
	@echo "  make install      Set up the virtual environment and install dependencies"
	@echo "  make run          Run the Flask application"
	@echo "  make clean        Remove virtual environment and temporary files"

# Install dependencies and set up the virtual environment
install: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	@echo "Setting up virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Virtual environment set up successfully."

# Run the Flask application
run: $(VENV_DIR)/bin/activate
	@echo "Running Flask application..."
	$(PYTHON_BIN) main.py

# Clean up
clean:
	@echo "Removing virtual environment and temporary files..."
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +
	@echo "Clean-up complete."
