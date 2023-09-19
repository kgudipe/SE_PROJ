SE PROJECT 1 Documentation

Team No.: 72

Team Members: 
Garlapati Sai Santhosh(sgarlap@ncsu.edu)
Koushik Gudipelly(kgudipe@ncsu.edu)
Akhilsai Chittipolu(achitti@ncsu.edu)
Sai Rithwik Pokala(spokala@ncsu.edu)

As the part of project 1, we were assigned 5 projects and below are the pain points and learnings we got during our journey with these projects.

The project “Feature Hunt” is basically a platform that allows users to share/vote/discuss feature requests and product owners to organize them to make better product decisions.
Below are the challenges and learnings we have gone through in our process.
Circular dependencies between the 'app.py' and 'ping.py' files posed a complex issue in the project's codebase. 
Incompatibility between the Python version used and that of the virtual environment presented a versioning challenge. 
Ensuring the smooth functionality of 'Mongosh' in connection with 'enzyme adapter react 16' for cloud cluster connectivity was essential. 
We successfully executed the frontend and established a MongoDB cluster. Additionally, we achieved interactivity between the frontend and Flask-based backend. Our ongoing efforts are directed towards optimizing API calls for efficient data exchange between project components. 
A 'wheel dependency error' presented an obstacle to project functionality. We methodically resolved this issue by reviewing and removing unnecessary dependencies from the project's setup configuration file, enhancing both stability and efficiency.

Our next project “Teacher'sPetBot” is a Discord Bot for class instructors to streamline their Discord servers. Discord is a great tool for communication and its functionalities can be enhanced by bots and integrations.

Initially, we encountered deprecated dependencies, necessitating extensive upgrades to ensure compatibility. Furthermore, there was a problem when creating Discord bot and connecting it to the server. We faced this issue because we followed the documentation provided which is old and there are some new features added into discord which made a difficulty.

After that, we have tried to run “Sync Ends” project, it basically states that automates communication between service providers and consumers. Each team maintains a Postman collection to test and document their APIs. The backend team registers their service, and we handle updates. When API changes occur, we notify consumers, streamlining the update process. Slack integration simplifies this, allowing you to focus on core functionality.
Below are our pain points and learnings from this project:
•	While installing building wheel for multidict.multilib package in pyproject.xml did not run successfully and we resolved it by checking the dependencies to that of python 4.11 latest version

•	And also python setup.py bdist_wheel did not run successfully and we did it using Microsoft Visual C++ version build tools to 14.0 or greater 

•	We also got this error originates from a subprocess, and is likely not a problem with pip which was ERROR: Failed building wheel for regex and resolved it 

•	And also Failed to build multidict regex typed-ast yarl which we resolved using building wheel for yarl

•	And we also did extensive site packages installing to avoid dependency issues.

Next, we tried on the project, “Constable Github-Action”, This 3rd party application that does the same job as the action, but without the hassle of you creating a pull request or installing an action on your repository. Now, you can run constable reports on your repository just by a single click on our website. The website can be found here: https://constable-webapp.herokuapp.com.

Below are the pain points and learnings for this project:
•	Attempted to export environment variables directly in YAML, which didn't work which resolved using shell scripts in CI/CD environment

•	got error in the env:
GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} and resolved using generative token      from multiple users

•	while installing virtual environment got dependency mismatch issues and resolved using downgrading the python version

•	Got issues while running the action commands in git and resolved manually each time using thollander/actions-comment-pull-request@master

After working on all the given projects, we have finally decided to work on the project “Movie Recommender” for the Project 2. The pain points we faced, process to be followed to avoid those pain points and the future scope are described as below:

In the realm of digital entertainment, where options abound and time is limited, the Movie Recommender project emerges as your reliable companion for navigating the world of movies. This provides insight into the inner mechanics of our application, crafted to elevate your cinematic journey.

But like any journey, there have been hurdles and lessons learned along the way. In Project 1, we encountered a challenge involving the search bar's POST method, a puzzle we successfully unraveled through error messages and code examination. Our experience taught us that vigilance and careful debugging are essential companions on the path to software excellence.
What practices we are committing to perform in project2 to avoid the pain: 

As we embark on Project 2 and beyond, let's carry forward these insights. Let's navigate the future with clarity, ensuring a smoother and more delightful cinematic journey for all. Join us as we delve deeper into Movie Recommender, where the world of movies awaits your exploration."

Future scope:

We will try to develop a good UI for the application.

We will provide user specific login and logout functionality so that the application can suggest according to the specific user interests.

We will try to increase the size of the movies database and also try to increase the prediction accuracy.

Following link for our selected project:
https://youtu.be/W9M-fZr-ZaA 

