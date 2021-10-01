# :jigsaw: TSSuBERT :jigsaw:

This GitHub repository contains the Corpus and Model contributions of the paper introducing the TSSuBERT model (under submission).

## :world_map: Parts of this repository

* [Model](./Model): Contains the architecture of the model using TensorFlow as well as the transformers library and the trained weights we used in the paper.
* [TES 2012-2016](./TES%202012-2016): Contains the Gold Standard, the generated summaries - including Oracles -, and the qualitative assessment.
	* [Summaries](./TES%202012-2016/Summaries): Contains the Gold Standard and two generated extractive Oracle for the corpus as well as COWTS, SEMCOWTS, SCC, TSSuBERT and TSSubERT-F generated summaries.
	* [Gold Standard](./TES%202012-2016/Gold%20Standard): Contains the Gold Standard generated using the [Wikipedia Current Event portal](https://en.wikipedia.org/wiki/Portal:Current_events)
	* [Qualitative assessment](./TES%202012-2016/Qualitative%20assessment): Contains the questions and their associated answers we created for the manual annotations + additional informations retrieved during assessment.

## :floppy_disk: Overview of the TES 2012-2016 dataset

We used the tweets from the list provided by [1], you can find the set of ids [here](https://figshare.com/articles/Twitter_event_datasets_2012-2016_/5100460 "Set of ids for the corpus").
The corpus contains around 150 million of ids, at the time we wrote this lines we were able to retrieve around 82 million of tweets.

For more annotations including tweets ids, please contact us. We can't release this amount of tweets ids on this Git due to the distibution restrictions imposed by Twitter.

### Some statistics about the entire collection

| Number of events | Number of days | Mean number of tweets per event | Mean Gold Standard length |
| :--------------- | :------------- | :------------------------------ | :------------------------ |
| 28 | 545 | 2,939,842 | 265 |

Some statistics about each event [here](./stats_corpus.md).

[1] Zubiaga, A. (2018). A longitudinal assessment of the persistence of twitter datasets. J. Assoc. Inf. Sci. Technol., 69(8):974–984.

## :peacock: Examples

### Example 1

#### Event: Sismo Ecuador 2016

##### Description: [Wikipedia](https://en.wikipedia.org/wiki/2016_Ecuador_earthquake)

The tweets were retrieved by [1] from the April 17, 2016 to April 28, 2016 with the following keywords: '#sismoecuador', '#terremotoecuador', 'terremoto', 'ecuador'

##### Gold Standard:

```
2016-04-17,"The death toll from Saturday night's earthquake in Ecuador rises to 262 with more than 2,500 people injured."
2016-04-18,"Aid starts to flow in after an earthquake kills over 270 people in Ecuador."
2016-04-19,"The death toll from Saturday's earthquake has risen to at least 480 with 1,700 missing. Another 2,500 have been injured. President Rafael Correa states it is the worst disaster in Ecuador in seven decades, and the reconstruction will have a 'huge economic impact' on the country."
2016-04-20,"A magnitude-6.1 aftershock has struck off the coast of Ecuador at 3:33 a.m. local time, the US Geological Survey says, in the same area as the massive earthquake on Saturday. People in Ecuador start burying their dead as the death toll from the earthquake passes 500. President Rafael Correa announces a sales tax increase, and a one-time levy on millionaires as the country deals with the enormous damage from this disaster. The death toll rises to 570 with 163 people listed as missing. Those made homeless climbs to over 23,500."
2016-04-23,"The death toll from the earthquake passes 650 with over 50 people missing. It is now the deadliest earthquake in South America this century."
2016-04-25,"The United Nations World Food Programme announces it is stepping up assistance to Ecuador’s most vulnerable areas following an earthquake that killed over 650 people."
```

##### Oracle ROUGE-2:

```
2016-04-17: " #Ecuador #Earthquake Sat M7.8 Update
Death toll has risen to 262
More than 2,500 people injured
+135 #Aftershocks https://t.co/gU8i9BUaEM Earthquake in Ecuador:
#newsalert https://t.co/EaVifjbfOz"
2016-04-18: A devastating M7.8 #EcuadorEarthquake on Sat. killed over 270 people https://t.co/uiCcDy6j5L https://t.co/rC5MxM53OO Ecuador Earthquake Kills at Least 41 #EarthquakeInEcuador... https://t.co/liljCtaFXy #EarthquakeInEcuador #EcuadorEarthquake
2016-04-19: " RT @CBCAlerts: more @cbcnews Death toll in #EcuadorEarthquake jumps to 233, President Rafael Correa confirms: https://t.co/lSP1042MSy #EcuadorEarthquake: 480 confirmed dead, but 1,700 more missing @CarlosVerareal another organization accepting donations to help https://t.co/606oUhecAo #EcuadorEarthquake: Death toll rises to 480, 1,700 still missing
https://t.co/u8JzZBFyCY Almost 500 dead and 2500 injured but no one is talking about it #EcuadorEarthquake"
2016-04-20: " RT @mashable: How you can help the survivors of the massive earthquake in Ecuador https://t.co/Hi9x1IA7eC #EcuadorEarthquake https://t.co/A… Magnitude-6.1 aftershock hits #Ecuador following deadly #Earthquake #EcuadorEarthquake https://t.co/TZ46DcgSn2 https://t.co/LY5wIqhdyH Ecuador Suffers Two More Earthquakes After Saturday's Deadly One 😔 #EcuadorEarthquake https://t.co/d28AF1w95w Sentimos en Quito / @IGecuador #SISMO 2016/04/20-03:35:08 Magnitud:6.3 Near Coast of Ecuador https://t.co/gd38XjX2ij https://t.co/N13AZnkbEU Death toll of #EcuadorEarthquake passes 500 dead as President signals shrinking economy https://t.co/ATRWIouGEE Thoughts are with the people of Ecuador #EcuadorEarthquake Ecuadorean President Rafael Correa to speak shortly regarding #EcuadorEarthquake ""In the next hours, according to the Constitution, sales tax will increase for one year (to cover recovery costs)"" #EcuadorEarthquake RT @democracynow: #EcuadorEarthquake Death Toll Rises to 413 https://t.co/sANIj17i3c https://t.co/mraHFQpZCI"
2016-04-23: " Death toll from #EcuadorEarthquake tops 650

https://t.co/ZELviLCWeL https://t.co/MsiHGbZ4rR Foreign ministers of South America at #UNASUR meeting will analyze the possibility to visit quake affected areas #EcuadorEarthquake"
2016-04-25: " Photo: Center of Portoviejo, Ecuador, empty as clean up work continues following earthquake https://t.co/4Y61O1IORM https://t.co/6Shc7PJi9J Glad one of the major networks is covering this crisis.. Over 650 people killed and no significant media coverage https://t.co/7o5p9w20xf"
```

##### TSSuBERT-F:

```
2016-04-17: RT @thecableng: #Ecuador declares state of emergency after earthquake killed 233 https://t.co/Tqdhgc90PK via @thecableng #ecuadorearthquake 
2016-04-18: Ecuador earthquake death toll rises to 272  #Earthquake #Ecuador #Ecuadorearthquake #Ecuadorsince1979 #Ecuado https://t.co/QeldVmTJ6E 
2016-04-19: "Portoviejo rescue op continues as #EcuadorEarthquake death toll hits 413 https://t.co/vNcCUD5WAA https://t.co/S83OX8IvEi RT @LaraMuchacha: 🙋Follow
  ┊　　★
  ☆
@SuhilaBnLachhab 
https://t.co/HONTAdKCft    
#SouhilaBenLachhab
#EcuadorEarthquake #RAW https://t.co/… Fatal https://t.co/8CVmpvH7P5 #Ecuador #earthquake death toll passes 400 with many still trapped https://t.co/lKbgpBAqvj via @guardian #Ecuadorearthquake RT @WorldVisionUSA: Nat'l state of emergency after 7.8 #EcuadorEarthquake. Our relief response is underway—Help: https://t.co/OllKDLVc2j ht… "
2016-04-20: "@cnnbrk Death toll from Saturday's magnitude-7.8 #EcuadorEarthquake  stands at 525. https://t.co/PmzQriZnfJ Ecuador hit by 6.1-magnitude aftershock  #earthquake #EcuadorEarthquake #Aftershock https://t.co/HLBLWIWJit Another earthquake hits #Ecuador #EcuadorEarthquake https://t.co/IXCWbPAcj9 Responding to the #EcuadorEarthquake? Some useful lessons in our Nepal earthquake paper! https://t.co/eCFD3fFhve https://t.co/tahTkfpOGV RT @CRSRiceBowl: We continue to #pray for all those impacted by the #EcuadorEarthquake. #Ecuador https://t.co/n0mMx4FYVd @POTUS @MashiRafael @GuillaumeLong @HillaryClinton @HFA *President Obama,TPS for Ecuador *Please #EcuadorEarthquake https://t.co/ALxwAh6N4F RT @GlobalMiraism: It's time for action! https://t.co/sIrbRqDuou RT @Oxfam: #EcuadorEarthquake
413 dead
2,658 injured
805 buildings destroyed
6 regions in state of emergency
https://t.co/ZUXGn6zILh
#Ecuad… "
2016-04-21: "BREAKING NEWS:
Magnitude 6.2 earthquake strikes near coast of Ecuador #EcuadorEarthquake Shot de pasinerval!! :( #TerremotoEcuador #basta !!!! "
2016-04-22:
2016-04-23:
2016-04-24: "This is the future United States of America under Obama and Hillary  https://t.co/r7w0V3qMbZ Thank you to the people of the United States.   https://t.co/4kl82eB89b I was in this town Friday,got hit again Sat w/another earthquake- #EcuadorEarthquake #Ecuador https://t.co/LHvnN8twZH "
2016-04-25:
2016-04-26:
2016-04-27:
2016-04-28:
```

##### TSSuBERT:

```
2016-04-17,"RT @thecableng: #Ecuador declares state of emergency after earthquake killed 233 https://t.co/Tqdhgc90PK via @thecableng #ecuadorearthquake #PHOTOS - DEATH TOLL IN #ECUADOR EARTHQUAKE RISES TO 235
https://t.co/x4PxJHGPz5 #EcuadorEarthquake  #News #WorldNews RT @NatashaFatah: Images of the destruction caused by #EcuadorEarthquake. State of emergency declared. #Ecuador  https://t.co/v7NzE2AX0C #SismoEcuador

Follow 👇🏼

➡️ @ali_alfaisall 
➡️ https://t.co/EifnRmc2WH
➡️ https://t.co/S9TK1RcdhV https://t.co/ZxFyYB894s #Böhmermann 
#M05KOE 
#SismoEcuador 
#17Abr 
#BVBHSV 

Follow 👇#IhabAmir 
➡@Ihab_Amir.  🎶🎸🎤 
😎 https://t.co/ya2OjcPWQ1 You speak for me too, Michael. https://t.co/MPFLsuXP6B #SismoEcuador| We have declared in the port of #Manta emergency, we will divert ships to other ports, @waltersolisv. https://t.co/33uu4MuZOD @PrinceRoyce united #Ecuador @cruzrojaecuador #helpMiEcua🇪🇨 #EcuadorEarthquake rtw https://t.co/JlOBXAPS8H Nat'l state of emergency after 7.8 #EcuadorEarthquake. Our relief response is underway—Help: https://t.co/OllKDLVc2j https://t.co/ktIwLGWuh4 We are signing off for the night (GMT), please follow @planamericas for latest #EcuadorEarthquake updates. Deadly earthquake hits #Ecuador #EcuadorEarthquake #Ecuador... https://t.co/N2ho1dWJxb Hundreds dead after earthquake last night in #EcuadorEarthquake  https://t.co/YAaTbL9WQ7 https://t.co/QWMrvpb441 UPDATE: #EcuadorEarthquake death toll reaches 262: https://t.co/HGGA0ksQTR Search for victims, survivors continues. https://t.co/KrDETbsuOK Here's the latest on the #EcuadorEarthquake. Follow us for the latest updates on this #WNNBreaking #BreakingNews https://t.co/iL4FCL9KJZ RT @JoshuaHoyos: State Dept: There have been no reports of deceased U.S. citizens at this time #SismoEcuador #EcuadorEarthquake YOU CAN HELP US!! #terremotoecuador https://t.co/1i9YHkivll My moms town ☹️ https://t.co/WK1myGxs4N "
2016-04-18,"#Mother #nature showing #Power  #earthrightnow #Ecuador  #EcuadorEarthquake #JapanEarthquake #JapanQuake #earthquake #heartfelt #Condolence RT @souhilafans2: 😍👇Follow👇👸
https://t.co/puJIjGsV5k 👈
#souhilabenlachhab #BostonMarathon #houwx #EcuadorEarthquake #RCBvDD #1d #jlo https:… #BreakingNews https://t.co/nGlw3dmoxm State Department confirms death of 1 US citizen in Ecuador earthquake; work… https://t.co/5n4hUsewLy RT @LIFT_Logistics: Continuously updated SITREPS on Ecuador Earthquake. Thanks To @HumanityRoad! - https://t.co/yPu4MtLq2D #HADR #EcuadorEa… Ecuador earthquake: death toll soars to 350 with fears mounting it will &lt;b&gt;...&lt;/b&gt; NA #ecuadorearthquake #trending https://t.co/C7wHwSKBFW "
2016-04-19,"RT @LaraMuchacha: 🙋Follow
  ┊　　★
  ☆
@SuhilaBnLachhab 
https://t.co/HONTAdKCft    
#SouhilaBenLachhab
#EcuadorEarthquake #RAW https://t.co/… Fatal https://t.co/8CVmpvH7P5 RT @telesurenglish: 5.9 magnitude aftershock hits coastal town of Muisne. https://t.co/iwIkqPUu8E #EcuadorEarthquake https://t.co/sZ0I6CG17h #EcuadorEarthquake
413 dead
2,658 injured
805 buildings destroyed
6 regions in state of emergency
https://t.co/ZUXGn6zILh
#Ecuador "
2016-04-20,"Responding to the #EcuadorEarthquake? Some useful lessons in our Nepal earthquake paper! https://t.co/eCFD3fFhve https://t.co/tahTkfpOGV @POTUS @MashiRafael @GuillaumeLong @HillaryClinton @HFA *President Obama,TPS for Ecuador *Please #EcuadorEarthquake https://t.co/ALxwAh6N4F Magnitude 6.1 earthquake strikes off Ecuador coast: USGS https://t.co/GWgGEcumBI #ecuadorearthquake #മാതൃഭൂമി https://t.co/y3YfhdkMjN "
2016-04-21,"#TronoSofia13 
#TerremotoEcuador 
#Temuco 
 Plz Follow 🎤🎤🎤
🎶🎶🎶🎶🎶🎶
👇👇
📷📷https://t.co/QxQDc1xszU 
👇👇
🐥🐥 @RaphaelJabbour1 
#RaphaelJabbour "
2016-04-22,
2016-04-23,
2016-04-24,
2016-04-25,
2016-04-26,
2016-04-27,
2016-04-28,
```

##### Qualitative assessment

###### Questions

```
2016-04-17:
Question 1: How many dead?
Question 2: How many injured?

2016-04-18:
Question 1: How many dead?

2016-04-19:
Question 1: How many dead?
Question 2: How many injured?
Question 3: How many people are missing?
Question 4: What did President Rafael Correa state about the reconstruction of the country after this disaster?

2016-04-20:
Question 1: How many dead?
Question 3: How many people are missing?
Question 5: What happened in the same area as the massive earthquake at 3:33 a.m. local time in Ecuador?
Question 6: What are the economic measures announced by the president Rafael Correa to deal with the damages caused by the earthquake?

2016-04-23:
Question 1: How many dead?
Question 3: How many people are missing?

2016-04-25:
Question 7: What has the United Nations World Food Programme announced to do for the Ecuador’s most vulnerable areas?
```

###### Answers

```
2016-04-17: "<Q1><Q2>The death toll from Saturday night's earthquake in Ecuador rises to 262</Q1> with more than 2,500 people injured</Q2>."
2016-04-18: "Aid starts to flow in after <Q1>an earthquake kills over 270 people in Ecuador</Q1>."
2016-04-19: "<Q1><Q3>The death toll from Saturday's earthquake has risen to at least 480</Q1> with 1,700 missing</Q3>. <Q2>Another 2,500 have been injured</Q2>. <Q4>President Rafael Correa states it is the worst disaster in Ecuador in seven decades, and the reconstruction will have a 'huge economic impact' on the country</Q4>."
2016-04-20: "<Q5>A magnitude-6.1 aftershock has struck off the coast of Ecuador at 3:33 a.m. local time, the US Geological Survey says, in the same area as the massive earthquake on Saturday</Q5>. <Q1>People in Ecuador start burying their dead as the death toll from the earthquake passes 500</Q1>. <Q6>President Rafael Correa announces a sales tax increase, and a one-time levy on millionaires as the country deals with the enormous damage from this disaster</Q6>. <Q1>The death toll rises to 570</Q1> <Q3>with 163 people listed as missing</Q3>. Those made homeless climbs to over 23,500."
2016-04-23: "<Q1>The death toll from the earthquake passes 650</Q1> <Q3>with over 50 people missing</Q3>. It is now the deadliest earthquake in South America this century."
2016-04-25: "<Q7>The United Nations World Food Programme announces it is stepping up assistance to Ecuador’s most vulnerable areas following an earthquake that killed over 650 people</Q7>."
```

### Example 2

#### Event: Superbowl 2012

##### Description: [Wikipedia](https://en.wikipedia.org/wiki/Super_Bowl_XLVI)

The tweets were retrieved by [1] from the February 3, 2012 to February 7, 2012 with the following keywords: '#superbowl'

##### Gold Standard:

```
2012-02-05: "In American football, Super Bowl XLVI is played in Indianapolis with the New York Giants defeating the New England Patriots 21-17. Quarterback Eli Manning of the Giants wins his second Super Bowl Most Valuable Player Award."
```

##### Oracle ROUGE-2:

```
2012-02-05: New York Giants defeat New England Patriots 21-17 to win Super Bowl XLVI. #SuperBowl Who playing in the #Superbowl ? How Indianapolis won at the #SuperBowl: http://t.co/kjlrPH2U New!! http://t.co/VnNeQ0hP #superbowl #patriots #newengland #health #GIANTS WIN! Eli Manning does it again as Giants win Super Bowl XLVI: http://t.co/j0JhOO9v #nfl #sb46 Quarterback Eli Manning wins his second #SuperBowl MVP http://t.co/ap0KkWTH
```

##### TSSuBERT-F:

```
2012-02-03,
2012-02-04,
2012-02-05,"Law firm #sb46 #superbowl sunday! One game one winner! Go #giants. Prime. #superbowl #thisscreenismassive http://t.co/HcZRyGg0 Opinions on companies leaking ads before #SuperBowl? #SuperBowl Sunday 
Gooooooooooooooo @Patriots No foreign policy during the #SuperBowl, @NBC "
2012-02-06,
2012-02-07,
```

##### TSSuBERT:

```
2012-02-03: Go  #NyGiants #SuperBowl Sunday \=D/ It's going to be a great game Sunday #superbowl Me and @MKMetera all set for #SuperBowl #FakeBaller http://t.co/GCOSuNIx #JunkFood is a billion dollar industry in #America during #SuperBowl weekend... sooo #Pumped for #SuperBowl Sunday!! GO #Patriots @BrickWarehouse family room #bff #SuperBowl @BrandIndex is the source for data on brands that move the needle during the #SuperBowl  @AdAge releases pre-Super Bow…http://t.co/tkmYIwl1 
2012-02-04: UK entrepreneurs praised by Prime Minister David Cameron http://t.co/VH8nvX6N #SuperBowl What are people doing for the #Superbowl ? RT @WisdomsGrave: Judge who Ruled against Raw Milk in #Wisconsin quits to work for #Monsanto law firm http://t.co/cZbr2bEj #SuperBowl #h ... @HoosierWX is #SuperBowl Weather from #Indiana 's Weather Source #INwx #Indy #NFL This year's #SuperBowl is going to me boring! Americans.. #superBOWL http://t.co/yvsJhzod RT @UNITEHEREUnion Help us support moms during the #SuperBowl #1u #labor #fem2 http://t.co/uE7jTYKU 
2012-02-05: "Prime. #superbowl #thisscreenismassive http://t.co/HcZRyGg0 Opinions on companies leaking ads before #SuperBowl? #SuperBowl The law firm Green-Ellis.... First DOWN!!! @adage So #greenellis is known as the law firm, what is #Edelman known as, The PR firm? #SuperBowl No foreign policy during the #SuperBowl, @NBC From Bologna, Italy: go #Pats! @Patriots #superbowl #SuperBowl with my family! (: #superbowl #shrine  @ United States of America http://t.co/5kqJ2QhC #SNL peeps on #SB46 #Superbowl from France http://t.co/E69CVVp8 RT @eye_ris_xo: You people: #SuperBowl ; Me: #SuperStudying. 😒👊📝 @dkny watching from El Salvador !! #SuperBowl Calling David Tyree...Calling David Tyree... #SuperBowl Oh! A financial industry commercial! #NFL #superbowl Will #LadyGaga outtrend #superbowl on #twiiter us trends United States? Will now use #TaxAct for my taxes because of their #SuperBowl #commercial #giants catch the #SuperBowl If POTUS is interviewed live on #SuperBowl Sunday what's the right sporting event for our Prime Minister to be interviews? #canadianprobz #Superbowl sunday🏈🏈 going for the giant........ #Giants!!!! &lt;HIDES&gt; #SB46 "
2012-02-06: Official #SuperBowl #Hangoverday Hands down #winner!! http://t.co/oNCgy2CU #superbowl @RynFreeman @jimmyferlito @a_herrmann2011 @drewchappy #hITIT @JLysiak #Doing it 
2012-02-07:
```

##### Qualitative assessment

###### Questions

```
2012-02-05:
Question 1: Where did the Super Bowl 2012 take place?
Question 2: What were the two teams in this final?
Question 3: Which team won the title? What was the score?
Question 4: Who was named as MVP (Most Valuable Player) of this Super Bowl?
```

###### Answers

```
2012-02-05: "In American football, <Q1>Super Bowl XLVI is played in Indianapolis</Q1> with the <Q3><Q2>New York Giants defeating the New England Patriots</Q2> 21-17</Q3>. <Q4>Quarterback Eli Manning of the Giants wins his second Super Bowl Most Valuable Player Award</Q4>."
```

### Example 3

#### Event: Indyref 2014

##### Description: [Wikipedia](https://en.wikipedia.org/wiki/2014_Scottish_independence_referendum)

The tweets were retrieved by [1] from the September 17, 2014 to September 20, 2014 with the following keywords: '#indyref'

##### Gold Standard:

```
2014-09-18: "Voters in Scotland go to the polls to vote on the referendum on independence."
2014-09-19: "Scotland votes 'No' to Scottish independence."
2014-09-19: "Voter turnout in the referendum hits 84.5%, a record high for any election held in the United Kingdom since the introduction of universal suffrage in 1918."
2014-09-19: "Prime Minister David Cameron announces plans to devolve further powers to Scotland, as well as the UK's other constituent countries."
2014-09-19: "Alex Salmond announces his resignation as First Minister of Scotland and leader of the Scottish National Party following the referendum."
```

##### Oracle ROUGE-2:

```
2014-09-18: Voters in Scotland go to polls for referendum on independence from UK. #indyref #GoodMorning7 @WKBW #7EyewitnessNews
2014-09-19: " Scotland votes No to Scottish independence http://t.co/aCnGOFsxGs #indyref Turnout in the #indyref a record high for any election held in the UK since the introduction of universal suffrage 
http://t.co/MzLwzYn3NZ #Scotland sees record voter turnout for referendum - #LIVE #UPDATES http://t.co/vNPY4eGlFJ #IndyRef http://t.co/W2UsmzEgHP #ScotlandDecides #GBPUSD hits 1.65. #NO #indyref United kingdom #indyref http://t.co/81p1a0etjK #BREAKING UK Prime Minister David Cameron: more powers to Scotland, will deliver on #devolution, but balanced settlement needed #indyref Find out more about our plans to devolve power here: http://t.co/P5FBR3kSnv #localgov #indyref http://t.co/jIS8IxCmyU NEW: Scottish National Party leader Alex Salmond resigns as First Minister after Scotland votes No. #ScotlandDecides #indyref"
```

##### TSSuBERT-F:

```
2014-09-17,
2014-09-18,
2014-09-19,"David Cameron has called it. #indyref
https://t.co/uYrgjsAY5g Prime Minister David Cameron: ""We have delivered on devolution and we will do so again"" #ScotlandDecides #indyref http://t.co/pC6E0QhfdS #Scotland #Referendum: British Prime Minister #Cameron 'Delighted' With 'No' Vote #indyref  #ScotlandIndependence http://t.co/0cMnqdNija If Twitter had decided the #indyref (source: http://t.co/YJn2jWE0pQ / @Brandwatch data) http://t.co/mQfe5hW3bo RT @chrisjacobsHC: So if David Cameron had to resign if #indyref won, then @AlexSalmond will resign later today, right...? #DontBankOnIt #S… RT @svaxelaire: #indyref around the World with #twitter #infographic http://t.co/fSA3BG7TMm Alex Salmond says he will be speaking to British Pirime Minister David Cameron shortly #IndyRef #Scotland "
2014-09-20,
```

##### TSSuBERT:

```
2014-09-17: "@investor_bod @DaveOCarroll How? We are a tax haven and the money laundering capital of the world. #indyref RT @Kilsally: Northern Ireland DUP Finance Minister days David Cameron should have devolved corporation tax to Northern Ireland pre Scottis… #indyref vote YES...you too can have a turd as your Prime Minister. RT @ThereWasACoo: David Cameron ignored the referendum and – worse – the Scottish people | The Independent http://t.co/qbN8FD8Lzl #IndyRef … “@MrsJaneRace: @AlexSalmond wants to be Prime Minister of Scotland at the expense of the United Kingdom. #bettertogether” #indyref RT @YouGov: The British public are unimpressed by David Cameron's contribution to the #IndyRef debate - http://t.co/wXSUfZQnRJ http://t.co/… Balrog for Scotland's first post #indyref finance minister http://t.co/SRmkrQySR1 ""David Cameron To Scottish People: ‘I’ll Kill Myself If You Leave’"" #indyref http://t.co/wzYR1bMAfC Confused by calls for @David_Cameron to resign if Scotland votes ""No"" in #indyref. Why?!?!  Do the Scottish people not deserve democracy? @patrickharvie for Prime Minister, British or Scottish, I'll take either #indyref UNIONnnnnnnnnnnnnnnnnnnnn! #indyref #bettertogether #letsstaytogether #EdMiliband #VoteNo http://t.co/PKeth6lTvi @ScotsBok he was for the Union  http://t.co/mOPEAi46QU  @UK_Together #indyref Poverty, elitism, an unelected government, poll tax, those are the hallmarks of the 'United Kingdom' #indyref RT @RossHughes3: Hello @MichelleMone David Cameron doesn't have a vote but he tells us what to do. Have you told him that? #channel4 #indyr… RT @Freedom4Scots: Remember, voters; hold your nerve at the polling stations. Go for that #yes #voteyes #indyref #Scotland2014 #HopeNotFear Cameron says yes we can to #indyref http://t.co/RYMtyXe5ZT Look #indyref forget Prime ministers Presidents or Polls it's YOUR decisIon YOUR future Be cool! Independence or 🇬🇧? #Scotland #Indyref @PeterKGeoghegan @FrannLeach @newsundayherald This is only paper we trust in our home #indyref #newsworthy "
2014-09-18: "RT @darrenmillar: An open letter to #TeamScotland #IndyRef #Scotland #BBCindyref http://t.co/FAyZV3q0aO http://t.co/cX7iJYCWZt RT @PaulEnglishhack: Thousands of people have gathered in #georgesquare #voteyes #voteno #indyref #glasgow http://t.co/u6N4AdY3YS RT @1917paul: Millions take to streets calling for #Catalonia’s independence: http://t.co/6SPjRNwTVF #Spain #cwi #IndyRef RT @MartynMcL: On 15 Oct 2012, the Edinburgh Agreement was signed by First Minister Alex Salmond &amp; Prime Minister David Cameron #indyref All set #indyref http://t.co/n7qTRRjUYd Joey Jones outside number 10 incase david cameron resigns in the morning! #indyref RT @BioMickWatson: Leaked document paints bleak picture for independent Scotland http://t.co/PraTIjB8qA #indyref #nothanks US foreign policy perspective http://t.co/YNiQTAyFkb #ScotlandDecides #indyref This just in, Apple considering moving tax avoidance HQ from Ireland to Scotland if you just VOTE YES #indyref And we’re off.. polls open for Independence (or not) #indyref #BetterTogether ...and be a nation again. #voteyes #indyref #indyref Data map http://t.co/Mf4sDJ3DTv @charltonbrooker #Indyref revelation https://t.co/i72yM4v3Tq . @STVNews using @Pixel_Power for @youdecide2014 #ScottishReferendum #ScotlandDecides #indyref #ScotDecides http://t.co/8njdTjE4Ei @rachelburden @bbc5live @naughtiej @rosschawkins @McEwen_Nicola #matchsticks &amp; #expresso to hand #indyref 'Millions of red-face people calling each other bastards'.  Sounds about right. #indyref Hearing #snp being investigated by the electoral commission #indyref The more I hear that the world's rich and powerful wants the UK to remain united, the more I want it broken up. #indyref #indyref #scotland decides #voteyes#aye #glasgow #georgesquare #love #catalonia http://t.co/lwNoHthpWj So when will be the announcement of #ScotlandIndependence ?? #indyref "
2014-09-19: "We Are Family #indyref http://t.co/cIxYjGsBQR 🇬🇧We are The United Kingdom🇬🇧 #indyref #indyref. 'you love me,you really really love me'-David Cameron British Prime Minister will give ""clear direction"" on what is to happen in future.No doubt he's relieved not to be resigning #indyref STUC on First Minister’s resignation http://t.co/dsukCBq1Ly #indyref #stuc @C_RMcLaren Sources suggest both #indyref Going to the final run #indyref http://t.co/WKFYnXB0Q5 @number10cat can you help us find the #missingmotion? #indyref http://t.co/Ulh20gAC3p 2. I wrote this about how leading law firms are reacting to the #indyref outcome http://t.co/5ng43ivmiQ #AlexSalmond to step down #indyref Salmond, Sturgeon and others have to resign, election has to be called, independence buried for a generation #indyref RT @TheCityUK: On #indyref - see our #KeyFacts #infographic on the financial&amp;related professional services industry in #Scotland  http://t.… "
2014-09-20:
```

##### Qualitative assessment

###### Questions

```
2014-09-18:
Question 1: In which country does the referendum take place?

2014-09-19:
Question 2: What is the result of the referendum?
Question 3: Was the turnout for this referendum high? What was the participation rate?
Question 4: What did the Prime Minister David Cameron announce?
Question 5: What did Scottish First Minister Alex Salmond do after the referendum results?
```

###### Answers

```
2014-09-18: "<Q1>Voters in Scotland</Q1> go to the polls to vote on the referendum on independence."
2014-09-19: "Scotland votes <Q2>'No' to Scottish independence</Q2>."
2014-09-19: "<Q3>Voter turnout in the referendum hits 84.5%, a record high for any election held in the United Kingdom since the introduction of universal suffrage in 1918</Q3>."
2014-09-19: "<Q4>Prime Minister David Cameron announces plans to devolve further powers to Scotland, as well as the UK's other constituent countries</Q4>."
2014-09-19: "<Q5>Alex Salmond announces his resignation as First Minister of Scotland and leader of the Scottish National Party following the referendum</Q5>."
```

## :handshake: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

