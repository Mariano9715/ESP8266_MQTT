import network

#declaración de funciones
#conectar a la red wifi local
def conectar_red():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active():
        wlan.active(True)
        
    if not wlan.isconnected():
        wlan.connect("WLAN-SSID","password")
        print("Conectando...", end = "")
        while not wlan.isconnected():
            sleep_ms(100)
            print(".", end = "")

    config = wlan.ifconfig()
    print()
    print(f"Accedí con la IP: {config[0]}")
    
conectar_red()