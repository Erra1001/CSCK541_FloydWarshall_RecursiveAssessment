# CSCK541_FloydWarshall_RecursiveAssessment

The Floyd-Warshall algorithm is implemented in this repository using both an imperative and a recursive approach. The codebase includes unit tests as well as performance tests for evaluation.

## Methodology

This project was developed with a focus on comparing iterative and recursive implementations of the Floyd-Warshall algorithm. We have included unit tests for both versions and performance tests to evaluate the efficiency of each approach.

## Installation and Execution

### Installation

1. Download the repository by clicking the "Download ZIP" button on GitHub, or clone the repository using the following command:

    ```bash
    git clone https://github.com/Erra1001/CSCK541_FloydWarshall_RecursiveAssessment.git
    ```

2. Navigate into the directory:

    ```bash
    cd CSCK541_FloydWarshall_RecursiveAssessment
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Code

You can run the code in two ways:

1. Through any Python IDE (PyCharm, Jupyter, etc.)
    - Open `floyd_recursive.py` or `floyd_iterative.py` and run the script.

2. Through the command line
    - Navigate to the folder `CSCK541_FloydWarshall_RecursiveAssessment` and execute the following command to run unit tests:

        ```bash
        python -m unittest test_floyd_recursive.py
        ```
        
        ```bash
        python -m unittest test_floyd_iterative.py
        ```

    - To run performance tests:

        ```bash
        python performance_floyd.py
        ```

## Upcoming Features and TODOs
- Add more unit tests for edge cases.
- Explore and implement optimization techniques for both versions.

## Accessibility

This repository is public and can be accessed directly from the link provided in this report and any other submitted materials.

Feel free to explore and adapt as per your needs!
