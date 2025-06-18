# Discourse forum

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-04-10 07:52:12
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1)

Mock Exam: Tools in Data Science
The end term and the mock has been created using the TDS GPT Assistant. Since the GPT has ALL the GAs, Course Content Modules, Live Session Transcriptions (its works like RAG), it is really able to help you prepare for the end term. Use it!
Therefore you can also create your own mocks.

  
      

      ChatGPT
  

  
    

ChatGPT - IITM TDS Teaching Assistant

  TA for IIT Madras' Data Science course, guiding students with questions.


  

  
    
    
  

  


Below are variant questions across various topics relevant to the course. These questions have been curated from the topics areas we are focussing on. Therefore it will be very similar in content to the end term.

What it does not contain: Scenario based questions. These are complex to construct. We will address the topics for these questions in the live session.


LLMs
Pandas
Git, Docker, Bash


Q1: HTTP Method Semantics
Which HTTP method is not idempotent, meaning repeated identical requests may result in different outcomes each time?

A. GET
B. PUT
C. POST
D. DELETE

Answer: C. POST
Q2: IDE Features
Which feature is least likely to be found in a standard code editor or IDE?

A. Code formatting tools
B. Integrated terminal
C. Git integration
D. Cloud hosting of Docker containers

Answer: D. Cloud hosting of Docker containers
Q3: Pandas Summary Methods
You have a DataFrame with a region column. To get a quick summary of how many entries are in each region, which method is most useful?

A. df.describe()
B. df[“region”].value_counts()
C. df.count()
D. df.groupby(“region”).sum()

Answer: B. df[“region”].value_counts()
Q4: Python Exception Scope
You want to safely open a file, handle any errors, and ensure the file is always closed in Python. Which pattern should you use?

A. try: open(...) then finally: close()
B. open() and then except
C. open() and then raise
D. Use with open(...) as f: block

Answer: D. Use with open(...) as f: block
Q5: Chrome DevTools - Debugging
A frontend developer wants to trace JavaScript function calls step-by-step. Which Chrome DevTools panel should they use?

A. Console
B. Application
C. Sources
D. Elements

Answer: C. Sources
Q6: Data Cleaning Tools
You are cleaning survey responses and want to automatically match similar text entries like “NYC”, “New York City”, and “newyorkcity”. Which approach/tool would be most effective?

A. TRIM() in Excel
B. Manual Find and Replace
C. Fuzzy matching or clustering in OpenRefine
D. COUNTIF()

Answer: C. Fuzzy matching or clustering in OpenRefine
Q7: Geospatial Libraries
Which pair of Python libraries is best suited for geospatial analysis and rendering static maps?

A. pandas and seaborn
B. geopandas and matplotlib
C. folium and flask
D. sklearn and dash

Answer: B. geopandas and matplotlib
Q8: Statistical Significance
A psychologist tests if a training program changes memory performance and finds a p-value of 0.08. What can be concluded at the 0.05 significance level?

A. The result is highly significant
B. The null hypothesis must be rejected
C. There is insufficient evidence to reject the null hypothesis
D. The program is proven to work

Answer: C. There is insufficient evidence to reject the null hypothesis
Q9: Purpose of Kumu
What is a key use case for a tool like Kumu?

A. Animating time series
B. Designing deep learning models
C. Visualizing stakeholder networks and system relationships
D. Performing statistical analysis

Answer: C. Visualizing stakeholder networks and system relationships
Q10: DevTools Performance Diagnostics
To diagnose a slow webpage, you want to analyze scripts, rendering times, and long tasks. Which DevTools panel provides a timeline-based view?

A. Elements
B. Performance
C. Network
D. Lighthouse

Answer: B. Performance
Q11: Git Configuration
Which of the following files helps configure a Git project’s name, email, and default branch?

A. .gitignore
B. .gitattributes
C. .git/config
D. README.md

Answer: C. .git/config
Q13: Safe HTTP Method
Which HTTP method is considered safe, meaning it is only used for retrieval and must not change server state?

A. GET
B. DELETE
C. PATCH
D. POST

Answer: A. GET
Q14: Deduplicating Text Entries
A dataset has entries like “IBM”, “I.B.M.”, and “International Business Machines”. What is the best tool to cluster these for cleaning?

A. Excel TRIM
B. OpenRefine using key collision or fingerprinting
C. pandas merge()
D. CONCATENATE()

Answer: B. OpenRefine using key collision or fingerprinting
Q15: Geospatial + Interactive Mapping
A conservation biologist wants to visualize real-time animal tracking data on an interactive map. Which libraries would be best?

A. geopandas and plotly
B. folium and pandas
C. seaborn and shapely
D. rasterio and altair

Answer: B. folium and pandas
Q16: Pandas - Filtering Unique Entries
You have a DataFrame of customer orders and want to list only those customers who ordered once. Which Pandas method chain is most suitable?

A. df.groupby(“customer”).sum()
B. df[“customer”].value_counts() == 1
C. df.drop_duplicates()
D. df[“customer”].nunique()

Answer: B. df[“customer”].value_counts() == 1
Q17: Purpose of Kumu in System Design
How does Kumu help in system design or stakeholder mapping?

A. Organizing spreadsheets
B. Identifying leverage points in complex systems through visual maps
C. Rendering line graphs
D. Sending notifications

Answer: B. Identifying leverage points in complex systems through visual maps
Q18: Python Exception - Multiple Handlers
Which structure allows Python to handle different types of exceptions separately?

A. try…finally
B. if…else
C. Multiple except blocks
D. Nested try blocks

Answer: C. Multiple except blocks
Q19: Understanding Statistical Power
If a study has low statistical power, what is most likely to occur?

A. False positive (Type I error)
B. False negative (Type II error)
C. Confounding
D. Multicollinearity

Answer: B. False negative (Type II error)
Q20: Git Basics - Staging Area
Which Git command moves modified files to the staging area?

A. git push
B. git add
C. git fetch
D. git init

Answer: B. git add
Q21: Chrome DevTools - Local Storage
Where can you inspect local storage items (e.g. tokens, preferences) in Chrome DevTools?

A. Console
B. Application > Local Storage
C. Elements
D. Sources

Answer: B. Application > Local Storage
Q22: Chrome DevTools - JS Performance
Which DevTools feature helps measure execution time of scripts and CPU usage?

A. Console
B. Network
C. Performance
D. Application

Answer: C. Performance
Q23: Excel Data Import - Scientific Notation Issue
You import a CSV file where product IDs like "1E10" are being interpreted as scientific notation in Excel. What is the best way to preserve these IDs as text?

A. Format the column as General
B. Use =TEXT(A1, "0") after import
C. Set column format to Text during import or Text-to-Columns
D. Change regional settings

Answer: C. Set column format to Text during import or Text-to-Columns

Module: Everyday Tools
Q1: Spreadsheet Functions
You have a dataset in Excel where column A contains full names in the format “Last Name, First Name”. Which function can you use to extract the first name into a separate column?

A. =LEFT(A1, FIND(",", A1)-1)
B. =RIGHT(A1, LEN(A1) - FIND(",", A1))
C. =MID(A1, FIND(",", A1)+2, LEN(A1))
D. =SPLIT(A1, ",")

Answer: C — The MID function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

Module: Data Sourcing
Q2: Web Scraping Ethics
When performing web scraping to collect data, which of the following practices is considered unethical?

A. Respecting the website’s robots.txt file.
B. Sending requests at a rate that mimics human browsing behavior.
C. Scraping data from a website that requires login without permission.
D. Citing the source of the data collected.

Answer: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

Module: Data Preparation
Q3: Handling Missing Data
In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally not appropriate for handling these missing values?

A. Replacing missing values with the mean age.
B. Deleting rows with missing age values.
C. Replacing missing values with a fixed age, such as 0.
D. Leaving the missing values as they are without any action.

Answer: D — Leaving missing values unaddressed can lead to errors in analysis and modeling. Options A, B, and C are common strategies for handling missing data, depending on the context and the extent of the missingness.

Module: Data Analysis
Q4: Statistical Measures
Which of the following statistical measures is not sensitive to extreme values (outliers) in a dataset?

A. Mean
B. Median
C. Standard Deviation
D. Range

Answer: B — The median represents the middle value of a dataset and is not affected by outliers. In contrast, the mean, standard deviation, and range can be significantly influenced by extreme values.

Module: Large Language Models
Q5: Tokenization in NLP
In Natural Language Processing, what is the primary purpose of tokenization?

A. To translate text from one language to another.
B. To split text into individual words or subwords.
C. To encrypt text for secure communication.
D. To summarize large texts into shorter versions.

Answer: B — Tokenization involves breaking down text into smaller components, such as words or subwords, which can then be processed by language models. This is a fundamental step in NLP tasks.

Module: Geospatial and Network Analysis
Q6: Geographic Coordinate Systems
Which of the following coordinate systems is commonly used to represent locations on Earth’s surface?

A. Cartesian Coordinate System
B. Polar Coordinate System
C. Geographic Coordinate System (Latitude and Longitude)
D. Cylindrical Coordinate System

Answer: C — The Geographic Coordinate System uses latitude and longitude to specify locations on Earth’s surface. This system is widely used in geospatial analysis.

Module: Data Visualization
Q7: Effective Data Visualization
When creating a bar chart to compare the sales performance of different products, which practice should be avoided?

A. Ordering bars from highest to lowest value.
B. Using different colors for each bar without a legend.
C. Starting the y-axis at zero.
D. Labeling each bar with its exact value.

Answer: B — Using different colors for each bar without a legend can confuse the audience, as they may assume the colors represent different categories. Consistency and clarity are key in effective data visualization.

Module: Everyday Tools
Q8: VS Code Feature Use
You are editing a Python script in Visual Studio Code and want to quickly find and edit all occurrences of a variable name in the current file. What feature should you use?

A. Git integration
B. Debug panel
C. Multi-cursor editing
D. Terminal commands

Answer: C — Multi-cursor editing allows you to place multiple cursors in a file and edit text in multiple locations at once. It is useful for refactoring variable names or repeated patterns.

Module: Data Sourcing
Q9: Data API Identification
Which of the following data sources is most likely to provide structured data accessible via an API?

A. A scanned PDF document
B. A screenshot of a chart
C. The World Bank data portal
D. A newspaper article

Answer: C — The World Bank data portal provides structured datasets accessible via APIs. The other options involve unstructured or image-based content not suitable for direct data access.

Module: Data Preparation
Q10: Data Type Conversion in Excel
You imported a CSV file into Excel, and one of the columns containing numbers is treated as text. What is the easiest way to convert it into numeric format?

A. Use the CONCAT function
B. Format the column as Text
C. Use the VALUE() function
D. Use SUBSTITUTE()

Answer: C — The VALUE function converts text that appears as numbers into actual numeric values. This is useful when data is imported with formatting issues.

Module: Data Analysis
Q11: Outlier Detection
You are analyzing a dataset of employee salaries. Which visualization is best for quickly identifying outliers?

A. Line chart
B. Box plot
C. Histogram
D. Pie chart

Answer: B — A box plot clearly shows the spread of data and highlights outliers as individual points beyond the whiskers.

Module: Large Language Models
Q12: Prompt Engineering Strategy
To get consistent, structured responses from a language model when extracting key information, which approach is most effective?

A. Ask the model to “summarize” the text
B. Use open-ended questions
C. Use system messages and JSON schema formatting
D. Provide only one-word inputs

Answer: C — System messages and structured output formats like JSON schemas guide the model to generate reliable and consistent structured responses.

Module: Geospatial and Network Analysis
Q13: Network Centrality
In a social network graph of coworkers, which metric best identifies the person who connects the most groups together?

A. Degree centrality
B. Closeness centrality
C. Betweenness centrality
D. Eigenvector centrality

Answer: C — Betweenness centrality measures how often a node appears on shortest paths between other nodes, highlighting connectors or “bridges” in the network.

Module: Data Visualization
Q14: Choosing the Right Chart
You want to show how the composition of a marketing budget changes across three years. Which visualization is most appropriate?

A. Pie charts for each year
B. Scatter plots
C. Stacked bar chart
D. Line chart

Answer: C — A stacked bar chart shows parts of a whole across different categories and time periods, making it easier to compare budget composition over years.

### 🖼 Image Descriptions

**Image 1**: That's the logo for the Japanese company, Kubota Corporation.

The logo is a stylized white design on a black background. It depicts a six-petaled flower-like shape, created from interlocked, curved lines. The lines are thick and create a sense of interwovenness or connection. The overall impression is one of unity, strength, and possibly technological precision.

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-04-10 07:55:57
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2)



---

## Jayaram (@22f3002723)
- **Posted on**: 2025-04-11 05:30:28
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4)

@carlton @Jivraj
any link for last term’s end term question answer

---

## Durga Prasad (@22f3001307)
- **Posted on**: 2025-04-11 08:45:48
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5)

quizpractice.space
  

  
    

Practise End Term Quiz Question Papers

  Practice with IITM's online BS degree question papers and quizzes to improve your preparation.

### 🖼 Image Descriptions

**Image 1**: That's a close-up shot of a blurry image showing the letters "QP" in white against a black background. 


Here's a breakdown of the image's characteristics:

* **Blurriness:** The letters are significantly out of focus, giving them a soft, hazy appearance.  The edges are not sharp.

* **Lighting:** The letters appear brighter than the background, suggesting a light source illuminating them.  There's a slight gradient within the letters themselves, with the centers slightly brighter than the edges.

* **Font:** The font style appears to be sans-serif, simple, and somewhat blocky.

* **Contrast:**  The contrast between the white letters and the black background is high, making the letters visible despite the blur.

* **Overall Impression:** The image gives the impression of being either a low-resolution scan, a purposely blurred image, or possibly a slightly defocused photograph.

**Image 2**: Here's a description of the image:

The image shows a split screen. 


On the left is a dark-themed advertisement for a website called "quizpractice.space". The ad features the website's logo (a stylized "QP"), the text "Practice Previous Question Papers" in a large, bold font, a cartoon graduate student icon, and the tagline "IITM Online BS Degree www.quizpractice.space" at the bottom. The ad is clean and simple, with a professional appearance.


The right side of the image displays a computer screen showing an online exam interface. The top bar shows the URL of the quizpractice.space website and a title that indicates a practice exam for an IITM Diploma. The exam is timed (00:09 on the clock) and shows a multiple-choice question requiring the matching of mathematical expressions with their boolean values (true/false/invalid) or results. Options are presented as multiple-choice answers below the question.  A question menu allows the user to jump to other questions in the exam. The buttons "Exam Mode" and "Practise" are visible, suggesting a way to choose between test conditions. "Submit Exam" and "View Details" buttons are visible at the bottom. The interface is also dark-themed.


Overall, the image is clear and well-lit, showcasing the advertisement and online exam platform concurrently. The contrast between the dark theme of the exam and the lighter background of the advertisement makes both stand out.

---

## Tushar Jalan  (@23f2003751)
- **Posted on**: 2025-04-11 19:56:15
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6)

So here is more questions in the form of a little quiz (shared by someone in the group,DM for Credit )
  

      gkmfrombs.github.io
  

  
    

Quiz from PDF



  

  
    
    
  

  


That has 350 questions if you don’t want to go through all of them(it’s pretty time consuming)
in that case just do this PDF.(This pdf contains all the questions that is a bit conceptual i would say and some questions which i failed to do  )

  

      accounts.google.com
  

  
    

Google Drive: Sign-in

  Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).


  

  
    
    
  

  


(If you know context to the pdf’s name,we are friends )
Thank you,
Kindeeesstt Regards,(hopefully the last post on discourse for TDS),
Tushar Jalan

### 🖼 Image Descriptions

**Image 1**: That's a digital image of a stylized emoticon, resembling a smiley face, surrounded by hearts. 


Here's a breakdown of the image:

* **The Smiley:** The central figure is a bright yellow, almost orange-yellow, smiley face. It has closed eyes, indicated by simple, slightly curved lines, suggesting contentment or happiness. The mouth is a wide, upward-curving smile.  There are light pink blushes on its cheeks. The overall style is reminiscent of a classic emoji but with a slightly softer, rounder look.

* **The Hearts:** Three red hearts of varying sizes and angles surround the smiley. They are positioned somewhat overlapping, one at the top right, one at the bottom left, and another at the bottom right. These hearts are glossy and have a slightly three-dimensional look.

* **The Background:** The background is a dark, blurry reddish color. It's not sharply defined, but rather a diffused red tone that provides contrast to the yellow of the smiley face and the red of the hearts.  The red extends behind and slightly under the smiley, not creating a perfectly sharp border.

* **Overall Style:** The overall style is cute, cheerful, and playful. The image is likely intended to convey feelings of love, happiness, or affection. The pixelated or slightly low-resolution style also gives it a slightly retro or playful feel.

**Image 2**: That's a digital image of an emoji. 


Here's a description:

* **The Emoji:** It's a yellow circle representing a face, with simple, black dot eyes and a small, upward-curving smile line.  A single, light-blue teardrop hangs from the left side of the face, seemingly dripping down.

* **Style:** The style is simple and cartoonish, typical of emojis used in digital communication. The lines are not highly detailed; they are smooth and rounded.

* **Background:** There's a slightly darker orange border or halo around the emoji, extending slightly beyond the yellow circle. This orange area is uneven, suggesting either a clipping artifact or intentional design choice.

* **Overall Impression:** The emoji conveys a feeling of bittersweet happiness – happy but with a hint of sadness or maybe even relief. The single tear adds a layer of complexity to the otherwise cheerful expression.

**Image 3**: That's a close-up shot of a smiling emoticon, specifically a variation of the classic yellow smiley face. 


Here's a breakdown of the image:

* **The Face:** The emoticon is a bright yellow circle, representing the face. It has a simple, cartoonish style.

* **The Eyes:** Two small, curved black lines form the eyes, suggesting a happy and slightly mischievous expression. They are positioned relatively close together.

* **The Mouth:** The mouth is a wide, slightly irregular grin. The teeth are prominently displayed, shown as small, white rectangles. This detailed representation of teeth contributes to a slightly more exaggerated and playful look compared to a simpler smile line.

* **The Background:** A portion of an orange background is visible at the edges, suggesting the emoticon is likely part of a larger image or digital context.


The overall impression is one of cheerful, almost goofy happiness. The exaggerated teeth add to the fun and playful nature of the emoji.

---

## Tanush Tambe (@22f3002248)
- **Posted on**: 2025-04-12 00:18:31
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7)

Thank you for your efforts
Thanks
Edit: Opened in incognito and it worked.

---

## Divjot Singh (@24ds3000061)
- **Posted on**: 2025-04-12 11:48:23
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8)

Hi @carlton please upload the recording of Thursday’s TDS session on the YouTube playlist

---

## VENKATESWARLU THATHA  (@Venkatesh_2k01)
- **Posted on**: 2025-04-12 12:00:50
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9)

@carlton sir i have done the 350 questions . i am able to answer 80% of the questions on my own, correctly. will end term also be similar to these questions? are pyqs any helpful ?

---

## Jivraj Singh Shekhawat (@Jivraj)
- **Posted on**: 2025-04-12 12:09:15
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10)

Live Session - TDS - 2025/04/10 20:00 GMT+05:30 - Recording - Google Drive
Access recording through this gdrive link

---

## Pranaav (@23f1002223)
- **Posted on**: 2025-04-13 02:26:36
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11)

Thank you for the questions sir.

---
