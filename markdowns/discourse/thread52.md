# Discourse forum

## Anand S (@s.anand)
- **Posted on**: 2025-01-31 16:13:36
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1)

Please post any questions related to Graded Assignment 4 - Data Sourcing.
Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.
Deadline: Sunday, February 9, 2025 6:29 PM
@Jivraj @Saransh_Saini @carlton

---

## Anand S (@s.anand)
- **Posted on**: 2025-01-31 16:14:00
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2)



---

## Guddu Kumar Mishra  (@22f3001315)
- **Posted on**: 2025-02-01 07:54:31
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3)

Screenshot 2025-02-01 132301331×314 12.3 KB
what is the error here?? sir @Jivraj

### 🖼 Image Descriptions

**Image 1**: That's a screenshot showing JSON data and a test result. 


Here's a breakdown:

* **The JSON Data:** The main part displays a JSON object, a standard data format used for web applications. It contains four key-value pairs:

    * `"id"`: `"tt7144296"` (likely an identifier)
    * `"title"`: `"1. Kiss and Kill"` (a title, possibly of a movie or show)
    * `"year"`: `2017` (a year)
    * `"rating"`: `2.9` (a numerical rating)

* **The Error Message:** Below the JSON data, there's a message indicating a test result:

    * `Error: Expected: 2.9 Actual: 2.9` This suggests a test was run to check if the "rating" value was 2.9. The test passed because the expected value and actual value are the same.

* **Overall:** The image likely comes from a software development or testing environment where the JSON data is being validated. The test confirms the JSON data contains the expected rating value.  The dark background with light text is a common style for code editors or debugging tools.

---

## Vikram Jeet (@24ds2000024)
- **Posted on**: 2025-02-01 18:26:06
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5)

I have the Same doubt.

---

## Anand S (@s.anand)
- **Posted on**: 2025-02-02 05:30:16
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6)

@22f3001315 @21f3002277 @24ds2000024 – please try again after reloading the page. The new error message will be clearer, like this:
Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

## Sakthivel S (@23f2000237)
- **Posted on**: 2025-02-02 05:41:42
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7)

In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?
edit:  This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

## Anand S (@s.anand)
- **Posted on**: 2025-02-02 05:45:48
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8)

@23f2000237 A good point. Yes, please include all titles. I’ve reworded the question accordingly. Thanks.

---

## VIKASH PRASAD (@21f3002277)
- **Posted on**: 2025-02-02 06:31:48
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9)

Q3. How to handle the error ? @Jivraj
TypeError: Cannot read properties of null (reading ‘0’)
http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}


error resolved

---

## Guddu Kumar Mishra  (@22f3001315)
- **Posted on**: 2025-02-02 10:06:04
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11)

in my output which is correct
there are two \n instead of one .

---

## VIKASH PRASAD (@21f3002277)
- **Posted on**: 2025-02-02 10:38:33
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12)

it should one(for newline), my code is working now

---

## Vikram Jeet (@24ds2000024)
- **Posted on**: 2025-02-02 11:54:35
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13)

Dear Sir,
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

## VIKASH PRASAD (@21f3002277)
- **Posted on**: 2025-02-02 13:00:36
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14)

Q4. How to handle the error ? @Jivraj
Error: At 2025-02-05: Values don’t match

---

## K Hari Prasath (@23f2003853)
- **Posted on**: 2025-02-03 00:37:01
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15)

There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)
image1920×1080 337 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a computer screen displaying a webpage for a graded assignment from the Indian Institute of Technology Madras (IIT Madras). 


Here's a breakdown of what's visible:

* **Top Browser Bar:** A standard browser window is visible at the top, showing the URL of the assignment page, which includes the course name ("ns_25t1_se2002") and assignment details. Standard browser controls (back, forward, refresh) are visible. The IIT Madras logo is present in the top left.

* **Left Sidebar:** A navigation sidebar lists modules of the course, including "Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," "Module 4: Data Sourcing," and "Graded Assignment 4."  "Grades" and "Calc" are also visible as menu options.

* **Main Content Area:** The bulk of the screen shows details about the "Graded Assignment 4." This includes:
    * **Due Date:** Clearly stated with date and time.
    * **Submission Policy:**  Indicates that multiple submissions are allowed before the deadline.
    * **Troubleshooting:** Provides a list of common issues that might prevent students from accessing the assignment, such as ad blockers, cookie blockers, specific browser requirements (Chrome recommended), and antivirus interference.  It also advises using mobile internet or a different network if problems persist.
    * **Student ID Requirement:** A crucial instruction to use the student ID for accessing the assignment.
    * **Assignment Link:** A direct link to the assignment is provided.

* **Bottom Taskbar:** A standard Windows taskbar is at the bottom, showing various applications.

* **Time and Language:** The system clock at the bottom right shows the time and date. The language setting is shown as "ENG".

The overall impression is a student's view of an online course assignment page, with clear instructions and troubleshooting information. The design is straightforward and functional.

---

## Sakthivel S (@23f2000237)
- **Posted on**: 2025-02-03 10:06:13
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16)

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?
(Assuming they have interacted in this thread)

---

## Anand S (@s.anand)
- **Posted on**: 2025-02-03 11:16:46
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17)

Anyone scoring 10/10 on GA4 and replying with a relevant message on this thread will get 11/10

### 🖼 Image Descriptions

**Image 1**: That's a digital image of a simple, happy emoticon or emoji. 


Here's a description:

* **Shape and Color:** It's a perfectly round yellow circle, representing a face. The yellow is a bright, slightly saturated shade.

* **Features:**  The emoji has two small, dark (almost black) dots for eyes, positioned relatively close together. The mouth is a simple, slightly upward-curving black line, indicating a subtle, contented smile. There are no other details, such as nose or eyebrows.

* **Style:** The style is minimalist and flat; there's no shading or texturing to create depth or dimension. The lines are clean and simple.  The image resolution appears relatively low, resulting in a slightly pixelated look.

The overall impression is one of simple, uncomplicated happiness.

---

## K Hari Prasath (@23f2003853)
- **Posted on**: 2025-02-03 11:38:10
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18)

For me I just made filter of rating between 2 and 7 in site and typed in console as per  video. with that data got in console worked fine.
copy the coding and save in place use it for data extract when finally submit

---

## Maheshwar Ture (@22f2000113)
- **Posted on**: 2025-02-03 16:46:46
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19)

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name
image1414×295 19 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a screenshot of a search interface, likely from a website or application. 


Here's a breakdown:

* **Left Side (Search Filters):** This section contains search filters with the heading "Search filters" prominently displayed at the top. There's a button labeled "Expand all" with a downward-pointing arrow. Below this are two filter options:
    * "Title name" with a text input field where "Un matrimonio di troppo" (Italian for "A marriage too much") is already typed in.
    * "Title type" with a dropdown arrow indicating further options are available but not currently displayed.


* **Right Side (Search Results):** This area shows a large, empty space with a prominent message: "No results found". Below this is a suggestion: "Please adjust your filters or start a new search". A greyed-out magnifying glass icon with a cross over it is placed above this message.


The overall style is clean and minimalistic, typical of modern web interfaces. The color scheme is light, mostly white and light grey.  The language suggests the search interface may be in Italian.

---

## Nilay Chugh (@nilaychugh)
- **Posted on**: 2025-02-04 03:28:57
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20)

how to get the BBC weather API key?

---

## Joel Jeffrey (@JoelJeffrey)
- **Posted on**: 2025-02-04 05:47:12
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21)

Just a quick query on the Bonus mark.
Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

## Anand S (@s.anand)
- **Posted on**: 2025-02-04 06:15:20
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22)

@JoelJeffrey It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---
