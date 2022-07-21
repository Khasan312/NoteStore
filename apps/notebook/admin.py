from django.contrib import admin

from .models import Brand, Color, NoteBook, GPU, CPU, Core, Storage, Purpose, Condition

admin.site.register(NoteBook)
admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(Core)
admin.site.register(Storage)
admin.site.register(Purpose)
admin.site.register(Condition)
admin.site.register(Brand)
admin.site.register(Color)

