"""
Task Management System - Main Script
This script provides a menu-based interface for managing tasks.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("     TASK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")
    print("=" * 50)

def add_task_menu():
    """Handle adding a new task from user input."""
    print("\n--- Add New Task ---")
    try:
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        
        add_task(title, description, due_date)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

def mark_task_complete_menu():
    """Handle marking a task as complete."""
    print("\n--- Mark Task as Complete ---")
    try:
        if not tasks:
            print("No tasks available.")
            return
        
        # Display all tasks with their indices
        print("\nCurrent Tasks:")
        print("-" * 80)
        for i, task in enumerate(tasks):
            status = "✓ Completed" if task["completed"] else "○ Pending"
            print(f"{i + 1}. {task['title']} - {status}")
            print(f"   Due: {task['due_date']}")
        print("-" * 80)
        
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        mark_task_as_complete(task_index)
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

def view_progress_menu():
    """Display task progress."""
    print("\n--- Task Progress ---")
    progress = calculate_progress()
    
    print(f"Total Tasks: {progress['total_tasks']}")
    print(f"Completed Tasks: {progress['completed_tasks']}")
    print(f"Pending Tasks: {progress['pending_tasks']}")
    print(f"Progress: {progress['progress_percentage']}%")
    
    # Display progress bar
    if progress['total_tasks'] > 0:
        filled = int(progress['progress_percentage'] / 5)
        bar = "█" * filled + "░" * (20 - filled)
        print(f"[{bar}] {progress['progress_percentage']}%")

def main():
    """Main function to run the task management system."""
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                add_task_menu()
            elif choice == "2":
                mark_task_complete_menu()
            elif choice == "3":
                print("\n")
                view_pending_tasks()
            elif choice == "4":
                view_progress_menu()
            elif choice == "5":
                print("\nThank you for using Task Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
