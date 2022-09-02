
# no NSFW stuff
# BUT SHOULD I MAKE IT INTO A ROMANCE? (what would sell better, lol)
# Write their names as a "Breton/Imperial man","woman" and "sorcerer" before they introduce

# MAIN CHARACTERS
define i = Character("Ildari") # a Dunmer (dark elf) sorceress, quite young as for an elf, slender and beautiful
define it = Character("[[Ildari's thoughts]")
define n = Character("Niyya") # a Redguard (similar to an Afromerican) woman, porbably in her late 20-s
define nt = Character("[[Niyya's thoughts]")

# SIDE CHARACTERS
define t = Character("Talvas") # a young Dunmer sorcerer, gives a feel of young, determined, but a bit awkward student
define tt = Character("[[Talvas' thoughts]")
define ni = Character("Nikolai") # a Breton (similar to an Englishman) man, about Niyya's age
define m = Character("Marius Deanicci") # an Imperial (similar to an ancient Roman) man in his 40-ties
define a = Character("Ash spawn") # a robust, zombie-like monster made of animated ash
define c = Character("General Falx Carius") # a robust, zombie-like monster made of animated ash


# Imperial guy:
# finds emaciated, half-alive, defenseless Ildari attractive… until he realizes her # “disease” might be contagious
# considers being nice to her later on
# but gets angry and considers throwing her out because she acts suspicious and consumes their food, yet barely does any work
# probably xSTx

# Breton guy:
# a laid-back opportunist; sly
# doesn’t care about stuff, but likes to analyze and question things, as a sport
# for him Ildari is merely a curiosity, rather than someone to empathize with
# he does nothing to help her; “she may live, afflicted as she is”
# an interesting conversationsit
# probably an ENTP


define audio.unseen_horrors = "audio/music/unseen_horrors.mp3"
define audio.invariance = "audio/music/invariance.mp3"
define audio.crypto = "audio/music/crypto.mp3"
define audio.all_this = "audio/music/all_this.mp3"
define audio.invariance = "audio/music/invariance.mp3"
define audio.past_the_edge = "audio/music/past_the_edge.mp3"
define audio.welcome_to_horror_land = "audio/music/welcome_to_horror_land.mp3"
define audio.lasting_hope = "audio/music/lasting_hope.mp3"
define audio.anguish = "<from 92 to 150>audio/music/anguish.mp3"
define audio.ossuary_6_air = "audio/music/ossuary_6_air.mp3"
define audio.magic_forest = "audio/music/magic_forest.mp3"
define audio.night_of_chaos = "<from 92 to 150>audio/music/night_of_chaos.mp3"
define audio.ossuary_2_turn = "audio/music/ossuary_2_turn.mp3"

define audio.tempting_secrets = "audio/music/tempting_secrets.mp3"
define audio.anguish = "<from 92 to 150>audio/music/anguish.mp3"
define audio.reign_supreme = "audio/music/reign_supreme.mp3"

label start:

# unseen horrors?
# 1. BACK FROM THE DEAD
    play music unseen_horrors
    "[[heart beating]"
    "[[burst of nervous breathing]"
    "[[shrieks and as she discovers the walls are confined and she lies in a grave]"
    "[[nervous scratching]"
    '("ugh"s as she tries to move the stone up)'
    "(sound of the stone moving)"
    "[[a closeup shot of her grasping her heart that is lighting through the robes]"
    "[[sounds of the ash spawn voices]"
    "I'm..."
    "I’m alive."
    "I will live."
    "...will live."
    "{{closeup of her wounded fingers}"
    "F*ck!"
    "F*CK!"
    "HURTS!"
    "{{her blooded hand resting on her grave as she gets up.}"
    "I need to get away..."
    "...but my joints are pure fire."
    "{{a shot of her feet landing on the sand}"
    "Aghr!"
    "{{a slide of her leaning on her grave with knees deep in ash and clenching her teeth}"
    "(inhale, exhale)"
    "Baby steps, Ildari."
    "...baby steps."
    "{{a shot of her feet walking in the ash}"
    "(sound of 3 footsteps)"
    "One...{p}Two...{p}Three."
    "One. Two. Three."
    "{{screenshot of full body Ildari walking, balancing with her hands}"
    "Ash...{p}Cold...{p}Soft..."
    "One. Two. Three."
    "[[sound of feet in the sand]"
    "(more measured footsteps)"
    "You have to get out..."
    "Out of there, Ildari."
    "Get out."
    "{{closeup of her tired face}"
    "Out.{p}Out."
    "Out."
    "(ah!)"
    "{{Ildari falling}"
    "(whoobudoo)"
    "{{Ildari lying in blood-smeared ash}"
    "...get out."
    "[[silence]"

# Past the edge?
# 2. WE FOUND A CORPSE... ALMOST
    play music past_the_edge
    # but cut out this bugging suspense builder
    "{{a slide of a stormy sky}"
    "(the sounds of a thunderstorm in the bg + contemplational music)"
    n "...I've searched the whole storage room, we don't have any painkiller."
    n "Damn, I forgot to take more alcohol to disinfect her wounds."
    m "I had some alcohol with me. Don't worry. She's in clean clothes already. And her wounds are tended to."
    n "What? Did you... undress her?"
    m "Yes."
    n "Damn, I told you that I would tend to her chest wound!"
    nt "What a goddamn pervert you are! A suffering girl..."
    n "Why did you send me for the alcohol then?"
    m "Cut the crap."
    m "She's almost a corpse, that's just a matter of days."
    m "If you think it was a pleasure to unpack her tits... well, I've never seen a more disgusting chest wound than hers."
    m "And someone has already tried to tamper with that. It reeks of some wicked magic."
    n "Oh..."
    m "Damn, I might regret even touching her. It might be contagious..."
    n "Great Gods..."
    m "Yeah, she is weak. She barely opened her eyes while I was dressing her."
    m "She had no strength to utter even a single word."
    n "Poor girl..."
    m "On the other hand... nursing her might be worth it."
    m "Her clothes looked very expensive. If she's from a noble family..."
    n "Oh, stop!"
    n "She needs help regardless!"
    n "I need to see her!"


# MY HAND'S CAN'T HEAL
    play music welcome_to_horror_land
    "Ildari only slightly opens her eyes."
    it "Where... am I?"
    it "Someone... is talking outside."
    "She sits on her makeshift bed and examines her body."
    it "By the Three! Why must everything hurt so much!"
    "She looks at her chest, then the hands."
    i "Ooouch..."
    it "Bandages... why?"
    it "I don't want any bandages."
    "She unwraps her hands. The clotted blood stuck to the cloth, though."
    i "Auch! Ow!"
    "To her dread, she discovers that her fingertips were almost skinned to the bone. Sounds of pulsating heart."
    it "Damn!"
    it "I have instinctively performed my restoration spell."
    it "The spark... it died before it was even formed."
    it "I can't... It's no good."
    it "I feel faint..."

# 4. NIYYA
    play music past_the_edge
    "Niyya comes in."
    nt "She's awake. Perhaps she won't die after all!"
    "[[Niyya is overjoyed that she is concious.]"
    n "You - you are finally awake!"
    "[[Ildari seems sick and lies with her head in the pillow.]"
    i "Mhm."
    n "Oh, do you need something?"
    i "Wa..."
    i "Water."

# 3. WOKEN UP IN THE LAND OF HORRORS
    play music welcome_to_horror_land
    "[[then Ildari notices a huge ash spawn in the corner]"
    it "An ash spawn?"
    "[[nervous breathing]"
    it "...here?"
    "[[ash spawn produces a low noise]"
    it "So that's how my life will end."
    it "I'm going to be ripped apart like a pagan sacrifice."
    it "Whatever."
    it "...I can't."
    it "...I'm too tired for that."
    "[[She's so weak that she doesn't even do anything to protect herself]"

# WATER
    play music lasting_hope
    "[[Niyya arrives.]"
    n "I'm back!"
    n "Here."
    i "Finally..."
    "[[Ildari holds the water in her hands. The ash spawn is still there.]"
    "[[Zoom in on Ildari's heart (maybe it shouldn't be behind her clothes but exactly how it looks like under the shade of the clothes - on her bare skin)]"
    i "Ugh!"
    n "Is everything all right?"
    i "No."
    n "Oh, sorry to say that."
    n "What happened to you?"
    i "I... died."
    nt "Oh, poor girl. What she really must have gone through if she remebers things that way."
    nt "Better not to inquire too much about it."
    n "No, you didn't die. It's ok."
    n "You are safe now."
    "[[Ildari looks at her - she expresses mostly tiredness, but there's some hint that she considers Niyya's words a total bullshit.]"
    n "My name is Niyya. What's yours?"
    i "Hmm..."
    i "Il... dari."
    i "Ildari."
    "[[The ash spawn is still present thorough the conversation.]"
    i "What... is this place?"
    n "Highpoint Tower... or what is left of it. One of the oldest fortresses on Solstheim."
    n "I work there with a bunch of miners. Well, not really miners rather... fortune seekers?"
    n "I've decided to live there ever since this place was rumored to have abundant treasures."
    nt "If only the reality was so colorul..."
    n "The accomodation might not be the best - but, still it's not a bad way to make money, isn't it?."
    i "I... I want to be alone now."
    i "Tell... no one that I've... waken up."
    '[[Niyya seems excited about keeping that "secret". And Ildari trusting her.]'
    n "Ok."
    n "Call me if you need anything."
    i "Mhm."
    "[[Niyya leaves]"


# 5. SO, I'M WITH MINERS...
    play music reign_supreme
    it "Making money on digging into the fortress... what a pathetic idea."
    it "So it's just a bunch of brutes with pickaxes. Phi."
    it "Where did the hell I end up..."
    "[[Ildari's heart]"
    it "Ugh, I feel dizzy..."
    "[[Ildari again]"
    it "I must leave this place when I feel better and go to..."
    "[[Ildari's heart]"
    it "Shh... Shhhh..."
    "No."
    "NO!"
    "He... he..."
    "He killed you."
    "Yes."
    "Killed."
    it "Ouchhh. Ouchhh."
    it "Shh... Shhhh..."
    it "[[exhale]"
    it "I have nowhere to go."
    it "This... will be my home for now."
    it "Hmmm... at least I have someone to care for me."
    it "What's wrong with that ash spawn?"
    it "Oh...{p}I must be tired, I'm imagining things."
    it "Tomorrow... I'll be stronger."


#______________________________________________________________________________________


# 7. WAKING UP IN THE REALM OF NIGHTMARES
    play music ossuary_6_air
    "[[Ildari wakes up]"
    "[[She undresses her chest wound and looks at it]"
    "[[She's nearly crying]"
    it "F*ck."
    it "F*******CK!"
    it "Every breath I take... HURTS!"
    "it's botched"
    "it's all botched"
    it "How am I gonna keep on living with that?"
    "DAAAMN!"
    "do you know why it happened, Ildari?"
    it "All because I wanted more power."
    it "I'm left with THIS - to the end of my life."
    "there are noises outside"
    "Ildari?"
    it "Wait... are they talking about me?"



# 6. SAY "HELLO" TO THE MINERS, ILDARI
    it "yes, they are there"
    it "talking about me"
    "say hello to the miners, Ildari"
    m "...no, it doesn't look like anything I've seen before..."
    m "Oh, Ildari, right?"
    i "..."
    m "It's a pleasure to see that you got better."
    "this guy..."
    "heart"
    "he was staring at your wound"
    "at your heart stone"
    "what does he want to do with that?"
    m "My name is Marius Deannici."
    it "he must have thought i didn't notice him"
    it "i cannot trust him"
    ni "... and I am Nikolai."
    ni "Nice to meecha."
    i "Indeed."
    ni "Where did you get those wounds from?"
    "ash spawns"
    i "The ash spawns attacked me"
    i "I tried to fix the wound myself."
    i "...hence the seams."
    m "Do ash spawns... carry diseases?"
    i "I don't recall any."
    i "I need to get some fresh air."



# THE ASH IS SO SOFT...
    "[[Ildari walks outside, sees the landscape and takes a few deep breaths.]"
    "((inhale, exhale)"
    it "Oww... my head."
    "[[she dips her bare feet in the ash with relief]"
    "the ash is so soft and sweet"
    "Ildari"
    "look"
    "there are some larger pieces in the ash"
    "do you know what they are?"
    "BONES"
    "some time ago they were alive"
    "you can sense the spirits hovering above the bones, Ildari"
    "don't deny it"
    "you know?"
    "they can sense you, too"
    "HELLO"
    "[[Ildari runs inside]"


# WHO WERE YOU BEFORE, ILDARI?
    play music magic_forest
    "[[Niyya comes in]"
    n "I saw you running. What happened?"
    i "[[inhale/exhale]"
    n "Everything's all right?"
    i "Is this place... haunted?"
    n "No. Why would it be?"
    n "No one ever reported such thing."
    n "I'll tell the others to be watchful."
    i "NO."
    i "No."
    i "It was probably nothing."
    i "I must have been tired."
    "[[Niyya looks tender at her.]"
    n "You need to rest."
    nt "What a selfish jerk I am. I got so invested in playing the helper that I completely forgot to ask who she was before."
    nt "She doesn't seem happy in this place."
    nt "I should have studied more. I could have become a healer and help dozens like her, in a place more appropirate."
    nt "What can we offer her? There's just dirt and work to be done. The others, well, including myself have little time to help her."
    nt "I need her to trust me."
    n "What was your life like before?"
    "[[she sees the body parts again]"
    "you were ambitious"
    "too ambitious"
    "the price was..."
    "...your heart"
    it "Stop."
    it "Let me focus."
    n "Ildari?"
    i "I was on my way to... have it all."
    i "I had bright prospects for the future."
    i "I was wise... respected."
    "yes"
    i "Phm, even some men lost they head about me."
    it "Now I have mostly pain."
    n "I don't know what to say."
    n "I'm sorry. I feel for you."
    i "What had happened if someone like HER pities me."
    n "But no need to grieve - people can lose an arm and a leg and still be happy of other things."
    n "Well, at least you have me now."
    n "A friend... if you consider me a friend, of course."
    "[[Ildari smiles]"
    it "Maybe she's not that pathethic as I originally thought..."
    it "The only good thing I met in this hellhole."
    n "Want a hug?"
    "[[Ildari and Niyya hug]"
    i "Mmm..."
    nt "Looks like she really needed that hug."
    "[[they stop hugging]"
    "[[Ildari smirks]"
    nt "!"
    n "I... I'll be going now."
    "[[Niyya leaves]"
    nt "Sheesh, I really don't know her that well."
    nt "I only know her weak and sick."
    nt "The truth is... I don't really know her OTHER side."
    nt "I have a soft spot for the sufferning. Too soft."
    nt "...and she's got this pretty slender face that makes people more likeable."
    nt "Damn! Who can she be when she recovers?"
    nt "[[inhale, exhale]"
    nt "She's just lost and tired."


#______________________________________________________________________________________

# WHAT A MESS...
    play music night_of_chaos
    "[[ildari wakes up and there are fragments of the bodies all scattered around]"
    "[[a slide where she puts her feet on the ground and there are body parts on the floor]"
    i "What a mess..."
    # ? and something's wrong with my feet [her feet looks like skeleton's]




# DON'T. FOCUS. ON. THE. VOICES.
    "[[Ildari is in ashlands.]"
    "[[some doom/funeral music]"
    "[[buzzing of the flies]"
    "[[Ildari found a dead body of a mage (a bosmer in necromancer robes?)]"
    "(here come the whispers)"
    "body"
    "it's just a body"
    "flesh"
    "blood"
    "this one is real"
    "that was a mage"
    "was"
    "not now"
    "now it's flesh"
    "flesh"
    "flesh like around your heart"
    "[[sounds of fast heartbeat]"
    "[[Ildari's heart]"
    "[[His throat was slit.]"
    "slit throat"
    "slit"
    "cut"
    "that's not you Ildari"
    "[[His ghost is still hovering (or so Ildari sees) near his body]"
    "he was alive"
    "[[Next to him in the ash lies a (conjuration?) book]"
    "book"
    "spellbook"
    "you need spells"
    "you'll be dead without them"
    "DEAD"
    "[[She picks it up]"
    "[[Ildari returns to her room]"
    it "It's high time to me to do some magic, else I'll forever be stuck in this hellhole."
    "[[She opens a spellbook]"
    "(whispers intensify)"
    it "Voices."
    it "By the Three, I would do anything not to hear the voices!"
    "you have to try harder"
    "you didn't try hard enough"
    "try hard enough"
    "you don't try hard enough"
    "you were good"
    "you won't be good"
    "you are no good"
    "you won't be good"
    "no good"
    "good"
    "no good"
    "it will get worse"
    "[[she sits on bed with a dull expression]"
    it "How am I gonna keep on living like this?"
    it "Is it all what it takes to strip a man of will to live?"
    "[[A picture of the noose flashes briefly.]"
    "[[She imagines a dagger in her hand.]"
    "[[She imagines herself as the mage with her throat slit lying in the ash.]"
    it "No... no!"
    it "Those are not my thoughts!"
    it "I need to do something to stop the voices!"
    it "I can't live like that!"
    "Someone approaches."
    "Secret."
    "The books is your secret."
    "Hide it!"
    "Keep the secret!"
    "And now enters Niyya."
    "Ildari hides her book."
    it "Maybe... maybe it's time I confessed to someone - to her..."
    it "Maybe if I tell someone they will go?"
    it "She can't turn on me, can she?"
    # I WILL DO MY BEST TO HELP YOU
    play music magic_forest
    "[[Niyya enters Ildari's room]"
    i "Niyya, I think I have to... tell you something."
    i "But... I need you to keep this secret."
    n "Have I ever revealed any secret of yours, Ildari?"
    it "No, she haven't."
    "For now, at least."
    n "You can tell me. Feel free."
    i "[[inhale, exhale]"
    i "Do you want to know why I'm so tired?"
    n "Why?"
    i "When I wake up... I see a ghost, Niyya. Right in my room. And right when I leave it. And in the ashlands... They seem to follow everywhere I go."
    n "There are no ghosts Ildari."
    n "I've lived for so long in this place - it's safe."
    i "I think so, too. But I... I can't help noticing them. No matter how hard I try. And they are talking to me."
    n "I... don't know what to say."
    n "That must be tormenting you, isn't it?"
    i "Yes..."
    n "I... I don't understand what’s happening to you, Ildari - but I will try her best to help you."
    i "Tha... thanks."
    n "Do you want a hug?"
    "[[Niyya hugs Ildari.]"
    i "Wait... Do the others... suspect something?"
    i "I don't want anyone to know!"
    i "I... won't be trustworthy any longer."
    n "They are aware you have been weak for a long time... but I don't think so."
    n "I'm not sure how they mignt react to that fact, too."
    n "I won't tell anyone, I promise."
    n "Yet... I admire the fact that you manage to stay strong. Despite all of that."
    it "What a piece of good-intended bullshit."
    n "I need to go."
    it "Mhm."

    nt "Gods, so she sees imaginary ghosts. Ghosts, damn!"
    nt "Seeing the ghosts happens sometimes. Oh, what a crap it must be to see the imaginary ghosts in a world like this - where magic, ghosts, spriggans, even dragons can be such a common encounter."
    nt "It must be a hard time telling the real from the not. If she saw the ancient long-gone dwemer things would be different."


#______________________________________________________________________________________

###

# 9. SHE CAN WALK, SHE CAN WORK
    play music night_of_chaos
    "[[Niyya and m are talking, then Ildari approaches]"
    m "Seems like Ildari feels better now, her hands look better..."
    m "She could relieve us of some of that work."
    m "I suppose that kitchen duty would be suitable."
    n "But she is still weak."
    n "Her... head hurts."
    m "Don't babysit her, Niyya."
    m "Ildari, from now on you will be working in the kitchen."
    "this is an outright insult!"
    "you've fallen so low..."
    m "You seem to have enough strength to wander in the ashlands all day."
    i "Ye... Yes."
    m "Good. The ash yams are waiting for you, so get moving."
    "[[m leaves]"
    it "I have to do it."
    it "Can't let him reveal my secret."
    n "I'm sorry that happened."
    n "Umm... Ildari, are you sure it wouldn't be easier to tell about your affliction?"
    "tell who? HIM?"
    "[[Ildari has a very expressionless face]"
    i "No."


# 4. ASH YAMS AND REVENGE
    "[[Ildari looks at her hands and feet and notices that they are like skeleton's.]"
    it "Am I rotting?{p}Am I rotting?"
    "no, Ildari"
    "you are alive"
    "your heart stone is beating"
    "it hurts you, though"
    "it still hurts"
    "relentlessly"
    it "I'm so exhausted."
    "you have to do something"
    "you are being useless..."
    "[[Ildari sits by the kitchen table with a bowl and a knife and a heap of ash yams to peel]"
    "YOUR WORK AWAITS"
    it "Damn, this is embarassing."
    "[[sigh]"
    "[[a slide with her hands as she is peeling the ash yams]"
    it "...and to think that I was once a sorceress."
    "[[zoom in at her sad and tired face]"
    it "I had some other people to prepare my food."
    it "And I had whole days for my studies."
    it "Gaining knowledge."
    it "Refining techniques."
    "[[sigh]"
    it "It's all gone now."
    it "I'm too weak for that."
    "[[it's a memory Ildari recollects - she's lying covered with white cloth on a table, ready for the ritual, slightly smiling in her sleep]"
    it "What a fool I was to be so eager to undergo the ritual myself!"
    it "Wait..."
    it "No."

    ### ? THIS SHOULD BE REFORMATTED NOT AS THOUGHTS, BUT AS THE VOICES ?

    "[[slide with Neloth with a grim face on a golden background (from the bottom perspective so that he looks taller and more menancing)]"
    it "Neloth."
    it "That bastard..."
    it "He talked me into all of that!"
    it "He promised me almost godlike powers."
    it "[[slide with her heart]"
    it "And all I got is... pain."
    it "...and voices."
    it "[[sounds of the voices there]"
    it "[[slide with Ildari\'s hand clutching the peeling knife]"
    it "That all..."
    it "[[Ildari\'s angry face]"
    it "HIS FAULT!"


#______________________________________________________________________________________

# I CAN MAKE MY NIGHTMARES REAL
    play music ossuary_6_air
    "[[Ildari is in the ashlands]"
    it "Niyya..."
    it "I really appreciate what she's doing for me."
    it "But that damned Imperial~!"
    it "At least in ashlands I can be alone."
    i "ghosts"
    i "ghosts"
    i "ghosts everywhere"
    i "what could I talk about if i had friends"
    i "all i see is death"
    i "death death death death"
    i "they can only hate or pity me"
    i "instead, the ghosts keep talking to me" ### ? seem to know me better ?
    "you were a sorceress once, Ildari"
    "are you one now?"
    "no no no no"
    "she works in the kitchen"
    "Ildari"
    "you need to prove that you're a sorceress"
    "show the world how you can rise your servants from the ashes"
    "resurrect us!"
    i "Necromancy..."
    "[[zoom on Ildari's face]"
    it "Concentrate, Ildari."
    "[[zoom on her hand with a spell]"
    it "Concentrate."
    "[[she casts a spell (you need a sound)]"
    it "It doesn't work."
    "it doesn't"
    "pitiful"
    "[[she casts a spell again (you need a sound)]"
    it "Wait... it does."
    "[[a slide with ash spawns face + HEART]"
    a "Mmmmmm..."
    i "So... it's you."
    it "You were trying to communicate with me all that time."
    "[[the spell wears off (sound + upper perspective image with Ildari and bare ground.]"
    i "A creature made of ash..."
    i "...with a heart like mine."
    "[[Ildari bursts into an overly confident laughter]"
    "Ghosts!"
    "I can give them flesh."
    "I can make them real."
    "REAL!"
    "I WON'T BE THE ONLY ONE TO SEE THEM NOW!"
    "[[smug grin]"
    "Neloth, that fetcher~!"
    "He's going to see them, too!"
    ### ? maybe my source of torment can be my source of power? perhaps i'm far more used to death and ghosts that most of the sorcerers. And I got insensitive to death, suffering. That might be useful... ?



# THEY ALL LAGUH AT ME...
    "[[Ildari returns to her 'home', she's overjoyed. In background there's Nikolai.]"
    i "{{singing in whispers} He's going to see them. He's going to see them."
    i "{{Chuckles}"
    ni "{{snorts with laughter}"
    play music unseen_horrors
    it "What?"
    it "Sensless idiots, animals, beasts!"
    it "Ignorant fools to whose all virtue is naugth."
    it "Mocking my suffering. Mocking plans and ambitions."
    it "Do they know what kind of power I'm learning to wield?"
    it "What that damned heart stone could really do?"
    "he will learn what you can do"
    "it will be a pleasure to see his young face charring in the flames"
    "exposing the bones"
    "it's just some flesh"
    "with soul or without it"
    it "What?"
    it "No."
    it "Stop. Shut up."
    "all flesh is moldable"
    ### ? "you yourself were molded by neloth, too" ?
    "waiting for you to dip your hands in their intestines"
    "[[she sees some body parts scattered on the floor]"
    it "Damn!"



#______________________________________________________________________________________

# TALVAS THE REPLACEMENT
    play music ossuary_6_air
    "[[Ildari had gone to the ashlands again to practice ressurecting corpses.]"
    "Ildari"
    "there's a threat"
    "someone's"
    "someone's watching you"
    "[[Then she sees a young dunmer battling an ash spawn (that she conjured earlier) and filling a soul gem]"
    it "My ash spawn!"
    "he is storng"
    "quick"
    "young"
    "deadly"
    "brilliant"
    "sharp"
    "were you as sharp as him Ildari?"
    "you are certainly not sharp now"
    "you have the voices"
    "they won't let you be too sharp"
    "robes"
    "he looks so dashing in his robes"
    "you don't have such robes Ildari"
    "the robes you were buried in are bloodstained"
    "you wear rags"
    "and ash"
    "[[Ildari is staring at him.]"
    "[[The dunmer notices her.]"
    t "Uhm... hello."
    t "I didn't notice you."
    t "Been busy with that ash spawn."
    t "Is everything all right?"
    i "Quite so. Yes."
    t "Great."
    t "I'll be on my way then."
    i "Wait! Wait..."
    t "?"
    i "Who are you?"
    t "I'm Talvas. A new aprrentice of master Neloth."
    it "My replacement..."
    t "He lives there, in this tower."
    play music invariance
    "[[there's a slide with Tel Mithryn in the distance along with the sound of uneatrhly disturbing piano note. The image is distorted (there are black noises (blooddrops) on the 'frame' of the image.]"
    "this horrid place"
    "Neloth"
    i "A student..."
    t "Yes."
    it "How naïve he is."
    it "I won't be there to see how ethusiastic he will be when his master rips his heart out!"
    t "Uhm... what's your name, if i may ask?"
    i "Il..."
    "bit your toungue!"
    i "Ilena."
    i "What are you doing in the middle of nowhere?"
    t "My master send me to fill some soul gems."
    t "And you? It's dangerous out there."
    i "Bone broth."
    i "I'm collecting bones in the ash. For the bone broth."
    "madwoman"
    t "Are you sure you feel all right?"
    "madwoman"
    i "Yes. It will pass eventually."
    i "I need to go, sorry."
    "madwoman"
    t "Please, let me escort you to wherever you live."
    it "!"
    t "It's not the safest place."
    i "NO!"
    t "I won't... disturb you then."
    t "See you."
    it "Damn, I was acting weird."
    it "He sure suspects something."
    "Neloth"
    "he's a Neloth's pawn"
    play music magic_forest
    "[[A slide with Talvas alone]"
    tt "Poor madwoman."
    tt "Maybe I should follow her after all?"
    tt "Master will get angry that this took too long... but it can get real dangerous there."
    tt "After all, she's better alive that dead."
    play music invariance
    "[[Slide with Ildari amidst the wilderness]"
    "[[Ildari walks away.]"
    it "Oof. Whoa I'm finally away from him."
    "[[Slide with Talvas' feet just about to step on a twig]"
    tt "So far clear."
    "[[Slide with Talvas stepping on a branch. (sound of a branch breaking)]"
    t "Damn!"
    "NO!"
    "HE'S SPYING ON YOU"
    "RUN!"
    "he knows about your ash spawns!"
    "don't let him take your life so easily!"
    "[[slide with Ildari instantly running away]"
    "[[slide with Talvas facepalming]"
    t "Idiot, idiot, idiot, idiot!"
    t "You got her dead scared! Running in panic through the woods!"
    t "Now she might run into real danger!"



# ? SOMETHING'S OFF WITH HER ?
    play music reign_supreme
    "[[Marius is ordering the crates from the cart, Nikolai enters.]"
    m "Where's Ildari?"
    ni "Huh? Her? She's probably gone to the ashlands, as usual."
    m "Dammit! I told her to help me with the crates!"
    m "What does she do in those ashlands, anyways?"
    ni "I dunno. She's whacky. I saw her once or twice taking almost orgasmic pleasure in dipping her feet in the ash."
    m "What? Does she take skooma when no one's around?"
    ni "Nah, I don't think so."
    ni "I suspect it's something else, actually. Not only skooma addicts can behave like that."
    m "What, then?"
    ni 'I\'ve been to some strange cities before...'
    ni 'and in one of them they had this place called "asylum".'
    ni "It very much resembled a hospital. And, I promise, there was no skooma involved."
    ni "The people from the outside were gererally intact... but I haven't seen more madness in one place in my life!"
    ni "They were wailing! Shouting! Rolling on the floor! Stabbing themselves with forks!"
    ni "...smearing their feces on the walls!"
    ni "Pfff, some of them had to be even locked away in the cells - for the sake of safety!"
    ni "I'm not gonna set there my foot ever again!"
    m "So you think she's going insane?"
    m "We ought to lock her up for a while, just in case."
    m "Do you think she really is dangerous?"
    ni "Well, no one really knows until something happens. Even Ildari."
    ni "Locking up seems excessive for now. It may worsen things."
    ni "I myself would probably go mad solely because of being locked in the cell and constantly monitored."
    ni "We should fall back on such a drastic measure only if we get some more sound proofs of her being dangerous."
    m "We should watch her more closely, then."
    "[[Ildari is standing by the wall, listening to everything with eyes wide open]"
    it "WHAT?"
    it "Watch me more closely?"
    it "Calling me insane, Gods damn them!"
    it "What they are planning to do with me behind my back?"
    it "First this pitiful apprentice, then THEM?!"
    "you can never be really free from Neloth"
    "he's spinning his web around you like a spider"
    "and then he'll suck you dry"
    "if you want to live..."
    "TAKE ACTION"
    it "Stop. Please."
    it "Am I really becoming unhinged?"
    "you are not unhinged Ildari"
    "it's just that your hinges creak"
    "creak creak creak creak"
    "mwahahahaha"
    "[[get sound of the hinges creaking and nervous lauthter]"
    it "NO!"
    i "Shut up. Shut up."
    i "Shut up!"
    "[[Niyya enters the hallway, she gets worried.]"
    nt "What is she saying? There's no none there."
    "[[Ildari runs to her room.]"
    n "Ildari? Ildari!"
    n "Wait!"



# ILDARI? ILDARI! WAIT...
    play music night_of_chaos
    "[[Nikolai approaches Niyya]"
    ni "Cool it!"
    ni "You don't have to babysit her."
    n "{{inhale/exhale}"
    n "Ugh, her behavior is such a burden to me recently. Sheesh, I guess I have to confess to someone."
    ni "Well, if you wish so... then yeah."
    n "I'm afraid she's going..."
    ni "...mad? I think the same."
    ni "Good that you want to help her, but trust me, once people become REALLY insane, you can't really be friends with them."
    ni "For a sane person, like you I guess, it's unimaginable even in the slightiest bit in what kind of state their mind is."
    ni "They are not responsible for their actions nor their feelings."
    "[[here Niyya recollects hugging/(? kissing ?) Ildari]"
    ni "And from what I've heard... you can really be friends with people unless you FEEL the same, at least form time to time."
    ni "I don't want to get influenced by such people at all. No use tricking yourself they are just like any other."
    n "{{sigh}"
    n "Thank you."
    n "I'll keep that in mind."




# I KNOW ONLY PAIN AND DEATH, NIYYA
    play music unseen_horrors
    "[[Niyya has much colder expression.]"
    n "Ildari..."
    i "{{Ildari sobs loudly and breathes quickly and inconsistently, she has red nose from crying}"
    i "I see only death and monsters, Niyya."
    i "I know only pain and violence! Constant pain! It hurts! HURTS!"
    i "I'm not a human. I'm a beast."
    nt "Technically you are an elf, but I don't think I should say that."
    i "Hug me."
    i "Please..."
    "[[they hug]"
    nt "Sheesh, Nikolai was right. What have I gotten myself into."



#______________________________________________________________________________________




# THE PARASITE ILDARI
    m "If that damned fetcher will keep on shirking her job like that I'm gonna sell her old fancy clothes. The blood went off almost completely so they might fetch a high price."
    n "{{sighs}"
    m "Don't sigh, Niyya. She gets what she asks for."
    n "Maybe... maybe we should keep her there after all? She might not have anyone else to take care of her!"
    ni "what? You women and your pitiful sentiments."
    m "She's barely fit for any work yet she still consumes our precious food. And it got A LOT scarcer recently!"
    m "She leaves. Maybe someone in Raven Rock will give her some scraps if she'll beg humbly enough."
    "[[face of Niyya contemplating, looking at the side.]"
    n "Fine, I'll tell her that."



# SO I HAVE NO FRIENDS...
    "[[Niyya enters Ildari's room.]"
    "[[Ildari still has a tired face and red nose from crying.]"
    i "What again?"
    n "I need to talk with you."
    i "Hm?"
    n "Ildari, the fact that you see ghosts, doesn't mean that you should act as if you were there."
    n "That's not real! You should oppose if you still consider yourself a thinking being! Pull yourself together! Not run away to the ashlands!"
    m "There are no voices and ghosts, Ildari!"
    m "You spend whole days in ashlands instead of earning for your living!"
    it "That was Deanicci, yes? He told you all of that, yes?! YES?!"
    "[[niyya inhales/exhales loudly]"
    n "Marius wants you to leave."
    n "You will surely find a way to obtain food and a place to sleep in Raven Rock or somewhere. I'm sure there are benevolent people out there that will pity on you."
    n "I'm gonna take a break from... you."
    n "It's too much for me."
    n "Sorry."
    i "Oh, so she's such a soft and gentle being that she wants to leave before she sees how Neloth immerses me in sufferings!"
    "[[Ildari watches Niyya with eyes wide open]"
    "[[Niyya becomes on the verge of crying, too]"
    n "Ummm... I guess we can meet again as soon as this will be over."
    it 'What "THIS" you mean, Niyya? I have a f*cking heart stone. "THIS" will never go away, you cold b*tch!'
    n "Uhm... do you want a hug?"
    "[[they hug]"
    it "So I have no friends."
    "her flesh is so soft in your arms"
    "that's how a traitor feels"
    "traitor can have soft spots, too if you know where to hit them"
    "[[they stop hugging]"
    "[[Niyya sighs] (get some sigh sounds)"
    n "It will be allright."
    "[[Ildari sits in her hunched pose, smiling wildly with her hair covering her eyes]"
    i "Niyya..."
    i "{{whispers} Can I tell you a secret?"
    n "Yes..."
    i "{{whispers} But will you keep it?"
    n "Yes."
    i "{{whispers}Do you know that..."
    n "Hm?"
    i "{{whispers} Do you know that I've resurrected corpses?"
    n "Eh?"
    nt "Gods, she's completely out of her mind."
    n "You should have some rest, Ildari."
    n "I need to go."
    n "Goodbye."


# NIYYA'S SMALL, SOFT HEART
    play music anguish
    "(heartbeat sounds in the bg)"
    "[[A slide with Niyya with eyes wide open - zoom on her face.]"
    nt "Oh, no!"
    nt "What has gotten into me to say such things?!"
    nt "Nikolai, that scum. And Deannici..."
    nt "If she was handled with more care maybe she wouldn't crack up and say such gibberish!"
    nt "What was she talking about again? Necromancy?"
    nt "Is that a REAL secret or some sort of new hallucination?"
    nt "She's probably talking gibberish. Or..."
    nt "No, I can't tell anyone."
    nt "They'll get the wrong idea and then they might even turn on her!"
    n "{{sigh}"
    nt "I should convince the rest to let Ildari stay."
    nt "If we... I don't take care of her she might be lost. Forever."



# MIRROR, MIRROR - AND ALL MY FOES
    play music crypto
    # ossuary 2 is too intense
    "[[Ildari stands in front of the mirror - shot from the side.]"
    i "I've managed to get the robe of house Telvanni back while everyone was sleeping."
    "[[Now there's a picture with the table with some clutter on it, and the mirror above - in the mirror there's front view Ildari (from her chest up)"
    "[[smug]"
    i "Jeez, I look splendid in it."
    i "You wear such robes everyday, Neloth, don't you?"
    i "You even were generous enough to bury me in one of them as a way to honour my invaluable deeds for the house Telvanni."
    i "...having my body cut open and rearranged like a sacrificial cow!"
    i "You've promised me being almost like a god."
    "[[mad]"
    i "Yet, you've forgot to mention constant pain. And the Voices!"
    "[[smug]"
    i "You thought yourself so sly that you sent those pitiful miners to watch my every move."
    i "Thanks especially for my guardian angel, Niyya."
    "[[mad]"
    i "Whom you ordered to get close enough to me to stab me right where my heart was!"
    "[[smug]"
    i "How filthy of you."
    i "I know you are watching me closely of the other side of the mirror."
    i "So I'll let you know it: I'm gonna defend my life."
    i "Go on, pull all your aces out of your sleeve."
    i 'Your pitiful /"miners/" will be gone, soon.'
    "[[mad]"
    i "Tomorrow will be the night of my wrath!" ### ? or today ?
    "[[(a sound of impact magic and broken glass) - she destroys the mirror]"
    ### ? does everything go blank or do we see shattered glass ?




# THE NIGHT OF MY WRATH
    play music ossuary_2_turn
    "[[Ildari arrives with her servants]"
    i "Surrender."
    n "What?"
    n "No, no!"
    ni "What the f*ck are those?"
    i "SHUT UP!"
    i "You won't get my heart stone!"
    i "You laughted at my suffering!"
    "[[she is turned backwards to imperial, he grabs a pickaxe, swings it and tries to smash her head]"
    "[[A slide with she saying 'huh?' and imperial behind her back swinging an axe - and behind him there's an ash spawn with a sword]"
    "[[A slide with Ildari screaming being painfully hit with a pickaxe. (scream sound)]"
    "[[A slide with imperial being pierced with an ash spawn sword]"
    "[[A slide with Ildari instantly healing]"
    "[[A slide with Niyya and Nikolai wide-opened, being silent]"
    ni "..."
    n "..."



# CAGE THEM!
    nt "Ildari?"
    nt "No, that can't be..."
    nt "How did she...?"
    nt "So she was right about those ghosts?"
    n "No! Please!"
    n "I beg you!"
    i "TRAITOR!"
    i "Your betrayal hurt me the most!"
    i "I know you!{p}I know all of you!"
    i "Neloth's pawns!"
    "your stone"
    "it's safe in your chest for now"
    "if you arrest them"
    ni "I don’t know any Neloth!"
    ### ? her victims are whispering in the cell about: who Neloth might be? What's wrong with her? ?


# NIYYA'S LAMENT
    play music unseen_horrors
    nt "How naïve I was to help her."
    nt "And all my friends died because of that."
    "[[Ildari comes and Niyya stays silent.]"
    nt "Gods, I don't want to die!"
    nt "This isn't the ildari I knew. Or I never knew the real Ildari?"
    nt "What happened to you?"
    nt "Why, Ildari, why?"
    nt "You could have forget about your revenge. About all of that."
    nt "Move somewhere."
    nt "Be happy."
    nt "You had me, after all."
    nt 'Is that because of this wound, this "heart stone" of hers?'
    i "Ugh, I've bungled it all up again..."
    i "I need another fresh subject."
    i "Nikolai!"
    ni "No! Please!"
    "[[a slide of Ildari's hand casting a spell.]"
    ni "Uuugh!"
    ni "Quitet breathing."
    nt "No, there's no another reality."
    nt 'I wonder if that "Neloth" of hers even gives a sh*t about her!'



# YEARS OF RESEARCH
    "[[Ildari surrounded with ash spawns]"
    it  "These warrens are well suited to me."
    "[[Ildari leaning over a journal with madman's scribbles]"
    it "I can plot my vengeance undisturbed."
    "[[Ildari reads sth.]"
    it "Still, I can feel Neloth's gaze at my neck."
    i "Oh, shit, he sees me."
    "[[she looks at the window]"
    "[[she continues to read under the window]"
    "[[She's creating ash spawns/atronachs.]"
    it "Yet I know it isn't enough. Neloth is a wily old wizard. I need more power."



# DON'T BE RIDICULOUS, CARIUS
    play music tempting_secrets
    it "Oh, and I've discovered a crypt with a plenty of dead experiment subjects"
    "[[a shot of ildari incatning sth (and gesturing with her hands) over a lying carius) (get a mumbling spells sound - or record)]"
    "[[a shot of falx carius with closed eyes]"
    "[[a shot of falx carius with opened eyes, agitated]"
    c "ENEMIES!"
    c "They want to take down the fort!"
    "[[ildari with scornful face]"
    i "There are no enemies there!"
    "[[a slide with carius who got up and looks backwards]"
    c "A spy!"
    c "KILL HER!"
    "[[a slide with Ildari's hand blasting a powerful spell (a sound of powerful 'boom' spell)]"
    c "Nooo..."
    "[[silence]"
    ### ? a shot of carius sleeping again ?
    "[[a slide of Ildari hunching over with a heart stone in her hand.]"
    i "What went wrong?"
    i "Fuck, I've used up all my magic for today and there's still no results."
    i "This is becoming intolerable."
    i "I'm beginning to wonder if someone with a heartstone can be commanded at all."
    "[[Ildari laughs wildly while hunched]"
    ### ? you should remove either archer or backstabber
    "[[she would have a brief vision that someone is there to stab her in the back]"
    "[[then she realizes that she is still breathing and that was not real]"
    "[[she sees an archer]"
    i "Archer?!"
    "[[Ildari is almost crying]"
    it "NO! PLEASE!"
    it "I do not want to die"
    i "Oh."
    i "There's no one there, Ildari."
    i "No one..."
    i "Shhh..."
    it "Damn, I'm letting myself to be driven by such delusions and primary instincts."
    "[[another shot of Carius]"
    it "...driven by the loopholes in my personality."



# NIYYA'S BITTERNESS
    "[[there's Niyya in the cell, but she's far more wrinkled]"
    nt "I don't know how many years it's been there."
    nt "She's an elf, so that's nothing for her, but I've probably wasted half of my life in this cell!"
    nt "I've only grew older and more tired."
    nt "That b*tch!"
    nt 'I hope that this "Neloth" will finally put an end to her!'
    ### ? nt 'Huh?'
    ### ? "[[there's a shadow over her]"




# Ossuary 4 animate
# Ossuary 2 turn
# THIS TIME IT'S FOR REAL...
    play music ossuary_2_turn
    "Ildari was reading sth."
    "There are footsteps."
    "Someone's approaching"
    "This time it's for real"
    it "I knew it."
    it "I knew it all."
    "Ildari"
    "Say hello to your killer"
    "HELLO!"
    i "Shaddup!"
    "[[she comes to the platform and exclaims things]"
    "Neloth was a fool to send some lowlife to finish me off."
    "your chamber will be your fortress"
    "RUN!"
    "Prepare, Ildari"
    "The heart stone protects me."
    "The heart stone protects me."
    "[[movements indicating that she's preparing for the fight - hand on her staff, clenched fist, pulsating stone]"
    "[[last slide is the closeup of her determined face]"

    "THE END."

    # This ends the game.

    return
