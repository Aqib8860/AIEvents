from django.db import models


EVENT_CATEGORY = (
    ("Health", "Health"),
    ("Games", "Games"),
    ("Meetups", "Meetups"),
    ("Music", "Music"),
    ("Art", "Art"),
    ("Food", "Food"),
    ("Business", "Business"),
    ("Sports", "Sports"),
)

EVENT_TYPE = (
    ("Offline", "Offline"),
    ("Online", "Online"),
    ("Outdoor", "Outdoor"),
)

ENTRY_TYPE = (
    ("Free", "Free"),
    ("Paid", "Paid"),
)


class Events(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    event_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=EVENT_CATEGORY)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE)
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE)
    entry_fee = models.PositiveIntegerField()
    organizer_name = models.CharField(max_length=50)
    description = models.TextField()
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    booking_open = models.BooleanField()
    add_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="events")

    def __str__(self):
        return str(self.event_name)

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
