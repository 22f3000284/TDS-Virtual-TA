# Discourse forum

## Muskan Aggarwal (@muskan2431)
- **Posted on**: 2025-02-21 18:32:17
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/1](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/1)

image1337×683 31.9 KB
It seems that the question in Graded Assignment 5 for TDS is producing incorrect results despite the same logic working correctly for other variations of the problem. Please check into this question once as I have cross checked with many of the students and chatgpt and all of us faced  this issue in this question. Thanks!
@carlton @s.anand
code to take reference from:
import gzip
import pandas as pd
from datetime import datetime

log_path = 's-anand.net-May-2024.gz'
start_time = datetime.strptime('01:00:00', '%H:%M:%S').time()
end_time = datetime.strptime('15:00:00', '%H:%M:%S').time()
log_data = []

def parse_log(line):
    parts = line.split(' ')
    log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
    method, url, status = parts[5][1:], parts[6], int(parts[8])
    return log_time, method, url, status

with gzip.open(log_path, 'rt') as file:
    for entry in file:
        log_time, method, url, status = parse_log(entry)
        if method == 'GET' and url.startswith('/blog/') and 200 
ps: I shared code after the deadline hopefully no issues there!

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a problem statement and solution input box related to data analysis. 


Here's a breakdown:

* **Problem Statement:** The top section describes a data set with fields like IP address, remote logname, request time, HTTP request details (method, URL, protocol), status code, response size, referer URL, user agent, virtual host, and server IP. It clarifies that the data is space-separated, double-quote enclosed, and uses backslash escapes for quotes within fields.  The data is in GMT-0500 timezone.  The problem asks to determine the number of successful GET requests (HTTP status codes 200-299) made to pages under the `/blog/` path between 1:00 AM and 3:00 PM (15:00) on Mondays.

* **Solution Attempt:** A text box is provided, where a user has entered "1603" as the answer. However, this is marked as "Error: Incorrect answer," indicating that the solution is wrong.

* **Potential Business Applications:** The bottom section explains how analyzing this data might be used to:

    * **Optimize Infrastructure:** Improve server resource allocation for peak demand.
    * **Strategize Content Delivery:** Better target content based on popularity and usage patterns.
    * **Improve Marketing Efforts:** Optimize marketing campaigns based on peak usage periods.


In summary, the image presents a data analysis task focusing on extracting specific information from a log file to understand website traffic patterns and improve website performance and marketing strategies.  The user has attempted a solution that's deemed incorrect.

**Image 2**: That's a close-up shot of a laughing emoji. 


Here's a description:

* **Emoji:** The main focus is a yellow circle representing the emoji's face. It has a wide, open mouth with a prominent, pink tongue showing. The eyes are squeezed shut, indicated by two diagonal black lines pointing outwards, suggesting intense laughter.

* **Color:** The emoji itself is a bright, golden yellow. The background is a slightly darker, muted orange color, providing a subtle contrast.

* **Style:** The emoji's style is consistent with common digital emoji designs, appearing smooth and slightly glossy. The lines are clean and simple.

* **Overall Impression:** The image conveys a feeling of unrestrained, happy laughter. The emoji's expression is jovial and lighthearted.

---

## Amit (@amitchaurasia)
- **Posted on**: 2025-02-22 04:08:00
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/4](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/4)

I’m also facing same kind of issue in Q3, GA5, while cross checked answer from different methods getting same result 1603, which is showing incorrect.
Kindly check this issue.
Thanks

---

## Aryan Singh (@Aryxn)
- **Posted on**: 2025-02-22 05:52:55
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/5](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/5)

The same issue is being faced by many students, not only for this condition, but others as well. Please look into it

---

## B R GIRI SUBRAHMANYA (@23f2000573)
- **Posted on**: 2025-02-22 08:28:29
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/6](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/6)

actually i got 130 as answer. but the answer accepted by the portal was 129. i felt like, i have to change one or two numbers front and back, i tried the same before. it worked

### 🖼 Image Descriptions

**Image 1**: That's a digital image of a modified emoji. 


Here's a description:

* **Base Emoji:** The core of the image is a standard yellow emoji depicting a face with a wide, open-mouthed laugh. The eyes are closed in a happy expression, and the mouth is a large, curved smile with a visible pink tongue.

* **Modification:** A single, light blue droplet of sweat is positioned on the right side of the emoji's face, suggesting exertion or amusement. The blue color is vibrant and distinct against the yellow.

* **Background/Border:** The emoji appears to be slightly bordered or set against a darker orange or yellowish-orange background, creating a subtle frame around the smiley face. The background's color is similar enough to the emoji to be almost unnoticeable except for the edges where the difference is a bit more noticeable.

* **Overall Impression:** The image conveys a feeling of extreme, possibly humorous exertion or overwhelming delight, implied by the combination of the wide laugh and the sweat drop.  The style is informal and playful.

---

## Muskan Aggarwal (@muskan2431)
- **Posted on**: 2025-02-22 09:57:39
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/7](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/7)

For the same question? But it shouldnt be +1 -1 to get the correct answer right.

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-02-24 11:48:02
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/8](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/8)

Hi @muskan2431 we are running some checks.
Please bear with us,
Kind regards

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-02-25 11:13:32
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/9](https://discourse.onlinedegree.iitm.ac.in/t/q3-ga5-not-accepting-right-answer/168011/9)

We have determined that some students were affected by GA5 Q3. Whoever we have identified as having received the incorrect assessment will receive 1 mark for that particular question. These are the students that we have identified as been assessed incorrectly:




SN
Email




1
21f1000131@ds.study.iitm.ac.in


2
21f1001484@ds.study.iitm.ac.in


3
21f1001631@ds.study.iitm.ac.in


4
21f1001729@ds.study.iitm.ac.in


5
21f1001890@ds.study.iitm.ac.in


6
21f1002734@ds.study.iitm.ac.in


7
21f1002773@ds.study.iitm.ac.in


8
21f1003135@ds.study.iitm.ac.in


9
21f1003475@ds.study.iitm.ac.in


10
21f1003816@ds.study.iitm.ac.in


11
21f1005422@ds.study.iitm.ac.in


12
21f1005510@ds.study.iitm.ac.in


13
21f1006234@ds.study.iitm.ac.in


14
21f1006309@ds.study.iitm.ac.in


15
21f1006867@ds.study.iitm.ac.in


16
21f2000525@ds.study.iitm.ac.in


17
21f2000913@ds.study.iitm.ac.in


18
21f2000998@ds.study.iitm.ac.in


19
21f2001061@ds.study.iitm.ac.in


20
21f2001080@ds.study.iitm.ac.in


21
21f2001543@ds.study.iitm.ac.in


22
21f3000311@ds.study.iitm.ac.in


23
21f3000355@ds.study.iitm.ac.in


24
21f3000512@ds.study.iitm.ac.in


25
21f3000591@ds.study.iitm.ac.in


26
21f3000687@ds.study.iitm.ac.in


27
21f3000813@ds.study.iitm.ac.in


28
21f3001091@ds.study.iitm.ac.in


29
21f3001161@ds.study.iitm.ac.in


30
21f3001936@ds.study.iitm.ac.in


31
21f3001965@ds.study.iitm.ac.in


32
21f3002158@ds.study.iitm.ac.in


33
21f3002431@ds.study.iitm.ac.in


34
21f3002444@ds.study.iitm.ac.in


35
21f3002647@ds.study.iitm.ac.in


36
21f3002782@ds.study.iitm.ac.in


37
21f3003195@ds.study.iitm.ac.in


38
22ds2000011@ds.study.iitm.ac.in


39
22f1000376@ds.study.iitm.ac.in


40
22f1000821@ds.study.iitm.ac.in


41
22f1000902@ds.study.iitm.ac.in


42
22f1000935@ds.study.iitm.ac.in


43
22f1000989@ds.study.iitm.ac.in


44
22f1001095@ds.study.iitm.ac.in


45
22f1001316@ds.study.iitm.ac.in


46
22f1001391@ds.study.iitm.ac.in


47
22f1001416@ds.study.iitm.ac.in


48
22f1001438@ds.study.iitm.ac.in


49
22f1001542@ds.study.iitm.ac.in


50
22f1001551@ds.study.iitm.ac.in


51
22f1001552@ds.study.iitm.ac.in


52
22f1001862@ds.study.iitm.ac.in


53
22f2000108@ds.study.iitm.ac.in


54
22f2000113@ds.study.iitm.ac.in


55
22f2000116@ds.study.iitm.ac.in


56
22f2000273@ds.study.iitm.ac.in


57
22f2000467@ds.study.iitm.ac.in


58
22f2000813@ds.study.iitm.ac.in


59
22f2000898@ds.study.iitm.ac.in


60
22f2000946@ds.study.iitm.ac.in


61
22f2001041@ds.study.iitm.ac.in


62
22f2001336@ds.study.iitm.ac.in


63
22f2001532@ds.study.iitm.ac.in


64
22f2001590@ds.study.iitm.ac.in


65
22f3000275@ds.study.iitm.ac.in


66
22f3000337@ds.study.iitm.ac.in


67
22f3000419@ds.study.iitm.ac.in


68
22f3000422@ds.study.iitm.ac.in


69
22f3000487@ds.study.iitm.ac.in


70
22f3000563@ds.study.iitm.ac.in


71
22f3000694@ds.study.iitm.ac.in


72
22f3000814@ds.study.iitm.ac.in


73
22f3000819@ds.study.iitm.ac.in


74
22f3000831@ds.study.iitm.ac.in


75
22f3000833@ds.study.iitm.ac.in


76
22f3001050@ds.study.iitm.ac.in


77
22f3001074@ds.study.iitm.ac.in


78
22f3001108@ds.study.iitm.ac.in


79
22f3001278@ds.study.iitm.ac.in


80
22f3001316@ds.study.iitm.ac.in


81
22f3001675@ds.study.iitm.ac.in


82
22f3001688@ds.study.iitm.ac.in


83
22f3001777@ds.study.iitm.ac.in


84
22f3001834@ds.study.iitm.ac.in


85
22f3001930@ds.study.iitm.ac.in


86
22f3001961@ds.study.iitm.ac.in


87
22f3001967@ds.study.iitm.ac.in


88
22f3002011@ds.study.iitm.ac.in


89
22f3002175@ds.study.iitm.ac.in


90
22f3002184@ds.study.iitm.ac.in


91
22f3002236@ds.study.iitm.ac.in


92
22f3002265@ds.study.iitm.ac.in


93
22f3002291@ds.study.iitm.ac.in


94
22f3002307@ds.study.iitm.ac.in


95
22f3002394@ds.study.iitm.ac.in


96
22f3002447@ds.study.iitm.ac.in


97
22f3002498@ds.study.iitm.ac.in


98
22f3002565@ds.study.iitm.ac.in


99
22f3002634@ds.study.iitm.ac.in


100
22f3002712@ds.study.iitm.ac.in


101
22f3002813@ds.study.iitm.ac.in


102
22f3002844@ds.study.iitm.ac.in


103
22f3002948@ds.study.iitm.ac.in


104
22f3003003@ds.study.iitm.ac.in


105
22f3003237@ds.study.iitm.ac.in


106
23ds1000032@ds.study.iitm.ac.in


107
23ds2000055@ds.study.iitm.ac.in


108
23ds2000069@ds.study.iitm.ac.in


109
23ds3000146@ds.study.iitm.ac.in


110
23ds3000149@ds.study.iitm.ac.in


111
23ds3000224@ds.study.iitm.ac.in


112
23f1000232@ds.study.iitm.ac.in


113
23f1000257@ds.study.iitm.ac.in


114
23f1000292@ds.study.iitm.ac.in


115
23f1000587@ds.study.iitm.ac.in


116
23f1000776@ds.study.iitm.ac.in


117
23f1000813@ds.study.iitm.ac.in


118
23f1000844@ds.study.iitm.ac.in


119
23f1001472@ds.study.iitm.ac.in


120
23f1001651@ds.study.iitm.ac.in


121
23f1001684@ds.study.iitm.ac.in


122
23f1001788@ds.study.iitm.ac.in


123
23f1001861@ds.study.iitm.ac.in


124
23f1002075@ds.study.iitm.ac.in


125
23f1002114@ds.study.iitm.ac.in


126
23f1002279@ds.study.iitm.ac.in


127
23f1002345@ds.study.iitm.ac.in


128
23f1002362@ds.study.iitm.ac.in


129
23f1002535@ds.study.iitm.ac.in


130
23f1002563@ds.study.iitm.ac.in


131
23f1002586@ds.study.iitm.ac.in


132
23f1002630@ds.study.iitm.ac.in


133
23f1002929@ds.study.iitm.ac.in


134
23f1003000@ds.study.iitm.ac.in


135
23f1003115@ds.study.iitm.ac.in


136
23f2000119@ds.study.iitm.ac.in


137
23f2000273@ds.study.iitm.ac.in


138
23f2000762@ds.study.iitm.ac.in


139
23f2000794@ds.study.iitm.ac.in


140
23f2000822@ds.study.iitm.ac.in


141
23f2000926@ds.study.iitm.ac.in


142
23f2000942@ds.study.iitm.ac.in


143
23f2001274@ds.study.iitm.ac.in


144
23f2001347@ds.study.iitm.ac.in


145
23f2001494@ds.study.iitm.ac.in


146
23f2001529@ds.study.iitm.ac.in


147
23f2001539@ds.study.iitm.ac.in


148
23f2001661@ds.study.iitm.ac.in


149
23f2001960@ds.study.iitm.ac.in


150
23f2001992@ds.study.iitm.ac.in


151
23f2002034@ds.study.iitm.ac.in


152
23f2002121@ds.study.iitm.ac.in


153
23f2002865@ds.study.iitm.ac.in


154
23f2002939@ds.study.iitm.ac.in


155
23f2003529@ds.study.iitm.ac.in


156
23f2003751@ds.study.iitm.ac.in


157
23f2003893@ds.study.iitm.ac.in


158
23f2004115@ds.study.iitm.ac.in


159
23f2004244@ds.study.iitm.ac.in


160
23f2004366@ds.study.iitm.ac.in


161
23f2004443@ds.study.iitm.ac.in


162
23f2004473@ds.study.iitm.ac.in


163
23f2004510@ds.study.iitm.ac.in


164
23f2004637@ds.study.iitm.ac.in


165
23f2004770@ds.study.iitm.ac.in


166
23f2004793@ds.study.iitm.ac.in


167
23f2004936@ds.study.iitm.ac.in


168
23f2004979@ds.study.iitm.ac.in


169
23f2005010@ds.study.iitm.ac.in


170
23f2005193@ds.study.iitm.ac.in


171
23f2005325@ds.study.iitm.ac.in


172
23f2005398@ds.study.iitm.ac.in


173
23f2005474@ds.study.iitm.ac.in


174
23f2005525@ds.study.iitm.ac.in


175
23f2005665@ds.study.iitm.ac.in


176
23f2005701@ds.study.iitm.ac.in


177
23f2005706@ds.study.iitm.ac.in


178
23f2005738@ds.study.iitm.ac.in


179
23f3000975@ds.study.iitm.ac.in


180
23f3001271@ds.study.iitm.ac.in


181
23f3001462@ds.study.iitm.ac.in


182
23f3001572@ds.study.iitm.ac.in


183
23f3001745@ds.study.iitm.ac.in


184
23f3001752@ds.study.iitm.ac.in


185
23f3001764@ds.study.iitm.ac.in


186
23f3001848@ds.study.iitm.ac.in


187
23f3002196@ds.study.iitm.ac.in


188
23f3002427@ds.study.iitm.ac.in


189
23f3002537@ds.study.iitm.ac.in


190
23f3002643@ds.study.iitm.ac.in


191
23f3003016@ds.study.iitm.ac.in


192
23f3003027@ds.study.iitm.ac.in


193
23f3003871@ds.study.iitm.ac.in


194
23f3004013@ds.study.iitm.ac.in


195
23f3004024@ds.study.iitm.ac.in


196
23f3004066@ds.study.iitm.ac.in


197
23f3004134@ds.study.iitm.ac.in


198
23f3004230@ds.study.iitm.ac.in


199
23f3004238@ds.study.iitm.ac.in


200
23f3004264@ds.study.iitm.ac.in


201
23f3004394@ds.study.iitm.ac.in


202
23f3004444@ds.study.iitm.ac.in


203
24ds1000079@ds.study.iitm.ac.in


204
24ds2000062@ds.study.iitm.ac.in


205
24ds2000101@ds.study.iitm.ac.in


206
24ds2000112@ds.study.iitm.ac.in


207
24ds3000028@ds.study.iitm.ac.in


208
24ds3000031@ds.study.iitm.ac.in


209
24ds3000074@ds.study.iitm.ac.in


210
24f1000010@ds.study.iitm.ac.in


211
24f1000400@ds.study.iitm.ac.in


212
24f1000784@ds.study.iitm.ac.in


213
24f1000925@ds.study.iitm.ac.in


214
24f1001396@ds.study.iitm.ac.in


215
24f1001439@ds.study.iitm.ac.in


216
24f1001520@ds.study.iitm.ac.in


217
24f1002390@ds.study.iitm.ac.in


218
24f1002474@ds.study.iitm.ac.in


219
24f2000994@ds.study.iitm.ac.in


220
24f2002746@ds.study.iitm.ac.in


221
24f2003375@ds.study.iitm.ac.in


222
24f2004863@ds.study.iitm.ac.in



Kind regards,
TDS Team

---
