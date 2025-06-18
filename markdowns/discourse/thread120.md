# Discourse forum

## amit_kulkarni (@23f1001947)
- **Posted on**: 2024-11-08 15:08:58
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/1](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/1)

image756×295 19.5 KB
The question asks to use gpt-3.5-turbo-0125 model but the ai-proxy provided by Anand sir only supports gpt-4o-mini. So should we just use gpt-4o-mini or use the OpenAI API for gpt3.5 turbo?
@carlton

### 🖼 Image Descriptions

**Image 1**: Here's a description of the image:

The image shows a multiple-choice question related to the cost of using a language model. 


Here's a breakdown:

* **The Question:** The question asks to calculate the input cost (in cents) of a given text when passed to a language model named "gpt-3.5-turbo-0125".  The cost is 50 cents per million input tokens. The text itself is in Japanese.

* **The Text:** The Japanese text provided is: 私は静かな図書館で本を読みながら、時間の流れを忘れてしまいました。(Watashi wa shizuka na toshokan de hon o yominagara, jikan no nagare o wasurete shimaimashita.) This translates to "While reading a book in a quiet library, I lost track of time."

* **The Choices:** Four options are given as possible answers: 0.0018, 0.00175, 0.0017, and 0.00165 cents.

* **The Format:** The question is numbered (8), and the text input to the model is highlighted. The choices are presented as radio buttons, suggesting a single correct answer.

The image appears to be a screenshot of a quiz or exam related to natural language processing and the cost associated with using language models.

---

## amit_kulkarni (@23f1001947)
- **Posted on**: 2024-11-09 13:00:46
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/2](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/2)

I tried gpt-3.5-turbo-0125 with python’s tiktoken library , I got a different value for prompt token compared gpt-4o-mini from the proxy api.

---

## Abhimanyu  (@Abhimanyu.yd)
- **Posted on**: 2024-11-09 15:05:08
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3)

My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate.

---

## Jivraj Singh Shekhawat (@Jivraj)
- **Posted on**: 2024-11-09 16:53:51
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4)

Use the model that’s mentioned in the question.

---

## Akash Jana (@23f2000990)
- **Posted on**: 2025-06-13 13:45:28
- **Link**: [https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/6](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/6)

The answer should be 0.00165 right.

---
