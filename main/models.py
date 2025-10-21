from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Yaratilgan vaqti'), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqti"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        
    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id})>"