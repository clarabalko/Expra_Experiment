# packages laden

from   psychopy import visual, gui, core, event
import random
import os
import glob
import time
import pandas as pd

# Bilder importieren

img_dir = os.getcwd() + "images"                                                                # Arbeitsverzeichnis definieren!

stim_list      = glob.glob(os.path.join(img_dir, "*.jpeg"))
primate_img_list   = glob.glob(os.path.join(img_dir, "primate*"))
human_img_list = glob.glob(os.path.join(img_dir, "human*"))

# Outputordner definieren

# ...

# Abbruchkriterium für Training

# ...

# Anzahl von Trials und Blöcken

# ...

# keyboard input

trial_keys = ['a', 'l']
continue_key = 'space'


# Daten aufnehmen

vp_info = {
    "age"   : [],
    "gender": ["---","m", "w", "d"],            # vorauswählbare Antworten
    "vp_id" : []
}

vp_data = gui.DlgFromDict(vp_info, title = "Probandendaten",                    # Titel der Dialogbox
                          labels = ["Alter", "Geschlecht", "Probanden-ID"],     # Labels der Kästchen
                          alwaysOnTop = True)                                   # Dialogbox anzeigen

print(vp_info)                                                                  # Antworten werden automatisch in dict übernommen

age = vp_info["age"]
gender = vp_info["gender"]
vp_id = vp_info["vp_id"]
print(age, gender, vp_id)



# stuff specific to our experiment
win = visual.Window(
    color='grey',
    size=[1366, 768],                      # Display anpassen
    fullscr = False)                        # kann bei Mac nun geschlossen an


# Anzahl der Stimuli randomisieren

display_sizes = [9,18,36]

random.choice(display_sizes)


# Instruktionen (als dict?) definieren



# Experiment-Funktion
