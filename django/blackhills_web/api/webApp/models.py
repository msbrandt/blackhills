from django.contrib.gis.db import models

# Create your models here.
class DeerHarvest(models.Model):
	unit_number = models.IntegerField()
	bucks = models.IntegerField()
	does = models.IntegerField() 
	total_harvest = models.IntegerField()
	total_hunters = models.IntegerField()
	total_rec_days = models.IntegerField()
	percent_sucess = models.FloatField()
	section_title = models.IntegerField()



class PronhornHarvest(models.Model):
	unit_number = models.IntegerField()
	bucks = models.IntegerField()
	does = models.IntegerField()
	total_harvest = models.IntegerField()
	total_hunters = models.IntegerField()
	total_rec_days = models.IntegerField()
	percent_sucess = models.IntegerField()
	section_title = models.IntegerField()

	def __str__(self):
		return "Unit Number:%s - %s" % (self.unit_number, self.section_title)


class ElkHarvest(models.Model):
	unit_number = models.IntegerField()
	bulls = models.IntegerField()
	cows = models.IntegerField()
	total_harvest = models.IntegerField()
	total_hunters = models.IntegerField()
	total_rec_days = models.IntegerField()
	percent_sucess = models.IntegerField()
	section_title = models.IntegerField()

	def __str__(self):
		return "Unit Number:%s - %s" % (self.unit_number, self.section_title)


class Unit(models.Model):
	unit_number = models.IntegerField()
	total_public = models.FloatField()
	total_private = models.FloatField()
	polygon = models.MultiPolygonField()
	center_point = models.PolygonField()
	square_feet = models.FloatField(default=0.0)


class PublicLand(models.Model):
	unit_number = models.IntegerField()
	land_type = models.IntegerField()
	polygon = models.MultiPolygonField()
	center_point = models.PolygonField()
	square_feet = models.FloatField(default=0.0)


class LandTypes(models.Model):
	type_name = models.CharField(max_length=50)
	type_desc = models.CharField(max_length=255)


class WalkInAccess(models.Model):
	unit_number = models.IntegerField()
	land_type = models.IntegerField()
	polygon = models.MultiPolygonField()
	center_point = models.PolygonField()
	square_feet = models.FloatField(default=0.0)


class HarvestTitles(models.Model):
	title = models.CharField(max_length=100)
