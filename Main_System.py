from cgitb import text
import cv2,time,csv,datetime,threading,PySimpleGUI as sg
from pyzbar.pyzbar import decode, ZBarSymbol
from playsound import playsound
#初期設定
text1 = "起動中です。"
text2 = "しばらくお待ちください。"
m = 0
exitmode = 0
def qr_read():
    #ここはQR読み取り部です。触らないでね。
    global text1,text2,exitmode
    #日付設定
    delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(delta, 'JST')
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    font = cv2.FONT_HERSHEY_SIMPLEX
    mode = 0
    startSec = time.time()
    set = [time.time(),"name"]
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            value = decode(frame, symbols=[ZBarSymbol.QRCODE])
            if value:
                #QRコードがあるとき
                if mode == 1:
                    for qrcode in value:
                        x, y, w, h = qrcode.rect
                        dec_inf = qrcode.data.decode('utf-8')
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                        if (dec_inf.startswith('hob:')) : 
                            file = open('output.csv', 'a', newline='')
                            write = csv.writer(file)
                            text1 = str(dec_inf.replace('hob:','')) + 'をとうろくしました！'
                            text2 = str('たいせつにあつかってね！')
                            nowdate = datetime.datetime.now(JST)
                            set = [nowdate.strftime('%Y/%m/%d %H:%M:%S'),dec_inf.replace('hob:','')]
                            write.writerow(set)
                            mode = 0
                            file.close()
                            #playsound('success.wav')
                startSec = time.time()
            #QRコードがないとき
            elif mode == 0 and (time.time() - startSec) >= 3:
                text1 = 'かざしてね！'
                text2 = ''
                mode = 1
            #ウィンドウ生成
            cv2.imshow('pyzbar', frame)
        #終了処理
        if (cv2.waitKey(1) & 0xFF == ord('q')) or exitmode == 1:
            exitmode = 1
            break
    cap.release()
#GUI処理です。ここを触ってね。
def ui():
    sg.theme('GrayGrayGray')
    #グローバル変数です。QR読み取り部とデータ交換をしています。できれば触らないでね。
    global text1,text2,exitmode
    #文字とかのレイアウトです。好きなように。
    layout = [[sg.Text(text1, key='-text1-')],
          [sg.Text(text2, key='-text2-')],
          #[sg.Button('決定'), sg.Button('終了')]]
    ]
    #ウィンドウの大まかな設定です。sg.Window(ウィンドウタイトル,layout(ここはいじらないで), size=(大きさをここで指定))
    window = sg.Window('玩具管理プログラム', layout, size=(700, 100))
    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or event == '終了' or exitmode == 1: #終了時の処理です。
            exitmode = 1
            break
        #文字の変更はここで処理してます。
        window['-text1-'].update(f'{text1}')
        window['-text2-'].update(f'{text2}')
reading = threading.Thread(target=qr_read)
gui = threading.Thread(target=ui)
reading.start()
gui.start()
reading.join()
gui.join()