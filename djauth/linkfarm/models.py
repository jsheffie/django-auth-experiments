from django.db import models

class LinkFarm( models.Model ):
	name = models.CharField( max_length = 60 )
	# Using charField here for simplicipity for now
	link = models.CharField( max_length = 512 )

	def __unicode__( self ):
		return self.name