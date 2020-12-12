import re

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", " ", \
    "possible", r"\?"]

while True:
    try:
        question = input("Enter a question: ")
        answer = input("Enter a response: ")

        intent = question.lower()
        for word in uninteresting_words:
            intent = re.sub(word+" ", "", intent)
            if word == (r"\?" or " "):
                intent = re.sub(word, "", intent)

        intent = "_".join(intent.split())

        with open('testfaq.yml', 'r') as file:
            faqs = file.readlines()

        with open('testresponses.yml', 'r') as file:
            responses = file.readlines()

        faqsappend = '''
- intent: faq/{}
  examples: |
   -{}
'''.format(intent, question)
        faqs.append(faqsappend)
        faqs = "".join(faqs)

        responseappend = '''
  utter_faq/{}:
  - text: "{}"
'''.format(intent, answer)
        responses.append(responseappend)
        responses = "".join(responses)

        with open('testfaq.yml', 'w') as file:
            # yaml.dump(faqs,file)
            file.write(faqs)
            file.close()

        with open('testresponses.yml', 'w') as file:
            # yaml.dump(responses, file)
            file.write(responses)
            file.close()
    except:
        continue
