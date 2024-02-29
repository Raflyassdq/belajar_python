import sqlite3


#bagian membuat tabel
# buat_tabel = ''' CREATE TABLE IF NOT EXISTS PROFIL (
#                 nama TEXT NOT NULL,
#                 umur integer NOT NULL,
#                 alamat text NOT NULL,
#                 hobby text NOT NULL);'''
#
# cursor.execute(buat_tabel)
# koneksi.commit()

#input 1 data
# user = ('syihab', '22', 'jogja', 'main musik')
# cursor.execute("INSERT INTO profil VALUES(?,?,?,?);", user)
# koneksi.commit()

# fetch one
try:
    koneksi = sqlite3.connect('kotakode.db')
    cursor = koneksi.cursor()
    print("database telah dibuat dan berhasil terkoneksi  ke SQLite")
    #all_result = cursor.execute("SELECT * FROM profil").fetchall()
    #print(all_result)
    cursor.execute("DELETE FROM profil WHERE nama='syihab'")
    koneksi.commit()
    # membaca semua data
    cursor.execute('SELECT * FROM profil')
    for row in cursor.fetchall():
      print(row)
      # Update umur Boby
    cursor.execute('UPDATE profil SET umur = 44 WHERE nama = "Boby"')
    koneksi.commit()
      # Update alamat budi pake multiline string, biar ga kepanjangan sampe pojok
    sql = '''
        UPDATE profil 
        SET Alamat='lampung' WHERE nama="Budi"
    '''
    cursor.execute(sql)
    koneksi.commit()
    cursor.close()
    koneksi.close()
except Exception as e:
    print(str(e))
    