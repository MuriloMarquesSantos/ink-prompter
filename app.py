from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

import random

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def FUN_root():
  return render_template("index.html")

@app.route("/generateWorldThemes", methods = ['POST'])
def FUN_generateWorld():
  themes = [
    "Overgrown Ruins",
    "Merchant's Store",
    "Nature Untouched",
    "Townsquare",
    "Ancient Tree",
    "Inn in the Middle of Nowhere",
    "Deep in the Woods",
    "Shanty Town",
    "Cave Entrance",
    "By the Docks",
    "Rocky Ruins",
    "By the Beach",
    "Puzzled Platforms",
    "Exotic Flora",
    "Hall of Deities",
    "Cemetery",
    "Ancient Altar Room",
    "Desserted Drylands",
    "Abnormal Formations",
    "Volcanic Terrain",
    "Crystal Coves",
    "Path Along the Water",
    "Freezing Fjord",
    "Underwater Temple",
    "Eldritch Forest",
    "Buried Statues",
    "Idle Portal",
    "Market Place",
    "Astral Plains/ Dreamland"
  ]

  return render_template("themes.html", theme=random.choice(themes))

@app.route("/generateInkitoberThemes", methods = ['POST'])
def FUN_InkitoberThemes():
  themes = [
     "POISONOUS","CRUEL","DRAIN","TRANQUIL","WHALE","EXPENSIVE","ROASTED","GUARDED","MUDDY","SPELL","CLOCK","CHOP","CHICKEN","WEAK","PRICKLY","DROOLING","ANGULAR","STRETCH","EXHAUSTED","SWOLLEN","THUNDER","STAR","BOTTLE","GIFT","PRECIOUS","SCORCHED","DOUBLE","FLOWING","BREAKABLE","JOLT","SLICE"
  ]

  return render_template("themes.html", theme=random.choice(themes))

@app.route("/generateMedievalThemes", methods = ['POST'])
def FUN_MedievalThemes():
  themes = [
     "THE KNIGHT OF LIGHT","THE TIME TRAVELLER","THE KNIGHT OF SHADOWS","THE UNDEAD SORCERER","THE WARRIOR PRINCESS","THE OLD DRAGON","THE RIVER MAIDEN","THE ORC GENERAL","THE FARMER'S DAUGHTER","THE GOOD ORC","THE THIEF","THE WICKED FAE","THE SMITHIE'S SON","THE SHAPESHIFTING GIRL","THE DRUNKEN WARRIOR","THE GIANTESS","THE LADY OF THE BLADES","THE WARRIOR'S DAUGHTER","THE THREE WITCHES","THE PALADIN","THE WIZARD KING","THE STRONGMAN","THE DRAGON QUEEN","THE WANDERING ASSASSIN","THE CHILD MAGE","THE DRUNKEN FISTFIGHTER","THE OLD WIZARD","THE SAMURAI","THE BARBARIAN HERO","THE FIGHTING FRIAR","THE BARBARIAN HEROINE"
  ]

  return render_template("themes.html", theme=random.choice(themes))

if __name__ == "__main__":
  app.run()
