import qrcode

#la libreria qrcode non fa parte di quelle importate di default da python, 
# quindi va aggiunta a parte (Python >= 3.7)

def generate_qr(web_site, file_name):
    try:
        img = qrcode.make(
            web_site,
            box_size=20,
            )
        img.save(file_name)
        print(f'QR salvato correttamente come {file_name}')
    except Exception as ex:
        print(f'ERROR: {ex}')

while True:
    go_on = input('Scrivi "exit" per uscire o premi invio: ')
    if go_on == "exit":
        break
    input_web = input('Scrivi qui il sito web: ')
    nome_qr = input('Scrivi il nome del file: ') + '.png'

    generate_qr(input_web, nome_qr)