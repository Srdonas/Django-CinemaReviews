from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, FileExtensionValidator

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
    ]

    title = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(100), MinLengthValidator(3)]
    )
    description = models.TextField(
        max_length=500,
        validators=[MaxLengthValidator(500), MinLengthValidator(10)]
    )
    release_date = models.DateField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    image = models.ImageField(
        upload_to="movies",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpg', 'png'])]
    )

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['id']

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    autor = models.CharField(max_length=100)
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )  # 1 to 5 stars
    comments = models.TextField()

    def __str__(self):
        return f'Review by {self.autor} for {self.movie}'
