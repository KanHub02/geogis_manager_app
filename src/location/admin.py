from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin


from .models import Canton, Contour, Region, District

admin.site.register(Contour)

class ContourInline(admin.TabularInline):
    model = Contour
    fields = ["geometry", ]

class RegionInline(admin.TabularInline):
    model = Region
    fields = ["title", "geometry", "is_deleted"]
    readonly_fields = ["is_deleted"]

class DistrictInline(admin.TabularInline):
    model = District
    fields = ["title", "geometry", "is_deleted"]
    readonly_fields = ["is_deleted"]
    
class CantonInline(admin.TabularInline):
    model = Canton
    fields = ["title", "geometry", "is_deleted"]
    readonly_fields = ["is_deleted"]
    

@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title", "id"]
    readonly_fields = ["id", "created_at", "updated_at"]
    fields = ["title", "geometry", "is_deleted"]
    inlines = [DistrictInline, ]


@admin.register(Canton)
class CantonAdmin(LeafletGeoAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title", "id"]
    readonly_fields = ["id", "created_at", "updated_at"]
    fields = ["title", "geometry", "is_deleted"]
    inlines = [ContourInline,]


@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title", "id"]
    readonly_fields = ["id", "created_at", "updated_at"]
    fields = ["title", "geometry", "is_deleted"]
    inlines = [CantonInline]

