import asyncio
from bleak import BleakClient
from bleak.exc import BleakCharacteristicNotFoundError
import mysql.connector
import struct
import os
from dotenv import load_dotenv
from queue import Queue
import threading
import time

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
db_port = int(os.getenv("DB_PORT", 3306))

char_uuid = "00001526-1212-EFDE-1523-785FEABCD123"
address = "CF:01:6D:B4:C3:83"
raspPi_mac = "B8:27:EB:9D:BC:0E"

data_queue = Queue()


def db_worker():
    conn = None
    cursor = None
    while True:
        try:
            if conn is None or not conn.is_connected():
                try:
                    conn = mysql.connector.connect(
                        host=db_host,
                        user=db_user,
                        password=db_pass,
                        database=db_name,
                        port=db_port,
                        auth_plugin="mysql_native_password"
                    )
                    cursor = conn.cursor()
                    print("DB: Yhteys avattu")
                except Exception as e:
                    print(f"DB: Yhteyden avaus epäonnistui: {e}")
                    time.sleep(2)
                    continue

            item = data_queue.get()
            if item is None:
                continue

            (groupid, from_mac, to_mac, x, y, z, pos) = item

            query = "INSERT INTO posdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d)VALUES (%s, %s, %s, %s, %s, %s, %s)"
            params = (groupid, from_mac, to_mac, x, y, z, pos)
            cursor.execute(query, params)
            conn.commit()
            print(f"DB Insert OK: {x}, {y}, {z}, {pos}")

        except mysql.connector.Error as e:
            print(f"DB Error: {e}")
            if conn:
                try:
                    conn.close()
                except:
                    pass
            conn = None
            time.sleep(1)

        except Exception as e:
            print(f"Worker ERROR: {e}")
            time.sleep(1)


threading.Thread(target=db_worker, daemon=True).start()


def notif_callback(sender, data: bytearray):
    if len(data) != 7:
        print("Incorrect data size")
        return

    x, y, z, pos = struct.unpack("<HHHB", data)
    print(f"{x} {y} {z} {pos}")
    print(f"Vastaanotettu data: {data}")
    data_queue.put((25, address, raspPi_mac, x, y, z, pos))


async def main():
    try:
        async with BleakClient(address) as client:
            print(f"Connected to {address}")
            await client.start_notify(char_uuid, notif_callback)
            print("Listening for notifications...")
            await asyncio.Event().wait()
    except BleakCharacteristicNotFoundError:
        print("Characteristic not found")
    except Exception as e:
        print(f"Connection failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())