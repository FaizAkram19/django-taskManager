from django.db import models

# Create your models here.
class Priority(models.Model):
    levels = (
        ("1","High"),
        ("2","Medium"),
        ("3", "Low")
    )
    priority_idx= models.CharField(max_length=1, choices=levels)

    def __str__(self):
        return self.get_priority_idx_display() # to display the name of the choice and not 1,2,3 
    
class Task(models.Model):
    priorityLevel=models.ForeignKey(Priority, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)#This makes the pub_date get the datetime of when the object is saved, never changes
    updated_at=models.DateTimeField(auto_now=True)#This adds the date and time of whenever any changes to the object were made and saved
    due_date=models.DateTimeField("Due Date")
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title