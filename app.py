from flask import Flask, render_template, request, flash
from cassandra.cluster import Cluster

app = Flask(__name__)

cluster = Cluster()

session = cluster.connect('booking_keyspace')
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
'11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
'23', '24', '25', '26', '27', '28', '29', '30', '31']

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
'11', '12']

time_slot = ['7.00pm-8.30pm', '8.30pm-10.00pm', '10.00pm-11.30pm']


@app.route('/')
def index():
    return render_template('index.html', day_len = len(day),
    month_len = len(month), time_slot_len = len(time_slot), 
    day = day, month = month, time_slot = time_slot)

@app.route('/table', methods=["GET", "POST"])
def table():
    day = request.form.get("day")
    month = request.form.get("month")
    year = request.form.get("year")
    date = year + "-" + month + "-" + day
    time_slot = request.form.get("time_slot")
    rows = session.execute("SELECT * FROM customer_by_tableno_datetime")
    table1_booked = ""
    table2_booked = ""
    table3_booked = ""
    table4_booked = ""
    table5_booked = ""
    table6_booked = ""
    for row in rows:
        if str(row.time_begin) == "19:00:00.000000000" and str(row.time_end) == "20:30:00.000000000":
            check_time = "7.00pm-8.30pm"
        elif str(row.time_begin) == "20:30:00.000000000" and str(row.time_end) == "22:00:00.000000000":
            check_time = "8.30pm-10.00pm"
        else:
            check_time = "10.00pm-11.30pm"
        check_date = str(row.booking_date)
        if time_slot == check_time and date == check_date :
            table = row.table_no
            if table == "table 1":
                table1_booked = "disabled"
            if table == "table 2":
                table2_booked = "disabled"
            if table == "table 3":
                table3_booked = "disabled"
            if table == "table 4":
                table4_booked = "disabled"
            if table == "table 5":
                table5_booked = "disabled"
            if table == "table 6":
                table6_booked = "disabled"

    return render_template('table.html',  date = date, time_slot = time_slot, table1_booked = table1_booked, table2_booked = table2_booked, 
    table3_booked = table3_booked, table4_booked = table4_booked, table5_booked = table5_booked, table6_booked = table6_booked)
    

@app.route('/form', methods=["GET", "POST"])
def form():
    date = request.form.get("date")
    time_slot = request.form.get("time_slot")
    table = request.form.get("table")
    added=""
    exist = False
    if time_slot=="7.00pm-8.30pm":
        start_time = '19:00:00'
        end_time = '20:30:00'
    elif time_slot=="8.30pm-10.00pm":
        start_time = '20:30:00'
        end_time = '22:00:00'
    else: 
        start_time = '22:00:00'
        end_time = '23:30:00'  
    name = request.form.get("name")
    phone = request.form.get("phone")
    if bool(name) == True and bool(phone) == True:
        rows = session.execute("SELECT * FROM customer_by_tableno_datetime")
        for row in rows:
            if str(row.time_begin) == "19:00:00.000000000" and str(row.time_end) == "20:30:00.000000000":
                time = "7.00pm-8.30pm"
            elif str(row.time_begin) == "20:30:00.000000000" and str(row.time_end) == "22:00:00.000000000":
                time = "8.30pm-10.00pm"
            else:
                time = "10.00pm-11.30pm"
            if date == str(row.booking_date) and time_slot == time and table == row.table_no:
                exist = True

        if exist == True:
            flash('The reservation was taken', category='error')
        elif exist == False:
            session.execute("INSERT INTO customer_by_tableno_datetime (customer_id, customer_name, customer_phone, booking_date, table_no, time_begin, time_end) VALUES (uuid(), '" + name + "', '" + phone + "', '" + date + "', '" + table + "', '" + start_time + "', '" + end_time + "') IF NOT EXISTS")
            flash('Booking added!', category='success')
        added = "disabled"
        return render_template("form.html", added = added)
    else:
        return render_template("form.html", date = date, time_slot = time_slot, table = table)

@app.route('/admin')
def admin():
    rows = session.execute("SELECT * FROM customer_by_tableno_datetime")
    class customer:
        def __init__(self, id, booking_date, name, phone, table_no, time):
            self.id = id
            self.booking_date = booking_date
            self.name = name
            self.phone = phone
            self.table_no = table_no
            self.time = time
        
    customer_list = []

    for row in rows:
        if str(row.time_begin) == "19:00:00.000000000" and str(row.time_end) == "20:30:00.000000000":
            time = "7.00pm-8.30pm"
        elif str(row.time_begin) == "20:30:00.000000000" and str(row.time_end) == "22:00:00.000000000":
            time = "8.30pm-10.00pm"
        else:
            time = "10.00pm-11.30pm"
        customer_list.append(customer(row.customer_id, row.booking_date, row.customer_name, row.customer_phone, row.table_no, time))
    customer_list_len = len(customer_list)
    return render_template('admin.html', customer_list_len = customer_list_len, customer_list = customer_list)

@app.route('/delete', methods=["GET", "POST"])
def delete():
    booking_date = request.form.get("booking_date")
    table_no = request.form.get("table_no")
    time_slot = request.form.get("time")
    if time_slot=="7.00pm-8.30pm":
        start_time = '19:00:00'
        end_time = '20:30:00'
    elif time_slot=="8.30pm-10.00pm":
        start_time = '20:30:00'
        end_time = '22:00:00'
    else: 
        start_time = '22:00:00'
        end_time = '23:30:00'  
    session.execute("DELETE FROM customer_by_tableno_datetime WHERE booking_date='" + booking_date + "' and table_no='" + table_no + "' and time_begin='" + start_time + "' and time_end='" + end_time + "' IF EXISTS")
    return admin()

@app.route('/edit', methods=["GET", "POST"])
def edit():
    old_name = request.form.get("old_name")
    name = request.form.get("name")
    old_phone = request.form.get("old_phone")
    phone = request.form.get("phone")
    booking_date = request.form.get("booking_date")
    table_no = request.form.get("table_no")
    time_slot = request.form.get("time")
    if time_slot=="7.00pm-8.30pm":
        start_time = '19:00:00'
        end_time = '20:30:00'
    elif time_slot=="8.30pm-10.00pm":
        start_time = '20:30:00'
        end_time = '22:00:00'
    else: 
        start_time = '22:00:00'
        end_time = '23:30:00'  
    if bool(name) == True:
        session.execute("UPDATE customer_by_tableno_datetime SET customer_name='" + name + "'" + " WHERE booking_date='" + booking_date + "' and table_no='" + table_no + "' and time_begin='" + start_time + "' and time_end='" + end_time + "' IF customer_name='" + old_name + "'")
    elif bool(phone) == True:
        session.execute("UPDATE customer_by_tableno_datetime SET customer_phone='" + phone + "' " + "WHERE booking_date='" + booking_date + "' and table_no='" + table_no + "' and time_begin='" + start_time + "' and time_end='" + end_time + "' IF customer_phone='" + old_phone + "'")
    return admin()

if __name__ == "__main__":
    app.run(debug=True)