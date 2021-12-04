from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks



class HomePage(Page):
    templates = "home/home_page.html"

    

    logo_dark_bg = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    logo_dark_bg_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    logo_white_bg = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    logo_white_bg_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("title_and_text", blocks.titleandtext()),
            ("Rich_text_editor", blocks.Rich_Text_Block()),
            ("Info_block", blocks.info_block()),
            ("Cardblock", blocks.CardBlock()),
            ("About_block", blocks.about_block()),
            ("About_block_2", blocks.about_block_2()),
            ("About_block_3", blocks.about_block_3()),
            ("About_block_4", blocks.about_block_4()),
            ("Accordion_Block", blocks.AccordionBlock()),
            ("Simple_Horizontal_Divider", blocks.Simple_Horizontal_Divider()),
            ("Tabs1Block", blocks.Tabs1Block()),
            ("ImageSliderBlock", blocks.ImageSliderBlock()),
            ("info_block1", blocks.info_block1()),
            ("FeaturesElementBlock2", blocks.FeaturesElementBlock2()),
            ("FeaturesElementBlock3", blocks.FeaturesElementBlock3()),
            
            
        ],
        null = True,
        blank= True,
    )
  

    banner_tittle = models.CharField(max_length= 250, blank = False, null = True)
    banner_sub_tittle = models.CharField(max_length= 250, blank = False, null = True)
    header_address = models.CharField(max_length= 250, blank = False, null = True)
    support = models.CharField(max_length= 250, blank = False, null = True)

    
    
    

    content_panels = Page.content_panels +  [

        MultiFieldPanel(
            [
                FieldPanel('header_address'),
                FieldPanel('support'),
            ],
            heading="header optons",
        ),
        MultiFieldPanel(
            [
               FieldPanel('banner_tittle'),
               FieldPanel('banner_sub_tittle'),
               ImageChooserPanel('banner_image'),
               ImageChooserPanel('logo_white_bg'),
               PageChooserPanel('logo_white_bg_cta'),
               ImageChooserPanel('logo_dark_bg'),
               PageChooserPanel('logo_dark_bg_cta'),
            ],
            heading="Banner Options",
        ),     
           
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

