import pyautogui
import time

# Give yourself a few seconds to click on the window where you want to type the code
time.sleep(5)

# Define the code as a string with proper syntax
code = '''
SELECT 
    c.name AS client_name,
    ROUND(SUM(CASE WHEN bi.invested_amount IS NOT NULL THEN bi.invested_amount ELSE 0 END), 2) AS total_invested_in_bonds,
    ROUND(SUM(CASE WHEN si.invested_amount IS NOT NULL THEN si.invested_amount ELSE 0 END), 2) AS total_invested_in_stocks
FROM 
    clients c
LEFT JOIN 
    bonds_investments bi ON c.id = bi.client_id
LEFT JOIN 
    stocks_investments si ON c.id = si.client_id
GROUP BY 
    c.id, c.name
HAVING 
    SUM(CASE WHEN bi.invested_amount IS NOT NULL THEN bi.invested_amount ELSE 0 END) > 5000.00
ORDER BY 
    total_invested_in_bonds DESC;
'''

# Split the code into lines and process each line individually
for line in code.splitlines():
    # Trim leading and trailing whitespaces from each line
    stripped_line = line.lstrip()
    # Calculate the number of leading spaces (indentation level)
    indentation = len(line) - len(stripped_line)
    # Type the line with the calculated indentation
    pyautogui.write(' ' * indentation + stripped_line, interval=0.001)
    # Press enter to move to the next line
    pyautogui.press("enter")
