from django.db import models

from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

# Create your models here.

class MenuItems(Orderable):
    linkTitle = models.CharField( blank=True, null=True, max_length=50)
    linkUrl = models.URLField( blank=True, max_length= 500)
    linkPage = models.ForeignKey( 
                                 "wagtailcore.Page",
                                 null=True, 
                                 blank = True, 
                                 related_name = "+",
                                 on_delete= models.CASCADE,)
    open_in_new_tab = models.BooleanField( default=False, blank = True)
    
    page = ParentalKey("Menu", related_name ="menu_items")
    
      
    
    panels = [
        FieldPanel("linkTitle"),
        FieldPanel("linkUrl"),
        PageChooserPanel("linkPage"),
        FieldPanel("open_in_new_tab"),
    ]
    
@register_snippet   
class Menu(ClusterableModel):
    
    """Menu Name is created here"""
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from ="title", editable = True)
    
    panels = [
        MultiFieldPanel([
            
            FieldPanel("title"),
            FieldPanel("slug"),
        ] , heading="Menus"),
        InlinePanel("menu_items", label = "Menu Items")
              
    ]
    
    def __str__(self):
        return self.title