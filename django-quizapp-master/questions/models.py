from django.db import models
from main.models import Quiz



class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='текст')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False, verbose_name='ответ на вопрос')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'