import sqlite3
from sqlite3 import Error
import pandas as pd 

conn = sqlite3.connect('TestDB12.db')  
c = conn.cursor() 

c.execute('''CREATE TABLE Location([State_Code] INTEGER PRIMARY KEY,[AreaName]
VARCHAR(100))''')
c.execute('''CREATE TABLE Location_total([State_Code] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (State_Code) REFERENCES Location (State_Code))''')
c.execute('''CREATE TABLE Age_avg_val_gp([Age_gp] VARCHAR(50) PRIMARY
KEY,[avg_value] integer)''')
c.execute('''CREATE TABLE link_Ed_lang([id] INTEGER PRIMARY KEY,[State_Code] INTEGER,
[Section] VARCHAR(50),[Age_gp] VARCHAR(50),FOREIGN KEY (State_Code) REFERENCES Location
(State_Code))''')
c.execute('''CREATE TABLE Age_gp_pop([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_iilit([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_lit([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_lit_wo_Ed([id] INTEGER PRIMARY
KEY,[Tmales] INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang
(id))''')
c.execute('''CREATE TABLE Age_gp_bel_pri([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_pri([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_middle([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_sec([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_hsec([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_ntech_dip([id] INTEGER PRIMARY
KEY,[Tmales] INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang
(id))''')
c.execute('''CREATE TABLE Age_gp_tech_dip([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')
c.execute('''CREATE TABLE Age_gp_above_grad([id] INTEGER PRIMARY
KEY,[Tmales] INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang
(id))''')
c.execute('''CREATE TABLE Age_gp_unclassified([id] INTEGER PRIMARY KEY,[Tmales]
INTEGER, [Tfemales] integer,FOREIGN KEY (id) REFERENCES link_Ed_lang (id))''')

c.execute('''CREATE TABLE Ed_lang_vari([State_Code] INTEGER,[Section]
varchar(100), [Education_level] VARCHAR(100),[Males_bi_lang] integer,[Females_bi_lang]
integer,[Males_tri_lang] integer,[Females_tri_lang] integer,PRIMARY
KEY(State_Code,Section,Education_level),FOREIGN KEY (State_Code) REFERENCES
Location(State_Code))''')

c.execute('''CREATE TABLE Age_gr_lang_vari([State_Code] INTEGER,[Section]
varchar(100), [Age_gp] VARCHAR(50),[Males_bi_lang] integer,[Females_bi_lang]
integer,[Males_tri_lang] integer,[Females_tri_lang] integer,PRIMARY
KEY(State_Code,Section,Age_gp),FOREIGN KEY (State_Code) REFERENCES Location (State_Code))''')


conn.commit()

#starting Q1
conn = sqlite3.connect('TestDB10.db')  
c.execute(''' with casual1(State_Code,count3) as
(select State_Code, sum(Males_tri_lang+Females_tri_lang) from Ed_lang_vari where State_Code
!= 0 group by State_Code),
casual2(State_Code,countAll) as 
(select State_Code, Tmales + Tfemales from Location_total)
select L.areaName as State, (t1.count3*1.0/t2.countAll)*100 as percent from casual1
as t1, casual2 as t2,Location as L 
where t1.State_Code=t2.State_Code and t1.State_Code= L.State_Code order by percent''')
conn.commit()

#starting Q2
conn = sqlite3.connect('TestDB10.db')  
c = conn.cursor()
c.execute(''' with casual(Age_gp,count) as 
(select Age_gp, sum(Males_bi_lang+Females_bi_lang) from Age_gr_lang_vari where State_Code
!= 0 group by Age_gp)
select Age_gp from casual where count = (select max(count) from casual)''')
conn.commit()

#starting with Q3
conn = sqlite3.connect('TestDB10.db')  
c = conn.cursor()
c.execute(''' ''')
print(c.fetchall())
conn.commit()

#starting with Q4

conn = sqlite3.connect('TestDB10.db')  
c = conn.cursor()
c.execute(''' with count2(value2) as 
(select sum(Males_bi_lang+Females_bi_lang) from Age_gr_lang_vari where State_Code = 0),
count1(value1) as (select sum(Tmales+Tfemales) from Location_total)
select value1-value2 from count2,count1;''')

conn.commit()


