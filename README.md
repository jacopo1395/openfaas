# OpenFaas

Some example functions using OpenFaaS.

## Functions
### Weather
  _Return the weather given a city._

* **URL** /functions/weather

* **Method:** `POST`

* **Data Params** send in the body a `city_name=[text]`

* **Success Response:** **Content:** `json object`
 
* **Error Response:** error message

---

### Grey
  _Make black and white a photo given a URL of the image._

* **URL** /functions/grey

* **Method:** `POST`

* **Data Params** send in the body a `url=[text]`

* **Success Response:** **Content:** `file object`
 
* **Error Response:** error message


---

### Telegram
  _IFTTT bot sends me a telegram message given a text._

* **URL** /functions/telegram

* **Method:** `POST`

* **Data Params** send in the body a `message=[text]`

* **Success Response:** **Content:** success message
 
* **Error Response:** error message
* **Note:** the bot sends me a message to my *personal* account


# Vocal Commands
In vocal folder there is my python code. It simulates a *voice assistant* as Goggle Assistant or Alexa.
I used <a href="http://docs.kitt.ai/snowboy/">snowboy</a> to detect the vocal commands.

You can try 2 commands, but first you check on <a href="http://docs.kitt.ai/snowboy/">snowboy</a> documentation if you have all dependencies.

### show weather
* say `show weather`
* response: `weather information`

### send message
* say `send message`
* response: a telegram message is sends to me

# Presentation
<a href="https://github.com/jacopo1395/openfaas/blob/master/OpenFaaS.pdf">Click here</a>
