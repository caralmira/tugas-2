# 🕺 Tugas 4 - Carissa Almira Yudiva (2106751676) 🕺

★	[Heroku App](https://tugas-carissa.herokuapp.com/todolist/)

###  (1) The Importance of `{% csrf_token %}` to Implement The Element `<form>` 
Cross-Site Request Forgery (CSRF) can occur when a malicious site induces a user's browser to send a request to the server that results in a server modification. The `{% csrf_token %}` tag of Django can be used for CSRF attack. Because it holds user credentials, particularly cookies, the server will believe that the request made is the user's intention. By adding the `{% csrf_token %}` tag to the `<form>` tag in the Django project template, we can prevent 'unsafe' requests from CSRF. This tag will generate a unique token on the server when the page is rendered.

Without these tags, there will be a significant CSRF risk. Users can be duped by attackers into submitting unwanted requests.

###  (2) Making Forms Manually
Using the `<form>` tag, we can manually generate the form; don't forget to include the `{%csrf_token%}` as well. Widgets must be manually created using `<input>` tags and other elements. The name attribute of each widget will be used to specify the kind of model attribute that is entered.
```python
<form method "POST" action = "">
   {% csrf_token %}
  <label for = "title"> Title </label>
  <input type="text" id ="title" name="title"/>
  
  <label for="description">Description</label>
  <textarea id="description" name="description"></textarea>
  
  <input type="submit", value="Create">
</form>
```
The function in the views that had previously called the render form can then access the data once it has been submitted by using the `request.POST.get(name)` method.  
```python
def create_task(request):
  if request.method == 'POST':
    title = request.POST.get('title')
...
```
### (3) HTML Submission Data Flow
The information for each property will be saved and provided to the function in `views.py` when the user completes the form in the HTML template. Following that, a new model instance will be constructed depending on the attributes that were previously stored. The database will then be used to store this model instance. Finally, using a unique query, every instance in the database will be obtained and displayed in the HTML template.

### (4) Implementation
1. Run `python manage.py startapp todolist` in the terminal to create an application called `todolist` in the previously used Django task project.
2. Add a path so that users can access it via localhost by adding path to `urlspatterns` in `urls.py` and adding `todolist` to `INSTALLED_APPS` in  `settings.p y`
3. Construct a model:
   ```python
   class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE will instruct Django to cascade the deleting effect
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)
    ```
4. Write `register`, `login`, and `logout` functions in `todolist/views.py`, then create HTML for each function to implement registration, login, and logout forms so that users can utilize `todolist` effectively.
5. Create a `todolist` main page with the user's username, a button to add a new task, a button to log out, and a table with the task's creation date, title, and description, created date, and status.
6. Design a task creation form page. The user merely needs to submit the task title and description as data.
7. Establish routing to enable URL access to the functions. 
8. `Commit`, `push`, and `add` to the repository associated with the Heroku application.
9. Carry out a Heroku deployment for the application you've already created so that it can be accessed via the Internet.
10. Create two user accounts and three dummy datas using the Task model for each account on the Heroku website.

## Thank You!
