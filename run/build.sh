#!/bin/bash

# Change to the parent directory
cd ..

# Install necessary dependencies
pip install -r requirements.txt

# Run the main consumer application
python main.py &

# Run the company application 
python company_main.py &