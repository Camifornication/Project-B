from serial.tools import list_ports
import serial
import requests

steam_api_key = "61D1D964724B68FC9F340D584CD500E3"

def read_serial(port):
    line = port.read(1000)
    print(line)
    return line.decode()


def check_online(steamid):
    global online_status, personaname, game_playing
    response = requests.get(
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steam_api_key}&steamids={steamid}")
    data = response.json()
    personaname = data['response']['players'][0]['personaname']

    if 'gameextrainfo' in data['response']['players'][0]:
        game_playing = data['response']['players'][0]['gameextrainfo']
    else:
        game_playing = "gameplaying"


    if 'personastate' in data['response']['players'][0]:
        personastate = data['response']['players'][0]['personastate']
        if personastate == 0:
            online_status = "0" #"Offline"
        elif personastate == 1:
            online_status = "1" #"Online"
        elif personastate == 3:
            online_status = "2" #"Away"
        elif personastate == 4:
            online_status = "3" #"Snooze"
        else:
            online_status = "N/A"
    return online_status

def serial_communication(friend_steamid_sc):
    serial_ports = list_ports.comports()

    print("[INFO] Serial ports found:")
    for i, port in enumerate(serial_ports):
        print(str(i) + ". " + str(port.device))

    pico_port_index = 0
    pico_port = serial_ports[pico_port_index].device

    with serial.Serial(port=pico_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1) as serial_port:
        if serial_port.isOpen():
            print("[INFO] Using serial port", serial_port.name)
        else:
            print("[INFO] Opening serial port", serial_port.name, "...")
            serial_port.open()

        try:
            commands = ['exit', 'online status']
            choice = friend_steamid_sc
            while True:
                if choice != 'exit':
                    data = check_online(choice) + "ewigvuieflbhwuidbhiudgbwlhg" + personaname + "ewigvuieflbhwuidbhiudgbwlhg" + game_playing + "\r"
                    print(f"data in = {data}")
                    serial_port.write(data.encode())
                    pico_output = read_serial(serial_port)
                    pico_output = pico_output.replace('\r\n', ' ')
                    print("[PICO] " + pico_output)
                    break
                else:
                    print("[WARN] Unknown command.")

        except KeyboardInterrupt:
            print("[INFO] Ctrl+C detected. Terminating.")
        finally:
            serial_port.close()
            print("[INFO] Serial port closed. Bye.")