

import os
import time
from weakref import finalize
import requests, json, random
from fuzzywuzzy import fuzz
# import nerdfonts as nf

from User_Data import User_Data as UD
import PySimpleGUI as sg

import keyboard


# def print_fonts():
#     from tkinter import Tk, font
#     root = Tk()
#     print(*font.families(),sep='\n')


class App():
    def __init__(self,title="Type Speed"):
        keyboard.hook(self.hotkeys)

        # CONSTANTS
        self.title = title
        self.h1 = ("Helvetica", 18)
        self.normal = ("Helvetica", 12)

        # get user data
        self.ud = UD()
        print(self.ud.data)

        self.WPM = 0
        self.ACC = -1

        self.paragraph = self.get_paragraph()
        
        # set theme
        sg.theme(self.ud.data['theme'])

        # the screen number
        self.screen_int = 0 
        self.time = 0 
        self.ctrl_enter_press_flag = False
        self.start_flag = False

        # create window and run loop
        self.window = self.make_window()

        while True:

            event, values = self.window.read(timeout=10)
            print('event',str(event))
            print('values',values)
            print(self.WPM, self.ACC)

            if str(event) == '-MAIN-':
                self.WPM = 0
                self.ACC = -1
                self.screen_int = 0
                self.window = self.make_window()

            if str(event) == '-START-':
                self.WPM = 0
                self.ACC = -1
                self.paragraph = self.get_paragraph()
                self.start_flag = False
                self.screen_int = 1
                self.window = self.make_window()
                self.window['-INPUT-'].bind('<FocusIn>','+FOCUS_IN')

            if str(event) == '-SCORES-' or self.ctrl_enter_press_flag == True:
                self.ctrl_enter_press_flag = False
                
                if self.WPM != 0 and self.ACC != -1:
                    # add new score
                    self.ud.data['scores'].append({'WPM': self.WPM, 'ACC': self.ACC})

                    # sort scores
                    scores = self.ud.data['scores']
                    self.ud.data['scores'] = sorted(scores, key=lambda s: s['WPM'], reverse=True)[:10]

                    # save scores
                    self.ud.save()

                self.screen_int = 2
                self.window = self.make_window()

            if self.start_flag == True and self.screen_int == 1:
                self.time += 10 #miliseconds
                self.window['--TIME--'].update( str(self.time/1000) + 's')
                word_count = len(self.window['-INPUT-'].get().split(' '))

                self.WPM = (word_count*60)/( (self.time/1000)*60 )
                self.window['--WPM--'].update( '{:.2f}'.format(self.WPM))

                self.ACC = fuzz.ratio( self.paragraph , self.window['-INPUT-'].get())
                self.window['--ACC--'].update( '{:.2f}'.format( self.ACC ) )
            
            if str(event) == '-INPUT-+FOCUS_IN' and self.start_flag == False:
                self.start_flag = True
                self.window['-title-'].update('')
                self.window['-PARA-'].update(self.paragraph)

            if event == '__TIMEOUT__':
                continue
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if str(event) == '-COMBO-':
                if values['-COMBO-'] != sg.theme():
                    sg.theme(values['-COMBO-'])
                    self.ud.data['theme'] = values['-COMBO-']
                    self.ud.save()
                    self.window.close()
                    self.window = self.make_window()

    def make_window(self,si=None):

        if self.screen_int == 1:
            self.time = 0 
                
        try:
            self.window.close()
        except:
            pass

        return sg.Window(
            self.title, 
            self.get_screens()[self.screen_int],
            keep_on_top=True,
            use_custom_titlebar=True,
            finalize=True
            )

    def get_screens(self):
        screens = [ 
                    [
                        [ self.label("Main Screen",font=self.h1,key='-title-')  ],
                        [ self.label("Test your typing speed!",font=self.normal) ],
                        [ sg.Button("Start",font=self.normal,key='-START-') ],
                        [ sg.Button("Scores",font=self.normal,key='-SCORES-') ],
                        [ self.label("",font=self.normal) ],
                        [ self.label("Theme:",font=self.h1) ],
                        [ sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                    ],
                    [  
                        [ self.label("Press Tab to start",font=self.h1,key='-title-') ],
                        [ sg.Multiline(default_text = '',disabled =True,s=(50,10),justification='l',font=self.normal,focus=False,expand_x =True,key='-PARA-') ],
                        [ sg.Multiline(s=(50,10),justification='l',font=self.normal,expand_x =True,key='-INPUT-',focus=True) ],
                        [ self.label('Time:',font=self.normal ),self.label("",font=self.normal, key='--TIME--')] , 
                        [ self.label('Words Per Min:',font=self.normal ) ,self.label("",font=self.normal, key='--WPM--') ],
                        [ self.label('Accuracy:',font=self.normal ) ,self.label("",font=self.normal, key='--ACC--') ],
                        [ self.label("*** Press Ctrl+Enter to End ***",font=self.normal) ],
                    ]
                ]
        
        scores = [
                [ self.label("Scores",font=self.h1,key='-title-') ],
                [ self.label("WPM",font=self.normal), self.label("Accuracy",font=self.normal) ],
            ]

        for s in self.ud.data['scores']:
            print(s)
            scores.append([ self.label(str(s['WPM']),font=self.normal), self.label(str(s['ACC']),font=self.normal) ])

        scores.append([ sg.Button("Main Screen",font=self.normal,key='-MAIN-') ,sg.Button("Start",font=self.normal,key='-START-') ])
        
        screens.append(scores)

        return screens

    def spacer(self,size=1):
        return self.name('',size)

    def label(self,text,font=None,size=25,key=None):
        if font == None:
            font = self.normal
        return sg.Text(text , size=(size,1), justification='l',font=font,key=key,expand_x=True)

    def hotkeys(self,event):
        """ Hook and react to hotkeys with custom handler """
        try:
            pressed_keys = [e.name.lower() for e in keyboard._pressed_events.values()]
        except AttributeError:  # Fn might return as None
            pressed_keys = []

        print(pressed_keys)

        if len(pressed_keys) >= 2:
            if pressed_keys[0] == 'ctrl' and pressed_keys[1] == 'enter':
                self.ctrl_enter_press_flag = True

    def get_paragraph(self):
        response = requests.get('https://randomwordgenerator.com/json/paragraphs.json')

        if response.status_code == 200:
            paragraphs = json.loads(response.text)['data']
            # print(paragraphs)
            return random.choice(paragraphs)['paragraph']
        else:
            # no internet connection or something wrong with website
            paragraphs = [
                'The robot clicked disapprovingly, gurgled briefly inside its cubical interior and extruded a pony glass of brownish liquid. \"Sir, you will undoubtedly end up in a drunkard\'s grave, dead of hepatic cirrhosis,\" it informed me virtuously as it returned my ID card. I glared as I pushed the glass across the table.',
                'If you can imagine a furry humanoid seven feet tall, with the face of an intelligent gorilla and the braincase of a man, you\'ll have a rough idea of what they looked like -- except for their teeth. The canines would have fitted better in the face of a tiger, and showed at the corners of their wide, thin-lipped mouths, giving them an expression of ferocity.',
                'The trees, therefore, must be such old and primitive techniques that they thought nothing of them, deeming them so inconsequential that even savages like us would know of them and not be suspicious. At that, they probably didn\'t have too much time after they detected us orbiting and intending to land. And if that were true, there could be only one place where their civilization was hidden.',
                'Turning away from the ledge, he started slowly down the mountain, deciding that he would, that very night, satisfy his curiosity about the man-house. In the meantime, he would go down into the canyon and get a cool drink, after which he would visit some berry patches just over the ridge, and explore among the foothills a bit before his nap-time, which always came just after the sun had walked past the middle of the sky. At that period of the day the sun’s warm rays seemed to cast a sleepy spell over the silent mountainside, so all of the animals, with one accord, had decided it should be the hour for their mid-day sleep.',
                'It went through such rapid contortions that the little bear was forced to change his hold on it so many times he became confused in the darkness, and could not, for the life of him, tell whether he held the sheep right side up, or upside down. But that point was decided for him a moment later by the animal itself, who, with a sudden twist, jabbed its horns so hard into his lowest ribs that he gave a grunt of anger and disgust.',
                'Since they are still preserved in the rocks for us to see, they must have been formed quite recently, that is, geologically speaking. What can explain these striations and their common orientation? Did you ever hear about the Great Ice Age or the Pleistocene Epoch? Less than one million years ago, in fact, some 12,000 years ago, an ice sheet many thousands of feet thick rode over Burke Mountain in a southeastward direction. The many boulders frozen to the underside of the ice sheet tended to scratch the rocks over which they rode. The scratches or striations seen in the park rocks were caused by these attached boulders. The ice sheet also plucked and rounded Burke Mountain into the shape it possesses today.',
                'According to the caption on the bronze marker placed by the Multnomah Chapter of the Daughters of the American Revolution on May 12, 1939, \"College Hall (is) the oldest building in continuous use for Educational purposes west of the Rocky Mountains. Here were educated men and women who have won recognition throughout the world in all the learned professions.\"',
                'A long black shadow slid across the pavement near their feet and the five Venusians, very much startled, looked overhead. They were barely in time to see the huge gray form of the carnivore before it vanished behind a sign atop a nearby building which bore the mystifying information \"Pepsi-Cola.\"',
                'Out of another, I get a lovely view of the bay and a little private wharf belonging to the estate. There is a beautiful shaded lane that runs down there from the house. I always fancy I see people walking in these numerous paths and arbors, but John has cautioned me not to give way to fancy in the least. He says that with my imaginative power and habit of story-making a nervous weakness like mine is sure to lead to all manner of excited fancies and that I ought to use my will and good sense to check the tendency. So I try.',
                'Her eyebrows were a shade darker than her hair. They were thick and almost horizontal, emphasizing the depth of her eyes. She was rather handsome than beautiful. Her face was captivating by reason of a certain frankness of expression and a contradictory subtle play of features. Her manner was engaging.',
            ]
            return random.choice(paragraphs)

if __name__ == '__main__':
    # print_fonts()
    app = App()

    # print('0123456789'[:3])


