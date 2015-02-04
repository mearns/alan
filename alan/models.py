from django.db import models

class MarkupTextField(models.TextField):
    """
    Used for free form fields that can include markup.
    """
    pass

class Task(models.Model):

    name = models.CharField(
        max_length=255,
        help_text='A name used to identify this task. Should provide a terse summary of the task.',
    )

    description = MarkupTextField(
        help_text='Describe the work to be done in sufficient detail that it can be completed.',
        blank=True,
    )

