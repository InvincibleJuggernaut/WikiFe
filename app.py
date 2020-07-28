from flask import Flask, render_template, request
from datetime import date, timedelta
import urllib3
import json
import wikipedia

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/", methods=['POST'])
def search():
    global search_query
    search_query=request.form['query']
    try:
        global result
        result = wikipedia.search(search_query, results=16)
        return render_template('results.html', result0=result[0],
                           result1 = result[1],
                           result2 = result[2],
                           result3 = result[3],
                           result4 = result[4],
                           result5=result[5],
                           result6=result[6],
                           result7=result[7],
                           result8=result[8],
                           result9=result[9],
                           result10=result[10],
                           result11=result[11],
                           result12=result[12],
                           result13=result[13],
                           result14=result[14],
                           result15=result[15],
                           link0 = 'https://en.wikipedia.org/wiki/'+(result[0].replace(" ","_")),
                           link1 = 'https://en.wikipedia.org/wiki/'+(result[1].replace(" ","_")),
                           link2 = 'https://en.wikipedia.org/wiki/'+(result[2].replace(" ","_")),
                           link3 = 'https://en.wikipedia.org/wiki/'+(result[3].replace(" ","_")),
                           link4 = 'https://en.wikipedia.org/wiki/'+(result[4].replace(" ","_")),
                           link5='https://en.wikipedia.org/wiki/' + (result[5].replace(" ", "_")),
                           link6='https://en.wikipedia.org/wiki/' + (result[6].replace(" ", "_")),
                           link7='https://en.wikipedia.org/wiki/' + (result[7].replace(" ", "_")),
                           link8='https://en.wikipedia.org/wiki/' + (result[8].replace(" ", "_")),
                           link9='https://en.wikipedia.org/wiki/' + (result[9].replace(" ", "_")),
                           link10='https://en.wikipedia.org/wiki/' + (result[10].replace(" ", "_")),
                           link11='https://en.wikipedia.org/wiki/' + (result[11].replace(" ", "_")),
                           link12='https://en.wikipedia.org/wiki/' + (result[12].replace(" ", "_")),
                           link13='https://en.wikipedia.org/wiki/' + (result[13].replace(" ", "_")),
                           link14='https://en.wikipedia.org/wiki/' + (result[14].replace(" ", "_")),
                           link15='https://en.wikipedia.org/wiki/' + (result[15].replace(" ", "_"))
                           )
    except (IndexError, wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.HTTPTimeoutError, wikipedia.exceptions.PageError, wikipedia.exceptions.RedirectError, wikipedia.exceptions.WikipediaException):
        return render_template("exceptions.html")


@app.route("/info0.html")
def info0():
    info0=wikipedia.summary(result[0])
    return render_template('info0.html', info_0=info0, info_0_head=result[0])

@app.route("/info1.html")
def info1():
    info1 = wikipedia.summary(result[1])
    return render_template('info1.html', info_1=info1, info_1_head=result[1])

@app.route("/info2.html")
def info2():
    info2 = wikipedia.summary(result[2])
    return render_template('info2.html', info_2=info2, info_2_head=result[2])

@app.route("/info3.html")
def info3():
    info3 = wikipedia.summary(result[3])
    return render_template('info3.html', info_3=info3, info_3_head=result[3])

@app.route("/info4.html")
def info4():
    info4 = wikipedia.summary(result[4])
    return render_template('info4.html', info_4=info4, info_4_head=result[4])

@app.route("/info5.html")
def info5():
    info5 = wikipedia.summary(result[5])
    return render_template('info5.html', info_5=info5, info_5_head=result[5])

@app.route("/info6.html")
def info6():
    info6 = wikipedia.summary(result[6])
    return render_template('info6.html', info_6=info6, info_6_head=result[6])

@app.route("/info7.html")
def info7():
    info7 = wikipedia.summary(result[7])
    return render_template('info7.html', info_7=info7, info_7_head=result[7])

@app.route("/info8.html")
def info8():
    info8 = wikipedia.summary(result[8])
    return render_template('info8.html', info_8=info8, info_8_head=result[8])

@app.route("/info9.html")
def info9():
    info9 = wikipedia.summary(result[9])
    return render_template('info9.html', info_9=info9, info_9_head=result[9])

@app.route("/info10.html")
def info10():
    info10 = wikipedia.summary(result[10])
    return render_template('info10.html', info_10=info10, info_10_head=result[10])

@app.route("/info11.html")
def info11():
    info11 = wikipedia.summary(result[11])
    return render_template('info11.html', info_11=info11, info_11_head=result[11])

@app.route("/info12.html")
def info12():
    info12 = wikipedia.summary(result[12])
    return render_template('info12.html', info_12=info12, info_12_head=result[12])

@app.route("/info13.html")
def info13():
    info13 = wikipedia.summary(result[13])
    return render_template('info13.html', info_13=info13, info_13_head=result[13])

@app.route("/info14.html")
def info14():
    info14 = wikipedia.summary(result[14])
    return render_template('info14.html', info_14=info14, info_14_head=result[14])

@app.route("/info15.html")
def info15():
    info15 = wikipedia.summary(result[15])
    return render_template('info15.html', info_15=info15, info_15_head=result[15])

@app.route("/trending.html")
def trending():
    list_of_topics=[]
    list_of_views=[]
    list_of_links=[]
    yesterday=date.today() - timedelta(days=1)
    yesterday_date_ordered=yesterday.strftime("%Y/%m/%d")
    url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/' + yesterday_date_ordered
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    data=json.loads(r.data.decode('utf-8'))
    check=0
    for x in data['items'][0]['articles']:
            if(x['article']!='Main_Page' and x['article']!='Special:Search' and check<=19):
                redirect_url = 'https://en.wikipedia.org/wiki/'+x['article']
                x['article']=x['article'].replace("_"," ")
                list_of_topics.append(x['article'])
                list_of_views.append(x['views'])
                list_of_links.append(redirect_url)
                check+=1

    return render_template('trending.html', top=list_of_topics, view=list_of_views, link=list_of_links)

@app.route("/timetravel.html")
def timetravel():
    return render_template('timetravel.html')

@app.route("/timetravel.html", methods=['POST'])
def timetravelresults():
        list_of_topics=[]
        list_of_views=[]
        list_of_links=[]
        day_in_order=request.form['dayinput']
        url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/' + day_in_order
        http=urllib3.PoolManager()
        r=http.request('GET', url)    
        data=json.loads(r.data.decode('utf-8'))
        counter=0
        for x in data['items'][0]['articles']:
            if(x['article']!='Main_Page' and x['article']!='Special:Search' and counter<=19):
                redirect_url = 'https://en.wikipedia.org/wiki/'+x['article']
                x['article']=x['article'].replace("_"," ")
                list_of_topics.append(x['article'])
                list_of_views.append(x['views'])
                list_of_links.append(redirect_url)
                counter+=1
        return render_template("timetravelresults.html", top=list_of_topics, view=list_of_views, link=list_of_links)    
 
if __name__=="__main__":
    app.run(debug=True)
