from googletrans import Translator
import pandas as pd
from PIL import Image
import os
import geocoder
from datetime import datetime


source_lang='en'
dest_lang='hi'
def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text
def utils_change(dest_lang):
    p1='''
    As we stand at the cusp of the future political landscape, we invite you to participate in our 
    comprehensive online public survey. Your opinions and insights are invaluable as we seek to
    understand the collective vision of citizens regarding the trajectory of politics in the coming years.
    '''
    p2='''
    This survey delves into a myriad of crucial topics, ranging from economic policies and social justice issues to
    environmental sustainability and global relations. By participating, you contribute to the shaping of political 
    discourse, providing a voice that resonates across diverse communities.

    '''
    p3='''
    As we navigate an era of rapid technological advancements and global interconnectivity, your perspectives on the 
    role of technology in governance, the importance of international collaborations, and the evolving nature of 
    democracy are pivotal. This survey serves as a conduit for your aspirations, concerns, and expectations, 
    helping us to chart a course towards a political future that aligns with the collective will of the people.
    '''
    p4='''
    Your participation is a testament to the strength of democracy, highlighting the power of informed citizens
    in influencing the direction of our society. Together, let us embark on this journey of shaping the future 
    political landscape, ensuring that the voices of the public resonate in the corridors of power. Join us in
    this meaningful endeavor as we lay the groundwork for a political future that reflects the aspirations and 
    values of a diverse and engaged citizenry.
    '''
    p5='''
    Join us in this meaningful undertaking. Your input is not only appreciated but essential for building a 
    political system that is responsive to the needs and desires of the people it serves. Together, we can create 
    a future where the voices of the public hold sway, guiding our society towards progress, inclusivity, and 
    shared prosperity. Thank you for being a vital part of this democratic journey.
    '''
    dest_lang=dest_lang
    p1 = translate_text(p1,source_lang,dest_lang )
    p2 = translate_text(p2,source_lang,dest_lang )
    p3 = translate_text(p3,source_lang,dest_lang )
    p4 = translate_text(p4,source_lang,dest_lang )
    p5 = translate_text(p5,source_lang,dest_lang )
    content_data={
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'p4':p4,
        'p5':p5
    }
    return content_data
def get_location():
    location=geocoder.ip('me')
    current_datetime = datetime.now()
    location_data={
    'City':location.city,
    'Country':location.country,
    'Latitude':location.latlng[0],
    'Longitude':location.latlng[1],
    'date':current_datetime.strftime("%Y-%m-%d"),
    'time':current_datetime.strftime("%H:%M")
    }
    return location_data
def list_image_files(directory):
                image_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
                return image_files

# Directory containing your images
def images_list():
    image_directory = "./static/resizeimage"
    image_files = list_image_files(image_directory)
    image_list=[]
    for i, image_file in enumerate(image_files):
                image_path = os.path.join(image_directory, image_file)
                image_list.append(image_path)
    print(image_list)
    return image_list

    
    
