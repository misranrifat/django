"""
Services module for task-related business logic.
This layer separates business logic from views and models.
"""
from django.utils import timezone
from .models import Task

class TaskService:
    """Service class for task-related operations."""
    
    @staticmethod
    def get_tasks_by_status(completed=None):
        """
        Get tasks filtered by completion status.
        If completed is None, return all tasks.
        """
        if completed is None:
            return Task.objects.all()
        return Task.objects.filter(completed=completed)
    
    @staticmethod
    def get_overdue_tasks(days=7):
        """Get tasks that have been pending for more than 'days' days."""
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        return Task.objects.filter(
            completed=False,
            created_at__lt=cutoff_date
        )
    
    @staticmethod
    def mark_task_status(task_id, completed):
        """Mark a task as completed or pending."""
        task = Task.objects.get(id=task_id)
        task.completed = completed
        task.save()
        return task
    
    @staticmethod
    def get_task_statistics():
        """Get statistics about tasks."""
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(completed=True).count()
        pending_tasks = total_tasks - completed_tasks
        
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        return {
            'total': total_tasks,
            'completed': completed_tasks,
            'pending': pending_tasks,
            'completion_rate': round(completion_rate, 2)
        }
    
    @staticmethod
    def delete_all_tasks():
        """Delete all tasks from the database."""
        deleted_count, _ = Task.objects.all().delete()
        return deleted_count 