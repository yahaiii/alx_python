import json
import requests
import sys

def export_employee_todo_progress_to_json(employee_id):
    """
    Fetches an employee's TODO list and creates a JSON file with the data.

    Args:
        employee_id (int): The ID of the employee for whom to fetch TODO list and create a JSON file.
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

    # Create JSON data in the desired format
    json_data = {
        str(employee_id): [
            {"task": todo["title"], "completed": todo["completed"], "username": employee_username}
            for todo in todos_data
        ]
    }

    # Create JSON file and write data
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todo_progress_to_json(employee_id)
