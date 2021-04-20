import pyrebase
import cv_19
import city_cv_19
import weather
import weather2
import time
from flask import Flask, render_template, request,url_for,redirect,send_from_directory
from datetime import date,timedelta

config = {
    "apiKey": "AIzaSyApzWwpFCSxBR-OwZke8jsOJ1s85viymMA",
    "authDomain": "start-3a884.firebaseapp.com",
    "databaseURL": "https://start-3a884-default-rtdb.firebaseio.com",
    "projectId": "start-3a884",
    "storageBucket": "start-3a884.appspot.com",
    "messagingSenderId": "189396804497",
    "appId": "1:189396804497:web:11b0d66e64a548c7c9f030"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols') 
app.jinja_env.globals.update(
    zip=zip, 
    enumerate=enumerate, 
) 

@app.route('/')
def index():
    key= request.args.get("keyword")
    if key=="-- 선택 --" or key is None:
        return render_template("index.html")
        
    else:    
        today_1 = date.today()
        today = today_1.strftime("%Y%m%d")
        yesterday_1 = today_1 - timedelta(days=1)
        yesterday = yesterday_1.strftime("%Y%m%d")
        time1 = time.strftime("%H%M")
        time2 = time.strftime("%H%M")
        w_1_time ="0000"
        w_2_time ="0000"

        time1 = int(time1)
        time2 = int(time2)
        

        if  0 <= time1 < 1000 :
            
            
            if 0 <= time1 < 210 :
                w_1_time = "2300"
            if 210 <= time1 <510 :
                w_1_time = "0200" 
            if 510 <= time1 <810 :
                w_1_time = "0500"
            if 810 <= time1 <=959 :
                w_1_time = "0800"

            if 0 <= time2 < 40:
                w_2_time = "2300"
            if 40 <= time2 < 140:
                w_2_time = "0000"
            if 140 <= time2 < 240:
                w_2_time = "0100"
            if 240 <= time2 < 340:
                w_2_time = "0200"
            if 340 <= time2 < 440:
                w_2_time = "0300"
            if 440 <= time2 < 540:
                w_2_time = "0400"
            if 540 <= time2 < 640:
                w_2_time = "0500"
            if 640 <= time2 < 740:
                w_2_time = "0600"
            if 740 <= time2 < 840:
                w_2_time = "0700"
            if 840 <= time2 < 940:
                w_2_time = "0800"
            if 940 <= time2 < 959:
                w_2_time = "0900"
            
            
        elif 1000 <= time1 < 2400 :
            
            if 1000<=time1 <1110:
                w_1_time = "0800"
            if 1110<=time1 <1410:
                w_1_time = "1100"
            if 1410<=time1 <1710:
                w_1_time = "1400"
            if 1710<=time1 <2010:
                w_1_time = "1700"
            if 2010<=time1 <2310:
                w_1_time = "2000"
            if 2310<=time1 <2400:
                w_1_time = "2300"


            if 1000<=time2 < 1040:
                w_2_time = "0900"
            if 1040<=time2 < 1140:
                w_2_time = "1000"
            if 1140<=time2 < 1240:
                w_2_time = "1100"
            if 1240<=time2 < 1340:
                w_2_time = "1200"
            if 1340<=time2 < 1440:
                w_2_time = "1300"
            if 1440<=time2 < 1540:
                w_2_time = "1400"
            if 1540<=time2 < 1640:
                w_2_time = "1500"
            if 1640<=time2 < 1740:
                w_2_time = "1600"
            if 1740<=time2 < 1840:
                w_2_time = "1700"
            if 1840<=time2 < 1940:
                w_2_time = "1800"
            if 1940<=time2 < 2040:
                w_2_time = "1900"
            if 2040<=time2 < 2140:
                w_2_time = "2000"
            if 2140<=time2 < 2240:
                w_2_time = "2100"
            if 2240<=time2 < 2340:
                w_2_time = "2200"
            if 2340<=time2 < 2400:
                w_2_time = "2300"


        data1 = cv_19.get_cv_19_data(today,today)
        data2 = city_cv_19.get_city_cv_19_data(today,today)
        data3 = weather.get_weather_data(today,key,w_1_time)
        data4 = weather2.get_weather2_data(today,key,w_2_time)
        if not data3:
            data3 = weather.get_weather_data(yesterday,key,w_1_time)
       
        if not data4:
            data4 = weather.get_weather_data(yesterday,key,w_1_time)
      

        if not data1 or not data2:
            yesterday_1 = today_1 - timedelta(days=1)
            yesterday = yesterday_1.strftime("%Y%m%d")

            time1 = time.strftime("%H%M")
            time2 = time.strftime("%H%M")
            w_1_time ="0000"
            w_2_time ="0000"
            
            time1 = int(time1)
            time2 = int(time2)
           

            
            

            if  0 <= time1 < 1000 :
                
                
                if 0 <= time1 < 210 :
                    w_1_time = "2300"
                if 210 <= time1 <510 :
                    w_1_time = "0200" 
                if 510 <= time1 <810 :
                    w_1_time = "0500"
                if 810 <= time1 <=959 :
                    w_1_time = "0800"

                if 0 <= time2 < 40:
                    w_2_time = "2300"
                if 40 <= time2 < 140:
                    w_2_time = "0000"
                if 140 <= time2 < 240:
                    w_2_time = "0100"
                if 240 <= time2 < 340:
                    w_2_time = "0200"
                if 340 <= time2 < 440:
                    w_2_time = "0300"
                if 440 <= time2 < 540:
                    w_2_time = "0400"
                if 540 <= time2 < 640:
                    w_2_time = "0500"
                if 640 <= time2 < 740:
                    w_2_time = "0600"
                if 740 <= time2 < 840:
                    w_2_time = "0700"
                if 840 <= time2 < 940:
                    w_2_time = "0800"
                if 940 <= time2 < 959:
                    w_2_time = "0900"
                
                
            elif 1000 <= time1 < 2400 :
                
                if 1000<=time1 <1110:
                    w_1_time = "0800"
                if 1110<=time1 <1410:
                    w_1_time = "1100"
                if 1410<=time1 <1710:
                    w_1_time = "1400"
                if 1710<=time1 <2010:
                    w_1_time = "1700"
                if 2010<=time1 <2310:
                    w_1_time = "2000"
                if 2310<=time1 <2400:
                    w_1_time = "2300"


                if 1000<=time2 < 1040:
                    w_2_time = "0900"
                if 1040<=time2 < 1140:
                    w_2_time = "1000"
                if 1140<=time2 < 1240:
                    w_2_time = "1100"
                if 1240<=time2 < 1340:
                    w_2_time = "1200"
                if 1340<=time2 < 1440:
                    w_2_time = "1300"
                if 1440<=time2 < 1540:
                    w_2_time = "1400"
                if 1540<=time2 < 1640:
                    w_2_time = "1500"
                if 1640<=time2 < 1740:
                    w_2_time = "1600"
                if 1740<=time2 < 1840:
                    w_2_time = "1700"
                if 1840<=time2 < 1940:
                    w_2_time = "1800"
                if 1940<=time2 < 2040:
                    w_2_time = "1900"
                if 2040<=time2 < 2140:
                    w_2_time = "2000"
                if 2140<=time2 < 2240:
                    w_2_time = "2100"
                if 2240<=time2 < 2340:
                    w_2_time = "2200"
                if 2340<=time2 < 2400:
                    w_2_time = "2300"
                
            data1 = cv_19.get_cv_19_data(yesterday,yesterday)
            data2 = city_cv_19.get_city_cv_19_data(yesterday,yesterday)
            data3 = weather.get_weather_data(today,key,w_1_time)
            data4 = weather2.get_weather2_data(today,key,w_2_time)
            if not data3:
                data3 = weather.get_weather_data(yesterday,key,w_1_time)
        
            if not data4:
                data4 = weather.get_weather_data(yesterday,key,w_1_time)
                


        return render_template("index.html",data1=data1,data2=data2,data3=data3,data4=data4,city=key) 


@app.route('/sitemap.xml')
@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])



@app.route('/memo')
def memo():
    
    return render_template('memo.html')

@app.route('/remove')
def remove():
    db.child(user).child("text").remove()
  
    return redirect(url_for("s_login"))

@app.route('/login', methods=['GET','POST'])
def login():
    unsuccess1 = "로그인 실패"
    unsuccess2 = "아이디와 비밀번호를 확인해주세요."
    
    
    if request.method == 'POST':
        global email
        email = request.form['name']
        password = request.form['pw']
        try:
            auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for("s_index"))
        except:
            return render_template('login.html', us1=unsuccess1, us2=unsuccess2)
    return render_template('login.html')

@app.route('/join', methods=['GET','POST'])
def join():
    unsuccess3 = "가입 실패"
    unsuccess4 = "아이디와 비밀번호를 확인해주세요."
    
    
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pw']
        try:
            auth.create_user_with_email_and_password(email,password)
            return redirect(url_for("memo"))
        except:
            return render_template('join.html', us3=unsuccess3, us4=unsuccess4)
    return render_template('join.html')


@app.route('/s_login', methods=['GET', 'POST'])
def s_login():
    global user
    user = email[:email.index("@")]
    text = db.child(user).child('text').get() 
    try:
        text_list = text.val()[1:]
    except:
        text_list = text.val()
    try:
    #text를 입력하면 db에 저장하고 저장한값의 value값을 html로 전송
        if request.method == 'POST':
            try:
                g = len(text_list)+1
            except:
                g = 1
            
            memo = request.form['memo']
            db.child(user).child("text").update({f"{g}": memo })
            text = db.child(user).child('text').get()
        
            try:
                text_list = text.val()[1:]
            except:
                text_list = text.val()
            return render_template('s_login.html', text=text_list)  
        else:
            return render_template('s_login.html', text=text_list)
    except:
        return render_template('s_login.html')


@app.route('/modify', methods=['GET', 'POST'])
def modify():
    global user
    user = email[:email.index("@")]
    text = db.child(user).child('text').get() 
    try:
        text_list = text.val()[1:]
    except:
        text_list = text.val()
    try:
    #text를 입력하면 db에 저장하고 저장한값의 value값을 html로 전송
        if request.method == 'POST':
            
            
            memo = request.form['memo']
            chbx= request.form["chbx"]
            db.child(user).child("text").update({f"{chbx}": memo })
            text = db.child(user).child('text').get()
            
            try:
                text_list = text.val()[1:]
            except:
                text_list = text.val()
            return render_template('modify.html', text=text_list)  
        else:
            return render_template('modify.html', text=text_list)
    except:
        return render_template('modify.html')


@app.route('/s_index')
def s_index():
    global user
    user = email[:email.index("@")]
    key= request.args.get("keyword")
    text = db.child(user).child('text').get() 
    try:
        text_list = text.val()[1:]
    except:
        text_list = text.val()
    try:
        if key=="-- 선택 --" or key is None:
            return render_template("s_index.html", text=text_list)
            
        else:    
            today_1 = date.today()
            today = today_1.strftime("%Y%m%d")
            yesterday_1 = today_1 - timedelta(days=1)
            yesterday = yesterday_1.strftime("%Y%m%d")
            time1 = time.strftime("%H%M")
            time2 = time.strftime("%H%M")
            w_1_time ="0000"
            w_2_time ="0000"

            time1 = int(time1)
            time2 = int(time2)
            

            if  0 <= time1 < 1000 :
                
                
                if 0 <= time1 < 210 :
                    w_1_time = "2300"
                if 210 <= time1 <510 :
                    w_1_time = "0200" 
                if 510 <= time1 <810 :
                    w_1_time = "0500"
                if 810 <= time1 <=959 :
                    w_1_time = "0800"

                if 0 <= time2 < 40:
                    w_2_time = "2300"
                if 40 <= time2 < 140:
                    w_2_time = "0000"
                if 140 <= time2 < 240:
                    w_2_time = "0100"
                if 240 <= time2 < 340:
                    w_2_time = "0200"
                if 340 <= time2 < 440:
                    w_2_time = "0300"
                if 440 <= time2 < 540:
                    w_2_time = "0400"
                if 540 <= time2 < 640:
                    w_2_time = "0500"
                if 640 <= time2 < 740:
                    w_2_time = "0600"
                if 740 <= time2 < 840:
                    w_2_time = "0700"
                if 840 <= time2 < 940:
                    w_2_time = "0800"
                if 940 <= time2 < 959:
                    w_2_time = "0900"
                
                
            elif 1000 <= time1 < 2400 :
                
                if 1000<=time1 <1110:
                    w_1_time = "0800"
                if 1110<=time1 <1410:
                    w_1_time = "1100"
                if 1410<=time1 <1710:
                    w_1_time = "1400"
                if 1710<=time1 <2010:
                    w_1_time = "1700"
                if 2010<=time1 <2310:
                    w_1_time = "2000"
                if 2310<=time1 <2400:
                    w_1_time = "2300"


                if 1000<=time2 < 1040:
                    w_2_time = "0900"
                if 1040<=time2 < 1140:
                    w_2_time = "1000"
                if 1140<=time2 < 1240:
                    w_2_time = "1100"
                if 1240<=time2 < 1340:
                    w_2_time = "1200"
                if 1340<=time2 < 1440:
                    w_2_time = "1300"
                if 1440<=time2 < 1540:
                    w_2_time = "1400"
                if 1540<=time2 < 1640:
                    w_2_time = "1500"
                if 1640<=time2 < 1740:
                    w_2_time = "1600"
                if 1740<=time2 < 1840:
                    w_2_time = "1700"
                if 1840<=time2 < 1940:
                    w_2_time = "1800"
                if 1940<=time2 < 2040:
                    w_2_time = "1900"
                if 2040<=time2 < 2140:
                    w_2_time = "2000"
                if 2140<=time2 < 2240:
                    w_2_time = "2100"
                if 2240<=time2 < 2340:
                    w_2_time = "2200"
                if 2340<=time2 < 2400:
                    w_2_time = "2300"


            data1 = cv_19.get_cv_19_data(today,today)
            data2 = city_cv_19.get_city_cv_19_data(today,today)
            data3 = weather.get_weather_data(today,key,w_1_time)
            data4 = weather2.get_weather2_data(today,key,w_2_time)
            if not data3:
                data3 = weather.get_weather_data(yesterday,key,w_1_time)
        
            if not data4:
                data4 = weather.get_weather_data(yesterday,key,w_1_time)

            if not data1 or not data2:
                yesterday_1 = today_1 - timedelta(days=1)
                yesterday = yesterday_1.strftime("%Y%m%d")

                time1 = time.strftime("%H%M")
                time2 = time.strftime("%H%M")
                w_1_time ="0000"
                w_2_time ="0000"
                
                time1 = int(time1)
                time2 = int(time2)
            

                
                

                if  0 <= time1 < 1000 :
                    
                    
                    if 0 <= time1 < 210 :
                        w_1_time = "2300"
                    if 210 <= time1 <510 :
                        w_1_time = "0200" 
                    if 510 <= time1 <810 :
                        w_1_time = "0500"
                    if 810 <= time1 <=959 :
                        w_1_time = "0800"

                    if 0 <= time2 < 40:
                        w_2_time = "2300"
                    if 40 <= time2 < 140:
                        w_2_time = "0000"
                    if 140 <= time2 < 240:
                        w_2_time = "0100"
                    if 240 <= time2 < 340:
                        w_2_time = "0200"
                    if 340 <= time2 < 440:
                        w_2_time = "0300"
                    if 440 <= time2 < 540:
                        w_2_time = "0400"
                    if 540 <= time2 < 640:
                        w_2_time = "0500"
                    if 640 <= time2 < 740:
                        w_2_time = "0600"
                    if 740 <= time2 < 840:
                        w_2_time = "0700"
                    if 840 <= time2 < 940:
                        w_2_time = "0800"
                    if 940 <= time2 < 959:
                        w_2_time = "0900"
                    
                    
                elif 1000 <= time1 < 2400 :
                    
                    if 1000<=time1 <1110:
                        w_1_time = "0800"
                    if 1110<=time1 <1410:
                        w_1_time = "1100"
                    if 1410<=time1 <1710:
                        w_1_time = "1400"
                    if 1710<=time1 <2010:
                        w_1_time = "1700"
                    if 2010<=time1 <2310:
                        w_1_time = "2000"
                    if 2310<=time1 <2400:
                        w_1_time = "2300"


                    if 1000<=time2 < 1040:
                        w_2_time = "0900"
                    if 1040<=time2 < 1140:
                        w_2_time = "1000"
                    if 1140<=time2 < 1240:
                        w_2_time = "1100"
                    if 1240<=time2 < 1340:
                        w_2_time = "1200"
                    if 1340<=time2 < 1440:
                        w_2_time = "1300"
                    if 1440<=time2 < 1540:
                        w_2_time = "1400"
                    if 1540<=time2 < 1640:
                        w_2_time = "1500"
                    if 1640<=time2 < 1740:
                        w_2_time = "1600"
                    if 1740<=time2 < 1840:
                        w_2_time = "1700"
                    if 1840<=time2 < 1940:
                        w_2_time = "1800"
                    if 1940<=time2 < 2040:
                        w_2_time = "1900"
                    if 2040<=time2 < 2140:
                        w_2_time = "2000"
                    if 2140<=time2 < 2240:
                        w_2_time = "2100"
                    if 2240<=time2 < 2340:
                        w_2_time = "2200"
                    if 2340<=time2 < 2400:
                        w_2_time = "2300"
                    
                data1 = cv_19.get_cv_19_data(yesterday,yesterday)
                data2 = city_cv_19.get_city_cv_19_data(yesterday,yesterday)
                data3 = weather.get_weather_data(today,key,w_1_time)
                data4 = weather2.get_weather2_data(today,key,w_2_time)
                if not data3:
                    data3 = weather.get_weather_data(yesterday,key,w_1_time)
            
                if not data4:
                    data4 = weather.get_weather_data(yesterday,key,w_1_time)
                        


            return render_template("s_index.html",data1=data1,data2=data2,data3=data3,data4=data4,city=key,text=text_list) 


    except:
        return render_template('s_index.html')


if __name__ == "__main__":
    app.run(debug=True)


