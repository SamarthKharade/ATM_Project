from flask import Flask, flash, render_template, request, redirect, url_for, session
import mysql.connector
import bcrypt

from sqlalchemy import VARCHAR
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secure_key"
pin3=None
name3=None
name4=None
pin4=None
db = None
cursor = None
user=None
user_id=None

db2 = None
cursor2 = None


        # Database connection
try:
           db = mysql.connector.connect(
           host="localhost",
           user="root",
           password="Samarth@2004",
           database="atm_db",
           auth_plugin='mysql_native_password')
           cursor = db.cursor()
           print("Database connected successfully!")
except:
    print("Database not connected!!!")

#Login route

@app.route("/", methods=["GET", "POST"])
def login():
    global pin3
    global name3
    global cursor
    global name4
    global pin4
    global user
    global db
  
    global user_id
    """Handle user login."""
    if request.method == "POST":

        # Get user data from the form
        name3= request.form.get("name3")
        pin3 = request.form.get("pin2")



        

      

        # Debugging: Print received values
        print(f"Received: name={name3}, pin={pin3}")

        # Validate required fields
        if not str(name3) or not int(pin3):
            flash("Both fields are required!", "danger")
            return render_template("login.html")

        # Database connection
        #db2 = None
        
        #cursor2 = None
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Samarth@2004",
                database="atm_db",
                auth_plugin='mysql_native_password'
            )
            cursor = db.cursor()
            print("Database connected successfully")
            # Check if user exists
            name3=name3.strip()
            bal=20
            try:
              cursor.execute('SELECT card,pin FROM users WHERE card =%s and pin=%s', (int(name3),int(pin3),))
              user=cursor.fetchone()
              db.commit()
              print(user)
            except mysql.connector.Error as err:
                flash(f"Database Error: {err}", "danger")
           
            try:
               
               name4=str(user[0])
               pin4=int(user[1])
            except:
                name4=""
                pin4=""

          

            # Debugging: Print user data
            
            pin3=int(pin3)
            print(type(pin3))
            print(type(pin4))
            print(type(name3))
            print(type(name4))
            if user:
                # Compare PIN against the stored hashed PIN
                print(type(name4))
                print(type(name3))
              
                if name3.strip()==name4.strip():
                    if pin3==pin4:
                     # Successful login
                      pin3=pin4
                      name3=name4
                      flash("Login successful!", "success")
                      print("Login successful")


                      cursor.execute("SELECT * FROM users WHERE pin = %s AND card = %s", (int(pin3), int(name3)))  
                      user = cursor.fetchone()  # Fetch the first matching user

                      if user:
                        session["user_id"] = user[0]  # Store user ID in session
                        session["authenticated"] = True  # Mark user as authenticated
                         #return redirect(url_for("/dashboard"))
                        return render_template("dashboard.html")
                else:
                    flash("Invalid PIN. Please try again.", "danger")
                    print("Invalid PIN")
            else:
                flash("User not found. Please sign up.", "danger")
                print("User not found")

        except mysql.connector.Error as err:
            flash(f"Database Error: {err}", "danger")
        '''finally:
            #if cursor2:
               # cursor2.close()
            if db:
                db.close()'''
  
    
        

    return render_template("login.html")

   
# Sign up route

@app.route("/signup", methods=["GET", "POST"])

def register():
    """Handle user registration."""
    if request.method == "POST":
        # Get user data from the form
        name = request.form.get("name")
        bank = request.form.get("bank")
        card = request.form.get("card_number")
        pin = request.form.get("pin")
        confirm_pin = request.form.get("confirm_pin")
        initial_balance = request.form.get("balance")

        # Debugging: Print received values
        print(f"Received: Name={name}, Bank={bank}, PIN={pin}, Confirm PIN={confirm_pin}, Balance={initial_balance}")

        # Validate required fields
        if not name or not bank or not pin or not confirm_pin or not initial_balance:
            flash("All fields are required!", "danger")
            return render_template("signup.html")

        # Validate PIN match
        if pin != confirm_pin:
            flash("PINs do not match. Please try again.", "danger")
            return render_template("signup.html")
        
        try:
            cursor.execute('SELECT card FROM users')
            rows = cursor.fetchall()

                             # Print all rows
            for row in rows:
                 if int(card) in row:
                    flash("Already have same atm card!!!", "danger")
                    return render_template("signup.html")
            db.commit()
            print(user)

        except:
            print("Did not fetch the card!!!")



        # Encrypt PIN for security (Optional)
        # hashed_pin = generate_password_hash(pin)  # Use this if storing hashed PINs
        try:
   
            # Insert into users table
           query = "INSERT INTO users (name2, bank, card, pin, balance) VALUES (%s, %s, %s, %s, %s)"
           cursor.execute(query, (name, bank, card , pin, initial_balance))
           db.commit()
           print("Registration successful!")
           flash("Registration successful!", "success")
           return redirect(url_for("login"))
           

        except mysql.connector.Error as err:
            # db.rollback()
            print(f"Database Error: {err}")
            flash(f"Database Error: {err}", "danger")

        ''' finally:
            if cursor:
                cursor.close()
            if db:
                db.close()'''

    return render_template("signup.html")


@app.route("/balance")
def balance():
    global pin3
    global name3
    global cursor
   
    
    cursor.execute("SELECT balance FROM users WHERE pin=%s and card=%s",(int(pin3),int(name3),))
    balance3= cursor.fetchone()
    print(balance3)
    balance=float(balance3[0])


    return render_template("balance.html", balance=balance)


@app.route("/chagepin", methods=["GET", "POST"])


def changepin():
    global pin3
    global name3
    global cursor
    if request.method == "POST":
        old_pin = request.form.get("old")
        confirm_new_pin = request.form.get("new")
        if int(old_pin) != pin3:
            flash("Old PIN do not match. Please try again.", "danger")
           
            return render_template("changepin.html")
        if old_pin == confirm_new_pin:
            flash("New PIN cannot be the same as the old PIN. Please try again.", "danger")
            return render_template("changepin.html")
        

        
       
        
        try:
            query = "UPDATE users SET pin = %s WHERE pin = %s and card=%s"
            cursor.execute(query, (confirm_new_pin, pin3, name3))
            db.commit()
            print("PIN changed successfully!")
            flash("PIN changed successfully!", "success")
            return redirect(url_for("login"))
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            flash(f"Database Error: {err}", "danger")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    return render_template("changepin.html")


@app.route("/withdrawl2", methods=["GET", "POST"])
def withdrawl2():
    global pin3
    global name3
    global cursor
    global user_id
    if request.method == "POST":
        amount = request.form.get("amount_withdraw")
       
        cursor.execute("SELECT balance FROM users WHERE pin=%s and card=%s",(int(pin3),int(name3),))
        balance4= cursor.fetchone()
        balance=float(balance4[0])
        if float(amount)>balance:
            flash("Insufficient balance", "danger")
            return render_template("withdrawl2.html")
        else:
            balance=balance-float(amount)
            query = "UPDATE users SET balance = %s WHERE pin = %s"
            cursor.execute(query, (balance, pin3))
            db.commit()
            print("Amount withdrawn successfully!")
            flash("Amount withdrawn successfully!", "success")
            user_id = session["user_id"]
            typ = "Withdrawal"
            cursor.execute(
            "INSERT INTO transactions (user_id, transaction_type, amount) VALUES (%s, %s, %s)",
            (user_id, typ, float(amount))

        )
            db.commit()
            return redirect(url_for("balance"))
    return render_template("withdrawl2.html")


@app.route("/deposit2", methods=["GET", "POST"])
def deposit2():
    global pin3
    global name3
    global cursor
    global user_id
    if request.method == "POST":
        amount = request.form.get("amount_deposit")
        cursor.execute("SELECT balance FROM users WHERE pin=%s and card=%s",(int(pin3),int(name3),))
        balance4= cursor.fetchone()
        balance=float(balance4[0])
        balance=balance+float(amount)
        query = "UPDATE users SET balance = %s WHERE pin = %s and card=%s"
        cursor.execute(query, (balance, pin3,name3))
        db.commit()
        print("Amount deposited successfully!")
        flash("Amount deposited successfully!", "success")
        user_id = session["user_id"]
        typ = "Deposit"
        cursor.execute(
            "INSERT INTO transactions (user_id, transaction_type, amount) VALUES (%s, %s, %s)",
            (user_id, typ, float(amount))

        )
        db.commit()
        return redirect(url_for("balance"))
    return render_template("deposit2.html")

@app.route("/transactions")
def transactions():
    global pin3
    global name3
    global cursor
    print("Transactions")

    
     

    

    

    if not session.get("authenticated"):
        return redirect(url_for("login"))

    user_id = session["user_id"]
    print(user_id)
    cursor.execute("SELECT id, transaction_type, amount, timestamp FROM transactions WHERE user_id = %s ORDER BY timestamp DESC", (int(user_id),))
    transactions = cursor.fetchall()
    for transaction in transactions:
       print(transaction) 

    return render_template("transactions.html", transactions=transactions)



@app.route("/dashboard")
def handle_image_click():
    image_id = request.args.get('image_id')  # Get the image_id from the URL parameter
    
    if image_id == 'image1':
        return redirect(url_for('balance'))
    elif image_id == 'image2':
        return redirect(url_for('deposit2'))
    elif image_id == 'image3':
        return redirect(url_for('withdrawl2'))
    elif image_id == 'image4':
        return redirect(url_for('changepin'))
    elif image_id == 'image5':
        return redirect(url_for('transactions'))
    else:
        print("Unknown image clicked!")

    # Redirect back to the main page or another page
    


    return render_template("dashboard.html")
   



       
            # Check if user exists
            
           

   






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
