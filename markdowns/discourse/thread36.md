# Discourse forum

## Vikram Suriyanarayanan (@vikramjncasr)
- **Posted on**: 2025-02-14 03:57:16
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1)

@Jivraj @carlton sir please help
When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?
needs sudo permission all the time…
image2100×216 100 KB

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a screenshot of a terminal window, likely from a Linux or Unix-like operating system. 


Here's a breakdown of the content:

* **Top Lines:** The top lines show a username ("vikramjncasr"), the hostname ("ANJANEYA"), and the current working directory ("/mnt/c/IIT_Madras/TDS_Project_1"). There's also a command that appears to have been executed previously (`sudo rm -rf /uala`).

* **`ls /` Command and Output:** The main part of the screenshot displays the output of the command `ls /`. This command lists the contents of the root directory ("/"). The output shows a long list of directories, including common system directories like `bin`, `boot`, `etc`, `dev`, `home`, `lib`, `proc`, `run`, `sbin`, `srv`, `sys`, `tmp`, `usr`, and `var`.  Some directories have extensions like `.usr-is-merged`, suggesting a merged or combined filesystem structure.

* **Bottom Line:** The bottom line shows the command prompt again, indicating that the user is ready to enter another command.

The overall appearance is that of a standard terminal with a dark background and text in various colors (likely indicating different file types or permissions). The screenshot suggests the user is working within a virtual machine or a system with a Windows drive mounted (`/mnt/c`), as indicated by the path.

---

## Carlton D'Silva (@carlton)
- **Posted on**: 2025-02-14 04:53:36
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2)

Hi Vikram,
This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py
Inside the docker container, permission for the data folder is set by the Dockerfile
which then allows your application to access the root folder inside your docker image and create the /data folder.
So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

You create your application server that serves 2 endpoints on localhost:8000
You create a docker image that runs this application server.
You run the docker image using podman as described in the project page.
For mimicking the testing conditions. You need two files:
evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.
Hope that gives clarity.
Kind regards

---
