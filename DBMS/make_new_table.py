import sqlite3
from sqlite3 import Error
import pandas as pd 

Age_Ed = pd.read_csv("age-education.csv", header=None)
Mul_Age = pd.read_csv("multilingual-age.csv", header=None)
Mul_Ed = pd.read_csv("multilingual-education.csv", header=None)

Age_Ed = Age_Ed.loc[7:]
Mul_Age = Mul_Age.loc[5:]
Mul_Ed = Mul_Ed.loc[5:]
#print(Mul_Age)

i = 0
columns1=['table','State_Code','District_Code','AreaName','Section','Age_gp','Tot_person','Tmales','Tfemales','Illit_person','Illit_males','Illit_females','Lit_person','Lit_males','Lit_females','Lit_per_wo_Ed','Lit_males_wo_Ed','Lit_females_wo_Ed','Persons_bel_pri','Males_bel_pri','Females_bel_pri','Person_pri','Males_pri','Female_pri','Person_middle','Males_middle','Female_middle','Person_mat_sec','Males_mat_sec','Female_mat_sec','Person_high_sec','Males_high_sec','Females_high_sec','Person_wrt_ntech_dip','Males_wrt_ntech_dip','Females_wrt_ntech_dip','Person_wrt_tech_dip','Males_wrt_tech_dip','Females_wrt_tech_dip','Person_plus_grad','Males_above_grad','Females_above_grad','Person_other','Males_other','Females_other']
Age_Ed_mod= pd.DataFrame(columns = columns1)
while i<45 : 
    Age_Ed_mod[columns1[i]] = Age_Ed[i]
    i = i+1

j = 0
columns2=['State_Code','District_Code','AreaName','Section','Age_gp','Person_bi_lang','Males_bi_lang','Females_bi_lang','Person_tri_lang','Males_tri_lang','Females_tri_lang']
Mul_Age_mod = pd.DataFrame(columns =columns2)
while j<11 : 
    Mul_Age_mod[columns2[j]] = Mul_Age[j]
    j = j+1

k = 0
columns3=['State_Code','District_Code','AreaName','Section','Education_level','Person_bi_lang','Males_bi_lang','Females_bi_lang','Person_tri_lang','Males_tri_lang','Females_tri_lang']
Mul_Ed_mod = pd.DataFrame(columns =columns3)
while k<11 : 
    Mul_Ed_mod[columns3[k]] = Mul_Ed[k]
    k = k+1

    
Location = pd.DataFrame(columns = ['State_Code','AreaName'])
Ed_lang_vari = pd.DataFrame(columns =['State_Code','Section','Education_level','Males_bi_lang','Females_bi_lang','Males_tri_lang','Females_tri_lang'])
Age_gr_lang_vari = pd.DataFrame(columns =['State_Code','Section','Age_gp','Males_bi_lang','Females_bi_lang','Males_tri_lang','Females_tri_lang'])


Location['State_Code'] = Mul_Age_mod['State_Code']
Location['AreaName'] = Mul_Age_mod['AreaName']
Location = Location.drop_duplicates()               #table1 data


columns = ['State_Code','Section','Education_level','Males_bi_lang','Females_bi_lang','Males_tri_lang','Females_tri_lang']
for i in columns : 
    Ed_lang_vari[i] = Mul_Ed_mod[i]
Ed_lang_vari = Ed_lang_vari[Ed_lang_vari.Section != 'Total']
Ed_lang_vari = Ed_lang_vari[Ed_lang_vari.Education_level != 'Total']  #table2 data

columns = ['State_Code','Section','Age_gp','Males_bi_lang','Females_bi_lang','Males_tri_lang','Females_tri_lang']
for i in columns : 
    Age_gr_lang_vari[i] = Mul_Age_mod[i]
Age_gr_lang_vari = Age_gr_lang_vari[Age_gr_lang_vari.Section !='Total']
Age_gr_lang_vari = Age_gr_lang_vari[Age_gr_lang_vari.Age_gp !='Total'] #table3 data

Location_total = pd.DataFrame(columns = ['State_Code','Tmales','Tfemales'])
link_Ed_lang = pd.DataFrame(columns = ['id','State_Code','Section','Age_gp'])
Age_gp_pop = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_iilit = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_lit =  pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_lit_wo_Ed = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_bel_pri = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_pri = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_middle = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_sec = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_hsec = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_ntech_dip = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_tech_dip = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_above_grad = pd.DataFrame(columns = ['id','Tmales','Tfemales'])
Age_gp_unclassified = pd.DataFrame(columns = ['id','Tmales','Tfemales'])

Age_Ed_mod2 = pd.DataFrame(Age_Ed_mod)
#Age_Ed_mod2 = Age_Ed_mod2[Age_Ed_mod2.State_Code != '00']
Age_Ed_mod2 = Age_Ed_mod2[Age_Ed_mod2.Section != 'Total']
Age_Ed_mod2 = Age_Ed_mod2[Age_Ed_mod2.Age_gp != 'All ages']

x = [1]
i = 2
while i<=2016 :
    x.append(i)
    i = i+1

link_Ed_lang['State_Code'] = Age_Ed_mod2['State_Code']
link_Ed_lang['Age_gp'] = Age_Ed_mod2['Age_gp']
link_Ed_lang['Section'] = Age_Ed_mod2['Section']
link_Ed_lang['id'] = x

Age_gp_pop['Tmales'] = Age_Ed_mod2['Tmales']
Age_gp_pop['Tfemales'] = Age_Ed_mod2['Tfemales']
Age_gp_pop['id'] = x

Age_gp_iilit['Tmales'] =Age_Ed_mod2['Illit_males']
Age_gp_iilit['Tfemales'] =Age_Ed_mod2['Illit_females']####
Age_gp_iilit['id'] = x

Age_gp_lit['Tmales'] =  Age_Ed_mod2['Lit_males']
Age_gp_lit['Tfemales'] =  Age_Ed_mod2['Lit_females']
Age_gp_lit['id'] = x

Age_gp_lit_wo_Ed['Tmales']=  Age_Ed_mod2['Lit_males_wo_Ed']
Age_gp_lit_wo_Ed['Tfemales']=  Age_Ed_mod2['Lit_females_wo_Ed'] 
Age_gp_lit_wo_Ed['id'] = x

Age_gp_bel_pri['Tmales'] =  Age_Ed_mod2['Males_bel_pri']
Age_gp_bel_pri['Tfemales'] =  Age_Ed_mod2['Females_bel_pri']
Age_gp_bel_pri['id'] = x

Age_gp_pri['Tmales']=  Age_Ed_mod2['Males_pri']
Age_gp_pri['Tfemales']=  Age_Ed_mod2['Female_pri']
Age_gp_pri['id'] = x

Age_gp_middle['Tmales']=  Age_Ed_mod2['Males_middle']
Age_gp_middle['Tfemales']=  Age_Ed_mod2['Female_middle']
Age_gp_middle['id'] = x

Age_gp_sec['Tmales']=  Age_Ed_mod2['Males_mat_sec']
Age_gp_sec['Tfemales']=  Age_Ed_mod2['Female_mat_sec']
Age_gp_sec['id'] = x

Age_gp_hsec['Tmales']=  Age_Ed_mod2['Males_high_sec']
Age_gp_hsec['Tfemales']=  Age_Ed_mod2['Females_high_sec']
Age_gp_hsec['id'] = x

Age_gp_ntech_dip['Tmales']=  Age_Ed_mod2['Males_wrt_ntech_dip']
Age_gp_ntech_dip['Tfemales']=  Age_Ed_mod2['Females_wrt_ntech_dip']
Age_gp_ntech_dip['id'] = x

Age_gp_tech_dip['Tmales']=  Age_Ed_mod2['Males_wrt_tech_dip']
Age_gp_tech_dip['Tfemales']=  Age_Ed_mod2['Females_wrt_tech_dip']
Age_gp_tech_dip['id'] = x

Age_gp_above_grad['Tmales']=  Age_Ed_mod2['Males_above_grad']
Age_gp_above_grad['Tfemales']=  Age_Ed_mod2['Females_above_grad']
Age_gp_above_grad['id'] = x

Age_gp_unclassified['Tmales']=  Age_Ed_mod2['Males_other']
Age_gp_unclassified['Tfemales']=  Age_Ed_mod2['Females_other']
Age_gp_unclassified['id'] = x

Casualdata = pd.DataFrame(Age_Ed_mod)
Casualdata = Casualdata[Casualdata.Age_gp == "All ages"]
Casualdata = Casualdata[Casualdata.Section == "Total"]
Casualdata = Casualdata[Casualdata.State_Code != '00']

Location_total['Tmales'] = Casualdata['Tmales']
Location_total['Tfemales'] = Casualdata['Tfemales']
Location_total['State_Code'] = Casualdata['State_Code']

data =[['0-6',3],['7',7],['8',8],['9',9],['10',10],['11',11],['12',12],['13',13],['14',14],['15',15],['16',16],['17',17],['18',18],['19',19],['20-24',22],['25-29',27],
        ['30-34',32],['35-39',37],['40-44',42],['45-49',47],['50-54',52],['55-59',57],['60-64',62],['65-69',67],['70-74',72]
       ,['75-79',77],['80+',85]]
Age_avg_val_gp = pd.DataFrame(data,columns = ['Age_gp','avg_value'])





