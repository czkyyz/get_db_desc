
import pymysql#.cursors
from faker import Faker

conn = pymysql.connect(host='10.201.251.35',port=3306,user='txuser',passwd='!QAZ2wsx3edc4r',db='tx_alert',charset='utf8')

cursor = conn.cursor()

try:

    #for i in range(10001):
     
    #sql = "INSERT INTO tbl_audit_dlpfilecopy (`occurtime`, `policyname`, `process`, `action`, `srcfilename`, `dstfilename`, `filemd5`, `filesize`, `isencrypted`, `secretdescription`, `result`, `guid`, `hostname`, `ip`, `mask`, `mac`, `winuser`, `depnamelevel1`, `depnamelevel2`, `depnamelevel3`, `depnamelevel4`, `depnamelevel5`, `serverip`, `logtime`, `secretlevel`, `reason`, `groupname`, `logonuser`, `extend_1`, `extend_2`, `extend_3`, `extend_4`, `storageid`) VALUES ('2018-07-06 16:47:56', '', 'WINWORD.EXE', '0', 'E:\\财务数据的规范化要求.doc', 'E:\\财务数据的规范化要求.doc', '', '0', '0', '关键字:数据(1);财务(1);\r\n', '0', '{65047115-7CDC-4399-BAD7-6A1EE5EB898F}', 'WIN-713BOK7UQK8', '181008916', '4294901760', '00-0C-29-49-AD-3C', 'aaa', 'DLP专版测试部', 'll', '', '', '', '4294967295', '2018-07-06 16:48:03', '1', '', '关键字', 'win10', NULL, NULL, NULL, NULL, '');"

    sql1 = "select * from test"

    cursor.execute(sql1)

    desc = cursor.description

    #results = cursor.fetchall()

    #print(desc[0][0])
    ziduan = []
    fake = Faker()
    #ziduan = {}

    for i in range(0,len(desc)):

       # for row in desc[i][i]:
    #ziduan[desc[i][0]]=fake.name()
        ziduan.append(desc[i][0])
    value_list = []
    for i in range(0,len(desc)-1):
        value_list.append(fake.name())
    value = ','.join(value_list)
    # print(value)
    # sql2 = "INSERT INTO test VALUES (value);"
        
    # cursor.execute(sql2)

    #print(value_list)
    
    #print(ziduan)

    # for row in results:

    #     print(row)

    conn.commit()

    conn.close()

except:

    conn.rollback()

