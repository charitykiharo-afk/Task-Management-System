from datetime import datetime

def validate_task_title(title):
    """
    Validate task title.
    
    Args:
        title (str): The task title to validate
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If title is empty or not a string
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    if not title.strip():
        raise ValueError("Title cannot be empty.")
    return True
    
def validate_task_description(description):
    """
    Validate task description.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If description is empty or not a string
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if not description.strip():
        raise ValueError("Description cannot be empty.")
    return True
    
def validate_due_date(due_date):
    """
    Validate due date format (YYYY-MM-DD).
    
    Args:
        due_date (str): The due date to validate in YYYY-MM-DD format
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If due date is not in valid format or is in the past
    """
    try:
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        # Check if date is not in the past
        if date_obj.date() < datetime.now().date():
            raise ValueError("Due date cannot be in the past.")
        return True
    except ValueError as e:
        if "Due date cannot be in the past" in str(e):
            raise
        raise ValueError("Due date must be in YYYY-MM-DD format.")
