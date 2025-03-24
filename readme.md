# Verdad Sage Research 
Factor generation and testing for systematic trading strategy.

## Python Environment Set-up 
0. Open Terminal (Mac/Linux) or Command Prompt (Windows)
    - Navigate to the desired parent directory where you want to clone the repository:
    ```
    $ cd /path/to/your/directory  # Replace with your actual path
    ```
    - Clone repository 
        - For Mac/Linux (using SSH):
            ```
            # git clone git@github.com:alberttangalbert/insider-transaction-research.git
            ```
            Ensure you have SSH access set up with GitHub before using this method.
        - For Windows (using HTTPS):
            ```
            $ git clone https://github.com/alberttangalbert/insider-transaction-research.git
            ```
            If using SSH on Windows, ensure you have an SSH key set up with GitHub and use the SSH version instead.
1. Make sure to have Python 3.13.1 installed 
    ```
    $ python3 --version
    Python 3.13.1
    ```
3. Create environment
   ```
   $ python3 -m venv venv
   ```
4. Activate the virtual environment
    > Linux/macOS
    ```
   $ source venv/bin/activate
   ```
   > Windows Git Bash 
   ```
   $ source venv/Scripts/activate
   ```
5. Install requirements
    ```
   $ pip install -r requirements.txt 
   ```
7. Add folders for storing data
    ```
    mkdir data/processed
    mkdir data/raw
    ```

## Retrive Data 
1. Configure Snowflake Environemnt
    - Log into the `PSA31288.us-east-1` Snowflake account
    - Navigate to `Projects` and create new SQL Worksheet
    - Select `Intern` for `Role` and `COMPUTE_WH` for `Run on Warehouse`
    - Select `BIOTECH_PROJECT` for `Databases` and `READ_ONLY` for `Schemas`
2. Non-derivative Transactions 
    - Copy paste code from this [file](sql/fetch_ndt.sql) and run
    - Verify there are 4812408 rows 
    - Download the results as a .csv file
    - Save the file in `data` folder as `ndt.csv`
3. Returns and Market cap 
    - Copy paste code from this [file](sql/fetch_returns_market_cap.sql) and run
    - Verify there are 3868011 rows 
    - Download the results as a .csv file
    - Save the file in `data` folder as `returns_market_cap.csv.csv`

## Run Analyses
- [Cluster Buying Analysis](notebooks/cluster_buying.ipynb)
- [Net Transaction Analysis](notebooks/net_transaction.ipynb)
- [Non-routine Trading Analysis](notebooks/non_routine.ipynb)
- [Percent Shares Analysis](notebooks/percent_shares.ipynb)