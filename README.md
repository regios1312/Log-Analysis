
-----------------------------------------------------
There are a total of 3 views created in this project:

Query1:Contains no views
-----------------------------------------------------
Query2:Contains 1 view:

Execute this command in sql:

create view q2 as select articles.slug,articles.author,count(path) as views from articles join log on substr(path,10) like concat(articles.slug,'%') group by articles.slug ,articles.author order by views desc;
-----------------------------------------------------
Query3:Contains 2 views:
Execute these command in sql:

View1:
create view q31 as select date(time) as date,count(status) from log where status like '40%' group by date order by date asc;
View2:
create view q32 as select date(time) as date,count(status) from log group by date;
