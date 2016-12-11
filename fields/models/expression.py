# Representation of an expression
#
# An expression is a field based on zero or more
# columns or other expressions
#
# The idea is that we can use the relationship between
# expressions, (base) columns, and tables to dynamically
# determine the set of CTEs needed to generate a SQL
# statement
