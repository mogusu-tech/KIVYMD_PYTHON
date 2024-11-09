from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase
import json
import os


screen_helper = """
ScreenManager:
    MenuScreen:   #First Screen includes navigation drawer
    ListScreen: #Second Screen storing objects in alist
    CardScreen: #Third SCreen
    CarouselScreen: #FourthScreen
    DataTablesScreen: #FifthScreen
    NewEntryScreen: #SixthScreen 
<MenuScreen>:
    name:'menu'
    Image:    #IMAGE BACKGROUND TO FULLY COVER THE BACKGROUND
        source:'kisii.jpg'
        allow_stretch:True
        keep_ratio:False
        size_hint:1,1
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title:"MDTopAppBar"
                    pos_hint: {"top": 1}
                    left_action_items:
                        [['menu',lambda x: nav_drawer.set_state("open")],['menu',lambda x: nav_drawer.set_state("open")]]
                   
                    right_action_items:
                        [['menu',lambda x: nav_drawer.set_state("open")],['menu',lambda x: nav_drawer.set_state("open")]]
                    MDTabs:
                        id:tabs
                        #on_tab_switch: app.on_tab_switch(*args) #This is a function to be called when a tab is pressed
                        Tab:
                            title:"Tab 1"
                            MDLabel:
                                text:"This is content for Tab 1"
                                halign:'center'
                        Tab:
                            title:"Tab 2"
                            MDLabel:
                                text:"This is content for Tab 2"
                                halign:'center'
                        Tab:
                            title:"Tab 3"
                            MDLabel:
                                text:"This is content for Tab 3"
                                halign:'center'
                        Tab:
                            title:"Tab 4"
                            MDLabel:
                                text:"This is content for Tab 4"
                                halign:'center'
                MDProgressBar:
                    #orientation: 'vertical'    
                    value:50
                    color:app.theme_cls.accent_color
                    pos_hint: { "top":.9}
                    size_hint_y:None
                    height:20   
                MDBottomAppBar:
                    MDTopAppBar:
                        title:"MDBottomAppBar"
                        icon:"git"
                        type:"bottom"
                        mode:"end" #CAN BE FREE-END OR LEAVE IT BE AT MIDDLE                            
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text:"Andrew"
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text:"mogusuandrew07@gmail.com"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineAvatarIconListItem
                            on_press:root.manager.current = 'list'
                            text:'list'
                            IconLeftWidget:
                                icon:'format-list-bulleted' 
                        OneLineIconListItem:
                            text:'Upload'
                            IconLeftWidget:
                                icon:'file-upload'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon:'logout'
                        OneLineIconListItem:
                            on_press:root.manager.current = 'card'
                            text:'cards'
                            IconLeftWidget:
                                icon:'calendar'
                        OneLineIconListItem:
                            on_press:root.manager.current = 'carousel'
                            text:'CarouselScreen'
                            IconLeftWidget:
                                icon:'folder'
                        OneLineIconListItem:
                            on_press:root.manager.current = 'tables'
                            text:'CarouselScreen'
                            IconLeftWidget:
                                icon:'list'         
                #Widget:
                       
                            
 
                                                       
    
<ListScreen>
    name:'list'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    size:root.width, root.height
                    orientation: 'vertical'
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4  # Background color (light gray)
                        Rectangle:
                            pos: self.pos
                            size: self.size 
                    MDTopAppBar:
                        title: 'List'
                        anchor_title:'center'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')],["coffee", lambda x: print('Topbar item 2 clicked!')]]
                        right_action_items: [["menu", lambda x: print('Topbar item 3 clicked!')],["coffee", lambda x: print('Topbar item 4 clicked!')]]
                        elevation: 2
                        size_hint_y: None
                        height:dp(56)
                    #Addition of searchbar below toolbar
                    MDTextField:
                        id: search_field
                        hint_text:'Search'
                        mode:"rectangle"
                        icon_left:"magnify"
                        size_hint_x:1
                        pos_hint: {"center_x":0.5}
                        on_text:root.filter_items(self.text)
                    #Adding the list of items
                    ScrollView:
                        MDList:
                            id:menu_list
                            adaptive_height:True       
                    MDRoundFlatButton:
                        text:'HOME'
                        on_press:root.manager.current = 'menu'
                        #pos_hint: {"center_x":0.5}
                        size:dp(200),dp(50)
                    MDRoundFlatButton:
                        text:'Selected'
                        on_press:app.show_selected_items()
                        #pos_hint: {"center_x":0.5}
                        size:dp(200),dp(50)
                    MDRoundFlatButton:
                        text:'Enter New'
                        on_press:root.manager.current = 'entry'
                        #pos_hint: {"center_x":0.5}
                        size:dp(200),dp(50) 
                    MDRoundFlatButton:
                        text:'Delete_selected'
                        on_press:app.delete_item()
                        #pos_hint: {"center_x":0.5}
                        size:dp(200),dp(50)
                    MDBottomAppBar:
                        left_action_items: [["coffee", lambda x: print('bottombar item 1 clicked!')],["account", lambda x: print('bottombar item 2 clicked!')]]
                        right_action_items: [["menu", lambda x: print('bottombar item 3 clicked!')],["coffee", lambda x: print('bottombar item 4 clicked!')]]
                        icon: "help-circle"
                        mode: 'free-end'
                        type: 'bottom'
                        anchor: 'right'  
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                #Attion of components to a drawer
                MDLabel:
                    text:"More list"
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text:"Online list"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                #Add list to container if willing to
                
 
 
                
                
#Third Screen
<CardScreen>:
    name:'card'
    ScrollView:
        do_scroll_x:True # Used to enable horizontal scrolling when enabled
        do_scroll_y:False #Used for Vertical scrolling
        size_hint_x:1 #Ensures the scrollView uses the full height of the screen
        MDGridLayout:
            cols:2 
            #adaptive_height:True #Makes the GridLayout adapt to its content height
            adaptive_width:True #Makes the GridLayout adapt to its content width
            padding: 20
            spacing: 20
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'kisii.jpg'
                        allow_stretch:True
                        keep_ratio:False
                        radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen
                    
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'kisii.jpg'
                        allow_stretch:True
                        keep_ratio:False
                        radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'kisii.jpg'
                        allow_stretch:True
                        keep_ratio:False
                        radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen 
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'kisii.jpg'
                        allow_stretch:True
                        keep_ratio:False
                        radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen 
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'kisii.jpg'
                        allow_stretch:True
                        keep_ratio:False
                        radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen   
            MDCard:
                size_hint_x:None
                width: dp(150)
                size_hint_y: None #setting this None to fix the card height
                height:dp(150)
                elevation: 10
                radius: [10,10,10,10] #To make rounded corners
                on_press:root.manager.current = 'menu'
                MDBoxLayout:
                    orientation: 'vertical'
                    size:root.width, root.height
                    padding:5
                    spacing:5
                    radius: [10,10,10,10] #To make rounded corners
                    canvas.before:
                        Color:
                            rgba: 224/255, 160/255, 16/255, 0.4
                        RoundedRectangle:
                            size:self.size
                            pos: self.pos
                            radius: [10,10,10,10] #To make rounded corners
                    MDLabel:
                        text:"Card1"
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    FitImage:
                        source:'try1.jpg'
                        allow_stretch:False
                        keep_ratio:True
                        radius: [50,50,50,50] #To make rounded corners
                    MDLabel:
                        text:"More Information about the card above"
                        font_style: 'Caption'
                        size_hint_y:None
                        height: self.texture_size[1] #Set height based on text content
                        halign: 'center'
                        valign: 'top'
                        text_size: self.width,None # Set text size to container width to center-align
                    #Width: use this when only one widget to push at the top of the screen
        #MDBoxLayout:
            #orientation:"vertical"
            #size:root.width, root.height
            #MDRectangleFlatButton:
                #text:"Button1"
                #on_press:root.manager.current = 'button1'
                
  
                
<CarouselScreen>
    name:'carousel'
    MDCarousel:
        direction:"bottom" #points where to heading to
        BoxLayout:
            MDLabel:
                text:"Hello Carousel1"
                halign: 'center'
        BoxLayout:
            MDLabel:
                text:"Hello Carousel2"
                halign: 'center'  
        BoxLayout:
            MDLabel:
                text:"Hello Carousel3"
                halign: 'center'
                
   
                
                
<DataTablesScreen>
    name:"tables"
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Data Table Screen"
            halign: 'center'
            
            
            
            
<NewEntryScreen>
    name:'entry'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        MDTextField:
            id:name_field
            hint_text:"Name"
        MDTextField:
            id:age_field
            hint_text:"Your Age"
        MDTextField:
            id:city_field
            hint_text:"Your City"
        MDRectangleFlatButton:
            text: "Add Entry"
            on_release:app.add_entry()
        MDLabel:
            id:output_label
            text:""
        MDRectangleFlatButton:
            text: "Add Entry"
            on_release:app.add_entry()
        MDRoundFlatButton:
            text:'Back_To_list'
            on_press:root.manager.current = 'list'
            pos_hint: {"center_x":0.5}
            size:dp(200),dp(50)         
"""





# |************* List: menu_items ************************************************************************************************************|
# menu_items is a list of dictionaries, each representing an item with "text" and "icon" fields.
# The "text" field holds the item's name or label, while the "icon" field specifies the icon type for the item.
# This list is the main dataset displayed in the GUI and is used to populate the app's list view.
# *******************************************************************************************************************************************|
file_path = 'andrew.json'

# Function to save data (a list of dictionaries) to a JSON file
import json

def save_data(current_data, file_path):
    """Clear and then save data (list of dictionaries) to a JSON file."""
    # Clear the file by opening it in write mode and closing it immediately
    with open(file_path, 'w') as file:
        pass  # This clears the file

    # Now, save the new data
    with open(file_path, 'w') as file:
        json.dump(current_data, file, indent=4)
    print(f"Data saved to {file_path}.")


# Function to load data from a file if it exists, or save the provided data if not
def load_or_save_data(file_path, initial_data):
    """
    Load data from a file if it exists.
    If not, save the provided initial_data to the file.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
            print("Data loaded from file:", existing_data)
            return existing_data
    else:
        save_data(initial_data, file_path)
        return initial_data

# Function to modify existing data in the file by adding or updating an entry
def modify_data(file_path, new_entry):
    """
    Modify the existing data in the file by adding a new entry.
    If the file does not exist, it initializes it with the new entry.
    """
    # Load existing data if the file exists or initialize it with an empty list
    current_data = load_or_save_data(file_path, [])
    current_data.append(new_entry)  # Add new entry if it doesn't exist

    # Save the modified data back to the file
    save_data(current_data, file_path)
    print(f"Data modified. Entry updated or added: {new_entry}")
    print(f"The file has know {current_data} ")
# Function to modify existing data in the file by deleting all the selected data
def delete_data(file_path):
    global new_work_list
    """
    Modify the existing data in the file by adding a new entry.
    If the file does not exist, it initializes it with the new entry.
    """

    # Save the modified data back to the file
    save_data(new_work_list, file_path)
    print(f"Data modified. List Data updated to: {new_work_list}")
    print(f"The file has know {new_work_list} ")


# |************* List: menu_items ************************************************************************************************************|
# menu_items stores items loaded in the GUI.
# This list is automatically loaded into GUI ListScreen on entering
menu_items =[]


# |************* List: data_list ************************************************************************************************************|
# data_list stores items selected by the user in the GUI. It contains dictionaries with "text" and "active" fields.
# This list is dynamically populated based on the user's checkbox selections and is processed when items are added or deleted.
# *******************************************************************************************************************************************|
data_list = []


# |************* List: new_work_list ********************************************************************************************************|
# new_work_list holds items that remain after filtering out the selected items in data_list.
# It is used to update menu_items after deletions and ensure only unselected items are retained in the main list.
# *******************************************************************************************************************************************|
new_work_list = []









    # |************* Class DataTablesScreen(Screen) *******************************************************************************************|
    # This screen displays data in a table format using a data table layout, allowing structured and sortable data presentation.
    # *****************************************************************************************************************************************|
class DataTablesScreen(Screen):
    pass  # Placeholder for the DataTables screen logic and layout

    # |************* Class RightCheckbox(IRightBodyTouch, MDCheckbox) *************************************************************************|
    # Custom checkbox positioned to the right of list items. Inherits from IRightBodyTouch for integration as a right widget in a list item.
    # *****************************************************************************************************************************************|
class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container'''  # Comment for class documentation

    # |************* Class CarouselScreen(Screen) *********************************************************************************************|
    # This screen provides a carousel-style layout, allowing users to swipe through items in a horizontal scrolling view.
    # *****************************************************************************************************************************************|
class CarouselScreen(Screen):
    pass  # Placeholder for the Carousel screen logic and layout

    # |************* Class CardScreen(Screen) *************************************************************************************************|
    # This screen displays card-style UI elements, which can be used to present information in a card format.
    # *****************************************************************************************************************************************|
class CardScreen(Screen):
    pass  # Placeholder for the Card screen logic and layout

    # |************* Class MenuScreen(Screen) *************************************************************************************************|
    # Main menu screen where users can navigate to other screens and perform core app functions.
    # *****************************************************************************************************************************************|
class MenuScreen(Screen):
    pass  # Placeholder for the Menu screen logic and layout

    # |************* Class NewEntryScreen(Screen) *********************************************************************************************|
    # This screen allows users to input and submit new entries, which are added to the main list of items in the application.
    # *****************************************************************************************************************************************|
class NewEntryScreen(Screen):
    pass  # Placeholder for the New Entry screen logic and layout

    # |************* Class Tab(BoxLayout, MDTabsBase) *****************************************************************************************|
    # Custom tab class implementing the content for each tab in the app. Inherits from BoxLayout and MDTabsBase for tabbed content management.
    # *****************************************************************************************************************************************|
class Tab(BoxLayout, MDTabsBase):
    """Class implementing content for a tab."""  # Documentation string for the class




    #|************* Class ListScreen(Screen): **********************************************************************************************************************|
    #This section loads the list of contents from external displays them allows you to add them delete some and save it uses checkbox method for selection.
    #|**************************************************************************************************************************************************************|


class ListScreen(Screen):
    debounce_event = None  # Event used to delay search filtering for efficient input handling
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.checkboxes = {}   # Dictionary to store checkboxes by item text, allowing tracking of selected items

    # |**************************************** Method: on_enter **************************************************************************************************|
    # This method is called when entering the screen, loading the menu items into the widget and ensuring duplicates are cleared.
    # It populates the screen with list items and their associated checkboxes.
    # |************************************************************************************************************************************************************|
    def on_enter(self, *args):
        #Clear existing widgets from the list(to prevent duplicates if re-entered)
        global menu_items
        global load_or_save_data
        menu_items = load_or_save_data(file_path, [])
        self.ids.menu_list.clear_widgets()
        self.checkboxes.clear() #Clear checkboxes when reloading all items

        # Iterate through each item in menu_items and add it to the screen
        for item in menu_items:
            # Create the list item with text and on_press event
            list_item = OneLineAvatarIconListItem(text=item["text"] )
            list_item.bind(on_press=self.create_item_click_callback(item))

            # Add an icon to the left side of the list item
            icon = IconLeftWidget(icon=item["icon"])
            list_item.add_widget(icon)

            #Create a RightCheckbox and add it to the list item
            checkbox = RightCheckbox(active=False)
            list_item.add_widget(checkbox)

            #Store the checkbox in a dictionary with item text as the key
            self.checkboxes[item["text"]] = checkbox
            self.ids.menu_list.add_widget(list_item)


    # |**************************************** Method: get_selected_items ****************************************************************************************|
    # This method gathers all items with active checkboxes, stores them in a list of dictionaries, and prints the selected items.
    # The global data_list is updated with the selected items.
    # |************************************************************************************************************************************************************|
    def get_selected_items(self):
        selected_items = []
        global data_list

        # Iterate through the checkboxes and collect selected item texts
        for item_text,checkbox in self.checkboxes.items():
            if checkbox.active:
                # Create a dictionary for each selected item
                item_dict = {"text":item_text,
                             "active":checkbox.active,
                             }
                selected_items.append(item_dict)

        # Update global list with selected items
        data_list = selected_items[:]
        print("Selected Items:", selected_items)
        print("The external List has know items",data_list)


    # |**************************************** Method: create_item_click_callback *******************************************************************************|
    # This method returns a callback function that is triggered when an item is clicked,
    # allowing the program to handle item clicks and display selected item info.
    # |************************************************************************************************************************************************************|
    def create_item_click_callback(self, item):
        #Returns a function that, when called, will call on_item_click with correct info
        return lambda instance: self.on_item_click(item)

    # |**************************************** Method: on_item_click ********************************************************************************************|
    # This method handles the item click event, allowing specific actions when an item is clicked, such as logging item information.
    # |************************************************************************************************************************************************************|
    def on_item_click(self, item):
        #Action to print to console
        print(f"Clicked on item: {item['text']}")


    # |**************************************** Method: filter_items **********************************************************************************************|
    # This method filters the list based on a search text and displays only items matching the search criteria.
    # It clears existing widgets and updates them with the filtered results.
    # |************************************************************************************************************************************************************|
    def filter_items(self, search_text):
        # Clear existing widgets to display filtered results
        self.ids.menu_list.clear_widgets()
        self.checkboxes.clear() #Clear checkboxes to only track filtered items
        for item in menu_items:
            if search_text.lower() in item["text"].lower():
                # Create the list item with text and on_press event
                list_item = OneLineAvatarIconListItem(text=item["text"])
                list_item.bind(on_press=self.create_item_click_callback(item))

                # Add an icon to the list item
                icon = IconLeftWidget(icon=item["icon"])
                list_item.add_widget(icon)

                # Create a RightCheckbox and add it to the list item
                checkbox = RightCheckbox(active=False)
                list_item.add_widget(checkbox)

                # Store the checkbox in the dictionary for tracking purposes
                self.checkboxes[item["text"]]= checkbox
                self.ids.menu_list.add_widget(list_item)

    # |**************************************** Method: on_search_text ********************************************************************************************|
    # This method is called when the search text changes, implementing a debounce mechanism to delay filtering until user stops typing.
    # It cancels previous debounce events and schedules a new filter event after a delay.
    # |************************************************************************************************************************************************************|
    def on_search_text(self, search_text):
        # Cancel the previous debounce event if it exists
        if self.debounce_event:
            self.debounce_event.cancel()
        # Schedule a new debounce event to call filter_items after a delay
        self.debounce_event = Clock.schedule_once(lambda dt: self.filter_items(search_text), 1.5)




# |************* Screen Manager Setup *****************************************************************************************************|
# Initialize the ScreenManager to manage multiple screens in the app. Each screen is added to allow smooth navigation between them.
# The screens include MenuScreen, ListScreen, CardScreen, CarouselScreen, DataTablesScreen, and NewEntryScreen.
# ****************************************************************************************************************************************|
#THE ADDITION OF SCREENS WIDGETS TO sm SCREEN MANAGER
sm = ScreenManager()                             # Create a ScreenManager instance to handle screen transitions within the application
sm.add_widget(MenuScreen(name='menu'))           # Add the MenuScreen with the name 'menu' to manage main menu display
sm.add_widget(ListScreen(name='list'))           # Add the ListScreen with the name 'list' for displaying a list of items
sm.add_widget(CardScreen(name="card"))           # Add the CardScreen with the name 'card' to show card-like UI elements
sm.add_widget(CarouselScreen(name="carousel"))   # Add the CarouselScreen with the name 'carousel' for swiping through items
sm.add_widget(DataTablesScreen(name="tables"))   # Add the DataTablesScreen with the name 'tables' to display data in a table format
sm.add_widget(NewEntryScreen(name='entry'))      # Add the NewEntryScreen with the name 'entry' for creating new entries




# |************* Class DemoApp(MDApp) *******************************************************************************************************|
# This main application class (DemoApp) inherits from MDApp and builds the primary GUI layout, loading screens from a predefined Kivy string.
# It includes functions to handle selections, add new entries, and delete items from the list of dictionaries in the application.
# ******************************************************************************************************************************************|
class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)  # Load the screen interface from the screen_helper Kivy string
        return screen


    # |**************************************** Function: show_selected_items ******************************************************************|
    # This function calls a method from the ListScreen class to retrieve and display selected items.
    # It accesses ListScreen, retrieves selected items, and prints them for display in the main application.
    # |****************************************************************************************************************************************|
    def show_selected_items(self):
        list_screen = self.root.get_screen('list')         # Access ListScreen via ScreenManager
        selected_items = list_screen.get_selected_items()  # Retrieve selected items from ListScreen
        print("Main App Selected Items:", selected_items)  # Output selected items to console But not necessary used for testing purposes


    # |**************************************** Function: add_entry ****************************************************************************|
    # This function gathers input data from EntryScreen, validates it, and adds a new dictionary entry to the menu_items list.
    # The new entry is then displayed in ListScreen. The function also clears input fields and updates the output label.
    # |****************************************************************************************************************************************|
    def add_entry(self):
        global file_path
        global modify_data
        entry_screen = self.root.get_screen('entry')    # Access EntryScreen to gather inputs
        name = entry_screen.ids.name_field.text         # Retrieve name input
        age = entry_screen.ids.age_field.text           # Retrieve age input
        city = entry_screen.ids.city_field.text         # Retrieve city input
        list_screen = self.root.get_screen('list')      # Access ListScreen for refreshing content
        # Validate inputs: Ensure name and city are filled, and age is a valid digit
        if name and age.isdigit() and city:
            new_entry = {
                "text": name,
                "age": age,
                "city": city,
                "icon":"logout"
            }
            modify_data(file_path, new_entry) # Add the new entry to menu_items

            # Clear the input fields after adding the entry
            entry_screen.ids.name_field.text = ""
            entry_screen.ids.age_field.text = ""
            entry_screen.ids.city_field.text = ""

            # Update the output label to confirm the added entry
            entry_screen.ids.output_label.text = f"Added: {new_entry['text']}"
            print(menu_items)        # Print the menu_items list to verify the addition But not nesserary
            list_screen.on_enter()   # Refresh ListScreen to display the new entry in the GUI
        else:
            entry_screen.ids.output_label.text = "Please fill in all fields" # Display error if inputs are incomplete





    # |**************************************** Function: delete_item *************************************************************************|
    # This function removes selected items from the menu_items list based on the data_list (selected items from ListScreen).
    # It updates menu_items with only the remaining items, refreshes ListScreen, and prints the updated items to the console.
    # |****************************************************************************************************************************************|
    def delete_item(self):
        global menu_items                              # Access global lists for processing
        global data_list                               # Access global lists for processing
        global new_work_list                           # Access global lists for processing
        list_screen = self.root.get_screen('list')     # Access ListScreen to retrieve selections
        list_screen.get_selected_items()               # Populate data_list with selected items

        # Clear the new work list before populating it again
        new_work_list.clear()

        # Remove items from menu_items that are present in data_list (based on "text" key)
        print("Selected items:", data_list)

        for item in menu_items:
            # Compare only the "text" key in each dictionary from menu_items and data_list
            if not any(d["text"] == item["text"] for d in data_list):
                # If the "text" value of item is not in data_list, add it to new_work_list
                new_work_list.append(item)

        # Now update menu_items to contain only the remaining items
        print("new_work_list:", new_work_list)

        # Update menu_items to the filtered list in new_work_list
        menu_items.clear()  # Clear the menu_items list first to avoid duplicates
        menu_items.extend(new_work_list)  # Add the remaining items back to menu_items

        delete_data(file_path)
        # Print the updated menu_items list
        #print("The updated items:", menu_items)
        list_screen.on_enter()#Refreshes the content displayed on the screen




DemoApp().run()

"""
  MDBottomNavigation:
                        panel_color: "green"
                        selected_color_background: "orange"
                        text_color_active: "lightgrey"

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Mail'
                            icon: 'gmail'
                            badge_icon: "numeric-10"
                
                            

                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Twitter'
                            icon: 'twitter'
                            badge_icon: "numeric-5"
                
                          

                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'LinkedIN'
                            icon: 'linkedin'
                
"""