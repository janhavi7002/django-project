from django.contrib import admin
from django.utils import timezone

from .models import Student, MaintenanceHistory


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'admission_number',
        'branch',
        'year',
        'contact_number',
        'component_name',
        'quantity',
        'status',
        'componentissue_date',
        'componentdue_date',
        'faculty_referred',
        'is_deleted',
    )

    list_filter = (
        'status',
        'branch',
        'year',
        'is_deleted',
    )

    search_fields = (
        'name',
        'email',
        'admission_number',
        'component_name',
    )

    actions = [
        'move_to_history',
        'restore_records',
    ]

    def move_to_history(self, request, queryset):

        for obj in queryset:

            MaintenanceHistory.objects.create(
                student_name=obj.name,
                admission_number=obj.admission_number,
                component_name=obj.component_name,
                quantity=obj.quantity,
                deleted_by=request.user.username,
                reason="Deleted by Admin"
            )

            obj.is_deleted = True
            obj.deleted_at = timezone.now()
            obj.save()

    move_to_history.short_description = "Move selected records to Maintenance History"

    def restore_records(self, request, queryset):

        queryset.update(
            is_deleted=False,
            deleted_at=None
        )

    restore_records.short_description = "Restore selected records"


admin.site.register(MaintenanceHistory)