from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, created, edited or deleted.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # Custom business logic methods
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Return only completed tasks"""
        completed_tasks = TaskService.get_tasks_by_status(completed=True)
        serializer = self.get_serializer(completed_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Return only pending (not completed) tasks"""
        pending_tasks = TaskService.get_tasks_by_status(completed=False)
        serializer = self.get_serializer(pending_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """Mark a task as completed"""
        updated_task = TaskService.mark_task_status(pk, completed=True)
        serializer = self.get_serializer(updated_task)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def mark_pending(self, request, pk=None):
        """Mark a task as pending"""
        updated_task = TaskService.mark_task_status(pk, completed=False)
        serializer = self.get_serializer(updated_task)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Get tasks that are overdue"""
        days = int(request.query_params.get('days', 7))
        overdue_tasks = TaskService.get_overdue_tasks(days=days)
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get task statistics"""
        stats = TaskService.get_task_statistics()
        return Response(stats)
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """Delete all tasks"""
        deleted_count = TaskService.delete_all_tasks()
        return Response(
            {"message": f"Successfully deleted {deleted_count} tasks"},
            status=status.HTTP_204_NO_CONTENT
        )
