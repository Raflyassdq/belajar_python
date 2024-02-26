import serial

def read_serial(port, baudrate, timeout):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    try:
        while True:
            # Baca data dari port serial
            data = ser.readline().decode().strip()
            if data:
                print("Data:", data)
    except KeyboardInterrupt:
        ser.close()
        print("Program terminated.")

# Contoh pemanggilan fungsi
port = 'COM6'  # Ganti dengan port serial yang sesuai
baudrate = 9600  # Sesuaikan dengan baudrate dari perangkat Anda
timeout = 1  # Timeout untuk membaca dari port serial

read_serial(port, baudrate, timeout)