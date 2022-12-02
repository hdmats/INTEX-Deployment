from django.db import models

# Create your models here.
class condition(models.Model):
  condition_type = models.CharField(max_length=30)

  def __str__(self):
    return self.condition_type
  
  class Meta:
      db_table = 'condition'

class user(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  gender = models.CharField(max_length=6)
  height = models.IntegerField()
  weight = models.IntegerField()
  age = models.IntegerField()
  condition = models.ForeignKey(condition, blank=True, null=True, on_delete=models.DO_NOTHING)
  k = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  phos = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  na = models.IntegerField(blank=True)
  creatinine = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  albumin = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  bloodsugar = models.IntegerField(blank=True)

  @property
  def full_name(self):
    return '%s %s' % (self.first_name, self.last_name)
  
  def __str__(self):
    return self.full_name
  
  class Meta:
      db_table = 'user'

class nutrient(models.Model):
  food = models.CharField(max_length=30)
  measurement = models.CharField(max_length=30)
  sodium = models.IntegerField()
  protein = models.DecimalField(max_digits=5, decimal_places=2)
  water = models.DecimalField(max_digits=5, decimal_places=2)
  k = models.IntegerField()
  phos = models.IntegerField()

  @property
  def portion(self):
    return '%s %s' % (self.food, self.measurement) 
  
  def __str__(self):
    return self.portion
  
  class Meta:
      db_table = 'nutrients'

class journal_entry(models.Model):
  meal_date = models.DateField()
  meal_type = models.CharField(max_length=30)
  user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
  nutrients = models.ManyToManyField(nutrient)

  @property
  def entry(self):
    return '%s %s %s' % (self.meal_date, self.meal_type, self.user.full_name) 
  
  def __str__(self):
    return self.entry
  
  class Meta:
      db_table = 'journal_entry'

