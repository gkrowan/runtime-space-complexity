# runtime-space-complexity
MS-ADS Realtime Intelligent Systems Assignment 2

- Design and implement a Python module that ingests market data from a CSV file and applies multiple trading strategies with varying runtime and space complexities. You will analyze, compare, and optimize the performance of these strategies using profiling tools and theoretical Big-O analysis. The goal is to understand how algorithmic design choices affect both execution time and memory usage in financial systems.

- This assignment emphasizes computational efficiency, profiling, and performance visualization—critical skills for building scalable trading infrastructure.

## Environment Set Up 
- Create and activate a virtual environment in the project root
- Run the following command to install required pachages: 
    pip install -r requirements.txt

## Data Generation
- To generate synthetic market data, run: python generate_data.py
- Alternatively, use data/market_data.csv, which has already been generated using this process 

## How to Run the Process
- to execute the entire process, run: python main.py 
- This will execute: 
    - Loading the market data
    - Running the strategies on different subsets of the data
    - Recording and visualising the results 

## How to Run tests
- run: pytest
- pytest will automatically detect the unit test files in the test/ folder
- PASS/FAIL results will display in terminal
