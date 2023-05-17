from django.db import models

class ModelName(models.Model):
    name_string = models.CharField(max_length=50)
    # max_length - максимальная длина строки
    age_int = models.IntegerField(verbose_name="Возраст")
    # verbose_name - это то, что будет отображаться в админке
    email_string = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)
    # blank=True - поле может быть пустым ""
    # null=True - поле можно не заполнять
    float_number = models.FloatField(verbose_name="Число с плавающей точкой")
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True - поле заполняется автоматически при создании объекта
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True - поле заполняется автоматически при каждом обновлении объекта
    birthday = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    text = models.TextField(verbose_name="Текст", blank=True, null=True)

    def __str__(self):
        return self.name_string
    
    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        # verbose_name - это то, что будет отображаться в админке
        # verbose_name_plural - это то, что будет отображаться в админке во множественном числе
        ordering = ["-name_string", "age_int"]

class SecondModel(models.Model):
    model_name = models.ForeignKey(ModelName, verbose_name="Связанная модель", on_delete=models.CASCADE, related_name="second_models")
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50,null=True,blank=True)
    third = models.CharField(max_length=50, default="default value")
    four = models.DateField()
    six = models.IntegerField(default=0)
    seven = models.FloatField(default=0.0)
    eight = models.TextField(default="default text")
    nine = models.CharField(max_length=50, null=True, blank=True)

    # ForeignKey - поле для связи с другой моделью
    # on_delete=models.CASCADE - при удалении объекта из связанной модели, объекты из этой модели тоже удалятся
    # on_delete=models.SET_NULL - при удалении объекта из связанной модели, в поле связанной модели будет записано NULL (null=True обязательно)
    # on_delete=models.SET_DEFAULT - при удалении объекта из связанной модели, в поле связанной модели будет записано значение по умолчанию (default=)
    # on_delete=models.PROTECT - при удалении объекта из связанной модели, объекты из этой модели не удалятся
    # related_name="second_models" - имя для обратной связи

    def __str__(self):
        return f"{self.model_name.name_string}"
    
    class Meta:
        verbose_name = "Вторая модель"
        verbose_name_plural = "Вторые модели"
        ordering = ["-model_name"]
