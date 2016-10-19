from items import *
#   Basic Intro, Please improve this shit:
#   "One man. One desire. The goal to create a device protect himself and those around him, the only way he knew how.
#   Python."The words echo in your (Kirill Sodorov, Expert Programmer, Overall Nice Guy) head. Years of planning,
#   programming, bug fixing, getting angry, and progressive montages led to this moment. Over a cup of lukewarm coffee,
#   you finish the last function:- "def killcode". You lean back and revel in your own glory, ready to get a good
#   night's sleep to prepare for the big presentation in the University tomorrow. Researchers from round the country are
#   coming to witness your brainchild. This could be your big break. Let's hope everything goes to plan. You didn't
#   forget to logoff the lecture hall computer did you?


#   Needs to be finished, not sure about the final rooms tbh. Try out some stuff if you can please xxx
room_floor0 = {
    "name": "Bottom Floor",

    "description":
    """The Central Building bottom floor is suspiciously quiet. There is no smell of breakfast from the cafeteria.
The normal buzz of student life is nowhere to be seen. The elevator door appears to be out of whack. At least
nobody is around to pass on their flu on your big day.""",

    "exits": {"right": "Reception", "up": "Floor1"},

    "items": []
}

room_reception = {
    "name": "Reception",

    "description":
    """You walk over to the reception. There is nobody here, and there appears to be nobody around. Everything is left
on as if someone had to leave urgently. You notice a phone with a blinking notification indicator and a strange item.""",

    "exits":  {"left": "Floor0", "up": "Floor1"},

    "items": [item_phone, item_bodypillow]
}

room_floor1 = {
    "name": "First Floor",

    "description":
    """The First Floor is as desolate as the ground floor. Some things appear to be damaged as if there has been some
kind of apocalypse but that would be ridiculous. There is a totally standard incapacitated body to the left, and
the stairs to the right have been barricaded(?). If only you hadn't left your toolkit at home.""",

    "exits": {"down": "Floor0", "left": "body", "up": "Floor2Opening", "right": "Empty"},

    "items": []
}

room_empty = {
    "name": "Empty Room",

    "description":
    """It's an empty room. I don't know what you expected really. No easter eggs here, trust me.""",

    "exits": {"down": "Floor0", "left": "body", "up": "Floor2Opening", "right": "Empty"},

    "items": [item_easteregg]
}

room_body = {
    "name": "Incapacitated Body",

    "description":
    """You walk over to the lifeless body. You notice a pulse but they have clearly been struck to the head, or gotten
overly drunk for a Monday morning. As you are the protagonist of a text-based adventure, your first instinct is not
to help but to scavenge for any loot he might have. He appears to blessed with a chainsaw. That's convenient.""",

    "exits": {"right": "Floor1", "f": "PayRespects"},

    "items": [item_saw]
}

room_f = {
    "name": "Room of Respect Paying",

    "description":
    """Achievement Unlocked: Self-Respect.""",

    "exits": {"back": "body"},

    "items": [item_humility]
}

room_f2o = {
    "name": "Second Floor",

    "description":
    """After effortlessly clearing the barricade thanks to your mighty chainsaw, you climb the stairs to the second floor.
None of the lights are on, there's a mysterious odour coming from the bathroom, and in the near distance you notice a
shadowy figure lumbering about. The chainsaw would've been handy here.""",

    "exits": {"forward": "Fight", "down": "Floor1"},

    "items": [],

    "requirements": {
        "item": item_saw,
        "item_held": "You heroically tear apart the barricade with your chainsaw, but sadly it breaks.",
        "item_missing": "You headbutt the barrier in an attempt to break it, but it doesn't work. You need something else.",
    }
}

room_fight = {
    "name": "Shadowy Figure",

    "description":
    """You walk towards the figure and as you get closer, you notice the silhouette is Jing Wu. She is lurching about like
a zombie from World War Z, or rather a good film like 28 Days Later. As you step towards her, she notices your presence
and turns around. Under her breath she mutters "Wake Me Up Inside (Can't Wake up)" then starts to run towards you
aggressively. She appears noticeably triggered, and you deal with it in the only way a man can, with patriarchy
(fists).""",

    "exits": {"rko": "Floor2", "hadouken": "Floor2", "quickscope": "Floor2", "backhand": "Floor2", "worldstar": "Floor2"},

    "items": []
}

room_floor2 = {
    "name": "Second Floor",

    "description":
    """You have successfully showed her what for, whether that was required or not is another question.
Floor 2 is in an even worse state than Floor 1. Tables have been knocked over, windows have been smashed, jimmies have been rustled.
The only other human here is Jing Wu, and your only exit is to keep going up as you don't want to face your previous actions.""",

    "exits": {"left": "Jing Wu", "up": "Floor3", "right": "Bathroom"},

    "items": []
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """The Second Floor bathroom, a place of beauty and tranquility. Bad as the smell may be, it's comforting, a sense of homeliness.
One of the taps doesn't work and the toilet door has been smashed in. You are unsure whether this is abnormal.""",

    "exits": {"left": "Floor2", "right": "Stall"},

    "items": []
}

room_stall = {
    "name": "Stall",

    "description":
    """You almost too-enthusiastically peer into the bowl of the toilet and notice a piece of toilet paper with writing on it.
Please don't take it. You're above this. Just leave.""",

    "exits": {"left": "Bathroom"},

    "items": [item_note2]
}

room_jing = {
    "name": "Jing Wu",

    "description":
    """What you do have is a very particular set of skills. Skills you acquired over a very long career. Skills that make you a nightmare
for people like Jing. Luckily, your experience with said skills allowed you to stun her without causing any permanent damage. Well done.
In her pocket is a note that appears to have been frantically scrawled upon.""",

    "exits": {"right": "Floor2"},

    "items": [item_note]
}

room_floor3 = {
    "name": "Third Floor",

    "description":
    """The third floor looks far more battered than the previous floors combined. It is evident at this point that
something has gone very, very wrong. It couldn't be you.... could it? No, absolutely not, what a foolish assumption.
The door to the lecture hall is splattered with blood. Are they that excited?""",

    "exits": {"down": "Floor2", "left": "Lecture Hall"},

    "items": []
}

room_lecture = {
    "name": "Lecture Hall",

    "description":
    """As the lecture hall door opens you gaze around at the forsaken area. Carnage must have occurred in every corner of
the room. The spectacle is so unsightly it can't even be accurately depicted in the descriptive writing of say.. a
text based game.

Oh dear. You recognise now that perhaps you might have some involvement here. "Welcome Kirill" an automated
voice spoke from the front of the lecture hall. "All threats within the vicinity
have successfully been incapacitated". No, it couldn't be.. your wonderful creation, your beautiful bae. This disaster
was all caused by your machine??. Protectotron! y tho?""",

    "exits": {"down": "Floor2", "laptop": "PrintThreat"},

    "items": []
}

room_threat_id = {
    "name": "Your Computer",

    "description":
    """You frantically input the command.. trying to find some reason behind the madness that has ensued...
"Threat id - Possible freshers flu contamination" reads the machine. "Threat priority HIGH -
ethical decontamination by forced combat executed".

LOL you realise the incapacitation module has the ability to cause violent and unforgiving psychosis in subjects.
This mixed with your deep underlying fear of contracting one of university's greatest perils "freshers flu" may have
been somewhat misinterpreted in the many thousands of lines of code that govern this great invention.

Well on the bright side, you aren't technically a killer. Yay? But still, that's one hell of a bug.

You must find a way to end this. The killcode of course!... wait what was it again? Urgh who has time to remember
such arbitrary details. If only it was written down somewhere.""",

# trying to link the player back to the note left by jing?

    "exits": {"down": "Floor2", "cmd": "FinishHim"},

    "items": []
}

room_finish_him = {
    "name": "Finish Him!",

    "description":
        """ """,
    "exits": {" "},

    "items": []
}
rooms = {
    "Floor0": room_floor0,
    "Reception": room_reception,
    "Floor1": room_floor1,
    "body": room_body,
    "Floor2Opening": room_f2o,
    "Fight": room_fight,
    "Floor2": room_floor2,
    "Jing Wu": room_jing,
    "PayRespects": room_f,
    "Floor3": room_floor3,
    "Lecture Hall": room_lecture,
    "PrintThreat": room_threat_id,
    "FinishHim": room_finish_him,
    "Bathroom": room_bathroom,
    "Stall": room_stall,
    "Empty": room_empty
}
