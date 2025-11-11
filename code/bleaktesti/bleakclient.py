import asyncio

from bleak import BleakClient
from bleak.exc import BleakCharacteristicNotFoundError
import mysql.connector
import struct

char_uuid = "00001526-1212-EFDE-1523-785FEABCD123"
address = "CF:01:6d:B4:C3:83" 
raspPi_mac ="B8:27:EB:9D:BC:0E"


def notif_callback(sender, data: bytearray):
    x,y,z,pos = struct.unpack('<HHHB',data)
    print(x,y,z,pos)
    print(f"Lähetetty data: {data}")
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, send_data, x, y, z, pos, sender, raspPi_mac)



def send_data(x, y, z, pos, from_mac, to_mac, groupid=25):
    conn = mysql.connector.connect(
        host = "172.20.241.9",
        user = "dbaccess_rw",
        password = "fasdjkf2389vw2c3k234vk2f3",
        database = "measurements",
        port = 3306
    )
    try:
        cur = conn.cursor()
        query = "INSERT INTO measurements (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d) VALUES (%s,%s,%s,%s,%s,%s,%s) "
        params = (groupid, from_mac, to_mac, x, y, z, pos)
        cur.execute(query, params)
        conn.commit()
        cur.close()
    finally:
        conn.close()

async def main():
    try:
        async with BleakClient(address, pair=True) as client:
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
