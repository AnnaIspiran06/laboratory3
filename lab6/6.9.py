import re

def count_operations(expression):
    operators = re.findall(r'\*\*|//|[+\-*/%]', expression)
    return len(operators)


input_expression = input()
operations_count = count_operations(input_expression)
print(operations_count)
