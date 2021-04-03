from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# On line 5 and line 8, you define empty classes PostAdmin and CategoryAdmin. For the purposes of this tutorial, you don’t need to add any attributes or methods to these classes. They are used to customize what is shown on the admin pages. For this tutorial, the default configuration is enough.

# The last two lines are the most important. These register the models with the admin classes. If you now visit localhost:8000/admin, then you should see that the Post and Category models are now visible: