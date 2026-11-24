<h2>LLM-Task-Manager</h2>
<b>LLM-Task-Manager</b> is a web application that transforms a manager's brief notes into clean, structured task descriptions that can be pushed into a task tracker.
<br><br>
<div>
<b>The application allows users to:</b>
<ul>
<li>Reduce time spent on routine task creation.</li>
<li>Generate clear and professionally structured task descriptions using an LLM.</li>
<li>Store chat history, allowing users to reread previous conversations.</li>
</ul>
</div>
<br>
:high_brightness:<b>Tech Stack</b>:high_brightness:<br>
Python, FastAPI, JavaScript, HTML, CSS, LLM API
<br><br>
<hr>


<div>
<h3>Local Deployment</h3>
<hr>

Open a terminal and run the following commands:

```bash
git clone https://github.com/735Andrew/LLM-Task-Manager
cd LLM-Task-Manager 
python -m venv venv 
venv\Scripts\activate
(venv) pip install -r requirements.txt
```

Create a <b>.env</b> file in the root directory with the following variables:

```commandline 
LLM_API_TOKEN = <YOUR_API_TOKEN>
ACCESS_KEY = <YOUR_ACCESS_KEY>        # Your access key for logging
```
This project uses <b>GigaChat</b> as its LLM provider. <br>
You can obtain an API token here: :link: https://cloud.ru/ :link:

<br>
Open a terminal in the root directory and execute this command:

```bash
(venv) python main.py
```
Once the application has started, open your web browser and navigate to http://localhost:8000

</div>
<hr>

<div>
<h3>Current Status & Roadmap</h3>
<hr>
<b>Technical design decisions:</b>
<ul>
<li>The ACCESS KEY is stored in a browser :cookie: cookie and sent with subsequent requests.</li>
<li>Chat history is stored in the browser's localStorage.</li>
</ul>

<br>
<b>Possible future enhancements:</b>
<ul>
<li>Integrate application endpoints with a Task Tracker API to share LLM responses with a team.</li>
<li>Equip the LLM with some custom tools, such as meeting room booking.</li>
</ul>

</div>
<hr>