from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    """
    Add a new task to the tasks list.
    
    Args:
        title (str): The task title
        description (str): The task description
        due_date (str): The due date in YYYY-MM-DD format
        
    Returns:
        dict: The created task dictionary or None if validation fails
    """
    try:
        # Validate inputs
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
        
        # Create task dictionary
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        
        # Add to tasks list
        tasks.append(task)
        print("Task added successfully!")
        return task
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def mark_task_as_complete(index):
    """
    Mark a task as complete by its index.
    
    Args:
        index (int): The index of the task to mark as complete
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task index.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def view_pending_tasks():
    """
    Display all pending (incomplete) tasks.
    
    Returns:
        list: List of pending tasks
    """
    pending = [task for task in tasks if not task["completed"]]
    
    if not pending:
        print("No pending tasks!")
        return pending
    
    print("\nPending Tasks:")
    print("-" * 80)
    for i, task in enumerate(pending):
        print(f"{i + 1}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Status: {'Completed' if task['completed'] else 'Pending'}")
        print("-" * 80)
    
    return pending

def calculate_progress(tasks_list=None):
    """
    Calculate the progress of task completion.
    
    Args:
        tasks_list (list): Optional list of tasks. Uses global tasks if not provided.
        
    Returns:
        dict: Dictionary containing progress information
    """
    if tasks_list is None:
        tasks_list = tasks
    
    if len(tasks_list) == 0:
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "progress_percentage": 0
        }
    
    total = len(tasks_list)
    completed = sum(1 for task in tasks_list if task["completed"])
    pending = total - completed
    progress_percentage = (completed / total) * 100 if total > 0 else 0
    
    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "progress_percentage": round(progress_percentage, 2)
    }
