import urllib
import requests
import re
url_start =  'https://text-to-speech-demo.ng.bluemix.net/api/synthesize?text='
url_end = '&voice=en-US_AllisonVoice&accept=audio%2Fmp3'
text = """
and heave a finished bottle into the woods. In his 
goodnight kiss we smelled the cloying 
sweetness of Clorets, the mints he chewed to camouf
lage his dragon's breath. 
I can summon up that kiss right now by recalling Th
eodore Roethke's lines about his own 
father: 
The whiskey on your breath Could make a small boy d
izzy; But I hung on like death: 
Such waltzing was not easy. 
Such waltzing was hard, terribly hard, for with a b
oy's scrawny arms I was trying to hold 
my tipsy father upright. 
For years, the chief source of those incriminating 
bottles and cans was a grimy store a 
mile from us, a cinderblock place called Sly's, wit
h two gas pumps outside and a mangy 
dog asleep in the window. Inside, on rusty metal sh
elves or in wheezing coolers, you 
could find pop and Popsicles, cigarettes, potato ch
ips, canned soup, raunchy postcards, 
fishing gear, Twinkies, wine, and beer. When Father
 drove anywhere on errands, Mother 
would send us along as guards, warning us not to le
t him out of our sight. And so with 
one or more of us on board, Father would cruise up 
to Sly's, pump a dollar's worth of gas 
or plump the tires with air, and then, telling us t
o wait in the car, he would head for the 
doorway. 
Dutiful and panicky, we cried, "Let us go with you!
" 
"No," he answered. "I'll be back in two shakes." 
"Please!" 
"No!" he roared. "Don't you budge or I'll jerk a kn
ot in your tails!" 
So we stayed put, kicking the seats, while he ducke
d inside. Often, when he had parked 
the car at a careless angle, we gazed in through th
e window and saw Mr. Sly fetching 
down from the shelf behind the cash register two gr
een pints of Gallo wine. Father 
swigged one of them right there at the counter, stu
ffed the other in his pocket, and then 
out he came, a bulge in his coat, a flustered look 
on his reddened face.  
Because the mom and pop who ran the dump were neigh
bors of ours, living just down the 
tar-blistered road, I hated them all the more for p
oisoning my father. I wanted to sneak in 
their store and smash the bottles and set fire to t
he place. I also hated the Gallo brothers, 
Ernest and Julio, whose jovial faces beamed from th
e labels of their wine, labels I would 
find, torn and curled, when I burned the trash. I n
oted the Gallo brothers' address in 
California and studied the road atlas to see how fa
r that was from Ohio, because I meant 
to go out there and tell Ernest and Julio what they
 were doing to my father, and then, if 
they showed no mercy, I would kill them. 
5
While growing up on the back roads and in the count
ry schools and cramped Methodist 
churches of Ohio and Tennessee, I never heard the w
ord alcoholic, never happened 
across it in books or magazines. In the nearby town
s, there were no addiction-treatment 
programs, no community mental-health centers, no Al
coholics Anonymous chapters, no 
therapists. Left alone with our grievous secret, we
 had no way of understanding Father's 
drinking except as an act of will, a deliberate fol
ly or cruelty, a moral weakness, a sin. He 
drank because he chose to, pure and simple. Why our
 father, so playful and competent 
and kind when sober, would choose to ruin himself a
nd punish his family we could not 
fathom. 
Our neighborhood was high on the Bible, and the Bib
le was hard on drunkards. "Woe to 
those who are heroes at drinking wine and valiant m
en in mixing strong drink," wrote 
Isaiah. "The priest and the prophet reel with stron
g drink, they are confused with wine, 
they err in vision, they stumble in giving judgment
. For all tables are full of vomit, no 
place is without filthiness." We children had seen 
those fouled tables at the local 
truckstop where the notorious boozers hung out, our
 father occasionally among them. 
"Wine and new wine take away the understanding," de
clared the prophet Hosea. We had 
also seen evidence of that in our father, who could
 multiply seven-digit numbers in his 
head when sober but when drunk could not help us wi
th fourth-grade math. Proverbs 
warned: "Do not look at wine when it is red, when i
t sparkles in the cup and goes down 
smoothly. At the last it bites like a serpent and s
tings like an adder. Your eyes will see 
strange things, and your mind utter perverse things
." Woe, woe. 
Dismayingly often, these biblical drunkards stirred
 up trouble for their own kids. Noah 
made fresh wine after the flood, drank too much of 
it, fell asleep without any clothes on, 
and was glimpsed in the buff by his son Ham, whom N
oah promptly cursed. In one 
passage--it was so shocking we had to read it under
 our blankets with flashlights--the 
patriarch Lot fell down drunk and slept with his da
ughters. The sins of the fathers set 
their children's teeth on edge. 
Our ministers were fond of quoting St. Paul's prono
uncement that drunkards would not 
inherit the kingdom of God. These grave preachers a
ssured us that the wine referred to in 
the Last Supper was in fact grape juice. Bible and 
sermons and hymns combined to give 
us the impression that Moses should have brought do
wn from the mountain another stone 
tablet, bearing the Eleventh Commandment: Thou shal
t not drink. 
The scariest and most illuminating Bible story apro
pos of drunkards was the one about 
the lunatic and the swine. We knew it by heart: Whe
n Jesus climbed out of his boat one 
day, this lunatic came charging up from the graveya
rd, stark naked and filthy, frothing at 
the mouth, so violent that he broke the strongest c
hains. Nobody would go near him. 
Night and day for years, this madman had been waili
ng among the tombs and bruising 
himself with stones. Jesus took one look at him and
 said, "Come out of the man, you 
unclean spirits!" for he could see that the lunatic
 was possessed by demons. Meanwhile, 
some hogs were conveniently rooting nearby. "If we 
have to come out," begged the 
demons, "at least let us go into those swine." Jesu
s agreed, the unclean spirits entered the 
hogs, and the hogs raced straight off a cliff and p
lunged into a lake. Hearing the story in 
6
Sunday school, my friends thought mainly of the pig
s. (How big a splash did they make? 
Who paid for the lost pork?) But I thought of the r
edeemed lunatic, who bathed himself 
and put on clothes and calmly sat at the feet of Je
sus, restored--so the Bible said--to "his 
right mind." 
When drunk, our father was clearly in his wrong min
d. He became a stranger, as fearful 
to us as any graveyard lunatic, not quite frothing 
at the mouth but fierce enough, quick-
tempered, explosive; or else he grew maudlin and we
epy, which frightened us nearly as 
much. In my boyhood despair, I reasoned that maybe 
he wasn't to blame for turning into 
an ogre: Maybe, like the lunatic, he was possessed 
by demons. 
If my father was indeed possessed, who would exorci
se him? If he was a sinner, who 
would save him? If he was ill, who would cure him? 
If he suffered, who would ease his 
pain? Not ministers or doctors, for we could not br
ing ourselves to confide in them; not 
the neighbors, for we pretended they had never seen
 him drunk; not Mother, who fussed 
and pleaded but could not budge him; not my brother
 and sister, who were only kids. 
That left me. It did not matter that I, too, was on
ly a child, and a bewildered one at that. I 
could not excuse myself. 
On first reading a description of delirium tremens-
-in a book on alcoholism I smuggled 
from a university library--I thought immediately of
 the frothing lunatic and the frenzied 
swine. When I read stories or watched films about g
risly metamorphoses--Dr. Jekyll 
becoming Mr. Hyde, the mild husband changing into a
 werewolf, the kindly neighbor 
inhabited by a brutal alien--I could not help but s
ee my own father's mutation from sober 
to drunk. Even today, knowing better, I am attracte
d by the demonic theory of drink, for 
when I recall my father's transformation, the emerg
ence of his ugly second self, I find it 
easy to believe in being possessed by unclean spiri
ts. We never knew which version of 
Father would come home from work, the true or the t
ainted, nor could we guess how far 
down the slope toward cruelty he would slide.  
How far a man could slide we gauged by observing ou
r back-road neighbors--the out-of-
work miners who had dragged their families to our c
orner of Ohio from the desolate 
hollows of Appalachia, the tightfisted farmers, the
 surly mechanics, the balked and 
broken men. There was, for example, whiskey-soaked 
Mr. Jenkins, who beat his wife and 
kids so hard we could hear their screams from the r
oad. There was Mr. Lavo the wino, 
who fell asleep smoking time and again, until one n
ight his disgusted wife bundled up the 
children and went outside and left him in his easy 
chair to burn; he awoke on his own, 
staggered out coughing into the yard, and pounded h
er flat while the children looked on 
and the shack turned to ash. There was the truck dr
iver, Mr. Sampson, who tripped over 
his son's tricycle one night while drunk and got ma
d, jumped into his semi, and drove 
away, shifting through the dozen gears, and never c
ame back. We saw the bruised 
children of these fathers clump onto our school bus
, we saw the abandoned children 
huddle in the pews at church, we saw the stunned an
d battered mothers begging for help 
at our doors. 
7
Our own father never beat us, and I don't think he 
beat Mother, but he threatened often. 
The Old Testament Yahweh was not more terrible in H
is rage. Eyes blazing, voice 
booming, Father would pull out his belt and swear t
o give us a whipping, but he never 
followed through, never needed to, because we could
 imagine it so vividly. He shoved us, 
pawed us with the back of his hand, not to injure, 
just to clear a space. I can see him 
grabbing Mother by the hair as she cowers on a chai
r during a nightly quarrel. He twists 
her neck back until she gapes up at him, and then h
e lifts over her skull a glass quart 
bottle of milk, the milk spilling down his forearm,
 and he yells at her, "Say just one more 
word, one goddamn word, and I'll shut you up!" I fe
ar she will prick him with her sharp 
tongue, but she is terrified into silence, and so a
m I, and the leaking bottle quivers in the 
air, and milk seeps through the red hair of my fath
er's uplifted arm, and the entire scene is 
there to this moment, the head jerked back, the clu
b raised. 
When the drink made him weepy, Father would pack, k
iss each of us children on the 
head, and announce from the front door that he was 
moving out. "Where to?" we 
demanded, fearful each time that he would leave for
 good, as Mr. Simpson had roared 
away for good in his diesel truck. "Someplace where
 I won't get hounded every minute," 
Father would answer, his jaw quivering. He stabbed 
a look at Mother, who might say, 
"Don't run into the ditch before you get there," or
 "Good riddance," and then he would 
slink away. Mother watched him go with arms crossed
 over her chest, her face closed like 
the lid on a box of snakes. We children bawled. Whe
re could he go? To the truck stop, 
that den of iniquity? To one of those dark, ratty f
lophouses in town? Would he wind up 
sleeping under a railroad bridge or on a park bench
 or in a cardboard box, mummied in 
rags like the bums we had seen on our trips to Clev
eland and Chicago? We bawled and 
bawled, wondering if he would ever come back. He al
ways did come back, a day or a 
week later, but each time there was a sliver less o
f him. 
In Kafka's METAMORPHOSIS, which opens famously with
 Gregor Samsa waking up 
from uneasy dreams to find himself transformed into
 an insect, Gregor's family keep 
reassuring themselves that things will be just fine
 again "when he comes back to us." 
Each time alcohol transformed our father we held ou
t the same hope, that he would really 
and truly come back to us, our authentic father, th
e tender and playful and competent 
man, and then all things would be fine. We had grou
nds for such hope. After his tearful 
departures and chapfallen returns, he would sometim
es go weeks, even months, without 
drinking. Those were glad times. Every day without 
the furtive glint of bottles, every 
meal without a fight, every bedtime without sobs en
couraged us to believe that such bliss 
might go on forever.  
Mother was fooled by such a hope all during the for
ty-odd years she knew Greeley Ray 
Sanders. Soon after she met him in a Chicago delica
tessen on the eve of World War II 
and fell for his butter-melting Mississippi drawl a
nd his wavy red hair, she learned that he 
drank heavily. But then so did a lot of men. She wo
uld soon coax or scold him into 
breaking the nasty habit. She would point out to hi
m how ugly and foolish it was, this 
bleary drinking, and then he would quit. He refused
 to quit during their engagement, 
however, still refused during the first years of ma
rriage, refused until my older sister 
came along. The shock of fatherhood sobered him, an
d he remained sober through my 
8
birth at the end of the war and right on through un
til we moved in 1951 to the Ohio 
arsenal. The arsenal had more than its share of alc
oholics, drug addicts, and other 
varieties of escape artists. There I turned six and
 started school and woke into a child's 
flickering awareness, just in time to see my father
 begin sneaking swigs in the garage. 
He sobered up again for most of a year at the heigh
t of the Korean War, to celebrate the 
birth of my brother. But aside from that dry spell,
 his only breaks from drinking before I 
graduated from high school were just long enough to
 raise and then dash our hopes. Then 
during the fall of my senior year--the time of the 
Cuban Missile Crisis, when it seemed 
that the nightly explosions at the munitions dump a
nd the nightly rages in our household 
might spread to engulf the globe--Father collapsed.
 His liver, kidneys, and heart all 
conked out. The doctors saved him, but only by a ha
ir. He stayed in the hospital for 
weeks, going through a withdrawal so terrible that 
Mother would not let us visit him. If 
he wanted to kill himself, the doctors solemnly war
ned him, all he had to do was hit the 
bottle again. One binge would finish him. 
Father must have believed them, for he stayed dry t
he next fifteen years. It was an answer 
to prayer, Mother said, it was a miracle. I believe
 it was a reflex of fear, which he 
sustained over the years through courage and pride.
 He knew a man could die from drink, 
for his brother Roscoe had. We children never laid 
eyes on doomed Uncle Roscoe, but in 
the stories Mother told us he became a fairy-tale f
igure, like a boy who took the wrong 
turn in the woods and was gobbled up by the wolf. 
The fifteen-year dry spell came to an end with Fath
er's retirement in the spring of 1978. 
Like many men, he gave up his identity along with h
is job. One day he was a boss at the 
factory, with a brass plate on his door and a reput
ation to uphold; the next day he was a 
nobody at home. He and Mother were leaving Ontario,
 the last of the many places to 
which his job had carried them, and they were movin
g to a new house in Mississippi, his 
childhood stomping ground. As a boy in Mississippi,
 Father sold Coca-Cola during 
dances while the moonshiners peddled their brew in 
the parking lot; as a young blade, he 
fought in bars and in the ring, winning a state Gol
den Gloves championship; he gambled 
at poker, hunted pheasant, raced motorcycles and ca
rs, played semiprofessional baseball, 
and, along with all his buddies--in the Black Cat S
aloon, behind the cotton gin, in the 
woods--he drank hard. It was a perilous youth to dr
eam of recovering. 
After his final day of work, Mother drove on ahead 
with a car full of begonias and 
violets, while Father stayed behind to oversee the 
packing. When the van was loaded, the 
sweaty movers broke open a six-pack and offered him
 a beer.  
"Let's drink to retirement!" they crowed. "Let's dr
ink to freedom! to fishing! hunting! 
loafing! Let's drink to a guy who's going home!" 
At least I imagine some such words, for that is all
 I can do, imagine, and I see Father's 
hand trembling in midair as he thinks about the fif
teen sober years and about the doctors' 
warning, and he tells himself, Goddamnit, I am a fr
ee man, and Why can't a free man 
drink one beer after a lifetime of hard work? and I
 see his arm reaching, his fingers 
9
closing, the can tilting to his lips. I even supply
 a label for the beer, a swaggering brand 
that promises on television to deliver the essence 
of life. I watch the amber liquid pour 
down his throat, the alcohol steal into his blood, 
the key turn in his brain. 
Soon after my parents moved back to Father's treach
erous stomping ground, my wife and 
I visited them in Mississippi with our four-year-ol
d daughter. Mother had been too 
distraught to warn me about the return of the demon
s. So when I climbed out of the car 
that bright July morning and saw my father napping 
in the hammock, I felt uneasy, and 
when he lurched upright and blinked his bloodshot e
yes and greeted us in a syrupy voice, 
I was hurled back into childhood. 
"What's the matter with Papaw?" our daughter asked.
"Nothing," I said. "Nothing!" 
Like a child again, I pretended not to see him in h
is stupor, and behind my phony smile I 
grieved. On that visit and on the few that remained
 before his death, once again I found 
bottles in the workbench, bottles in the woods. Aga
in his hands shook too much for him 
to run a saw, to make his precious miniature furnit
ure, to drive straight down back roads. 
Again he wound up in the ditch, in the hospital, in
 jail, in the treatment center. Again he 
shouted and wept. Again he lied. "I never touched a
 drop," he swore. "Your mother's 
making it up." 
I no longer fancied I could reason with the men who
se names I found on the bottles--Jim 
Beam, Jack Daniel's--but I was able now to recall t
he cold statistics about alcoholism: ten 
million victims, fifteen million, twenty. And yet, 
in spite of my age, I reacted in the same 
blind way as I had in childhood, by vainly seeking 
to erase through my efforts whatever 
drove him to drink. I worked on their place twelve 
and sixteen hours a day, in the swelter 
of Mississippi summers, digging ditches, running el
ectrical wires, planting trees, mowing 
grass, building sheds, as though what nagged at him
 was some list of chores, as though 
by taking his worries upon my shoulders I could red
eem him. I was flung back into 
boyhood, acting as though my father would not drink
 himself to death if only I were 
perfect. 
I failed of perfection; he succeeded in dying. To t
he end, he considered himself not sick 
but sinful. "Do you want to kill yourself?" I asked
 him. "Why not?" he answered. "Why 
the hell not? What's there to save?" To the end, he
 would not speak about his feelings, 
would not or could not give a name to the beast tha
t was devouring him.  
In silence, he went rushing off the cliff. Unlike t
he biblical swine, however, he left 
behind a few of the demons to haunt his children. L
ife with him and the loss of him 
twisted us into shapes that will be familiar to oth
er sons and daughters of alcoholics. My 
brother became a rebel, my sister retreated into sh
yness, I played the stalwart and dutiful 
son who would hold the family together. If my fathe
r was unstable, I would be a rock. If 
he squandered money on drink, I would pinch every p
enny. If he wept when drunk--and 
only when drunk--I would not let myself weep at all
. If he roared at the Little League 
10
umpire for calling my pitches balls, I would throw 
nothing but strikes. Watching him 
flounder and rage, I came to dread the loss of cont
rol. I would go through life without 
making anyone mad. I vowed never to put in my mouth
 or veins any chemical that would 
banish my everyday self. I would never make a scene
, never lash out at the ones I loved, 
never hurt a soul. Through hard work, relentless wo
rk, I would achieve something 
dazzling--in the classroom, on the basketball court
, in the science lab, in the pages of 
books--and my achievement would distract the world'
s eyes from his humiliation. I would 
become a worthy sacrifice, and the smoke of my burn
ing would please God. 
It is far easier to recognize these twists in my ch
aracter than to undo them. Work has 
become an addiction for me, as drink was an addicti
on for my father. Knowing this, my 
daughter gave me a placard for the wall: Workaholic
. The labor is endless and futile, for I 
can no more redeem myself through work than I could
 redeem my father. I still panic in 
the face of other people's anger, because his drunk
en temper was so terrible. I shrink from 
causing sadness or disappointment even to strangers
, as though I were still concealing the 
family shame. I still notice every twitch of emotio
n in those faces around me, having 
learned as a child to read the weather in faces, an
d I blame myself for their least pang of 
unhappiness or anger. In certain moods I blame myse
lf for everything. Guilt burns like 
acid in my veins. 
I am moved to write these pages now because my own 
son, at the age of ten, is taking on 
himself the griefs of the world, and in particular 
the griefs of his father. He tells me that 
when I am gripped by sadness, he feels responsible;
 he feels there must be something he 
can do to spring me from depression, to fix my life
. And that crushing sense of 
responsibility is exactly what I felt at the age of
 ten in the face of my father's drinking. 
My son wonders if I, too, am possessed. I write, th
erefore, to drag into the light what eats 
at me--the fear, the guilt, the shame--so that my o
wn children may he spared.  
I still shy away from nightclubs, from bars, from p
arties where the solvent is alcohol. My 
friends puzzle over this, but it is no more peculia
r than for a man to shy away from the 
lions' den after seeing his father torn apart. I to
ok my own first drink at the age of twenty-
one, half a glass of burgundy. I knew the odds of m
y becoming an alcoholic were four 
times higher than for the children of nonalcoholic 
fathers. So I sipped warily. 
I still do--once a week, perhaps, a glass of wine, 
a can of beer, nothing stronger, nothing 
more. I listen for the turning of a key in my brain
. 
"""

text = re.sub(r'\s+', '+', text)
text = re.sub(r'[^\x00-\x7F]+','', text)
n = 2000 - (len(url_start) + len(url_end))
#text.index()
l = [text[i:i+n] for i in range(0, len(text), n)]

i1 = 0
for i in l:
    temp = url_start + i + url_end
    print (temp)
    print("")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(temp, "audio/file" + str(i1) + ".mp3")
    i1 = i1 + 1

print(len(l))


