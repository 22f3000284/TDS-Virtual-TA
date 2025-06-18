# Discourse forum

## Jivraj Singh Shekhawat (@Jivraj)
- **Posted on**: 2025-03-06 13:48:39
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1)

Please post any questions related to Graded Assignment 6 - Data Analysis
Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.
Deadline 2025-03-15T18:30:00Z

---

## Jivraj Singh Shekhawat (@Jivraj)
- **Posted on**: 2025-03-06 13:49:29
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2)



---

## Lovepreet Singh (@24f2006061)
- **Posted on**: 2025-03-02 11:45:12
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3)

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?
@carlton

---

## Sarang Tambe (@23f2005138)
- **Posted on**: 2025-03-02 11:57:04
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4)

@Jivraj @Saransh_Saini
I have similar concern
For Q1, I used the following code:
print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

And got the following output:
Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

Whereas options are below where none of them are correct.
image281×219 9.1 KB
Whereas for Q2 (Punjab and Yamaha) I used the following code:
print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

and got the following answers:
Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).
image278×216 9.19 KB

### 🖼 Image Descriptions

**Image 1**: That's an image of a multiple-choice question, likely from a software interface or online test. 


Here's a breakdown of the image:

* **Format:** The question presents four options, each preceded by a radio button (a small circle). Only one radio button can be selected. 

* **Content:** Each option consists of a string of text in the format: `'Attribute: Value'`.  The attributes are:

    * `Mileage` (appearing twice with different values)
    * `AvgDistance`
    * `EngineCapacity`

    The values associated with each attribute are numerical and include both positive (0.95, 0.21, 0.17) and negative (-0.05) numbers.

* **Selection:** One option, `'AvgDistance: -0.05'`, is already selected, as indicated by the filled-in radio button.

* **Context:** The context is unclear, but the data suggests that these might be correlation coefficients or some other statistical measure related to vehicle attributes (mileage, average distance traveled, engine capacity).  The negative value (-0.05) suggests a weak negative correlation.

**Image 2**: That's a close-up shot of a computer screen displaying a multiple-choice question or selection interface. 


Here's a breakdown of the image:

* **Format:** The interface presents four options, each preceded by a radio button (a small circle). Only one radio button can be selected at a time.

* **Options:** Each option consists of a string of text in the format of "Key: Value," where:
    * "Key" is a descriptive label like 'Mileage', 'AvgDistance', or 'EngineCapacity'.
    * "Value" is a numerical value, which could represent a measurement or some other quantifiable data.  These values include positive and negative decimals.

* **Selection:** One of the options ('Mileage: 0.24') has a filled-in radio button, indicating it's the currently selected choice.

* **Appearance:** The text is clear and easily readable, likely rendered using a standard computer font. The background is plain and uncluttered.  The radio buttons are typical of graphical user interfaces.

In essence, the image shows a part of a user interface where a user must choose one option from a list, based on the provided key-value pairs. The context suggests this might be part of a data analysis or a configuration setting.

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-03-04 10:11:22
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5)

@24f2006061 We are looking into it. We will update based on our analysis. Thanks for letting us know.
Kind regards

---

## Abhinav (@AbhinavOhri)
- **Posted on**: 2025-03-03 18:06:51
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6)

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one
image1383×263 25 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a multiple-choice question with four options. 


The question is a business case study asking to identify the key factor influencing the resale value of Yamaha motorcycles in Delhi, India. The factors considered are mileage, average daily distance traveled, and engine capacity. The analysis uses the Pearson Correlation Coefficient, and price retention is calculated as (resale price / original price).


The four options present Pearson Correlation Coefficients for each factor:

* **'Mileage: 0.01'**
* **'AvgDistance: 0.00'**
* **'EngineCapacity: 0.13'** (This option is marked as the correct answer.)
* **'EngineCapacity: 0.95'**


The question is worth 1 point. The overall style is that of an online assessment or quiz.

---

## Wasim Ansari (@24ds3000090)
- **Posted on**: 2025-03-07 17:12:28
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7)

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. @carlton @Jivraj @Saransh_Saini

---

## Shashannk (@23f2003413)
- **Posted on**: 2025-03-08 15:17:03
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8)

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out @carlton !

---

## RAJ K BOOPATHI (@23ds2000092)
- **Posted on**: 2025-03-10 07:56:14
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9)

I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---

## Pradeep Mondal (@21f2000709)
- **Posted on**: 2025-03-11 06:42:12
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10)

Any updates on these? I am too facing the same issue.
@carlton @Jivraj @Saransh_Saini

---

## Udipth (@Udipth)
- **Posted on**: 2025-03-11 17:42:32
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11)

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one
image2083×575 47.6 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a multiple-choice question with four options related to a statistical analysis of motorcycle resale value. 


Here's a breakdown:

* **Question:** The question describes a scenario where a strategic consultant needs to analyze factors influencing the resale value of Yamaha motorcycles in Maharashtra, India.  The consultant must use the Pearson Correlation Coefficient to determine the relationship between mileage, average daily distance traveled, and engine capacity, and the percentage of price retention (resale price/original price).

* **Options:** Four options are presented, each showing a variable and its corresponding Pearson Correlation Coefficient:
    * 'AvgDistance: 0.09'
    * 'Mileage: 0.95'
    * 'EngineCapacity: -0.02'
    * 'Mileage: 0.12'

* **Correct Answer:** The correct answer is implicitly 'Mileage: 0.95' because this shows a strong positive correlation between mileage and price retention. The question is asking for the impact of these variables, and a correlation of 0.95 is the strongest positive relationship.  The other values demonstrate either weak or negative correlations.


* **Visual Aspects:** The question and options are presented in a clean, simple layout typical of an online quiz or test. The options are presented as radio buttons, indicating that only one choice can be selected.  The point value of the question (1 point) is clearly visible.

---

## Shashannk (@23f2003413)
- **Posted on**: 2025-03-12 03:42:05
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12)

Kindly update us regarding the status of Q1 & Q2 @carlton @Jivraj

---

## LAKSHAY (@lakshaygarg654)
- **Posted on**: 2025-03-12 11:29:04
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13)

@Jivraj @carlton @Saransh_Saini
Dear TDS Team,
There are multiple issues in Graded Assignment 6 that require urgent attention:

Questions 1 and 2, along with their options, are ambiguous.
In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.
Thank you for your support.

---

## Pradeep Mondal (@21f2000709)
- **Posted on**: 2025-03-12 13:30:00
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14)

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.
For instance:

forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

---

## LAKSHAY (@lakshaygarg654)
- **Posted on**: 2025-03-12 14:11:15
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15)

Let’s wait for their response.
I submitted nearby option for Q3 and Q4

---

## Vivek Rekha Ashoka (@23f3001745)
- **Posted on**: 2025-03-12 14:36:43
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16)

@Jivraj @carlton @Saransh_Saini
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).
Thanks

---

## Jivraj Singh Shekhawat (@Jivraj)
- **Posted on**: 2025-03-13 09:47:03
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17)

Hi @all
Question intends you to select most correlated one.
Select option which is absolute highest.

---

## M v Sunil (@Sunil_mv)
- **Posted on**: 2025-03-14 14:30:12
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18)

@Jivraj  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---

## Shashank Tripathi (@23f3001601)
- **Posted on**: 2025-03-14 16:06:48
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19)

image1318×377 34.2 KB
what to do if 3 options have same value -0.04 and all are correct?

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a multiple-choice question within a larger context. 


**The Question:** The question stem describes a scenario where a strategic consultant is analyzing factors influencing motorcycle resale value in Maharashtra for a premium Honda dealership. They're using Pearson's Correlation Coefficient and calculating price retention as (resale price/original price). The goal is to identify which factor among mileage, average daily distance, and engine capacity has the strongest correlation with price retention.

**The Options:** Four options are presented, each showing a factor and its correlation coefficient:

* 'AvgDistance: -0.04'
* 'AvgDistance: 0.95'
* 'EngineCapacity: -0.04'
* 'Mileage: -0.04'

A radio button is placed before each option.  The option "Mileage: -0.04" is selected (indicated by a filled-in circle).


**Overall Presentation:** The text is clear and well-formatted, suggesting it's part of an online quiz or assessment. The question is detailed and requires a good understanding of correlation coefficients and their interpretation. The use of radio buttons implies that only one answer is correct.

---

## Khushi Shah (@23f2005471)
- **Posted on**: 2025-03-15 05:54:10
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20)

@carlton @Jivraj
My question 7 for GA6 is :
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance
Whose options provided are :
10418 meters
12287 meters
10965 meters
11149 meters
However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)
I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)
Kindly look into the question, and let me know about the same (the destination from central command post)

---
