# Discourse forum

## Arnav Mehta  (@21f3002647)
- **Posted on**: 2025-02-17 10:07:56
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1)

Dear TDS Team,
I have verified my submission, and my repository does include a Dockerfile, and the Docker image is accessible on DockerHub. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.
Looking forward to your confirmation.
Best regards,
Arnav Mehta
(21f3002647)
image250×534 3.92 KB
image713×238 11 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a file explorer-style interface, likely from a code editor or IDE (Integrated Development Environment). 


The background is dark, almost black. The entries are displayed in a vertical list with icons indicating file types:

* **Folders:** Folders are represented by yellow icons. We see a top-level folder (indicated by "..."), a folder named "LLM_PROJECT1," and a folder named "_pycache_".

* **Files:** Files are represented by white icons. The files listed are: "Dockerfile", "LICENSE", "app.py", "datagen.py", "evaluate.py", "requirements.txt", "tasksA.py", and "tasksB.py".  The filenames suggest a Python project (`.py` extensions). "requirements.txt" is a common file for listing project dependencies.


The overall appearance suggests a clean, organized project directory structure. The use of a dark theme is typical in many code editors.

**Image 2**: That's a screenshot of a webpage, likely from a code repository or similar platform like GitHub. 


Here's a breakdown of what's visible:

* **Top Center:** The main title displays "arnaavmehta2025/llm_project1" in bold, white text. This strongly suggests a project name within a user's repository.

* **Below Title:** "By arnavmehta2025 · Updated 2 days ago" indicates the owner and the last update.

* **Left Side:** A light-blue, isometric cube icon is prominent. This type of icon is often associated with 3D modeling, game development, or other projects involving spatial data or objects.

* **Below the Cube:** A small, blue "IMAGE" label might indicate the existence of an image file within the project.

* **Bottom Center:** Star (⭐) and Download (↓) icons with respective numbers (0 stars and 16 downloads) are shown, indicating the project's popularity and download count.

* **Background:** The background is dark gray or black, providing contrast to the lighter text and icon.

The overall style suggests a clean, minimalist interface common to online code hosting services.

---

## Arnav Mehta  (@21f3002647)
- **Posted on**: 2025-02-17 12:30:15
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2)

@Saransh_Saini sir what should i do?

---

## Saransh Saini (@Saransh_Saini)
- **Posted on**: 2025-02-17 15:43:39
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3)

@carlton Kindly have a look into this.

---

## Satvik  Sawhney (@satviksawhney)
- **Posted on**: 2025-02-18 00:48:03
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8)

Good Morning Sir,
Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.
Looking forward to your reply.
Thank you
Satvik Sawhney
23f2003680

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-02-18 05:00:31
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9)

So the reason for the failure is:
You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)
Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.
Then once you realised your mistake, on Feb 17th at 9:11 pm IST i.e yesteday, you changed your repo to put the files in the correct locations.
Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]
image250×534 3.92 KB
[/quote]
showing that your files are in the correct place.
We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.
Kind regards

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a screenshot of a file explorer or similar interface, likely from a code editor or IDE. 


The background is dark, almost black. The text is light-colored, making it easily readable against the dark background. 


The file list is organized vertically, showing folders and files nested within each other:

* **Top Level:** A folder indicated by three dots (...) is at the very top.
* **LLM_PROJECT1:** A folder named "LLM_PROJECT1" is directly below the top-level folder.
* **_pycache_:** A folder named "_pycache_" is nested under "LLM_PROJECT1".
* **Files within LLM_PROJECT1:** The remaining items are files (indicated by a file icon) within the "LLM_PROJECT1" folder. These files include:
    * Dockerfile
    * LICENSE
    * app.py
    * datagen.py
    * evaluate.py
    * requirements.txt
    * tasksA.py
    * tasksB.py

The file names suggest this might be a Python project, given the ".py" extensions and the presence of a `requirements.txt` file (typically used to list project dependencies). The "_pycache_" folder is a standard Python folder containing compiled bytecode. The `Dockerfile` indicates a containerized deployment strategy might be in use.

---

## Arnav Mehta  (@21f3002647)
- **Posted on**: 2025-02-18 06:35:49
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10)

@carlton sir
Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.
I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered 
Kind regards,
Arnav Mehta
21f3002647

### 🖼 Image Descriptions

**Image 1**: That's a close-up shot of a digital emoticon, specifically a sad-faced yellow emoji. 


Here's a breakdown of the image:

* **Shape and Color:** The emoji is circular, bright yellow, and sits on an orange background that's partially visible at the edges. The orange background suggests it might be from a messaging app or similar digital interface.

* **Facial Features:** The emoji has two small, dark-colored circles for eyes, positioned fairly close together. The mouth is a downward-curving arc, a classic representation of sadness. The features are simple and minimalistic.

* **Style:** The style is consistent with common digital emojis—simple, flat, and easily understandable. There's no shading or texture; the colors are solid.

* **Overall Impression:** The image clearly conveys sadness or disappointment due to the downturned mouth and the overall expression.

---

## Satvik  Sawhney (@satviksawhney)
- **Posted on**: 2025-02-18 08:28:16
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11)

Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.
Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.
Sir it is a humble request to please consider it.
Warm Regards,
Satvik Sawhney
23f2003680
Screenshot 2025-02-18 at 1.53.10 PM1889×467 54 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a dark-themed file explorer or version control system interface, likely from a Git repository or similar tool. 


The interface displays a list of files and folders organized hierarchically. Each entry shows:

* **File/Folder Icon:** A folder icon (yellow) denotes directories, and a file icon (white) indicates files.
* **Name:** The name of each file or folder is listed clearly. 
* **Commit Message:** A brief description of the changes made in the latest commit for that item.
* **Timestamp:** The date and time of the last modification or commit are shown, using relative terms like "2 days ago," "yesterday," and "3 days ago."
* **Icons on Right Side:** Small icons on the far-right side might represent different statuses or actions associated with each entry.

The overall style is clean and modern, with a dark background contrasting sharply with the light-colored text and icons.  The absence of scrollbars suggests that the entirety of the file list is visible within the capture.

---
