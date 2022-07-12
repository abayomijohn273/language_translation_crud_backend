from django.db import models

class TranslationsModel(models.Model):

    id=models.AutoField(primary_key=True)
    inputText=models.CharField(max_length=150)
    outputText=models.CharField(max_length=150)

    def __str__(self):
        return self.inputText or ''

    # def get_absolute_url(self):
    #     return reverse("DetailsModel_detail", kwargs={"pk": self.pk})
