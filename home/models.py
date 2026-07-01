from django.db import models


class Student(models.Model):

    STATUS_CHOICES = [
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    admission_number = models.CharField(max_length=30)

    branch = models.CharField(max_length=50)

    year = models.IntegerField()

    contact_number = models.CharField(max_length=10)

    component_name = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField(default=1)

    componentissue_date = models.DateField()

    componentdue_date = models.DateField()

    faculty_referred = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Issued"
    )

    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "students"

    def __str__(self):
        return f"{self.name} - {self.component_name}"


class MaintenanceHistory(models.Model):

    student_name = models.CharField(max_length=100)

    admission_number = models.CharField(max_length=30)

    component_name = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField()

    deleted_on = models.DateTimeField(auto_now_add=True)

    deleted_by = models.CharField(max_length=100)

    reason = models.CharField(
        max_length=200,
        default="Deleted by Admin"
    )

    class Meta:
        db_table = "maintenance_history"

    def __str__(self):
        return self.component_name