from django.db import models

# Create your models here.


class CoursesAvailable(models.Model):
	couse_name = models.CharField(max_length=255)
	couse_videos = models.CharField(max_length=255)
	couse_video_title = models.CharField(max_length=255)
	couse_video_description = models.CharField(max_length=255)
	couse_video_url = models.CharField(max_length=2083)
	couse_image_url = models.CharField(max_length=2083)
	couse_video_owner = models.CharField(max_length=255)
	couse_video_duration = models.CharField(max_length=255)


class CourseImages(models.Model):
	course_name = models.CharField(max_length=255)
	course_description = models.CharField(max_length=255)
	Image_course_name = models.CharField(max_length=2083)

class EmailReciever(models.Model):
	sender_name = models.CharField(max_length=255)
	sender_email = models.CharField(max_length=255)
	send_message = models.CharField(max_length=4000)










