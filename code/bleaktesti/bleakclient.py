import asyncio
from bleak import BleakClient
from bleak.exc import BleakCharacteristicNotFoundError
import mysql.connector
import struct
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
db_port = int(os.getenv("DB_PORT", 3306))


char_uuid = "00001526-1212-EFDE-1523-785FEABCD123"
address = "CF:01:6D:B4:C3:83"
raspPi_mac = "B8:27:EB:9D:BC:0E"

def notif_callback(sender, data: bytearray):
        x,y,z,pos = struct.unpack('<HHHB',data)
        print(x,y,z,pos)
        print(f"Vastaanotettu data: {data}")
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, send_data, x, y, z, pos, address, raspPi_mac)

def send_data(x,y,z,pos,from_mac,to_mac,groupid=25):
        try:
                conn = mysql.connector.connect(host=db_host, 
                                               user=db_user, 
                                               password=db_pass, 
                                               database=db_name, 
                                               port=db_port,
                                               auth_plugin='mysql_native_password')
                try:
                        cur = conn.cursor()
                        query = "INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d) VALUES (%s,%s,%s,%s,%s,%s,%s) "
                        params = (groupid, from_mac, to_mac, x, y, z, pos)
                        cur.execute(query, params)
                        conn.commit()
                        print(f"DB Insert OK: {x}, {y}, {z}, {pos}")
                        cur.close()
                finally:
                        conn.close()
        except mysql.connector.Error as err:
                print(f"Error: {err.msg}")
        except Exception as e:
                print(f"Error: {e}")

async def main():
        try:
                async with BleakClient(address) as client:
                        print(f"Connected to {client.name}")
                        print(f"Services: {client.services}")
                        await client.start_notify(char_uuid, notif_callback)
                        print("Listening for notifications...")
                        await asyncio.sleep(60)
                        await client.stop_notify(char_uuid)
        except BleakCharacteristicNotFoundError:
                print("Characteristic not found")
        except Exception as e:
                print(f"Connection failed: {e}")

asyncio.run(main())
