from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_custom_employee_ref(sender, instance, created, **kwargs):
    if created:
        instance.employee_ref = str(instance.id).zfill(5)
        instance.username = instance.employee_ref
        instance.save()