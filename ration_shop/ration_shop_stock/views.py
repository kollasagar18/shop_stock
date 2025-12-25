from django.shortcuts import render
from django.http import HttpResponse
from .db import db_con
from rest_framework.decorators import api_view

# ---------------- HOME PAGES ----------------

def home(request):
    return render(request, "home.html")

def sale(request):
    return render(request, "sale.html")

def buy(request):
    return render(request, "buy.html")

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

        # jowar
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
