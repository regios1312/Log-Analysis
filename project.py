import psycopg2


def query1():
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute("select articles.slug as title,count(path) as views from "
                + "articles join log on substr(path,10) like "
                + "concat(articles.slug,'%') "
                + "group by articles.slug order by views desc limit 3")
    results = cur.fetchall()
    print(results)
    conn.close()


def query2():
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    # cur.execute("create view q2 as select articles.slug,articles.author,
    #             count(path) as views from articles join log on
    #             substr(path,10) like concat(articles.slug,'%') group by
    #             articles.slug ,articles.author order by views desc")
    cur.execute(" select authors.name,sum(views) as views from authors "
                + "join q2 on authors.id=q2.author group "
                + "by authors.name order by views desc ")
    results = cur.fetchall()
    print(results)
    conn.close()


def query3():
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    # cur.execute("create view q31 as select date(time) as
    #             date,count(status) from log where status like '40%'
    #             group by date order by date asc")
    # cur.execute("create view q32 as select date(time) as date,count(status)
    #             from log group by date")
    cur.execute("select q31.date,trunc(q31.count*100.0/q32.count,2) as per "
                + "from q31,q32 where q31.date=q32.date and "
                + "trunc(q31.count*100.0/q32.count,2)>=1 ")
    results = cur.fetchall()
    print(results)
    conn.close()


query1()
query2()
query3()
