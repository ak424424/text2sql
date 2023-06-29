# Further improvement
# 1. Spelling correction through enriching algorithm with database information.
# For example, user types table name as 'analitics' and algorithm suggests to change naming to 'analytics'
# since there is no such table
# 2. Generate the list of possible tables and columns based on question. Currently, user needs to provide information
# what table to use and what columns, by enriching algorithm with database information the model can suggest tables
# and columns
# 3. Introduce more sophisticated SQL queries

# Model evaluation
# 1. Exact match of the model's response and actual answer
# 2. Match of SQL query output from the model's response and actual answer to cope with semantic errors
# 3. Failure analysis - analysis of failed generated SQL queries