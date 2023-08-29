

screen_helper = """

ScreenManager:
    MenuScreen:
    NorthScreen:
    SouthScreen:
    ChineScreen:
    ChatScreen:
    EggScreen:
    chickenScreen:
    IceScreen:
    JuiceScreen:
    OrderScreen:
    
    
    


<MenuScreen>:
    name: 'menu'
    MDRaisedButton:
        text: 'SOUTH INDIAN'
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.7}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'South'
    MDRaisedButton:
        text: 'NORTH INDIAN'
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.7}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'North'
    MDRaisedButton:
        text: "    CHINEESE     "
        size_hint:0.16,0.16
        size:200,100
        pos_hint: {"x": 0.05, "y": 0.5}
        theme_text_color: "Custom" 
        text_color:1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chine'
    MDRaisedButton:
        text: "        CHATS       "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.5}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chat'
    MDRaisedButton:
        text: "     CHICKEN     "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.3}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chicken'
    MDRaisedButton:
        text: "         JUICE        "
        size_hint:0.16,0.16
        pos_hint:{"x": 0.54, "y": 0.3}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Juice'
    MDRaisedButton:
        text: "     ICE CREAM "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.1}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Ice'
    MDRaisedButton:
        text: "           EGG         "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.1}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Egg'
<NorthScreen>:
    name: 'North'
    
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-python"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
    
<SouthScreen>:
    name: 'South'
    MDRectangleFlatButton:
        text: 'Idli'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "langauge-java"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<ChineScreen>:
    name: 'Chine'
    MDRectangleFlatButton:
        text: 'Noodles'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-html15"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
        
<ChatScreen>:
    name: 'Chat'
    MDRectangleFlatButton:
        text: 'Pani Puri'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-python"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<EggScreen>:
    name: 'Egg'
    MDRectangleFlatButton:
        text: 'egg birayani'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-python"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<chickenScreen>:
    name: 'Chicken'
    MDRectangleFlatButton:
        text: 'biryani'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-java"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<IceScreen>:
    name: 'Ice'
    MDRectangleFlatButton:
        text: 'vanilla'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "android"
        icon: "language-javas"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<JuiceScreen>:
    name: 'Juice'
    MDRectangleFlatButton:
        text: 'pepsi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Dosa'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Sambar'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Rice Bath'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Special Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Poori Saagu'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        on_press: root.manager.current = 'Order'
    
    MDFloatingActionButton:
        text: 'Back'
        icon: "language-javas"
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    
    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        pos_hint: {'x':0.75,'y':-0.37}
        
<OrderScreen>:
    name:'Order'
    MDLabel:
        text:'order placed'
        pos_hint:{'x':0.4}
    MDRaisedButton:
        text: 'GO BACK TO HOME PAGE'
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'menu'
    
    
        
    

"""


