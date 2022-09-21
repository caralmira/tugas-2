# Tugas 2 - Carissa Almira Yudiva (2106751676)

[Heroku App](http://tugas-2-carissa.herokuapp.com/katalog/)

### (1) Django Framework *Request & Response*
![DJANGO (1)](https://user-images.githubusercontent.com/112609904/190112853-9386aae5-b401-4c20-8a7e-d5b9cdae04eb.jpg)

### (2) Django Framework Explanation
1. Middlewares predominantly manage incoming requests. In the `settings.py` file, you may find a list of the Middlewares currently in use.
   ```python
   MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]
   ```
2. The request reaches the URL router, which employs the `urls.py` variable `urlpatterns`:
   ```python
   from django.urls import path
   from katalog.views import show_catalog

   app_name = 'katalog'

   urlpatterns = [
      path('', show_catalog, name='show_catalog'),
   ]
   ```
3. Once matched against `urlpatterns`, it will be sent to `views.py` based on the called views:
   ```python
   from django.shortcuts import render
   from katalog.models import CatalogItem

   def show_catalog(request):
      data_barang_catalog = CatalogItem.objects.all()
      context = {
      'list_barang': data_barang_catalog,
      'nama'      : 'Carissa Almira',
      'studentid' : '2106751676',
   }
   return render(request, "katalog.html", context)
   ```
4. If there is any database activity, views will send a query to the `models.py` file:
   ```python
   from django.db import models

   class CatalogItem(models.Model):
      item_name = models.CharField(max_length=255)
      item_price = models.BigIntegerField()
      item_stock = models.IntegerField()
      description = models.TextField()
      rating = models.IntegerField()
      item_url = models.URLField()
   ```
5. Then, it will be sent to the database to process the required info.
6. Views will then receive response data in the form of query results.
7. Views will then select the HTML that corresponds to the one that was previously mapped.
8. HTML is returned to the client as a response to the requested URL.

### (3) Using Virtual Environment
   Virtual Environment is used as a place to experiment with a project, so that one project does not interfere with another project's environment. Every Django application or project will likely require the installation of additional packages or libraries. Occasionally, various Django projects require different versions of packages. Utilizing a virtual environment will make it easier to handle each of the several Django projects.

   As a result, the virtual environment acts as a barrier between projects, so when one project is installing something, the other projects are unaffected. By utilizing a virtual environment, we are able to build a unique, isolated environment.   Therefore, each Django project should have its own virtual environment.

   In fact, it is not secure without a virtual environment, as it may impact other apps or projects. Nonetheless, Django projects can be constructed without a virtual environment. However, it will be challenging in an environment with numerous projects. As indicated previously, adopting virtual environments will facilitate the independent management of many Django projects.

### (4) Implementation
1. Created the `show_catalog(request)` method in `views.py`. Retrieve model data and return it in HTML format.

   `show_catalog(request)` method:
   ```python
   def show_catalog(request):
      data_barang_catalog = CatalogItem.objects.all()
      context = {
      'list_barang': data_barang_catalog,
      'nama'      : 'Carissa Almira',
      'studentid' : '2106751676',
   }
   return render(request, "katalog.html", context)
   
   Inside `models.py`:
   ```python
      from django.db import models

      class CatalogItem(models.Model):
         item_name = models.CharField(max_length=255)
         item_price = models.BigIntegerField()
         item_stock = models.IntegerField()
         description = models.TextField()
         rating = models.IntegerField()
         item_url = models.URLField()
   ```

2. Routing in `urls.py` for displaying HTML sites in the browser.
   a. Add to katalog:
      ```python
         path('', show_catalog, name='show_catalog'),
      ```
   b. Add to project_django:
      ```python
      path('katalog/', include('katalog.urls')),
      ```
3. Use `context` in the `show_catalog(request)` method to convert the obtained data into HTML:
   ```python
      context = {
         'list_barang': data_barang_catalog,
         'nama'      : 'Carissa Almira',
         'studentid' : '2106751676',
      }
   ```
 4. Add the `context` dictionary;s data to the `katalog.html` file.
  
    ```html
       {% extends 'base.html' %}

       {% block content %}

       <h1>Lab 1 Assignment PBP/PBD</h1>

       <h5>Name: </h5>
       <p>{{nama}}</p>

       <h5>Student ID: </h5>
       <p>{{studentid}}</p>

       <table>
          <tr>
            <th>Item Name</th>
            <th>Item Price</th>
            <th>Item Stock</th>
            <th>Rating</th>
            <th>Description</th>
            <th>Item URL</th>
          </tr>
          {% comment %} Add the data below this line {% endcomment %}
          {% for barang in list_barang %}
          <tr>
              <th>{{barang.item_name}}</th>
              <th>{{barang.item_price}}</th>
              <th>{{barang.item_stock}}</th>
              <th>{{barang.description}}</th>
              <th>{{barang.rating}}</th>
              <th>{{barang.item_url}}</th>
          </tr>
          {% endfor %}
       </table>

       {% endblock content %}
     ```
4. Create an application on Heroku. Added repository secret along with the application's name and API Key. Then, execute `add`, `commit` and `push` followed by deployment.

### Sources:
https://www.diva-portal.org/smash/get/diva2:1503540/FULLTEXT01.pdf
https://towardsdatascience.com/a-beginners-guide-to-using-djangos-impressive-data-management-abilities-9e94efe3bd6e
