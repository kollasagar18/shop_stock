from django.shortcuts import render
from django.http import HttpResponse
from .db import db_con
from rest_framework.decorators import api_view
import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from rest_framework.response import Response
import os


# ---------------- HOME PAGES ----------------

def home(request):
    return render(request, "home.html")

def sale(request):
    return render(request, "sale.html")

def buy(request):
    return render(request, "buy.html")
def predict_page(request):
    return render(request, "predict.html")

# ---------------- TOTAL STOCK (GRAPH) ----------------

def total_stack(request):
    import matplotlib.pyplot as plt
    import pandas as pd

    query = "select * from ratio_shop_stock"
    data = pd.read_sql(query, db_con())

    bars = plt.bar(data["items"], data["stock"])
    plt.xlabel("Items")
    plt.ylabel("Stock")
    plt.title("Ration Shop Stock")
    plt.xticks(rotation=45)

    plt.bar_label(bars)
    plt.show()

    return render(request, "home.html")




@api_view(["POST"])
def add_stock(request):
    
    
    
    data = request.POST.dict()
    db = db_con()
    cu = db.cursor()

    try:
        ri = int(data["rice"])
        su = int(data["sugar"])
        pa = int(data["palmolein_oil"])
        re = int(data["red_gram_dal"])
        jo = int(data["jowar"])
        ra = int(data["raagi"])

        # rice
        cu.execute("select stock from ratio_shop_stock where items=%s", ("rice",))
        s = int(cu.fetchone()[0]) + ri
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "rice"))

        # sugar
        cu.execute("select stock from ratio_shop_stock where items=%s", ("sugar",))
        s = int(cu.fetchone()[0]) + su
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "sugar"))

        # palmolein oil
        cu.execute("select stock from ratio_shop_stock where items=%s", ("palmolein_oil",))
        s = int(cu.fetchone()[0]) + pa
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "palmolein_oil"))

        # red gram dal
        cu.execute("select stock from ratio_shop_stock where items=%s", ("red_gram_dal",))
        s = int(cu.fetchone()[0]) + re
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "red_gram_dal"))

        # jowar
        cu.execute("select stock from ratio_shop_stock where items=%s", ("jowar",))
        s = int(cu.fetchone()[0]) + jo
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "jowar"))

        # raagi
        cu.execute("select stock from ratio_shop_stock where items=%s", ("raagi",))
        s = int(cu.fetchall()[0][0]) + ra
        cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "raagi"))

        db.commit()
        return HttpResponse("Data was added successfully")

    except ValueError:
        return HttpResponse("Please enter numbers only")

    finally:
        cu.close()
        db.close()
@api_view(["POST"])
def sale_stack(request):
    data = request.POST.dict()
    db = db_con()
    cu = db.cursor()

    try:
        ri = int(data["rice"])
        su = int(data["sugar"])
        pa = int(data["palmolein_oil"])
        re = int(data["red_gram_dal"])
        jo = int(data["jowar"])
        ra = int(data["raagi"])

        # rice
        cu.execute("select stock from ratio_shop_stock where items=%s", ("rice",))
        rice=cu.fetchall()
        if int(rice[0][0]) >= ri:
            s = int(rice[0][0]) - ri
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "rice"))
        else:
            return HttpResponse("Out of stock: rice")

        # sugar
        cu.execute("select stock from ratio_shop_stock where items=%s", ("sugar",))
        sugar=cu.fetchall()
        if int(sugar[0][0]) >= su:
            s = int(sugar[0][0]) - su
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "sugar"))
        else:
            return HttpResponse("Out of stock: sugar")

        # palmolein oil
        cu.execute("select stock from ratio_shop_stock where items=%s", ("palmolein_oil",))
        palmolein=cu.fetchall()
        if int(palmolein[0][0]) >= pa:
            s = int(palmolein[0][0]) - pa
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "palmolein_oil"))
        else:
            return HttpResponse("Out of stock: palmolein oil")

        # red gram dal
        cu.execute("select stock from ratio_shop_stock where items=%s", ("red_gram_dal",))
        red=cu.fetchall()
        if int(red[0][0]) >= re:
            s = int(red[0][0]) - re
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "red_gram_dal"))
        else:
            return HttpResponse("Out of stock: red gram dal")

       
        cu.execute("select stock from ratio_shop_stock where items=%s", ("jowar",))
        jowar=cu.fetchall()
        if int(jowar[0][0]) >= jo:
            s = int(jowar[0][0]) - jo
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "jowar"))
        else:
            return HttpResponse("Out of stock: jowar")

        # raagi
        cu.execute("select stock from ratio_shop_stock where items=%s", ("raagi",))
        raagi=cu.fetchall()
        if int(raagi[0][0]) >= ra:
            s = int(raagi[0][0]) - ra
            cu.execute("update ratio_shop_stock set stock=%s where items=%s", (s, "raagi"))
        else:
            return HttpResponse("Out of stock: raagi")

        db.commit()
        return HttpResponse("Sale completed successfully")

    except ValueError:
        return HttpResponse("Please enter numbers only")

    finally:
        cu.close()
        db.close()
@api_view(["POST"])
def predict_data(request):

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    product = request.data.get("product")

    allowed_products = [
        "rice",
        "wheat",
        "sugar",
        "oil",
        "dal",
        "salt"
    ]

    if product not in allowed_products:
        return Response({
            "error": "Invalid product"
        })

    # Graph Data
    graph_query = f"""
    SELECT month_name, {product}
    FROM sales_history
    """

    graph_data = pd.read_sql(graph_query, db_con())

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8,5))
    plt.bar(
        graph_data["month_name"],
        graph_data[product]
    )

    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title(f"{product.capitalize()} Sales History")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ration_shop_stock/static/graph.png")
    plt.close()
    # ML Data
    query = f"""
    SELECT month_no, {product}
    FROM sales_history
    """

    data = pd.read_sql(query, db_con())

    X = data[['month_no']]
    y = data[product]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    current_month = data['month_no'].max()

    next_month = current_month + 1

    if next_month > 12:
        next_month = 1

    next_month_name = month_names[next_month]

    prediction =model.predict(
    pd.DataFrame(
        {'month_no': [next_month]}
    )
)

    return Response({
    "product": product,
    "next_month": next_month_name,
    "predicted_sales": round(float(prediction[0]), 2),
    "graph": "/static/graph.png"
})