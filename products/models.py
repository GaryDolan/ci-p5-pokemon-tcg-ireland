"""
Models for products app
"""
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

# Tuple to control product sale status
STATUS = ((0, "Not On sale"), (1, "On Sale"))


class Category(models.Model):
    """Model to represent a product category"""
    class Meta:
        """
        Meta class to define verbose name
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        """Returns the category display name"""
        return self.display_name


class CardSet(models.Model):
    """Model to represent the card set of a product"""
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        """Returns the card set display name"""
        return self.display_name


class Expansion(models.Model):
    """Model to represent the expansion of a product"""
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        """Returns the expansion display name"""
        return self.display_name


class Product(models.Model):
    """Model to represent a product"""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    card_set = models.ForeignKey(
        'CardSet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    expansion = models.ForeignKey(
        'Expansion',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pre_sale_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    on_sale = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    def get_num_reviews(self):
        """Returns the number of reviews attached to a product"""
        review_count = 0
        reviews = Review.objects.filter(product=self, approved=True)
        review_count = reviews.count()
        return review_count

    def get_avg_rating(self):
        """Returns the average review rating of a product"""
        reviews = Review.objects.filter(product=self, approved=True)
        # Perform aggregation to calculate the average rating
        rating_aggregation = reviews.aggregate(Avg('review_rating'))

        # Get the average rating from the aggregation result
        # Results of an agg are stored in fieldname__avg
        average_rating = rating_aggregation['review_rating__avg']

        # return an int if specified
        if average_rating is not None:
            return average_rating
        else:
            return 0

    # Returns a list with a number of iterable elements
    # equal to nearest whole num of average rating
    # so 3.6 would round to and return [0,1,2,3]
    def get_avg_num_of_stars_list(self):
        """Returns a list with 1 element per star based on average rating """
        reviews = Review.objects.filter(product=self, approved=True)
        # Perform aggregation to calculate the average rating
        rating_aggregation = reviews.aggregate(Avg('review_rating'))

        # Get the average rating from the aggregation result
        # Results of an agg are stored in fieldname__avg
        average_rating = rating_aggregation['review_rating__avg']

        # return a list with number of entries = average rating val
        stars = []
        if average_rating is not None:
            rounded_rating = round(average_rating)
            for i in range(rounded_rating):
                stars.append(i)
        return stars


class Review(models.Model):
    """Model to represent a product review"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    review_rating = models.IntegerField()
    review_text = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"
