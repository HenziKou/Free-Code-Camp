from typing import List

def arithmetic_arranger(problems: List[str], solve = False) -> str:

	top = ""
	bot = ""
	line = ""
	total = ""
	result = ""

	# Limit only 5 problems
	if ( len(problems) > 5 ) : return "Error: Too many problems."

	for problem in problems:
		n1, op, n2 = problem.split()
		offset = max( int(n1), int(n2) ) + 2

		if ( (len(n1) > 4) or (len(n2) > 4) ):
			return "Error: Numbers cannot be more than four digits."

		elif ( (n1.isdigit() == False) or (n2.isdigit() == False) ):
			return "Error: Numbers must only contain digits."

		elif ( (op == "+") or (op == "-") ):
			# Solve
			if (op == "+"):
				val = str( int(n1) + int(n2) )
			else:
				val = str( int(n1) - int(n2) )

			# Formatting strings
			if problem != problems[-1]:
				top += n1.rjust(offset) + "    "
				bot += op + n2.rjust(offset - 1) + "    "
				line += ("-" * offset) + "    "
				total += val.rjust(offset) + "    "
			else:
				top += n1.rjust(offset)
				bot += op + n2.rjust(offset - 1)
				line += ("-" * offset)
				total += val.rjust(offset)

		else:
			return "Error: Operator must be '+' or '-'."

	result += top + '\n' + bot + '\n' + line

	if (solve == True):
		result += total

	return result 

