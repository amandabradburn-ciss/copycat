# Retrospective Document


CopyCat was a group  project that we started in April. We first proposed the idea of creating a code vulnerability scanner that could take user Python code as input and use an LLM to scan the code and identify vulnerabilities. We eventually established a set plan and requirements for the project, deciding that the user’s code would be scanned by Bandit, while the LLM would parse Bandit’s output rather than directly scanning the code itself.

We eventually had some difficulty with the LLM we had chosen initially. The usage limits had changed and it was no longer a financially feasible option, so we had to change the LLM we were using to a more affordable model. While this was a small hiccup, we were able to adapt and find a solution; something that I found we did well as a team.

By early May, we had the project in a beta state that was able to take in Python code and output the vulnerability and CWE number. The website was basic, but the LLM and Bandit were functioning correctly and producing accurate results.

After the beta release, we received feedback that we should try to incorporate the LLM more directly into the scanning of the code. After this, we decided to broaden the scope of our project. We added multiple language support, LLM-assisted scanning of the code, and the ability to use more powerful models when inputting matching code.

We were able to complete this, so it is reflected in our final project. However, unlike the Python setup, we were unable to get Applications to take the place of Bandit for the other three languages.

If we were to start the project over again, we would probably broaden the scope from the beginning so we could find implementations for the other languages. Overall, this project was successful.
