import pymysql

conn = pymysql.Connect (host = 'project-db-stu3.smhrd.com', user='Insa4_IOTB_hacksim_5', password='aishcool5', db = 'Insa4_IOTB_hacksim_5', port=3308)

cur = conn.cursor()
sql = 'select * from music'

cur.execute(sql)
result = cur.fetchall()

cur.close()
conn.close()

print(result)


