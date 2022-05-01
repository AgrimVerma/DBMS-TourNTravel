from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=35, unique=True, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class location(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=2)
    country = models.CharField(max_length=2, default='US')
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class attraction(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    location = models.ForeignKey(
        location, on_delete=models.CASCADE)

    # city = models.CharField(max_length=30, default='Stony Brook')
    attractionName = models.CharField(max_length=30)
    attractionDescription = models.CharField(max_length=1000)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.attractionName


class flight(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    departureDate = models.DateField()
    sourceLocation = models.CharField(max_length=30)
    destinationLocation = models.CharField(max_length=30)
    fareEconomy = models.DecimalField(max_digits=6, decimal_places=2)
    fareBusiness = models.DecimalField(max_digits=6, decimal_places=2)
    fareFirst = models.DecimalField(max_digits=6, decimal_places=2)
    numSeatsRemainingEconomy = models.IntegerField()
    numSeatsRemainingBusiness = models.IntegerField()
    numSeatsRemainingFirst = models.IntegerField()

    def __str__(self):
        return str(self.id)


class hotel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    dailyCost = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    companyName = models.CharField(max_length=30, default='hotel')

    def __str__(self):
        return self.companyName


class train(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    departureDate = models.DateField()
    sourceLocation = models.CharField(max_length=30)
    destinationLocation = models.CharField(max_length=30)
    fareEconomy = models.DecimalField(max_digits=6, decimal_places=2)
    fareBusiness = models.DecimalField(max_digits=6, decimal_places=2)
    fareFirst = models.DecimalField(max_digits=6, decimal_places=2)
    numSeatsRemainingEconomy = models.IntegerField()
    numSeatsRemainingBusiness = models.IntegerField()
    numSeatsRemainingFirst = models.IntegerField()

    def __str__(self):
        return str(self.id)


class review(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    submissionDate = models.DateField(auto_now=True)


class payment(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
    cardNo = models.CharField(max_length=16)

    def __str__(self):
        return str(self.id)


class booking(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    startDate = models.DateTimeField(auto_now=True)
    # TRANSPORTATION_TYPES = [('flight'), ('train')]
    # classType = models.CharField(max_length=10)

    Flight = models.ForeignKey(
        flight, on_delete=models.CASCADE, default=None, null=True)
    Train = models.ForeignKey(
        train, on_delete=models.CASCADE, default=None, null=True)
    Hotel = models.ForeignKey(
        hotel, on_delete=models.CASCADE, default=None, null=True)

    # Type = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.id)


class purchase(models.Model):
    transactionDate = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    Type = models.CharField(max_length=10, default="", null=True)
    bookingID = models.ForeignKey(
        booking, on_delete=models.CASCADE)
    paymentID = models.ForeignKey(
        payment, on_delete=models.CASCADE)
