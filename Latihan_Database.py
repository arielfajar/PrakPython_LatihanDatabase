#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[3]:


import mysql.connector

conn = mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023')

print(conn)
conn.close()


# In[4]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MAHASISWA (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30) NOT NULL,
                    Alamat VARCHAR(255) NOT NULL,
                    Mata_kuliah_yang_diikuti VARCHAR(10),
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[5]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50) NOT NULL,
                    Mata_kuliah_yang_diajar VARCHAR(50),
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[6]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MATA_KULIAH (
                    Kode_MK VARCHAR(10) NOT NULL,
                    Nama_MK VARCHAR(50) NOT NULL,
                    Waktu DATE,
                    Ruangan VARCHAR(10),
                    Gedung VARCHAR(20)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[7]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MAHASISWA (NIM, Nama, Alamat, Mata_kuliah_yang_diikuti, Umur, Jenis_kelamin)VALUES (%s, %s, %s, %s, %s, %s)"
val = [("MH370", "Amin", "Planet Bekasi", "APSI", "19", "L"),
       ("MH371", "Krisnawati", "Jakarta", "PBO", "17", "P"),
       ("MH372", "Upin", "Madiun", "MIKRO", "18", "L"),
       ("MH373", "Ipin", "Magetan", "PYTHON", "19", "L"),
       ("MH374", "Adit", "Tangerang", "STATISTIKA", "18", "L"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[8]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, Nama_Dosen, Mata_kuliah_yang_diajar, Umur, Jenis_kelamin)VALUES (%s, %s, %s, %s, %s)"
val = [("DS001", "Darmawan", "APSI", "19", "L"),
       ("DS002", "Masbahah", "PBO", "17", "P"),
       ("DS003", "Fendi", "MIKRO", "16", "L"),
       ("DS004", "Yusuf", "PYTHON", "19", "L"),
       ("DS005", "Trisna", "STATISTIKA", "18", "P"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[9]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (Kode_MK, Nama_MK, Waktu, Ruangan, Gedung)VALUES (%s, %s, %s, %s, %s)"
val = [("MK001", "APSI", "2023-03-1", "R1L1", "G.Biru"),
       ("MK002", "PBO", "2023-03-2", "R1L2", "G.Hijau"),
       ("MK003", "MIKRO", "2023-03-3", "R1L3", "G.Hijau"),
       ("MK004", "PYTHON", "2023-03-4", "R2L1", "G.Biru"),
       ("MK005", "STATISTIKA", "2023-03-5", "R1L2", "G.Biru"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[10]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()


sql = "SELECT   matkul.Nama_MK, mahasiswa.Nama, dosen.Nama_Dosen FROM MATA_KULIAH matkul    INNER JOIN MAHASISWA mahasiswa ON mahasiswa.Mata_kuliah_yang_diikuti = matkul.Nama_MK    INNER JOIN DOSEN dosen ON dosen.Mata_kuliah_yang_diajar = matkul.Nama_MK"

cursorObject.execute(sql)

result = cursorObject.fetchall()

for row in result:
    print(row)

dataBase.close()


# In[ ]:




