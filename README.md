# CRE Stress Test Simulator
Author: Dylan Todd
Created: 12.04.23
Updated: 12.04.23  

## Project Overview
This Flask-based web application simulates stress scenarios in commercial real estate lending. It allows users to input various parameters and assesses the impact on key loan performance metrics.

## Directory Structure
CRE_Stress_Test_Simulator/
├── app.py                   # Main Flask application file
├── templates/               # HTML templates for the web interface
│   ├── index.html           # Input form for scenario parameters
│   └── result.html          # Displays the simulation results
├── static/                  # Static files like CSS and JS
└── README.md                # Project description and instructions

## Setup and Running
- Install Flask: `pip install Flask`
- Clone the repository and navigate to the project directory.
- Run the application: `FLASK_APP=app.py flask run`
- Access the web interface at `http://localhost:5000`.

## Application Flow
- Users input various CRE lending parameters on the homepage.
- The app simulates stress scenarios based on these inputs.
- Results, including the impact on loan performance, are displayed.

## Stress Test Simulation
The simulation considers factors like market fluctuations, rent roll changes, and construction budget overruns. It analyzes key metrics like debt service coverage ratio and loan-to-value ratio.
