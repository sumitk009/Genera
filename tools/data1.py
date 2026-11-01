from engine import T, F

# ---------------- GEOGRAPHY ----------------
T("GEO", "CITY", """
Andhra Pradesh|आंध्र प्रदेश|Amaravati|अमरावती
Arunachal Pradesh|अरुणाचल प्रदेश|Itanagar|ईटानगर
Assam|असम|Dispur|दिसपुर
Bihar|बिहार|Patna|पटना
Chhattisgarh|छत्तीसगढ़|Raipur|रायपुर
Goa|गोवा|Panaji|पणजी
Gujarat|गुजरात|Gandhinagar|गांधीनगर
Haryana|हरियाणा|Chandigarh|चंडीगढ़
Himachal Pradesh|हिमाचल प्रदेश|Shimla|शिमला
Jharkhand|झारखंड|Ranchi|रांची
Karnataka|कर्नाटक|Bengaluru|बेंगलुरु
Kerala|केरल|Thiruvananthapuram|तिरुवनंतपुरम
Madhya Pradesh|मध्य प्रदेश|Bhopal|भोपाल
Maharashtra|महाराष्ट्र|Mumbai|मुंबई
Manipur|मणिपुर|Imphal|इंफाल
Meghalaya|मेघालय|Shillong|शिलांग
Mizoram|मिज़ोरम|Aizawl|आइज़ोल
Nagaland|नागालैंड|Kohima|कोहिमा
Odisha|ओडिशा|Bhubaneswar|भुवनेश्वर
Punjab|पंजाब|Chandigarh|चंडीगढ़
Rajasthan|राजस्थान|Jaipur|जयपुर
Sikkim|सिक्किम|Gangtok|गंगटोक
Tamil Nadu|तमिलनाडु|Chennai|चेन्नई
Telangana|तेलंगाना|Hyderabad|हैदराबाद
Tripura|त्रिपुरा|Agartala|अगरतला
Uttar Pradesh|उत्तर प्रदेश|Lucknow|लखनऊ
Uttarakhand|उत्तराखंड|Dehradun|देहरादून
West Bengal|पश्चिम बंगाल|Kolkata|कोलकाता
Andaman and Nicobar Islands|अंडमान और निकोबार द्वीपसमूह|Port Blair|पोर्ट ब्लेयर
Ladakh|लद्दाख|Leh|लेह
Lakshadweep|लक्षद्वीप|Kavaratti|कवरत्ती
Puducherry|पुदुच्चेरी|Puducherry|पुदुच्चेरी
""", "What is the capital of {k}?", "{k} की राजधानी क्या है?",
  "{v} is the capital of which state/UT?", "{v} किस राज्य/केंद्रशासित प्रदेश की राजधानी है?", kpool="STATE")

T("GEO", "CITY", """
Japan|जापान|Tokyo|टोक्यो
China|चीन|Beijing|बीजिंग
France|फ्रांस|Paris|पेरिस
Germany|जर्मनी|Berlin|बर्लिन
Italy|इटली|Rome|रोम
Russia|रूस|Moscow|मॉस्को
Egypt|मिस्र|Cairo|काहिरा
Canada|कनाडा|Ottawa|ओटावा
Australia|ऑस्ट्रेलिया|Canberra|कैनबरा
Brazil|ब्राज़ील|Brasilia|ब्रासीलिया
Argentina|अर्जेंटीना|Buenos Aires|ब्यूनस आयर्स
Pakistan|पाकिस्तान|Islamabad|इस्लामाबाद
Bangladesh|बांग्लादेश|Dhaka|ढाका
Nepal|नेपाल|Kathmandu|काठमांडू
Bhutan|भूटान|Thimphu|थिम्पू
Afghanistan|अफ़गानिस्तान|Kabul|काबुल
Iran|ईरान|Tehran|तेहरान
Iraq|इराक़|Baghdad|बगदाद
Saudi Arabia|सऊदी अरब|Riyadh|रियाद
Turkey|तुर्की|Ankara|अंकारा
Thailand|थाईलैंड|Bangkok|बैंकॉक
Malaysia|मलेशिया|Kuala Lumpur|कुआलालंपुर
Myanmar|म्यांमार|Naypyidaw|नेपीदॉ
South Korea|दक्षिण कोरिया|Seoul|सियोल
North Korea|उत्तर कोरिया|Pyongyang|प्योंगयांग
Vietnam|वियतनाम|Hanoi|हनोई
United Kingdom|यूनाइटेड किंगडम|London|लंदन
United States of America|संयुक्त राज्य अमेरिका|Washington, D.C.|वाशिंगटन डी.सी.
Spain|स्पेन|Madrid|मैड्रिड
Portugal|पुर्तगाल|Lisbon|लिस्बन
Greece|यूनान (ग्रीस)|Athens|एथेंस
Switzerland|स्विट्ज़रलैंड|Bern|बर्न
Netherlands|नीदरलैंड|Amsterdam|एम्स्टर्डम
Sweden|स्वीडन|Stockholm|स्टॉकहोम
Norway|नॉर्वे|Oslo|ओस्लो
Austria|ऑस्ट्रिया|Vienna|वियना
Poland|पोलैंड|Warsaw|वारसॉ
Kenya|केन्या|Nairobi|नैरोबी
Nigeria|नाइजीरिया|Abuja|अबुजा
Ethiopia|इथियोपिया|Addis Ababa|अदीस अबाबा
Cuba|क्यूबा|Havana|हवाना
Mexico|मेक्सिको|Mexico City|मेक्सिको सिटी
Peru|पेरू|Lima|लीमा
New Zealand|न्यूज़ीलैंड|Wellington|वेलिंगटन
Maldives|मालदीव|Male|माले
Qatar|क़तर|Doha|दोहा
Ukraine|यूक्रेन|Kyiv|कीव
""", "What is the capital of {k}?", "{k} की राजधानी क्या है?",
  "{v} is the capital of which country?", "{v} किस देश की राजधानी है?", kpool="COUNTRY")

T("GEO", "CUR", """
Japan|जापान|Yen|येन
United States of America|संयुक्त राज्य अमेरिका|US Dollar|अमेरिकी डॉलर
United Kingdom|यूनाइटेड किंगडम|Pound Sterling|पाउंड स्टर्लिंग
Russia|रूस|Ruble|रूबल
China|चीन|Yuan (Renminbi)|युआन (रेनमिन्बी)
Bangladesh|बांग्लादेश|Taka|टका
Nepal|नेपाल|Nepalese Rupee|नेपाली रुपया
Pakistan|पाकिस्तान|Pakistani Rupee|पाकिस्तानी रुपया
Sri Lanka|श्रीलंका|Sri Lankan Rupee|श्रीलंकाई रुपया
Bhutan|भूटान|Ngultrum|नगुल्ट्रम
Maldives|मालदीव|Rufiyaa|रुफ़िया
Afghanistan|अफ़गानिस्तान|Afghani|अफ़ग़ानी
Iran|ईरान|Iranian Rial|ईरानी रियाल
Saudi Arabia|सऊदी अरब|Saudi Riyal|सऊदी रियाल
Thailand|थाईलैंड|Baht|बाट
Malaysia|मलेशिया|Ringgit|रिंगित
Indonesia|इंडोनेशिया|Rupiah|रुपिया
South Korea|दक्षिण कोरिया|Won|वॉन
Vietnam|वियतनाम|Dong|दोंग
Myanmar|म्यांमार|Kyat|क्यात
South Africa|दक्षिण अफ्रीका|Rand|रैंड
Switzerland|स्विट्ज़रलैंड|Swiss Franc|स्विस फ्रैंक
Turkey|तुर्की|Turkish Lira|तुर्की लीरा
Brazil|ब्राज़ील|Real|रियल
Poland|पोलैंड|Zloty|ज़्लोटी
Sweden|स्वीडन|Krona|क्रोना
Australia|ऑस्ट्रेलिया|Australian Dollar|ऑस्ट्रेलियाई डॉलर
Germany|जर्मनी|Euro|यूरो
Kenya|केन्या|Kenyan Shilling|केन्याई शिलिंग
Egypt|मिस्र|Egyptian Pound|मिस्री पाउंड
Israel|इज़राइल|Shekel|शेकेल
Ukraine|यूक्रेन|Hryvnia|रिव्निया
""", "What is the currency of {k}?", "{k} की मुद्रा क्या है?")

T("GEO", "RIVER", """
Kolkata|कोलकाता|Hooghly|हुगली
Delhi|दिल्ली|Yamuna|यमुना
Agra|आगरा|Yamuna|यमुना
Ahmedabad|अहमदाबाद|Sabarmati|साबरमती
Varanasi|वाराणसी|Ganga|गंगा
Patna|पटना|Ganga|गंगा
Kanpur|कानपुर|Ganga|गंगा
Haridwar|हरिद्वार|Ganga|गंगा
Nashik|नासिक|Godavari|गोदावरी
Hyderabad|हैदराबाद|Musi|मूसी
Lucknow|लखनऊ|Gomti|गोमती
Ayodhya|अयोध्या|Saryu|सरयू
Surat|सूरत|Tapi|तापी
Vijayawada|विजयवाड़ा|Krishna|कृष्णा
Cuttack|कटक|Mahanadi|महानदी
Srinagar|श्रीनगर|Jhelum|झेलम
Ujjain|उज्जैन|Shipra|क्षिप्रा
Jabalpur|जबलपुर|Narmada|नर्मदा
Guwahati|गुवाहाटी|Brahmaputra|ब्रह्मपुत्र
Tiruchirappalli|तिरुचिरापल्ली|Kaveri|कावेरी
Kota|कोटा|Chambal|चंबल
Ludhiana|लुधियाना|Sutlej|सतलुज
Jamshedpur|जमशेदपुर|Subarnarekha|स्वर्णरेखा
London|लंदन|Thames|टेम्स
Paris|पेरिस|Seine|सीन
Cairo|काहिरा|Nile|नील
Baghdad|बगदाद|Tigris|दजला
Vienna|वियना|Danube|डेन्यूब
Rome|रोम|Tiber|टाइबर
Berlin|बर्लिन|Spree|स्प्री
Washington, D.C.|वाशिंगटन डी.सी.|Potomac|पोटोमैक
Lahore|लाहौर|Ravi|रावी
Dhaka|ढाका|Buriganga|बूढ़ीगंगा
""", "{k} is situated on the banks of which river?", "{k} किस नदी के तट पर स्थित है?")

T("GEO", "RIVER", """
Bhakra Nangal Dam|भाखड़ा नांगल बाँध|Sutlej|सतलुज
Hirakud Dam|हीराकुड बाँध|Mahanadi|महानदी
Tehri Dam|टिहरी बाँध|Bhagirathi|भागीरथी
Sardar Sarovar Dam|सरदार सरोवर बाँध|Narmada|नर्मदा
Nagarjuna Sagar Dam|नागार्जुन सागर बाँध|Krishna|कृष्णा
Mettur Dam|मेट्टूर बाँध|Kaveri|कावेरी
Idukki Dam|इडुक्की बाँध|Periyar|पेरियार
Salal Dam|सलाल बाँध|Chenab|चेनाब
Farakka Barrage|फरक्का बैराज|Ganga|गंगा
Ukai Dam|उकाई बाँध|Tapi|तापी
Gandhi Sagar Dam|गांधी सागर बाँध|Chambal|चंबल
Pong Dam|पोंग बाँध|Beas|ब्यास
Jayakwadi Dam|जायकवाड़ी बाँध|Godavari|गोदावरी
Indira Sagar Dam|इंदिरा सागर बाँध|Narmada|नर्मदा
Tungabhadra Dam|तुंगभद्रा बाँध|Tungabhadra|तुंगभद्रा
""", "{k} is built on which river?", "{k} किस नदी पर बना है?")

T("GEO", "STATE", """
Jim Corbett National Park|जिम कॉर्बेट राष्ट्रीय उद्यान|Uttarakhand|उत्तराखंड
Kaziranga National Park|काज़ीरंगा राष्ट्रीय उद्यान|Assam|असम
Ranthambore National Park|रणथंभौर राष्ट्रीय उद्यान|Rajasthan|राजस्थान
Gir National Park|गिर राष्ट्रीय उद्यान|Gujarat|गुजरात
Kanha National Park|कान्हा राष्ट्रीय उद्यान|Madhya Pradesh|मध्य प्रदेश
Bandipur National Park|बांदीपुर राष्ट्रीय उद्यान|Karnataka|कर्नाटक
Periyar National Park|पेरियार राष्ट्रीय उद्यान|Kerala|केरल
Sundarbans National Park|सुंदरबन राष्ट्रीय उद्यान|West Bengal|पश्चिम बंगाल
Simlipal National Park|सिमलीपाल राष्ट्रीय उद्यान|Odisha|ओडिशा
Tadoba National Park|ताडोबा राष्ट्रीय उद्यान|Maharashtra|महाराष्ट्र
Hemis National Park|हेमिस राष्ट्रीय उद्यान|Ladakh|लद्दाख
Dachigam National Park|दाचीगाम राष्ट्रीय उद्यान|Jammu and Kashmir|जम्मू और कश्मीर
Great Himalayan National Park|ग्रेट हिमालयन राष्ट्रीय उद्यान|Himachal Pradesh|हिमाचल प्रदेश
Namdapha National Park|नामदफा राष्ट्रीय उद्यान|Arunachal Pradesh|अरुणाचल प्रदेश
Dudhwa National Park|दुधवा राष्ट्रीय उद्यान|Uttar Pradesh|उत्तर प्रदेश
Betla National Park|बेतला राष्ट्रीय उद्यान|Jharkhand|झारखंड
Mudumalai National Park|मुदुमलाई राष्ट्रीय उद्यान|Tamil Nadu|तमिलनाडु
Valmiki National Park|वाल्मीकि राष्ट्रीय उद्यान|Bihar|बिहार
Keibul Lamjao National Park|केईबुल लामजाओ राष्ट्रीय उद्यान|Manipur|मणिपुर
Panna National Park|पन्ना राष्ट्रीय उद्यान|Madhya Pradesh|मध्य प्रदेश
""", "{k} is located in which state/UT?", "{k} किस राज्य/केंद्रशासित प्रदेश में स्थित है?")

T("GEO", "STATE", """
Chilika Lake|चिल्का झील|Odisha|ओडिशा
Dal Lake|डल झील|Jammu and Kashmir|जम्मू और कश्मीर
Loktak Lake|लोकटक झील|Manipur|मणिपुर
Sambhar Lake|सांभर झील|Rajasthan|राजस्थान
Vembanad Lake|वेम्बनाड झील|Kerala|केरल
Lonar Lake|लोनार झील|Maharashtra|महाराष्ट्र
Hussain Sagar Lake|हुसैन सागर झील|Telangana|तेलंगाना
Pichola Lake|पिछोला झील|Rajasthan|राजस्थान
Kolleru Lake|कोल्लेरु झील|Andhra Pradesh|आंध्र प्रदेश
Naini Lake|नैनी झील|Uttarakhand|उत्तराखंड
Tsomgo (Changu) Lake|त्सोमगो (छांगू) झील|Sikkim|सिक्किम
Umiam (Barapani) Lake|उमियम (बड़ापानी) झील|Meghalaya|मेघालय
Pangong Tso|पैंगोंग त्सो|Ladakh|लद्दाख
Wular Lake|वूलर झील|Jammu and Kashmir|जम्मू और कश्मीर
""", "{k} is located in which state/UT?", "{k} किस राज्य/केंद्रशासित प्रदेश में स्थित है?")

T("GEO", "STATE", """
Kanchenjunga|कंचनजंगा|Sikkim|सिक्किम
Nanda Devi|नंदा देवी|Uttarakhand|उत्तराखंड
Anamudi|अनामुडी|Kerala|केरल
Doddabetta|दोदाबेट्टा|Tamil Nadu|तमिलनाडु
Guru Shikhar|गुरु शिखर|Rajasthan|राजस्थान
Dhupgarh|धूपगढ़|Madhya Pradesh|मध्य प्रदेश
Saramati|सारामति|Nagaland|नागालैंड
""", "The peak {k} is located in which state?", "{k} शिखर किस राज्य में स्थित है?")

T("GEO", "COUNTRY", """
Mount Everest|माउंट एवरेस्ट|Nepal|नेपाल
Mount Kilimanjaro|माउंट किलिमंजारो|Tanzania|तंजानिया
Mount Fuji|माउंट फ़ूजी|Japan|जापान
Mount Elbrus|माउंट एल्ब्रुस|Russia|रूस
Aconcagua|एकोंकागुआ|Argentina|अर्जेंटीना
Mount Olympus|माउंट ओलंपस|Greece|यूनान (ग्रीस)
""", "{k} is located in which country?", "{k} किस देश में स्थित है?")

T("GEO", "CITY", """
Pink City|गुलाबी नगरी|Jaipur|जयपुर
City of Lakes|झीलों की नगरी|Udaipur|उदयपुर
Silicon Valley of India|भारत की सिलिकॉन वैली|Bengaluru|बेंगलुरु
City of Joy|आनंद का शहर|Kolkata|कोलकाता
Manchester of India|भारत का मैनचेस्टर|Ahmedabad|अहमदाबाद
Financial Capital of India|भारत की वित्तीय राजधानी|Mumbai|मुंबई
Blue City|नीला शहर|Jodhpur|जोधपुर
Golden City|स्वर्ण नगरी|Jaisalmer|जैसलमेर
Orange City|संतरों का शहर|Nagpur|नागपुर
Steel City of India|भारत का इस्पात नगर|Jamshedpur|जमशेदपुर
Pearl City|मोतियों का शहर|Hyderabad|हैदराबाद
Queen of Hills|पहाड़ों की रानी|Mussoorie|मसूरी
Detroit of India|भारत का डेट्रॉयट|Chennai|चेन्नई
Venice of the East|पूर्व का वेनिस|Alappuzha|अलप्पुझा
Queen of the Arabian Sea|अरब सागर की रानी|Kochi|कोच्चि
Eternal City|अनंत नगर|Rome|रोम
Big Apple|बिग एप्पल|New York|न्यूयॉर्क
""", "Which city is known as the '{k}'?", "'{k}' के नाम से कौन-सा शहर जाना जाता है?")

T("GEO", "CITY", """
Taj Mahal|ताजमहल|Agra|आगरा
Red Fort|लाल किला|Delhi|दिल्ली
Qutub Minar|कुतुब मीनार|Delhi|दिल्ली
Charminar|चारमीनार|Hyderabad|हैदराबाद
Gateway of India|गेटवे ऑफ इंडिया|Mumbai|मुंबई
Victoria Memorial|विक्टोरिया मेमोरियल|Kolkata|कोलकाता
Hawa Mahal|हवा महल|Jaipur|जयपुर
Meenakshi Temple|मीनाक्षी मंदिर|Madurai|मदुरै
Golden Temple|स्वर्ण मंदिर|Amritsar|अमृतसर
Lingaraj Temple|लिंगराज मंदिर|Bhubaneswar|भुवनेश्वर
Jagannath Temple|जगन्नाथ मंदिर|Puri|पुरी
Mysore Palace|मैसूर पैलेस|Mysuru|मैसूरु
Gol Gumbaz|गोल गुंबद|Bijapur (Vijayapura)|बीजापुर (विजयपुरा)
Leaning Tower|पीसा की मीनार|Pisa|पीसा
Eiffel Tower|एफिल टॉवर|Paris|पेरिस
Colosseum|कोलोसियम|Rome|रोम
Big Ben|बिग बेन|London|लंदन
Statue of Liberty|स्टैच्यू ऑफ लिबर्टी|New York|न्यूयॉर्क
Sydney Opera House|सिडनी ओपेरा हाउस|Sydney|सिडनी
Burj Khalifa|बुर्ज खलीफा|Dubai|दुबई
Kremlin|क्रेमलिन|Moscow|मॉस्को
""", "In which city is the {k} located?", "{k} किस शहर में स्थित है?")

T("STA", "CITY", """
United Nations|संयुक्त राष्ट्र|New York|न्यूयॉर्क
World Health Organization (WHO)|विश्व स्वास्थ्य संगठन (WHO)|Geneva|जिनेवा
International Monetary Fund (IMF)|अंतर्राष्ट्रीय मुद्रा कोष (IMF)|Washington, D.C.|वाशिंगटन डी.सी.
World Bank|विश्व बैंक|Washington, D.C.|वाशिंगटन डी.सी.
UNESCO|यूनेस्को|Paris|पेरिस
World Trade Organization (WTO)|विश्व व्यापार संगठन (WTO)|Geneva|जिनेवा
International Labour Organization (ILO)|अंतर्राष्ट्रीय श्रम संगठन (ILO)|Geneva|जिनेवा
International Court of Justice|अंतर्राष्ट्रीय न्यायालय|The Hague|हेग
UNICEF|यूनिसेफ|New York|न्यूयॉर्क
Food and Agriculture Organization (FAO)|खाद्य एवं कृषि संगठन (FAO)|Rome|रोम
Interpol|इंटरपोल|Lyon|लियोन
NATO|नाटो|Brussels|ब्रुसेल्स
OPEC|ओपेक|Vienna|वियना
Amnesty International|एमनेस्टी इंटरनेशनल|London|लंदन
SAARC Secretariat|सार्क सचिवालय|Kathmandu|काठमांडू
ASEAN Secretariat|आसियान सचिवालय|Jakarta|जकार्ता
Asian Development Bank|एशियाई विकास बैंक|Manila|मनीला
New Development Bank (BRICS)|न्यू डेवलपमेंट बैंक (ब्रिक्स)|Shanghai|शंघाई
ISRO|इसरो|Bengaluru|बेंगलुरु
Reserve Bank of India|भारतीय रिज़र्व बैंक|Mumbai|मुंबई
SEBI|सेबी|Mumbai|मुंबई
NABARD|नाबार्ड|Mumbai|मुंबई
Election Commission of India|भारत निर्वाचन आयोग|New Delhi|नई दिल्ली
UPSC|संघ लोक सेवा आयोग|New Delhi|नई दिल्ली
International Olympic Committee|अंतर्राष्ट्रीय ओलंपिक समिति|Lausanne|लुसाने
FIFA|फ़ीफ़ा|Zurich|ज्यूरिख
International Cricket Council (ICC)|अंतर्राष्ट्रीय क्रिकेट परिषद (ICC)|Dubai|दुबई
UN Environment Programme (UNEP)|संयुक्त राष्ट्र पर्यावरण कार्यक्रम|Nairobi|नैरोबी
UNHCR|यूएनएचसीआर|Geneva|जिनेवा
""", "Where is the headquarters of the {k} located?", "{k} का मुख्यालय कहाँ स्थित है?")

# ---------------- STATIC GK ----------------
T("STA", "STATE", """
Kathak|कथक|Uttar Pradesh|उत्तर प्रदेश
Bharatanatyam|भरतनाट्यम|Tamil Nadu|तमिलनाडु
Kathakali|कथकली|Kerala|केरल
Mohiniyattam|मोहिनीअट्टम|Kerala|केरल
Kuchipudi|कुचिपुड़ी|Andhra Pradesh|आंध्र प्रदेश
Odissi|ओडिसी|Odisha|ओडिशा
Manipuri|मणिपुरी|Manipur|मणिपुर
Sattriya|सत्रिया|Assam|असम
Garba|गरबा|Gujarat|गुजरात
Bihu|बिहू|Assam|असम
Bhangra|भांगड़ा|Punjab|पंजाब
Ghoomar|घूमर|Rajasthan|राजस्थान
Lavani|लावणी|Maharashtra|महाराष्ट्र
Yakshagana|यक्षगान|Karnataka|कर्नाटक
Giddha|गिद्धा|Punjab|पंजाब
Theyyam|तेय्यम|Kerala|केरल
Bagurumba|बगुरुम्बा|Assam|असम
Kalbelia|कालबेलिया|Rajasthan|राजस्थान
""", "{k} is a dance form of which state?", "{k} किस राज्य का नृत्य है?")

T("STA", "STATE", """
Onam|ओणम|Kerala|केरल
Pongal|पोंगल|Tamil Nadu|तमिलनाडु
Lohri|लोहड़ी|Punjab|पंजाब
Durga Puja (grand celebration)|दुर्गा पूजा (भव्य उत्सव)|West Bengal|पश्चिम बंगाल
Hornbill Festival|हॉर्नबिल महोत्सव|Nagaland|नागालैंड
Rath Yatra (Puri)|रथ यात्रा (पुरी)|Odisha|ओडिशा
Pushkar Fair|पुष्कर मेला|Rajasthan|राजस्थान
Sonepur Fair|सोनपुर मेला|Bihar|बिहार
Wangala Festival|वांगाला महोत्सव|Meghalaya|मेघालय
Gudi Padwa|गुड़ी पड़वा|Maharashtra|महाराष्ट्र
Hemis Festival|हेमिस महोत्सव|Ladakh|लद्दाख
Kharchi Puja|खर्ची पूजा|Tripura|त्रिपुरा
Bihu (Rongali)|बिहू (रोंगाली)|Assam|असम
""", "{k} is mainly associated with which state/UT?", "{k} मुख्यतः किस राज्य/केंद्रशासित प्रदेश से संबंधित है?")

T("STA", "ABB", """
GDP|GDP|Gross Domestic Product|सकल घरेलू उत्पाद
GNP|GNP|Gross National Product|सकल राष्ट्रीय उत्पाद
SEBI|SEBI|Securities and Exchange Board of India|भारतीय प्रतिभूति एवं विनिमय बोर्ड
NABARD|NABARD|National Bank for Agriculture and Rural Development|राष्ट्रीय कृषि एवं ग्रामीण विकास बैंक
GST|GST|Goods and Services Tax|वस्तु एवं सेवा कर
UPSC|UPSC|Union Public Service Commission|संघ लोक सेवा आयोग
ISRO|ISRO|Indian Space Research Organisation|भारतीय अंतरिक्ष अनुसंधान संगठन
DRDO|DRDO|Defence Research and Development Organisation|रक्षा अनुसंधान एवं विकास संगठन
NASA|NASA|National Aeronautics and Space Administration|राष्ट्रीय वैमानिकी एवं अंतरिक्ष प्रशासन
UNESCO|UNESCO|United Nations Educational, Scientific and Cultural Organization|संयुक्त राष्ट्र शैक्षिक, वैज्ञानिक एवं सांस्कृतिक संगठन
UNICEF|UNICEF|United Nations International Children's Emergency Fund|संयुक्त राष्ट्र अंतर्राष्ट्रीय बाल आपातकालीन कोष
WTO|WTO|World Trade Organization|विश्व व्यापार संगठन
IMF|IMF|International Monetary Fund|अंतर्राष्ट्रीय मुद्रा कोष
NATO|NATO|North Atlantic Treaty Organization|उत्तरी अटलांटिक संधि संगठन
SAARC|SAARC|South Asian Association for Regional Cooperation|दक्षिण एशियाई क्षेत्रीय सहयोग संगठन
ASEAN|ASEAN|Association of Southeast Asian Nations|दक्षिण-पूर्व एशियाई राष्ट्र संघ
OPEC|OPEC|Organization of the Petroleum Exporting Countries|पेट्रोलियम निर्यातक देशों का संगठन
CAG|CAG|Comptroller and Auditor General|नियंत्रक एवं महालेखा परीक्षक
MGNREGA|MGNREGA|Mahatma Gandhi National Rural Employment Guarantee Act|महात्मा गांधी राष्ट्रीय ग्रामीण रोज़गार गारंटी अधिनियम
CBI|CBI|Central Bureau of Investigation|केंद्रीय अन्वेषण ब्यूरो
NIA|NIA|National Investigation Agency|राष्ट्रीय अन्वेषण अभिकरण
CRPF|CRPF|Central Reserve Police Force|केंद्रीय रिज़र्व पुलिस बल
BSF|BSF|Border Security Force|सीमा सुरक्षा बल
ITBP|ITBP|Indo-Tibetan Border Police|भारत-तिब्बत सीमा पुलिस
CISF|CISF|Central Industrial Security Force|केंद्रीय औद्योगिक सुरक्षा बल
NDRF|NDRF|National Disaster Response Force|राष्ट्रीय आपदा प्रतिक्रिया बल
AIIMS|AIIMS|All India Institute of Medical Sciences|अखिल भारतीय आयुर्विज्ञान संस्थान
IRCTC|IRCTC|Indian Railway Catering and Tourism Corporation|भारतीय रेलवे खानपान एवं पर्यटन निगम
LIC|LIC|Life Insurance Corporation|जीवन बीमा निगम
ATM|ATM|Automated Teller Machine|स्वचालित टेलर मशीन
PIN (postal)|PIN (डाक)|Postal Index Number|डाक सूचकांक संख्या
UPI|UPI|Unified Payments Interface|एकीकृत भुगतान इंटरफ़ेस
NEFT|NEFT|National Electronic Funds Transfer|राष्ट्रीय इलेक्ट्रॉनिक निधि अंतरण
RTGS|RTGS|Real Time Gross Settlement|रियल टाइम ग्रॉस सेटलमेंट
IPC|IPC|Indian Penal Code|भारतीय दंड संहिता
RTI|RTI|Right to Information|सूचना का अधिकार
PAN|PAN|Permanent Account Number|स्थायी खाता संख्या
GPS|GPS|Global Positioning System|वैश्विक स्थिति निर्धारण प्रणाली
LASER|LASER|Light Amplification by Stimulated Emission of Radiation|विकिरण के उद्दीपित उत्सर्जन द्वारा प्रकाश प्रवर्धन
RADAR|RADAR|Radio Detection and Ranging|रेडियो डिटेक्शन एंड रेंजिंग
DNA|DNA|Deoxyribonucleic Acid|डीऑक्सीराइबोन्यूक्लिक अम्ल
RNA|RNA|Ribonucleic Acid|राइबोन्यूक्लिक अम्ल
HIV|HIV|Human Immunodeficiency Virus|मानव प्रतिरक्षा अपूर्णता विषाणु
AIDS|AIDS|Acquired Immuno Deficiency Syndrome|उपार्जित प्रतिरक्षा अपूर्णता सिंड्रोम
CPU|CPU|Central Processing Unit|केंद्रीय प्रसंस्करण इकाई
RAM|RAM|Random Access Memory|रैंडम एक्सेस मेमोरी
ROM|ROM|Read Only Memory|रीड ओनली मेमोरी
URL|URL|Uniform Resource Locator|यूनिफ़ॉर्म रिसोर्स लोकेटर
HTML|HTML|HyperText Markup Language|हाइपरटेक्स्ट मार्कअप लैंग्वेज
PDF|PDF|Portable Document Format|पोर्टेबल डॉक्यूमेंट फ़ॉर्मेट
USB|USB|Universal Serial Bus|यूनिवर्सल सीरियल बस
FDI|FDI|Foreign Direct Investment|प्रत्यक्ष विदेशी निवेश
MSP|MSP|Minimum Support Price|न्यूनतम समर्थन मूल्य
PDS|PDS|Public Distribution System|सार्वजनिक वितरण प्रणाली
CPI|CPI|Consumer Price Index|उपभोक्ता मूल्य सूचकांक
""", "What is the full form of {k}?", "{k} का पूर्ण रूप क्या है?")

T("STA", "PER", """
Gitanjali|गीतांजलि|Rabindranath Tagore|रवींद्रनाथ टैगोर
Godan|गोदान|Munshi Premchand|मुंशी प्रेमचंद
The Discovery of India|डिस्कवरी ऑफ इंडिया|Jawaharlal Nehru|जवाहरलाल नेहरू
Hind Swaraj|हिंद स्वराज|Mahatma Gandhi|महात्मा गांधी
My Experiments with Truth|सत्य के साथ मेरे प्रयोग|Mahatma Gandhi|महात्मा गांधी
Arthashastra|अर्थशास्त्र|Kautilya (Chanakya)|कौटिल्य (चाणक्य)
Abhijnanashakuntalam|अभिज्ञानशाकुंतलम्|Kalidasa|कालिदास
Rajatarangini|राजतरंगिणी|Kalhana|कल्हण
Harshacharita|हर्षचरित|Banabhatta|बाणभट्ट
Mudrarakshasa|मुद्राराक्षस|Vishakhadatta|विशाखदत्त
Ain-i-Akbari|आइन-ए-अकबरी|Abul Fazl|अबुल फ़ज़ल
Babarnama|बाबरनामा|Babur|बाबर
Humayun-nama|हुमायूँनामा|Gulbadan Begum|गुलबदन बेगम
Kitab-ul-Hind|किताब-उल-हिंद|Al-Biruni|अल-बरूनी
Indica|इंडिका|Megasthenes|मेगस्थनीज़
Ramcharitmanas|रामचरितमानस|Tulsidas|तुलसीदास
Padmavat|पद्मावत|Malik Muhammad Jayasi|मलिक मुहम्मद जायसी
Kamayani|कामायनी|Jaishankar Prasad|जयशंकर प्रसाद
Madhushala|मधुशाला|Harivansh Rai Bachchan|हरिवंश राय बच्चन
Anandamath|आनंदमठ|Bankim Chandra Chatterjee|बंकिम चंद्र चट्टोपाध्याय
Malgudi Days|मालगुडी डेज़|R. K. Narayan|आर. के. नारायण
The God of Small Things|द गॉड ऑफ स्मॉल थिंग्स|Arundhati Roy|अरुंधति रॉय
Midnight's Children|मिडनाइट्स चिल्ड्रन|Salman Rushdie|सलमान रुश्दी
Train to Pakistan|ट्रेन टू पाकिस्तान|Khushwant Singh|खुशवंत सिंह
Wings of Fire|विंग्स ऑफ फायर|A. P. J. Abdul Kalam|ए. पी. जे. अब्दुल कलाम
Mein Kampf|मीन कैम्फ़|Adolf Hitler|एडॉल्फ हिटलर
Das Kapital|दास कैपिटल|Karl Marx|कार्ल मार्क्स
The Wealth of Nations|द वेल्थ ऑफ नेशंस|Adam Smith|एडम स्मिथ
Hamlet|हैमलेट|William Shakespeare|विलियम शेक्सपियर
Paradise Lost|पैराडाइज़ लॉस्ट|John Milton|जॉन मिल्टन
On the Origin of Species|ऑन द ओरिजिन ऑफ स्पीशीज़|Charles Darwin|चार्ल्स डार्विन
A Brief History of Time|ए ब्रीफ हिस्ट्री ऑफ टाइम|Stephen Hawking|स्टीफन हॉकिंग
War and Peace|युद्ध और शांति|Leo Tolstoy|लियो टॉल्स्टॉय
The Prince|द प्रिंस|Niccolò Machiavelli|निकोलो मैकियावेली
Utopia|यूटोपिया|Thomas More|थॉमस मोर
Leviathan|लेवियाथन|Thomas Hobbes|थॉमस हॉब्स
The Social Contract|द सोशल कॉन्ट्रैक्ट|Jean-Jacques Rousseau|जीन-जैक्स रूसो
Gulliver's Travels|गुलिवर्स ट्रैवल्स|Jonathan Swift|जोनाथन स्विफ्ट
Panchatantra|पंचतंत्र|Vishnu Sharma|विष्णु शर्मा
Mahabhashya|महाभाष्य|Patanjali|पतंजलि
Ashtadhyayi|अष्टाध्यायी|Panini|पाणिनि
Brihat Samhita|बृहत्संहिता|Varahamihira|वराहमिहिर
Aryabhatiya|आर्यभटीय|Aryabhata|आर्यभट
Siddhanta Shiromani|सिद्धांत शिरोमणि|Bhaskaracharya|भास्कराचार्य
Gita Govinda|गीत गोविंद|Jayadeva|जयदेव
Pather Panchali|पथेर पांचाली|Bibhutibhushan Bandyopadhyay|विभूतिभूषण बंद्योपाध्याय
Nil Darpan|नील दर्पण|Dinabandhu Mitra|दीनबंधु मित्र
Long Walk to Freedom|लॉन्ग वॉक टू फ्रीडम|Nelson Mandela|नेल्सन मंडेला
The Audacity of Hope|द ऑडेसिटी ऑफ होप|Barack Obama|बराक ओबामा
The Diary of a Young Girl|एक युवा लड़की की डायरी|Anne Frank|ऐनी फ्रैंक
Playing It My Way|प्लेइंग इट माई वे|Sachin Tendulkar|सचिन तेंदुलकर
""", "Who is the author of '{k}'?", "'{k}' के लेखक कौन हैं?")

T("HIS", "PER", """
Jai Jawan Jai Kisan|जय जवान जय किसान|Lal Bahadur Shastri|लाल बहादुर शास्त्री
Do or Die (Karo ya Maro)|करो या मरो|Mahatma Gandhi|महात्मा गांधी
Delhi Chalo|दिल्ली चलो|Subhas Chandra Bose|सुभाष चंद्र बोस
Give me blood, I will give you freedom|तुम मुझे खून दो, मैं तुम्हें आज़ादी दूँगा|Subhas Chandra Bose|सुभाष चंद्र बोस
Swaraj is my birthright|स्वराज मेरा जन्मसिद्ध अधिकार है|Bal Gangadhar Tilak|बाल गंगाधर तिलक
Garibi Hatao|गरीबी हटाओ|Indira Gandhi|इंदिरा गांधी
Total Revolution (Sampoorna Kranti)|संपूर्ण क्रांति|Jayaprakash Narayan|जयप्रकाश नारायण
Simon Go Back|साइमन गो बैक|Lala Lajpat Rai|लाला लाजपत राय
Sare Jahan Se Accha|सारे जहाँ से अच्छा|Muhammad Iqbal|मुहम्मद इक़बाल
Jai Jagat|जय जगत|Vinoba Bhave|विनोबा भावे
Jai Jawan Jai Kisan Jai Vigyan|जय जवान जय किसान जय विज्ञान|Atal Bihari Vajpayee|अटल बिहारी वाजपेयी
Vande Mataram (song)|वंदे मातरम् (गीत)|Bankim Chandra Chatterjee|बंकिम चंद्र चट्टोपाध्याय
""", "Who gave the slogan/composed '{k}'?", "'{k}' का नारा/रचना किसकी है?")

T("HIS", "PER", """
Maurya Dynasty|मौर्य वंश|Chandragupta Maurya|चंद्रगुप्त मौर्य
Gupta Dynasty|गुप्त वंश|Sri Gupta|श्रीगुप्त
Nanda Dynasty|नंद वंश|Mahapadma Nanda|महापद्म नंद
Mughal Empire in India|भारत में मुगल साम्राज्य|Babur|बाबर
Slave Dynasty (Mamluk)|गुलाम वंश|Qutb-ud-din Aibak|कुतुबुद्दीन ऐबक
Khilji Dynasty|खिलजी वंश|Jalal-ud-din Khilji|जलालुद्दीन खिलजी
Tughlaq Dynasty|तुगलक वंश|Ghiyas-ud-din Tughlaq|गयासुद्दीन तुगलक
Lodi Dynasty|लोदी वंश|Bahlol Lodi|बहलोल लोदी
Sayyid Dynasty|सैयद वंश|Khizr Khan|खिज्र खाँ
Sur Empire|सूर साम्राज्य|Sher Shah Suri|शेरशाह सूरी
Maratha Empire|मराठा साम्राज्य|Shivaji|शिवाजी
Sikh Empire|सिख साम्राज्य|Maharaja Ranjit Singh|महाराजा रणजीत सिंह
Pala Dynasty|पाल वंश|Gopala|गोपाल
Shunga Dynasty|शुंग वंश|Pushyamitra Shunga|पुष्यमित्र शुंग
Satavahana Dynasty|सातवाहन वंश|Simuka|सिमुक
Haryanka Dynasty|हर्यंक वंश|Bimbisara|बिम्बिसार
Rashtrakuta Dynasty|राष्ट्रकूट वंश|Dantidurga|दंतिदुर्ग
""", "Who was the founder of the {k}?", "{k} का संस्थापक कौन था?")

T("HIS", "PER", """
Taj Mahal|ताजमहल|Shah Jahan|शाहजहाँ
Red Fort (Delhi)|लाल किला (दिल्ली)|Shah Jahan|शाहजहाँ
Jama Masjid (Delhi)|जामा मस्जिद (दिल्ली)|Shah Jahan|शाहजहाँ
Humayun's Tomb|हुमायूँ का मकबरा|Hamida Banu Begum|हमीदा बानो बेगम
Buland Darwaza|बुलंद दरवाज़ा|Akbar|अकबर
Fatehpur Sikri|फतेहपुर सीकरी|Akbar|अकबर
Charminar|चारमीनार|Muhammad Quli Qutb Shah|मुहम्मद कुली कुतुब शाह
Gol Gumbaz|गोल गुंबद|Muhammad Adil Shah|मुहम्मद आदिल शाह
Konark Sun Temple|कोणार्क सूर्य मंदिर|Narasimhadeva I|नरसिंहदेव प्रथम
Brihadeshwara Temple (Thanjavur)|बृहदेश्वर मंदिर (तंजावुर)|Rajaraja Chola I|राजराज चोल प्रथम
Alai Darwaza|अलाई दरवाज़ा|Alauddin Khilji|अलाउद्दीन खिलजी
Hawa Mahal|हवा महल|Sawai Pratap Singh|सवाई प्रताप सिंह
Jantar Mantar (Jaipur)|जंतर मंतर (जयपुर)|Sawai Jai Singh II|सवाई जयसिंह द्वितीय
Lotus Temple|लोटस टेम्पल|Fariborz Sahba|फरीबोर्ज़ साहबा
Tomb of Itimad-ud-Daula|इतिमाद-उद-दौला का मकबरा|Nur Jahan|नूरजहाँ
Gateway of India|गेटवे ऑफ इंडिया|George Wittet|जॉर्ज विटेट
Grand Trunk Road (reconstructed)|ग्रैंड ट्रंक रोड (पुनर्निर्माण)|Sher Shah Suri|शेरशाह सूरी
""", "Who built/designed the {k}?", "{k} का निर्माण/डिज़ाइन किसने करवाया/किया?")

T("SCI", "PER", """
Telephone|टेलीफोन|Alexander Graham Bell|अलेक्ज़ेंडर ग्राहम बेल
Electric bulb|विद्युत बल्ब|Thomas Alva Edison|थॉमस अल्वा एडिसन
Wireless telegraphy (radio)|वायरलेस टेलीग्राफी (रेडियो)|Guglielmo Marconi|गुग्लिएल्मो मार्कोनी
Television|टेलीविज़न|John Logie Baird|जॉन लोगी बेयर्ड
Steam engine (improved)|भाप इंजन (सुधारित)|James Watt|जेम्स वाट
Aeroplane|हवाई जहाज़|Wright Brothers|राइट बंधु
Printing press|छपाई मशीन|Johannes Gutenberg|जोहानेस गुटेनबर्ग
Dynamite|डायनामाइट|Alfred Nobel|अल्फ्रेड नोबेल
Penicillin|पेनिसिलिन|Alexander Fleming|अलेक्ज़ेंडर फ्लेमिंग
Law of Gravitation|गुरुत्वाकर्षण का नियम|Isaac Newton|आइज़ैक न्यूटन
Theory of Relativity|सापेक्षता का सिद्धांत|Albert Einstein|अल्बर्ट आइंस्टीन
Electron|इलेक्ट्रॉन|J. J. Thomson|जे. जे. थॉमसन
Neutron|न्यूट्रॉन|James Chadwick|जेम्स चैडविक
Proton|प्रोटॉन|Ernest Rutherford|अर्नेस्ट रदरफोर्ड
X-rays|एक्स-किरणें|Wilhelm Röntgen|विल्हेम रॉन्टजेन
Radium|रेडियम|Marie Curie|मैरी क्यूरी
Smallpox vaccine|चेचक का टीका|Edward Jenner|एडवर्ड जेनर
Rabies vaccine|रेबीज़ का टीका|Louis Pasteur|लुई पाश्चर
Circulation of blood|रक्त परिसंचरण|William Harvey|विलियम हार्वे
Theory of natural selection|प्राकृतिक चयन का सिद्धांत|Charles Darwin|चार्ल्स डार्विन
Laws of heredity|आनुवंशिकता के नियम|Gregor Mendel|ग्रेगर मेंडल
Cell|कोशिका|Robert Hooke|रॉबर्ट हुक
Periodic Table|आवर्त सारणी|Dmitri Mendeleev|दिमित्री मेंडेलीव
Electromagnetic induction|विद्युत चुंबकीय प्रेरण|Michael Faraday|माइकल फैराडे
Lightning conductor|तड़ित चालक|Benjamin Franklin|बेंजामिन फ्रैंकलिन
Miner's safety lamp|खनिकों का सुरक्षा लैंप|Humphry Davy|हम्फ्री डेवी
Laws of planetary motion|ग्रहीय गति के नियम|Johannes Kepler|योहानेस केप्लर
Heliocentric theory|सूर्यकेंद्रित सिद्धांत|Nicolaus Copernicus|निकोलस कोपरनिकस
Cinematograph|सिनेमैटोग्राफ|Lumière Brothers|ल्युमियर बंधु
Morse code telegraph|मोर्स कोड टेलीग्राफ|Samuel Morse|सैमुअल मोर्स
Raman Effect|रमण प्रभाव|C. V. Raman|सी. वी. रमन
Quantum theory|क्वांटम सिद्धांत|Max Planck|मैक्स प्लांक
Pasteurisation|पाश्चुरीकरण|Louis Pasteur|लुई पाश्चर
Bose–Einstein statistics (with Einstein)|बोस–आइंस्टीन सांख्यिकी (आइंस्टीन के साथ)|S. N. Bose|एस. एन. बोस
Chandrasekhar Limit|चंद्रशेखर सीमा|S. Chandrasekhar|एस. चंद्रशेखर
""", "Who is credited with the discovery/invention of {k}?", "{k} की खोज/आविष्कार का श्रेय किसे दिया जाता है?")

# ---------------- SCIENCE TABLES ----------------
T("SCI", "DIS", """
Vitamin A|विटामिन A|Night blindness|रतौंधी
Vitamin B1 (Thiamine)|विटामिन B1 (थायमिन)|Beriberi|बेरीबेरी
Vitamin B3 (Niacin)|विटामिन B3 (नायसिन)|Pellagra|पेलाग्रा
Vitamin B12|विटामिन B12|Pernicious anaemia|पर्निशियस एनीमिया
Vitamin C|विटामिन C|Scurvy|स्कर्वी
Vitamin D|विटामिन D|Rickets|रिकेट्स
Vitamin K|विटामिन K|Delayed blood clotting|रक्त का देर से थक्का जमना
Iodine|आयोडीन|Goitre|घेंघा
Iron|लोहा|Anaemia|रक्ताल्पता (एनीमिया)
Protein|प्रोटीन|Kwashiorkor|क्वाशियोरकर
""", "Deficiency of {k} causes which disease?", "{k} की कमी से कौन-सा रोग होता है?",
  "{v} is caused by the deficiency of:", "{v} किसकी कमी से होता है?")

T("SCI", "TYPE", """
Tuberculosis|क्षय रोग (टीबी)|Bacteria|जीवाणु
Cholera|हैज़ा|Bacteria|जीवाणु
Typhoid|टायफाइड|Bacteria|जीवाणु
Tetanus|टेटनस|Bacteria|जीवाणु
Diphtheria|डिप्थीरिया|Bacteria|जीवाणु
Leprosy|कुष्ठ रोग|Bacteria|जीवाणु
Plague|प्लेग|Bacteria|जीवाणु
Malaria|मलेरिया|Protozoa|प्रोटोजोआ
Amoebiasis|अमीबियासिस|Protozoa|प्रोटोजोआ
Kala-azar|काला-अज़ार|Protozoa|प्रोटोजोआ
Sleeping sickness|निद्रा रोग|Protozoa|प्रोटोजोआ
Polio|पोलियो|Virus|विषाणु
Measles|खसरा|Virus|विषाणु
Dengue|डेंगू|Virus|विषाणु
Rabies|रेबीज़|Virus|विषाणु
Chickenpox|चेचक (छोटी माता)|Virus|विषाणु
Mumps|कण्ठमाला|Virus|विषाणु
Influenza|इन्फ्लुएंज़ा|Virus|विषाणु
Hepatitis B|हेपेटाइटिस B|Virus|विषाणु
AIDS|एड्स|Virus|विषाणु
Ringworm|दाद|Fungus|कवक
Athlete's foot|एथलीट फुट|Fungus|कवक
""", "{k} is caused by:", "{k} किसके कारण होता है?")

T("SCI", "UNIT", """
Force|बल|Newton|न्यूटन
Energy|ऊर्जा|Joule|जूल
Power|शक्ति|Watt|वाट
Pressure|दाब|Pascal|पास्कल
Frequency|आवृत्ति|Hertz|हर्ट्ज़
Electric current|विद्युत धारा|Ampere|एम्पियर
Electrical resistance|विद्युत प्रतिरोध|Ohm|ओम
Electric charge|विद्युत आवेश|Coulomb|कूलॉम
Potential difference|विभवांतर|Volt|वोल्ट
Capacitance|धारिता|Farad|फैराड
Magnetic flux density|चुंबकीय क्षेत्र (फ्लक्स घनत्व)|Tesla|टेस्ला
Inductance|प्रेरकत्व|Henry|हेनरी
Radioactivity|रेडियोधर्मिता|Becquerel|बेकरेल
Luminous intensity|ज्योति तीव्रता|Candela|कैंडेला
Amount of substance|पदार्थ की मात्रा|Mole|मोल
Thermodynamic temperature|ऊष्मागतिक तापमान|Kelvin|केल्विन
Work|कार्य|Joule|जूल
Loudness of sound|ध्वनि की प्रबलता|Decibel|डेसिबल
Illuminance|प्रदीप्ति|Lux|लक्स
Magnetic flux|चुंबकीय फ्लक्स|Weber|वेबर
Absorbed radiation dose|अवशोषित विकिरण मात्रा|Gray|ग्रे
Plane angle|समतल कोण|Radian|रेडियन
""", "What is the SI unit of {k}?", "{k} का SI मात्रक क्या है?")

T("SCI", "MEAS", """
Barometer|बैरोमीटर|Atmospheric pressure|वायुमंडलीय दाब
Thermometer|थर्मामीटर|Temperature|तापमान
Hygrometer|आर्द्रतामापी (हाइग्रोमीटर)|Humidity|आर्द्रता
Anemometer|पवन वेगमापी (एनीमोमीटर)|Wind speed|पवन की गति
Seismograph|भूकंपमापी (सिस्मोग्राफ)|Earthquake intensity|भूकंप की तीव्रता
Hydrometer|हाइड्रोमीटर|Specific gravity of liquids|द्रवों का आपेक्षिक घनत्व
Lactometer|लैक्टोमीटर|Purity of milk|दूध की शुद्धता
Sphygmomanometer|रक्तदाबमापी|Blood pressure|रक्तचाप
Ammeter|एम्मीटर|Electric current|विद्युत धारा
Voltmeter|वोल्टमीटर|Potential difference|विभवांतर
Altimeter|उन्नतिमापी|Altitude|ऊँचाई
Odometer|ओडोमीटर|Distance travelled by a vehicle|वाहन द्वारा तय की गई दूरी
Pyrometer|पायरोमीटर|Very high temperatures|बहुत उच्च तापमान
Rain gauge|वर्षामापी|Rainfall|वर्षा
Photometer|फोटोमीटर|Light intensity|प्रकाश की तीव्रता
Salinometer|सैलिनोमीटर|Salinity|लवणता
""", "What does a {k} measure?", "{k} किसे मापता है?",
  "Which instrument is used to measure {v}?", "{v} मापने के लिए किस यंत्र का उपयोग किया जाता है?")

T("SCI", "HOR", """
Pancreas|अग्न्याशय|Insulin|इंसुलिन
Thyroid|थायरॉइड|Thyroxine|थायरॉक्सिन
Adrenal|अधिवृक्क|Adrenaline|एड्रेनालिन
Pituitary|पीयूष|Growth hormone|वृद्धि हार्मोन
Pineal|पीनियल|Melatonin|मेलाटोनिन
Testis|वृषण|Testosterone|टेस्टोस्टेरोन
Ovary|अंडाशय|Oestrogen|एस्ट्रोजन
Parathyroid|पैराथायरॉइड|Parathormone|पैराथॉर्मोन
""", "Which hormone is secreted by the {k} gland (or organ)?", "{k} ग्रंथि (या अंग) से कौन-सा हार्मोन स्रावित होता है?",
  "{v} is secreted by which gland?", "{v} किस ग्रंथि से स्रावित होता है?")

T("SCI", "SYM", """
Hydrogen|हाइड्रोजन|H|H
Helium|हीलियम|He|He
Lithium|लिथियम|Li|Li
Carbon|कार्बन|C|C
Nitrogen|नाइट्रोजन|N|N
Oxygen|ऑक्सीजन|O|O
Fluorine|फ्लोरीन|F|F
Neon|नियॉन|Ne|Ne
Sodium|सोडियम|Na|Na
Magnesium|मैग्नीशियम|Mg|Mg
Aluminium|एल्युमिनियम|Al|Al
Silicon|सिलिकॉन|Si|Si
Phosphorus|फॉस्फोरस|P|P
Sulphur|सल्फर|S|S
Chlorine|क्लोरीन|Cl|Cl
Argon|आर्गन|Ar|Ar
Potassium|पोटैशियम|K|K
Calcium|कैल्शियम|Ca|Ca
Iron|लोहा|Fe|Fe
Copper|ताँबा|Cu|Cu
Zinc|जस्ता|Zn|Zn
Silver|चाँदी|Ag|Ag
Gold|सोना|Au|Au
Mercury|पारा|Hg|Hg
Lead|सीसा|Pb|Pb
Tin|टिन|Sn|Sn
Platinum|प्लैटिनम|Pt|Pt
Nickel|निकल|Ni|Ni
Iodine|आयोडीन|I|I
Uranium|यूरेनियम|U|U
Tungsten|टंगस्टन|W|W
Boron|बोरॉन|B|B
Bromine|ब्रोमीन|Br|Br
Cobalt|कोबाल्ट|Co|Co
Chromium|क्रोमियम|Cr|Cr
Manganese|मैंगनीज़|Mn|Mn
Titanium|टाइटेनियम|Ti|Ti
""", "What is the chemical symbol of {k}?", "{k} का रासायनिक प्रतीक क्या है?",
  "'{v}' is the chemical symbol of which element?", "'{v}' किस तत्व का रासायनिक प्रतीक है?")

T("SCI", "FORM", """
Water|जल|H<sub>2</sub>O|H<sub>2</sub>O
Carbon dioxide|कार्बन डाइऑक्साइड|CO<sub>2</sub>|CO<sub>2</sub>
Common salt|साधारण नमक|NaCl|NaCl
Ammonia|अमोनिया|NH<sub>3</sub>|NH<sub>3</sub>
Methane|मीथेन|CH<sub>4</sub>|CH<sub>4</sub>
Sulphuric acid|सल्फ्यूरिक अम्ल|H<sub>2</sub>SO<sub>4</sub>|H<sub>2</sub>SO<sub>4</sub>
Hydrochloric acid|हाइड्रोक्लोरिक अम्ल|HCl|HCl
Nitric acid|नाइट्रिक अम्ल|HNO<sub>3</sub>|HNO<sub>3</sub>
Baking soda|खाने का सोडा|NaHCO<sub>3</sub>|NaHCO<sub>3</sub>
Caustic soda|कॉस्टिक सोडा|NaOH|NaOH
Quick lime|बिना बुझा चूना|CaO|CaO
Slaked lime|बुझा हुआ चूना|Ca(OH)<sub>2</sub>|Ca(OH)<sub>2</sub>
Limestone|चूना पत्थर|CaCO<sub>3</sub>|CaCO<sub>3</sub>
Ozone|ओज़ोन|O<sub>3</sub>|O<sub>3</sub>
Glucose|ग्लूकोज़|C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>|C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>
Laughing gas|हँसाने वाली गैस|N<sub>2</sub>O|N<sub>2</sub>O
Bleaching powder|ब्लीचिंग पाउडर|CaOCl<sub>2</sub>|CaOCl<sub>2</sub>
Hydrogen peroxide|हाइड्रोजन परॉक्साइड|H<sub>2</sub>O<sub>2</sub>|H<sub>2</sub>O<sub>2</sub>
Acetic acid|एसिटिक अम्ल|CH<sub>3</sub>COOH|CH<sub>3</sub>COOH
Urea|यूरिया|CO(NH<sub>2</sub>)<sub>2</sub>|CO(NH<sub>2</sub>)<sub>2</sub>
Marble|संगमरमर|CaCO<sub>3</sub>|CaCO<sub>3</sub>
Rust (iron oxide)|जंग (आयरन ऑक्साइड)|Fe<sub>2</sub>O<sub>3</sub>|Fe<sub>2</sub>O<sub>3</sub>
""", "What is the chemical formula of {k}?", "{k} का रासायनिक सूत्र क्या है?")

# ---------------- SPORTS TABLES ----------------
T("STA", "SPORT", """
Ranji Trophy|रणजी ट्रॉफी|Cricket|क्रिकेट
Duleep Trophy|दलीप ट्रॉफी|Cricket|क्रिकेट
Irani Cup|ईरानी कप|Cricket|क्रिकेट
Thomas Cup|थॉमस कप|Badminton|बैडमिंटन
Uber Cup|उबर कप|Badminton|बैडमिंटन
Davis Cup|डेविस कप|Tennis|टेनिस
Santosh Trophy|संतोष ट्रॉफी|Football|फुटबॉल
Durand Cup|डूरंड कप|Football|फुटबॉल
Agha Khan Cup|आगा खान कप|Hockey|हॉकी
Beighton Cup|बेटन कप|Hockey|हॉकी
Walker Cup|वॉकर कप|Golf|गोल्फ
Ryder Cup|राइडर कप|Golf|गोल्फ
Swaythling Cup|स्वेथलिंग कप|Table Tennis|टेबल टेनिस
Bledisloe Cup|ब्लेडिस्लो कप|Rugby|रग्बी
Sultan Azlan Shah Cup|सुल्तान अज़लान शाह कप|Hockey|हॉकी
Subroto Cup|सुब्रतो कप|Football|फुटबॉल
""", "The {k} is associated with which sport?", "{k} किस खेल से संबंधित है?")

T("STA", "SPORT", """
Love|लव|Tennis|टेनिस
Deuce|ड्यूस|Tennis|टेनिस
Birdie|बर्डी|Golf|गोल्फ
Bogey|बोगी|Golf|गोल्फ
Googly|गुगली|Cricket|क्रिकेट
Yorker|यॉर्कर|Cricket|क्रिकेट
Maiden over|मेडन ओवर|Cricket|क्रिकेट
Slam dunk|स्लैम डंक|Basketball|बास्केटबॉल
Scrum|स्क्रम|Rugby|रग्बी
Checkmate|चेकमेट|Chess|शतरंज
Bully|बुली|Hockey|हॉकी
Penalty corner|पेनल्टी कॉर्नर|Hockey|हॉकी
Shuttlecock|शटलकॉक|Badminton|बैडमिंटन
Offside|ऑफसाइड|Football|फुटबॉल
Free throw|फ्री थ्रो|Basketball|बास्केटबॉल
Lunge|लंज|Fencing|तलवारबाज़ी
Raider|रेडर|Kabaddi|कबड्डी
Pole vault|पोल वॉल्ट|Athletics|एथलेटिक्स
Spike|स्पाइक|Volleyball|वॉलीबॉल
Gambit|गैम्बिट|Chess|शतरंज
""", "The term '{k}' is used in which sport?", "'{k}' शब्द किस खेल में प्रयुक्त होता है?")
