import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list, creates a CSV file, and writes the data.
    
    Args:
        employee_id (int): The ID of the employee for whom to fetch TODO list and create a CSV file.
    """
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee_data = employee_response.json()
    employee_username = employee_data['username']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()

    # Export TODO list data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            task_completed = "True" if todo["completed"] else "False"
            writer.writerow([employee_id, employee_username,task_completed, todo["title"]])

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
