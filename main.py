from db import db_con
def bye_stack():
    db=db_con()
    cu=db.cursor()
    
    try:
        ri=int(input("enter tha rice :-"))
        su=int(input("enter tha suger:-"))
        pa=int(input("enter tha palmolein_oil:-"))
        re=int(input("enter tha red_gram_dal:-"))
        jo = int(input("enter tha jowar:- "))
        ra =int(input("enter tha raagi :-"))
        
        
        
    
    
    # rice
        cu.execute("select stock from ratio_shop_stock where items=%s ",("rice",))
        rice=cu.fetchall()
        print(rice)
       
        s=int(rice[0][0])+ri
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"rice",))
        
        #sugar 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("sugar",))
        sugar =cu.fetchall()
        s=int(sugar[0][0])+su
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"sugar",))
        
        #palmolein_oil
        cu.execute("select stock from ratio_shop_stock where items=%s ",("palmolein_oil",))
        palmolein_oil=cu.fetchall()
        s=int(palmolein_oil[0][0])+pa
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"palmolein_oil",))
        
        #red_gram_dal
        cu.execute("select stock from ratio_shop_stock where items=%s ",("red_gram_dal",))
        red_gram_dal=cu.fetchall()
       
        s=int(red_gram_dal[0][0])+re
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"red_gram_dal",))
        
        #jowar 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("jowar",))
        jowar=cu.fetchall()
        print(jowar)
        s=int(jowar[0][0])+jo
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"jowar",))
        
        #raagi 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("raagi",))
        raagi=cu.fetchall()
        s=int(raagi[0][0])+ra
        cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"raagi",))
        
        db.commit()
        cu.execute("select * from ratio_shop_stock ")
        data=cu.fetchall()
        return(data)
    
    except ValueError:
        return("enter tha numbers")  
    finally:
        cu.close()
        db.close()
    
 
def get_stacl():
    from db import db_con
    import matplotlib.pyplot as m
    import pandas as p
    qu="select * from ratio_shop_stock"
    data=p.read_sql(qu,db_con())

    bars=m.bar(data["items"],data["stock"])
    m.xlabel("Items")
    m.ylabel("Stock")
    m.title("Ration Shop Stock")
    m.xticks(rotation=45)

    # 🔥 THIS LINE SHOWS VALUES ON TOP
    m.bar_label(bars)


    m.show()




def sale_stack():
    db=db_con()
    cu=db.cursor()
    try:
        
        ri=int(input("enter tha rice :-"))
        su=int(input("enter tha suger:-"))
        pa=int(input("enter tha palmolein_oil:-"))
        re=int(input("enter tha red_gram_dal:-"))
        jo = int(input("enter tha jowar:- "))
        ra =int(input("enter tha raagi :-"))
        
        
        
    
    
    # rice
        cu.execute("select stock from ratio_shop_stock where items=%s ",("rice",))
        rice=cu.fetchall()
        if int(rice[0][0]) >= ri:
            s=int(rice[0][0])-ri
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"rice",))
        else:
            return f" out of stact rice have {int(rice[0][0])}"
        
            
       
        
        #sugar 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("sugar",))
        sugar =cu.fetchall()
        if int(sugar[0][0])>=su:
            
            s=int(sugar[0][0])-su
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"sugar",))
        else:
            print(int(sugar[0][0]))
            return "out of stack sugar"
        #palmolein_oil
        
        cu.execute("select stock from ratio_shop_stock where items=%s ",("palmolein_oil",))
        palmolein_oil=cu.fetchall()
        if int(palmolein_oil[0][0])>=pa:
            s=int(palmolein_oil[0][0])+pa
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"palmolein_oil",))
        else:
            return "out of stack palmoin_oil"
            
        
        
        #red_gram_dal
        cu.execute("select stock from ratio_shop_stock where items=%s ",("red_gram_dal",))
        red_gram_dal=cu.fetchall()
        
        if int(red_gram_dal[0][0])>= re:
            s=int(red_gram_dal[0][0])-re
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"red_gram_dal",))
        else:
            return "out of stack red_gram_dal"
            
        
        #jowar 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("jowar",))
        jowar=cu.fetchall()
        if int(jowar[0][0])>=jo:
            s=int(jowar[0][0])-jo
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"jowar",))
        else:
            return "out of stack jowar"
        
        #raagi 
        cu.execute("select stock from ratio_shop_stock where items=%s ",("raagi",))
        raagi=cu.fetchall()
        if int(raagi[0][0])>=ra:
            s=int(raagi[0][0])+ra
            cu.execute("update ratio_shop_stock set stock=%s where items=%s ",(s,"raagi",))
        else:
            return " out of stack raagi"
        
        db.commit()
        cu.execute("select * from ratio_shop_stock ")
        data=cu.fetchall()
        return(data)

    except ValueError:
        return("enter tha numbers")  
    finally:
        cu.close()
        db.close()
if __name__ == "__main__":
    print("Application Started")