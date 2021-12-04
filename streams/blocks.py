"""Stream fields are created here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.db import models
from wagtail.core.fields import RichTextField

class titleandtext(blocks.StructBlock):
    title = blocks.CharBlock(required = True, help_text = "Add title here")
    text = blocks.CharBlock(required = True, help_text = "Add title here")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title&Text"

class info_block(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required = True, help_text = "Add title here")
    text = blocks.CharBlock(required = True, help_text = "Add title here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
        template = "streams/info_block.html"
        icon = "edit"
        label = "Info Block"

class about_block(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 470 pixels ")
    video = blocks.URLBlock(required=False, help_text = "Enter youtube video link here ")    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add Big Bold title here")
    text = blocks.RichTextBlock(required = True, help_text = "Add main para here")
    icon1 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_1 = blocks.CharBlock(required = True, help_text = "Add sub title 1 here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    sub_title_text_1 = blocks.RichTextBlock(required = True, help_text = "Add text under sub title 1 here") 
    icon2 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")  
    sub_title_2 = blocks.CharBlock(required = True, help_text = "Add sub title 2 here") 
    button_page_1= blocks.PageChooserBlock(required=False)
    button_url_1 = blocks.URLBlock(required=False)
    sub_title_text_2 = blocks.RichTextBlock(required = True, help_text = "Add text under sub title 2 here")
    
    class Meta:
        template = "streams/about_block.html"
        icon = "placeholder"
        label = "About Block1"

class about_block_2(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = True, help_text = "Add para here")
    icon1 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_1 = blocks.CharBlock(required = True, help_text = "Add title here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    sub_title_text_1 = blocks.RichTextBlock(required = True, help_text = "Add pare here")  
    icon2 = blocks.CharBlock(required = False, help_text = "Add flaticon class here") 
    sub_title_2 = blocks.CharBlock(required = True, help_text = "Add title here") 
    button_page_2= blocks.PageChooserBlock(required=False)
    button_url_2 = blocks.URLBlock(required=False)
    sub_title_text_2 = blocks.RichTextBlock(required = True, help_text = "Add para here")
    icon3 = blocks.CharBlock(required = False, help_text = "Add flaticon class here" )
    sub_title_3= blocks.CharBlock(required = True, help_text = "Add title here") 
    button_page_3= blocks.PageChooserBlock(required=False)
    button_url_3 = blocks.URLBlock(required=False)
    sub_title_text_3 = blocks.RichTextBlock(required = True, help_text = "Add para here")
    icon4 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_4 = blocks.CharBlock(required = True, help_text = "Add title here") 
    button_page_4= blocks.PageChooserBlock(required=False)
    button_url_4 = blocks.URLBlock(required=False)
    sub_title_text_4 = blocks.RichTextBlock(required = True, help_text = "Add para here")
    icon5 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    imagebox_heading = blocks.CharBlock(required = True, help_text= "Add headign for box over image here")
    imagebox_text = blocks.CharBlock(required = True, help_text = "Add text for box over image here")
    image = ImageChooserBlock(required=False, help_text = "Best size 460 x 455 pixels ")
    
    class Meta:
        template = "streams/about-block-2.html"
        icon = "placeholder"
        label = "About Block2"
        
class about_block_3(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = True, help_text = "Add para here")   
    sub_title_1 = blocks.CharBlock(required = True, help_text = "Add title here")    
    sub_title_1_text = blocks.RichTextBlock(required = True, help_text = "Add pare here")     
    image = ImageChooserBlock(required=False, help_text = "Best size 460 x 455 pixels ")
    
    class Meta:
        template = "streams/about-block-3.html"
        icon = "placeholder"
        label = "About Block3"
        
class about_block_4(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = True, help_text = "Add para here")   
    sub_title_1 = blocks.CharBlock(required = True, help_text = "Add title here")    
    percent1 = blocks.RichTextBlock(required = True, help_text = "Add % here")     
    sub_title_2 = blocks.CharBlock(required = True, help_text = "Add title here")    
    percent2 = blocks.RichTextBlock(required = True, help_text = "Add % here")     
    sub_title_3 = blocks.CharBlock(required = True, help_text = "Add title here")    
    percent3 = blocks.RichTextBlock(required = True, help_text = "Add % here")     
    sub_title_4 = blocks.CharBlock(required = True, help_text = "Add title here")    
    percent4 = blocks.RichTextBlock(required = True, help_text = "Add % here")     
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 530 pixels ")
    
    class Meta:
        template = "streams/about-block-4.html"
        icon = "placeholder"
        label = "About Block4"
        
class info_block1(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")      
    paragraph = blocks.RichTextBlock(required = True, help_text = "Add paragraph here")  
    button_label = blocks.CharBlock(required = True, help_text = "Add button lable here") 
    button_page= blocks.PageChooserBlock(required=False)
    button_url= blocks.URLBlock(required=False)           
    image = ImageChooserBlock(required=False, help_text = "Best size 570 x 350 pixels ")
    
    class Meta:
        template = "streams/about-block-4.html"
        icon = "placeholder"
        label = "Chart-Element"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_text", blocks.CharBlock(required=False, help_text="Enter button text here")),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "3CardsBlock"

class FeaturesElementBlock2(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_text", blocks.CharBlock(required=False, help_text="Enter button text here")),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/feature-element-2.html"
        icon = "placeholder"
        label = "Feature-Element-2"

class FeaturesElementBlock3(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True, help_text=" best size is 260 x 270 pixels")),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                ("text_on_hover", blocks.CharBlock(required=False, help_text="Enter hover text here")),
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/feature-element-3.html"
        icon = "placeholder"
        label = "Feature-Element-3"
        
class ImageSliderBlock(blocks.StructBlock):
    """Cards with image only """

    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True, help_text=" best size is 140 x 130 pixels")),                
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/clients-element.html"
        icon = "placeholder"
        label = "ImageSlideBlock"

class AccordionBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    Block_Title = blocks.CharBlock(required=True, help_text="Add your title")
    First_Section_Title = blocks.CharBlock(required=True, help_text="Add your title")
    First_Section_Content_Heading = blocks.CharBlock(required=True, help_text="Add your title")
    First_Section_Content_Text = blocks.CharBlock(required=True, help_text="Add your title")  

    Sections = blocks.ListBlock(
        blocks.StructBlock(
            [    
                ("Section_ID", blocks.CharBlock(required=True, max_length=40, unique=True,  help_text="Make sure you must enter a unique word or alphanumeric text as ID")),
                ("Section_Title", blocks.CharBlock(required=True, max_length=40,  help_text="Enter Title for the sections text here")),
                ("Section_Content_Heading", blocks.CharBlock(required=False, help_text="Enter heading for the sections text here")),
                ("Section_Content_Text", blocks.CharBlock(required=False, help_text="Enter text for the sections here")),               
                ("Button_Text", blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")),
                ("Button_Page", blocks.PageChooserBlock(required=False)),
                ("Button_Url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]   )   )
    
    class Meta:  # noqa
        template = "streams/Accordion.html"
        icon = "placeholder"
        label = "Accordion:TypeOne"
    
class Tabs1Block(blocks.StructBlock):
    """Tabs with text and button(s)."""
    
    Block_Title = blocks.CharBlock(required=False, help_text="Add section title here")
    First_tab_Title = blocks.CharBlock(required=True, help_text="Add Title for the first tab")
    First_Section_Content_Heading = blocks.CharBlock(required=True, help_text="Add Heading for the first tab")
    First_Section_Content_Text = blocks.CharBlock(required=True, help_text="Add Text for the first tab")
    Button_Text = blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")  
    Button_Page = blocks.CharBlock(required = False, help_text="You can select a page to connect to the button")
    Button_Url = blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")

    tabs = blocks.ListBlock(
        blocks.StructBlock(
            [    
                ("Tab_ID", blocks.CharBlock(required=True, max_length=40, unique=True,  help_text="Make sure you must enter a unique word or alphanumeric text as ID")),
                ("Tab_Title", blocks.CharBlock(required=True, max_length=40,  help_text="Enter Title for the sections text here")),
                ("Section_Content_Heading", blocks.CharBlock(required=False, help_text="Enter heading for the sections text here")),
                ("Section_Content_Text", blocks.RichTextBlock(required=False, help_text="Enter text for the sections here")),               
                ("Button_Text", blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")),
                ("Button_Page", blocks.PageChooserBlock(required=False, help_text="You can select a page to connect to the button" )),
                ("Button_Url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]   )   )
          
    class Meta:  # noqa
        template = "streams/tab_1.html"
        icon = "placeholder"
        label = "Tabs:TypeOne"

class Rich_Text_Block(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "RichTextBlock"
        
class Simple_Horizontal_Divider(blocks.StructBlock):

    class Meta:
        template = "streams/Simple_Horizontal_Divider.html"
        icon = "placeholder"
        label = "SimpleHorizontalDivider"