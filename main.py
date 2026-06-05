from db import db_con
def sale_stack():
    db = db_con()
    cu = db.cursor()

    try:

        ri = int(input("Enter Rice: "))
        su = int(input("Enter Sugar: "))
        pa = int(input("Enter Palmolein Oil: "))
        re = int(input("Enter Red Gram Dal: "))
        jo = int(input("Enter Jowar: "))
        ra = int(input("Enter Raagi: "))

        # Rice
        cu.execute("SELECT stock FROM ratio_shop_stock WHERE items=%s", ("rice",))
        rice = cu.fetchall()

        if int(rice[0][0]) >= ri:
            s = int(rice[0][0]) - ri
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "rice")
            )
        else:
            return f"Out of stock. Rice available: {rice[0][0]}"

        # Sugar
        cu.execute("SELECT stock FROM ratio_shop_stock WHERE items=%s", ("sugar",))
        sugar = cu.fetchall()

        if int(sugar[0][0]) >= su:
            s = int(sugar[0][0]) - su
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "sugar")
            )
        else:
            return f"Out of stock. Sugar available: {sugar[0][0]}"

        # Palmolein Oil
        cu.execute(
            "SELECT stock FROM ratio_shop_stock WHERE items=%s",
            ("palmolein_oil",)
        )
        palmolein_oil = cu.fetchall()

        if int(palmolein_oil[0][0]) >= pa:
            s = int(palmolein_oil[0][0]) - pa
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "palmolein_oil")
            )
        else:
            return f"Out of stock. Palmolein Oil available: {palmolein_oil[0][0]}"

        # Red Gram Dal
        cu.execute(
            "SELECT stock FROM ratio_shop_stock WHERE items=%s",
            ("red_gram_dal",)
        )
        red_gram_dal = cu.fetchall()

        if int(red_gram_dal[0][0]) >= re:
            s = int(red_gram_dal[0][0]) - re
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "red_gram_dal")
            )
        else:
            return f"Out of stock. Red Gram Dal available: {red_gram_dal[0][0]}"

        # Jowar
        cu.execute("SELECT stock FROM ratio_shop_stock WHERE items=%s", ("jowar",))
        jowar = cu.fetchall()

        if int(jowar[0][0]) >= jo:
            s = int(jowar[0][0]) - jo
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "jowar")
            )
        else:
            return f"Out of stock. Jowar available: {jowar[0][0]}"

        # Raagi
        cu.execute("SELECT stock FROM ratio_shop_stock WHERE items=%s", ("raagi",))
        raagi = cu.fetchall()

        if int(raagi[0][0]) >= ra:
            s = int(raagi[0][0]) - ra
            cu.execute(
                "UPDATE ratio_shop_stock SET stock=%s WHERE items=%s",
                (s, "raagi")
            )
        else:
            return f"Out of stock. Raagi available: {raagi[0][0]}"

        db.commit()

        cu.execute("SELECT * FROM ratio_shop_stock")
        data = cu.fetchall()

        return data

    except ValueError:
        return "Please enter numbers only"

    finally:
        cu.close()
        db.close()