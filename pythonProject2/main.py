class Author(models.Model):
    full_name = models.CharField()
    name = models.CharField(null=True)

    def some_method(self):
        self.name = self.full_name.split()[0]

    self.save()