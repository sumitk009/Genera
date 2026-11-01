import random
from engine import F, X
R = random.Random(11)

# ---------------- HINDI ----------------
F("HIN","HSYN","""
|'सूर्य' का पर्यायवाची शब्द कौन-सा है?|दिनकर|=
|'चंद्रमा' का पर्यायवाची शब्द कौन-सा है?|शशि|=
|'पृथ्वी' का पर्यायवाची शब्द कौन-सा है?|धरा|=
|'आकाश' का पर्यायवाची शब्द कौन-सा है?|गगन|=
|'जल' का पर्यायवाची शब्द कौन-सा है?|नीर|=
|'पवन' का पर्यायवाची शब्द कौन-सा है?|समीर|=
|'कमल' का पर्यायवाची शब्द कौन-सा है?|पंकज|=
|'हाथी' का पर्यायवाची शब्द कौन-सा है?|गज|=
|'घोड़ा' का पर्यायवाची शब्द कौन-सा है?|तुरंग|=
|'अग्नि' का पर्यायवाची शब्द कौन-सा है?|पावक|=
|'सागर' का पर्यायवाची शब्द कौन-सा है?|जलधि|=
|'पर्वत' का पर्यायवाची शब्द कौन-सा है?|गिरि|=
""")
F("HIN","HANT","""
|'सुख' का विलोम शब्द कौन-सा है?|दुःख|=
|'अमृत' का विलोम शब्द कौन-सा है?|विष|=
|'उत्थान' का विलोम शब्द कौन-सा है?|पतन|=
|'आदि' का विलोम शब्द कौन-सा है?|अंत|=
|'स्वर्ग' का विलोम शब्द कौन-सा है?|नरक|=
|'प्रकाश' का विलोम शब्द कौन-सा है?|अंधकार|=
|'आशा' का विलोम शब्द कौन-सा है?|निराशा|=
|'सत्य' का विलोम शब्द कौन-सा है?|असत्य|=
|'दिन' का विलोम शब्द कौन-सा है?|रात|=
|'नया' का विलोम शब्द कौन-सा है?|पुराना|=
""")
F("HIN","HOW","""
|अनेक शब्दों के लिए एक शब्द: 'जो कभी न मरे'|अमर|=
|अनेक शब्दों के लिए एक शब्द: 'जिसका कोई शत्रु न हो'|अजातशत्रु|=
|अनेक शब्दों के लिए एक शब्द: 'जो ईश्वर में विश्वास रखता हो'|आस्तिक|=
|अनेक शब्दों के लिए एक शब्द: 'जो ईश्वर में विश्वास न रखता हो'|नास्तिक|=
|अनेक शब्दों के लिए एक शब्द: 'जो पढ़ा-लिखा न हो'|निरक्षर|=
|अनेक शब्दों के लिए एक शब्द: 'जो सब कुछ जानता हो'|सर्वज्ञ|=
|अनेक शब्दों के लिए एक शब्द: 'जो दूसरों पर उपकार करे'|परोपकारी|=
|अनेक शब्दों के लिए एक शब्द: 'जो आँखों के सामने हो'|प्रत्यक्ष|=
""")
F("HIN","HID","""
|मुहावरे का अर्थ: 'आँखों का तारा होना'|बहुत प्यारा होना|=
|मुहावरे का अर्थ: 'नौ दो ग्यारह होना'|भाग जाना|=
|मुहावरे का अर्थ: 'ऊँट के मुँह में जीरा'|बहुत कम मात्रा|=
|मुहावरे का अर्थ: 'दाँतों तले उँगली दबाना'|आश्चर्य करना|=
|मुहावरे का अर्थ: 'आसमान से बातें करना'|बहुत ऊँचा होना|=
|मुहावरे का अर्थ: 'अंगूर खट्टे होना'|न मिलने पर बहाना बनाना|=
""")
F("HIN",None,"""
|हिंदी दिवस प्रतिवर्ष कब मनाया जाता है?|14 सितंबर|=|10 जनवरी;15 अगस्त;26 जनवरी
|हिंदी वर्णमाला में कितने स्वर माने जाते हैं?|11|=|10;13;14
|हिंदी में कारकों की संख्या कितनी है?|8|=|6;7;9
|हिंदी भाषा की लिपि कौन-सी है?|देवनागरी|=|गुरमुखी;ब्राह्मी;रोमन
|'विद्यालय' शब्द में कौन-सी संधि है?|दीर्घ संधि? |=|x
""".replace("|'विद्यालय' शब्द में कौन-सी संधि है?|दीर्घ संधि? |=|x\n",""))
F("HIN",None,"""
|'पुस्तक' शब्द का लिंग क्या है?|स्त्रीलिंग|=|पुल्लिंग;उभयलिंग;नपुंसकलिंग
|'राम पुस्तक पढ़ता है' वाक्य में 'पुस्तक' कौन-सा कारक है?|कर्म कारक|=|कर्ता कारक;करण कारक;संप्रदान कारक
|'गंगा' शब्द कौन-सी संज्ञा है?|व्यक्तिवाचक संज्ञा|=|जातिवाचक संज्ञा;भाववाचक संज्ञा;द्रव्यवाचक संज्ञा
""")

# ---------------- ENGLISH ----------------
F("ENG","ESYN","""
What is the synonym of 'Big'?||Large|=
What is the synonym of 'Happy'?||Joyful|=
What is the synonym of 'Begin'?||Commence|=
What is the synonym of 'Brave'?||Courageous|=
What is the synonym of 'Quick'?||Rapid|=
What is the synonym of 'Smart'?||Intelligent|=
What is the synonym of 'Weak'?||Feeble|=
What is the synonym of 'Rich'?||Wealthy|=
What is the synonym of 'Angry'?||Furious|=
What is the synonym of 'Help'?||Assist|=
""")
F("ENG","EANT","""
What is the antonym of 'Ancient'?||Modern|=
What is the antonym of 'Generous'?||Selfish|=
What is the antonym of 'Victory'?||Defeat|=
What is the antonym of 'Expand'?||Contract|=
What is the antonym of 'Brave'?||Cowardly|=
What is the antonym of 'Honest'?||Dishonest|=
What is the antonym of 'Rapid'?||Slow|=
What is the antonym of 'Increase'?||Decrease|=
What is the antonym of 'Accept'?||Reject|=
What is the antonym of 'Arrive'?||Depart|=
""")
F("ENG","EOW","""
One word for 'a person who loves books':||Bibliophile|=
One word for 'the study of birds':||Ornithology|=
One word for 'government by the people':||Democracy|=
One word for 'life story written by oneself':||Autobiography|=
One word for 'one who cannot read or write':||Illiterate|=
One word for 'a place where birds are kept':||Aviary|=
One word for 'fear of heights':||Acrophobia|=
One word for 'a person who walks in sleep':||Somnambulist|=
""")
F("ENG",None,"""
Choose the correct word: He ___ to school every day.||goes|=|go;going;gone
Choose the correct word: She has been living here ___ 2015.||since|=|for;from;by
Choose the correct word: The sun ___ in the east.||rises|=|rise;rose;rising
Choose the correct word: I ___ a letter yesterday.||wrote|=|write;written;writing
Choose the correct word: He is senior ___ me.||to|=|than;from;of
What is the plural of 'child'?||children|=|childs;childes;childrens
What is the past tense of 'go'?||went|=|gone;goes;going
Choose the correctly spelt word.||Separate|=|Seperate;Seprate;Separete
Fill in the blank: He is an ___ man.||honest|=|dishonest;horrible;hungry
Choose the correct preposition: He is good ___ mathematics.||at|=|in;on;with
Choose the correct form: I have ___ my homework.||done|=|did;do;doing
Passive voice of 'He wrote a letter.'||A letter was written by him.|=|A letter is written by him.;A letter has written by him.;He was written by a letter.
Meaning of the idiom 'A piece of cake':||Very easy|=|Very tasty;Very small;Very costly
Meaning of the idiom 'Once in a blue moon':||Very rarely|=|Very often;Every night;Never
Choose the correct article: ___ umbrella is useful in rain.||An|=|A;The;No article
""")

# ---------------- BIHAR GK ----------------
F("BIH","BPL","""
Where is the famous Mahabodhi Temple located?|प्रसिद्ध महाबोधि मंदिर कहाँ स्थित है?|Bodh Gaya|बोधगया
Where was the first Buddhist Council held?|प्रथम बौद्ध संगीति कहाँ हुई थी?|Rajgir|राजगीर
Where was the third Buddhist Council held?|तृतीय बौद्ध संगीति कहाँ हुई थी?|Pataliputra|पाटलिपुत्र
Mahavira was born near which place in Bihar?|महावीर स्वामी का जन्म बिहार में किस स्थान के निकट हुआ था?|Vaishali|वैशाली
Where did Mahavira attain Nirvana?|महावीर स्वामी को निर्वाण कहाँ प्राप्त हुआ?|Pavapuri|पावापुरी
The tomb of Sher Shah Suri is located at:|शेरशाह सूरी का मकबरा कहाँ स्थित है?|Sasaram|सासाराम
Which city of Bihar is known as the 'Silk City'?|बिहार का कौन-सा शहर 'सिल्क सिटी' कहलाता है?|Bhagalpur|भागलपुर
The Barabar Caves are located in which district?|बराबर की गुफाएँ किस जिले में स्थित हैं?|Jehanabad|जहानाबाद
Valmiki National Park is in which district of Bihar?|वाल्मीकि राष्ट्रीय उद्यान बिहार के किस जिले में है?|West Champaran|पश्चिम चंपारण
Dr. Rajendra Prasad was born in which district?|डॉ. राजेंद्र प्रसाद का जन्म किस जिले में हुआ था?|Siwan|सीवान
Veer Kunwar Singh of the 1857 revolt belonged to:|1857 के विद्रोह के नायक वीर कुँवर सिंह किस स्थान के थे?|Jagdishpur (Bhojpur)|जगदीशपुर (भोजपुर)
Madhubani painting belongs to which region?|मधुबनी चित्रकला किस क्षेत्र से संबंधित है?|Mithila|मिथिला
Gandhiji's first Satyagraha in India was at:|भारत में गांधीजी का पहला सत्याग्रह कहाँ हुआ?|Champaran|चंपारण
Gandhi Setu connects Patna with:|गांधी सेतु पटना को किससे जोड़ता है?|Hajipur|हाजीपुर
The Kesaria Buddhist Stupa is in which district?|केसरिया बौद्ध स्तूप किस जिले में है?|East Champaran|पूर्वी चंपारण
The Pitrapaksha Mela for ancestors is held at:|पितृपक्ष मेला (पितरों के लिए) कहाँ लगता है?|Gaya|गया
""")
F("BIH","BPER","""
Who founded the ancient Nalanda Mahavihara?|प्राचीन नालंदा महाविहार की स्थापना किसने की?|Kumaragupta I|कुमारगुप्त प्रथम
Vikramshila University was founded by:|विक्रमशिला विश्वविद्यालय की स्थापना किसने की?|Dharmapala|धर्मपाल
Who was the first Chief Minister of Bihar?|बिहार के प्रथम मुख्यमंत्री कौन थे?|Shri Krishna Sinha|श्री कृष्ण सिंह
Who is known as 'Loknayak'?|'लोकनायक' के नाम से कौन जाने जाते हैं?|Jayaprakash Narayan|जयप्रकाश नारायण
The poet of 'Urvashi', Rashtrakavi from Bihar:|'उर्वशी' के रचयिता बिहार के राष्ट्रकवि:|Ramdhari Singh Dinkar|रामधारी सिंह 'दिनकर'
Bidesia folk theatre is associated with:|बिदेसिया लोकनाट्य किससे संबंधित है?|Bhikhari Thakur|भिखारी ठाकुर
Who is called 'Bihar Kesari'?|'बिहार केसरी' किसे कहा जाता है?|Shri Krishna Sinha|श्री कृष्ण सिंह
""")
F("BIH",None,"""
Which is the capital of Bihar?|बिहार की राजधानी कौन-सी है?|Patna|पटना|Gaya/गया;Muzaffarpur/मुज़फ़्फ़रपुर;Bhagalpur/भागलपुर
Guru Gobind Singh was born at:|गुरु गोबिंद सिंह का जन्म कहाँ हुआ था?|Patna Sahib|पटना साहिब|Anandpur Sahib/आनंदपुर साहिब;Amritsar/अमृतसर;Nanded/नांदेड़
Aryabhata worked at:|आर्यभट ने कहाँ कार्य किया?|Kusumapura (Patna)|कुसुमपुर (पटना)|Ujjain/उज्जैन;Kanchi/कांची;Taxila/तक्षशिला
Muzaffarpur is famous for which fruit?|मुज़फ़्फ़रपुर किस फल के लिए प्रसिद्ध है?|Litchi|लीची|Mango/आम;Banana/केला;Guava/अमरूद
Which river is called the 'Sorrow of Bihar'?|किस नदी को 'बिहार का शोक' कहा जाता है?|Kosi|कोसी|Gandak/गंडक;Sone/सोन;Bagmati/बागमती
Bihar was separated from the Bengal Presidency in:|बिहार को बंगाल प्रेसिडेंसी से कब अलग किया गया?|1912|=|1905;1911;1936
Jharkhand was separated from Bihar in the year:|झारखंड बिहार से किस वर्ष अलग हुआ?|2000|=|1998;2001;2005
Bihar Diwas is celebrated on:|बिहार दिवस कब मनाया जाता है?|22 March|22 मार्च|15 November/15 नवंबर;26 January/26 जनवरी;12 January/12 जनवरी
Total seats in the Bihar Legislative Assembly:|बिहार विधानसभा की कुल सीटें:|243|=|234;245;250
Number of Lok Sabha seats from Bihar:|बिहार से लोकसभा की कुल सीटें:|40|=|39;42;48
Number of districts in Bihar:|बिहार में जिलों की संख्या:|38|=|36;37;40
Number of administrative divisions in Bihar:|बिहार में प्रमंडलों की संख्या:|9|=|7;8;10
State bird of Bihar:|बिहार का राजकीय पक्षी:|House Sparrow|गौरैया|Peacock/मोर;Koel/कोयल;Parrot/तोता
State animal of Bihar:|बिहार का राजकीय पशु:|Gaur (Indian bison)|गौर (भारतीय बाइसन)|Tiger/बाघ;Elephant/हाथी;Deer/हिरण
State tree of Bihar:|बिहार का राजकीय वृक्ष:|Peepal|पीपल|Banyan/बरगद;Neem/नीम;Mango/आम
Chhath Puja is dedicated to which deity?|छठ पूजा किस देवता को समर्पित है?|Sun God (Surya)|सूर्य देव|Lord Shiva/भगवान शिव;Lord Vishnu/भगवान विष्णु;Goddess Durga/देवी दुर्गा
The oldest university of Bihar (est. 1917):|बिहार का सबसे पुराना विश्वविद्यालय (1917):|Patna University|पटना विश्वविद्यालय|Magadh University/मगध विश्वविद्यालय;Bhagalpur University/भागलपुर विश्वविद्यालय;Nalanda University/नालंदा विश्वविद्यालय
Sonepur cattle fair is held at the confluence of:|सोनपुर पशु मेला किस संगम पर लगता है?|Ganga and Gandak|गंगा और गंडक|Ganga and Sone/गंगा और सोन;Ganga and Kosi/गंगा और कोसी;Ganga and Yamuna/गंगा और यमुना
""")

# ---------------- SCIENCE (Bihar Police level) ----------------
F("SCB",None,"""
The process by which green plants prepare food is:|हरे पौधे जिस प्रक्रिया से भोजन बनाते हैं:|Photosynthesis|प्रकाश संश्लेषण|Respiration/श्वसन;Transpiration/वाष्पोत्सर्जन;Digestion/पाचन
The powerhouse of the cell is:|कोशिका का 'पावरहाउस' कौन है?|Mitochondria|माइटोकॉन्ड्रिया|Nucleus/केंद्रक;Ribosome/राइबोसोम;Golgi body/गॉल्जीकाय
The universal blood donor group is:|सर्वदाता रक्त समूह कौन-सा है?|O negative|O ऋणात्मक (O−)|AB positive/AB धनात्मक;A positive/A धनात्मक;B negative/B ऋणात्मक
The hardest natural substance is:|सबसे कठोर प्राकृतिक पदार्थ है:|Diamond|हीरा|Graphite/ग्रेफाइट;Quartz/क्वार्ट्ज़;Iron/लोहा
Which gas is used in fire extinguishers?|अग्निशामक में कौन-सी गैस प्रयुक्त होती है?|Carbon dioxide|कार्बन डाइऑक्साइड|Oxygen/ऑक्सीजन;Hydrogen/हाइड्रोजन;Methane/मीथेन
The pH value of pure water is:|शुद्ध जल का pH मान है:|7|=|5;9;14
The most abundant gas in the atmosphere is:|वायुमंडल में सबसे अधिक पाई जाने वाली गैस है:|Nitrogen|नाइट्रोजन|Oxygen/ऑक्सीजन;Argon/आर्गन;Carbon dioxide/कार्बन डाइऑक्साइड
Light travels fastest in:|प्रकाश सबसे तेज़ किसमें चलता है?|Vacuum|निर्वात|Water/जल;Glass/काँच;Air/वायु
A concave lens is used to correct:|अवतल लेंस किस दोष को दूर करता है?|Myopia|निकट दृष्टि दोष|Hypermetropia/दूर दृष्टि दोष;Cataract/मोतियाबिंद;Colour blindness/वर्णांधता
Number of bones in an adult human body:|वयस्क मानव शरीर में हड्डियों की संख्या:|206|=|201;208;212
Normal human body temperature:|मानव शरीर का सामान्य तापमान:|37 °C|=|35 °C;39 °C;42 °C
Number of chromosomes in a human body cell:|मानव शरीर की कोशिका में गुणसूत्रों की संख्या:|46|=|23;44;48
Which vitamin is made in the skin by sunlight?|सूर्य के प्रकाश से त्वचा में कौन-सा विटामिन बनता है?|Vitamin D|विटामिन D|Vitamin A/विटामिन A;Vitamin C/विटामिन C;Vitamin K/विटामिन K
The largest organ of the human body is:|मानव शरीर का सबसे बड़ा अंग है:|Skin|त्वचा|Liver/यकृत;Heart/हृदय;Lungs/फेफड़े
Number of chambers in the human heart:|मानव हृदय में कक्षों की संख्या:|4|=|2;3;5
Deficiency of insulin causes:|इंसुलिन की कमी से होता है:|Diabetes|मधुमेह|Goitre/घेंघा;Anaemia/रक्ताल्पता;Rickets/रिकेट्स
The pigment that traps sunlight in plants:|पौधों में सूर्य का प्रकाश सोखने वाला वर्णक:|Chlorophyll|क्लोरोफिल|Haemoglobin/हीमोग्लोबिन;Melanin/मेलानिन;Keratin/केराटिन
The planet closest to the Sun is:|सूर्य के सबसे निकट का ग्रह है:|Mercury|बुध|Venus/शुक्र;Earth/पृथ्वी;Mars/मंगल
The largest planet of the solar system is:|सौरमंडल का सबसे बड़ा ग्रह है:|Jupiter|बृहस्पति|Saturn/शनि;Neptune/वरुण;Earth/पृथ्वी
The 'Red Planet' is:|'लाल ग्रह' किसे कहा जाता है?|Mars|मंगल|Venus/शुक्र;Jupiter/बृहस्पति;Mercury/बुध
The metal that is liquid at room temperature:|कमरे के तापमान पर द्रव अवस्था वाली धातु:|Mercury|पारा|Sodium/सोडियम;Iron/लोहा;Zinc/जस्ता
A gas used to fill weather balloons:|मौसम गुब्बारों में भरी जाने वाली गैस:|Helium|हीलियम|Oxygen/ऑक्सीजन;Chlorine/क्लोरीन;Carbon dioxide/कार्बन डाइऑक्साइड
The acid present in lemon is:|नींबू में पाया जाने वाला अम्ल है:|Citric acid|साइट्रिक अम्ल|Acetic acid/एसिटिक अम्ल;Lactic acid/लैक्टिक अम्ल;Formic acid/फॉर्मिक अम्ल
The acid present in curd is:|दही में पाया जाने वाला अम्ल है:|Lactic acid|लैक्टिक अम्ल|Citric acid/साइट्रिक अम्ल;Tartaric acid/टार्टरिक अम्ल;Formic acid/फॉर्मिक अम्ल
The sting of an ant contains:|चींटी के डंक में कौन-सा अम्ल होता है?|Formic acid|फॉर्मिक अम्ल|Acetic acid/एसिटिक अम्ल;Citric acid/साइट्रिक अम्ल;Oxalic acid/ऑक्सैलिक अम्ल
The study of fungi is called:|कवकों के अध्ययन को कहते हैं:|Mycology|कवक विज्ञान (माइकोलॉजी)|Botany/वनस्पति विज्ञान;Zoology/प्राणि विज्ञान;Virology/विषाणु विज्ञान
Sound with frequency above 20,000 Hz is called:|20,000 हर्ट्ज़ से अधिक आवृत्ति की ध्वनि कहलाती है:|Ultrasound|पराश्रव्य ध्वनि|Infrasound/अवश्रव्य ध्वनि;Audible sound/श्रव्य ध्वनि;Echo/प्रतिध्वनि
Newton's first law of motion is also called the law of:|न्यूटन का गति का प्रथम नियम कहलाता है:|Inertia|जड़त्व का नियम|Gravitation/गुरुत्वाकर्षण का नियम;Momentum/संवेग का नियम;Action–reaction/क्रिया–प्रतिक्रिया का नियम
Rusting of iron requires:|लोहे में जंग लगने के लिए आवश्यक है:|Oxygen and water|ऑक्सीजन और जल|Only oxygen/केवल ऑक्सीजन;Only water/केवल जल;Nitrogen and water/नाइट्रोजन और जल
Plants lose water vapour through:|पौधे जलवाष्प किस क्रिया से खोते हैं?|Transpiration|वाष्पोत्सर्जन|Respiration/श्वसन;Photosynthesis/प्रकाश संश्लेषण;Digestion/पाचन
""")

# ---------------- MATHS (generated, bilingual) ----------------
def D(ans, step, fmt):
    c = []
    for k in (-3,-2,-1,1,2,3,4):
        v = ans + k*step
        if v > 0 and v != ans: c.append(v)
    R.shuffle(c)
    return fmt(ans), [fmt(v) for v in c[:3]]
def M(en, hi, ans, step, fmt=lambda v: f"{v:g}"):
    a, d = D(ans, step, fmt); X("MTH", en, hi, a, d, "MTH")
for n, p in [(200,15),(250,40),(400,35),(500,12),(600,25),(800,45),(1200,15),(1500,60),(360,25),(450,20)]:
    M(f"What is {p}% of {n}?", f"{n} का {p}% कितना होता है?", n*p//100, max(1,n*p//1000))
for P, r, t in [(2000,5,3),(3000,4,5),(5000,6,2),(8000,5,4),(10000,8,3),(4000,10,2)]:
    M(f"Find the simple interest on ₹{P} at {r}% per annum for {t} years.", f"₹{P} पर {r}% वार्षिक दर से {t} वर्ष का साधारण ब्याज ज्ञात कीजिए।", P*r*t//100, 50, lambda v: f"₹{v}")
for _ in range(5):
    while True:
        L = [R.randint(10, 60) for _ in range(5)]
        if sum(L) % 5 == 0: break
    s = ", ".join(map(str, L)); M(f"Find the average of {s}.", f"{s} का औसत ज्ञात कीजिए।", sum(L)//5, 2)
for a, b, k in [(2,3,40),(3,5,25),(4,5,30),(1,3,50)]:
    T = (a+b)*k; M(f"Divide ₹{T} in the ratio {a}:{b}. What is the larger share?", f"₹{T} को {a}:{b} के अनुपात में बाँटने पर बड़ा हिस्सा कितना होगा?", T*max(a,b)//(a+b), 10, lambda v: f"₹{v}")
for cp, p in [(200,25),(400,10),(500,20),(800,50),(1000,40)]:
    sp = cp*(100+p)//100; M(f"An article bought for ₹{cp} is sold for ₹{sp}. Find the profit percent.", f"₹{cp} में खरीदी वस्तु ₹{sp} में बेची गई। लाभ प्रतिशत ज्ञात कीजिए।", p, 5, lambda v: f"{v}%")
for sp_, t in [(60,4),(45,6),(80,3),(72,5)]:
    d = sp_*t; M(f"A train covers {d} km in {t} hours. What is its speed in km/h?", f"एक ट्रेन {t} घंटे में {d} किमी चलती है। उसकी चाल (किमी/घंटा) क्या है?", sp_, 5)
for a, b in [(12,6),(20,30),(15,10),(30,60),(24,12)]:
    M(f"A can do a work in {a} days and B in {b} days. In how many days will they finish it together?", f"A किसी काम को {a} दिन में और B {b} दिन में कर सकता है। दोनों मिलकर कितने दिन में करेंगे?", a*b//(a+b), 1)
for x, y in [(12,18),(8,12),(15,20),(16,24),(18,27)]:
    import math
    M(f"Find the LCM of {x} and {y}.", f"{x} और {y} का ल.स.प. (LCM) ज्ञात कीजिए।", x*y//math.gcd(x,y), 6)
    M(f"Find the HCF of {x} and {y}.", f"{x} और {y} का म.स.प. (HCF) ज्ञात कीजिए।", math.gcd(x,y), 1)
for n in [144,196,225,324,441,529,625,729]:
    M(f"What is the value of √{n}?", f"√{n} का मान क्या है?", int(n**.5), 2)
for a, b, c in [(10,6,4),(25,8,5),(40,12,3),(18,9,6)]:
    M(f"Find the value of {a} + {b} × {c}.", f"{a} + {b} × {c} का मान ज्ञात कीजिए।", a+b*c, 4)
for l, w in [(12,8),(15,10),(20,9)]:
    M(f"The length and breadth of a rectangle are {l} m and {w} m. Find its area (sq m).", f"एक आयत की लंबाई {l} मी और चौड़ाई {w} मी है। उसका क्षेत्रफल (वर्ग मी) ज्ञात कीजिए।", l*w, 6)
for r in [7,14,21]:
    M(f"Find the area of a circle of radius {r} cm (π = 22/7).", f"{r} सेमी त्रिज्या वाले वृत्त का क्षेत्रफल ज्ञात कीजिए (π = 22/7)।", 22*r*r//7, 22)
for a0, d_ in [(3,4),(5,5),(10,7),(2,9)]:
    s = [a0+d_*i for i in range(5)]
    M(f"Find the next term: {', '.join(map(str,s))}, ?", f"अगला पद ज्ञात कीजिए: {', '.join(map(str,s))}, ?", a0+d_*5, d_)
