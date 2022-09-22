# 🕺💥 Tugas 3 - Carissa Almira Yudiva (2106751676) 💥🕺

★	[Heroku App: HTML](https://tugas-carissa.herokuapp.com/mywatchlist/)

★	[Heroku App: XML](https://tugas-carissa.herokuapp.com/mywatchlist/xml)

★	[Heroku App: JSON](https://tugas-carissa.herokuapp.com/mywatchlist/json)

###  🖥 (1) Difference Between JSON, HTML, & XML 🖥
| | **JSON**  | **XML** | **HTML** |
| ------------ | ------------- | ------------- | ------------ 
| Purpose | Data Delivery  | Data Delivery  | Display Data |
| Save Elements | `Key:Value` (Map)  | `<variable>...</variable>` (Tree Structure) | `<title>..</title>` |
| Security | The majority of the time, JSON processing is secure, unless JSONP is employed, which can result in Cross-Site Request Forgery (CSRF) attacks. | External entity expansion and DTD validation are enabled by default, which makes XML structures vulnerable to many attacks. |  |
| Language | Javascript  | Markup Language  | Markup Language |
| Speed | Fast  | Slow  | Fast |
| Processing | No Process | Can do processing/calculation | The HTML parsing process accepts as input a stream of code points, which are then sent via a tokenization step and a tree construction stage to produce a Document object. |
| File | `.json` | `.xml` | `.html` |

###  🪄 (2) The Importance of *Data Delivery* in Implementing a Platform  🪄
When significant amounts of data are involved, a database is required to store the data. Then, when you wish to display these data, writing them one by one in HTML is inefficient. Therefore, data delivery is required to move the data from one stack to another in order to connect HTML and the database. Additionally, HTML and data can be separated to create a more organized document.

###  🧐 (3) Implementation 🧐
1. First, I activate the virtual environment
2. Used the command to create a `django-app` named `mywatchlist`
3. Registered the `mywatchlist` by adding it to the `INSTALLED_APPS` variable
4. Creating models in `models.py`
   ```python
   class MyWatchlist(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
   ```
5. Migrate the model schema into a local Django database
6. Create a file contains movies information named `initial_watchlist_data.json`:
   ```python
   [
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": "Sudah",
            "title": "Brooklyn Nine-Nine",
            "rating": 8,
            "release_date": "2013-09-17",
            "review": "This show is just good fun to watch good by yourself or with someone it's just enjoyable tv great stories and characters please do watch this show it's worth it!"      
        }
    },
    .....]
    ```
7. Inputting the movies data into the local Django database
8. Create three functions in the `views.py` file that accept `request` parameters for HTML, JSON, and XML features.
9. Create routing in the `urls.py` file and include XML, HTML, and JSON paths.
10. Deploy to Heroku followd by `add`,`commit`, dan `push` to Github


###  📱(4) Screenshot Postman 📱
