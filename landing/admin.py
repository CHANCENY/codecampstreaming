from django.contrib import admin
from .models import CoursesAvailable, CourseImages, EmailReciever

# Register your models here.


class CoursesAvailableAdmin(admin.ModelAdmin):
	list_display =('couse_name','couse_videos','couse_video_title','couse_video_description','couse_video_owner','couse_video_duration')


class CourseImagesAdmin(admin.ModelAdmin):

	list_display=('course_name','course_description','Image_course_name')


class EmailRecieverAdmin(admin.ModelAdmin):
	list_display=('sender_name','sender_email')



admin.site.register(CoursesAvailable,CoursesAvailableAdmin)
admin.site.register(CourseImages,CourseImagesAdmin)
admin.site.register(EmailReciever,EmailRecieverAdmin)

