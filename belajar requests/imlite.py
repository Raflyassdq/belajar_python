import sqlite3

koneksi = sqlite3.connect('imdb.db')

cursor = koneksi.cursor()
print ('database telah dibuat dan berhasil terkoneksi')

buat_tabel = '''CREATE TABLE IF NOT EXISTS fix (
                ID_Nation TEXT,
                Nation TEXT,
                ID_Year INTEGER,
                Year INTEGER,
                Population INTEGER,
                Slug_Nation TEXT);'''

cursor.execute(buat_tabel)
koneksi.commit()

more_items = [('01000US', 'United States', '2017', '2017', '321004407', 'united-states'), 
            ('01000US', 'United States', '2020', '2020', '326569308', 'united-states'),
            ('01000US', 'United States', '2019', '2019', '324697795', 'united-states'),
            ('01000US', 'United States', '2018', '2018', '322903030', 'united-states'),
            ('01000US', 'United States', '2017', '2017', '321004407', 'united-states'),
            ('01000US', 'United States', '2016', '2016', '318558162', 'united-states'),
            ('01000US', 'United States', '2015', '2015', '316515021', 'united-states'),
            ('01000US', 'United States', '2014', '2014', '314107084', 'united-states'),
            ('01000US', 'United States', '2013', '2013', '311536594', 'united-states'),
            ]
cursor.executemany("INSERT INTO fix VALUES(?,?,?,?,?,?);", more_items)
koneksi.commit()                   

cursor.execute("UPDATE fix SET Nation = 'Indonesia' WHERE ID_Year = 2017")
koneksi.commit()

cursor.execute('SELECT * FROM fix')
for row in cursor.fetchall():
      print(row)



