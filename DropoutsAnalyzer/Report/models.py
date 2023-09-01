from django.db import models


class School(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    caste = models.CharField(max_length=20, choices=[('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('OBC', 'Other Backward Class'), ('GEN', 'General')])
    age = models.IntegerField()
    standard = models.IntegerField()

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name


class Dropout(models.Model):
    REASON_CHOICES = [
        ('lack_of_interest', 'Lack of Interest'),
        ('financial_issues', 'Financial Issues'),
        ('personal_reasons', 'Personal Reasons'),
        ('academic_difficulties', 'Academic Difficulties'),
        ('other_reason', 'Other Reason')
    ]

    reason = models.CharField(
        max_length=50,
        choices=REASON_CHOICES,
        default='lack_of_interest'
    )

    custom_reason = models.TextField(
        blank=True,
        null=True,
        verbose_name="Custom Reason",
        help_text="Please provide your custom reason here if you selected 'Other Reason' above."
    )

    date = models.DateField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='dropout')

    def save(self, *args, **kwargs):
        if self.reason != 'other_reason':
            self.custom_reason = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reason
