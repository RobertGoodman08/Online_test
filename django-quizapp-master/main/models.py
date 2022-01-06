from django.db import models
import random

# project quizes Пагинация


DIFF_CHOICES = (
    ('легкий', 'легкий'),
    ('средний', 'средний'),
    ('сложные', 'сложные'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120, verbose_name='тема')
    number_of_questions = models.IntegerField(verbose_name='количество вопросов')
    required_score_to_pass = models.IntegerField(help_text="требуемый балл в %")
    difficluty = models.CharField(max_length=50, choices=DIFF_CHOICES, verbose_name='трудность')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name = ' Группировать вопросы'
        verbose_name_plural = 'Группировать вопросы'