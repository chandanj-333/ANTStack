<br />_API built using Djangorestframework that computes the taxes and the final bill amount that can be used by All-in-One Store that sells everything from groceries, medicines, clothes, books, music CDs, imported commodities etc._<br />

**STEPS TO RUN THIS PROJECT ON YOUR LOCAL MACHINE:**<br />

1.Clone this Repository (`git clone <URL>`) <br />
2.Move to the ANTStack Directory (`cd ANTStack`)<br />
3.Install all the dependencies (`pip install -r requirements.txt`) <br />
4.Makemigrations for the model (`python manage.py makemigrations`) <br />
5.Migrate the model (`python manage.py migrate`) <br />
6.Run Development server (`python manage.py runserver`) <br />
7.Use any API testing tool to test the API (_endpoint:_ `http://127.0.0.1:8000/items/`  _Method Supported:_ `POST`)<br />

**INPUT:**<br />

`[{
       "item": "Classical Songs Collection",
       "itemCategory": "Music",
       "quantity": 1,
       "price": 500
   },
   {
       "item": "Pants",
       "itemCategory": "Clothes",
       "quantity": 2,
       "price": 1200
   }]`

<br />**Calculation Done:**<br />

_Gets 1st Item "Classical Songs Collection" calculates totalPrice(assuming price given is for single quantity price*quantity)_ <br />
_calculates tax for the totalPrice (500*0.03=15)_ <br />
_so totalPrice after tax now is 500+15=515_ <br />

_similarly calculates for next Item "Clothes" (totalPrice=2400 tax will be 12% as price exceeds 1000)_ <br />
_totalPrice after tax now is 2400+288=2688 for the_ <br />

_Calculates TotalBill = 2688+515 which exceeds 2000 so,5% discount is applied_ <br />
_totalAmountPayable is TotalBill-Discount=3203-160.15=3042.85_ <br />

<br />**OUTPUT:**<br />

`{
	"DateofPurchase": "2022-01-25T17:42:07.291825",
	"Item": {
		"Classical Songs Collection": 515.0,
		"Pants": 2688.0
	},
	"Discount": 160.15,
	"TotalPayable": 3042.85
}`

<br />Returns Items with totalcost after tax ,Discount and Total amount Payable<br />
<br /> **Note: Items for sorted on ItemNames** <br />

<br/>**Sreenshot:**<br />

![img.png](img.png)
