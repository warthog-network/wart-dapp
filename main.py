import sys
import webbrowser
import pyperclip
from PySide6 import QtCore
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from entry_screen import Ui_MainWindow
from error import Ui_Error
from wallets_select import Ui_WalletsWindow
from db import DB
from utils import *
from mnemonic import Mnemonic
from mnemon import Ui_Dialog
import re
from addmnemo import Ui_Dialog_Mnemo
from addprivkey import Ui_Dialog_Priv
from mainwindow import Ui_MainWindow_Wart
from confirm import Ui_Dialog_Confrim
from confir import Ui_Confirm
from reg import Ui_Reg
from PySide6.QtGui import QScreen
privkey = None
address = ''
window = None
tx_buffer = None
balance_buffer = 0
con_status = "connecting"
pass1 = None
mnemo = Mnemonic("english")
flag = False
PUBLIC_NODES = ['193.218.118.57:3001', '193.218.118.57:3001', '185.209.228.16:3001', '51.75.21.134:3001', 'node.0xf10.com']
IP = None
db = DB()
PEER = 'http://'


class Register(QDialog):
    def __init__(self, parent):
        super(Register, self).__init__()
        self.register = Ui_Reg()
        self.register.setupUi(self)
        self.setWindowTitle("Warthog Network")
        self.parent = parent
        self.register.ok_btn.clicked.connect(self.ok)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)
        self.show()

    def close_(self):
        self.close()

    def ok(self):
        global pass1, flag
        pass1 = self.register.textEdit.toPlainText()
        pass2 = self.register.textEdit_2.toPlainText()
        if pass1 != pass2:
            err = Error()
            err.error.label.setText("Password mismatch")
            err.show()
            err.exec_()
            return
        elif len(pass1) < 8:
            err = Error()
            err.error.label.setText("Password`s length less 8")
            err.show()
            err.exec_()
            return
        pass1 = self.register.textEdit.toPlainText()
        flag = True
        self.close()


class Login(QDialog):
    def __init__(self, parent, addr):
        super(Login, self).__init__()
        self.login = Ui_Confirm()
        self.login.setupUi(self)
        self.setWindowTitle("Warthog Network")
        self.addr = addr
        self.login.ok_btn.clicked.connect(self.ok)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)
        self.show()


    def ok(self):
        global address, privkey, balance_buffer
        passw = self.login.textEdit.toPlainText()
        walletdata = db.get_wallet_by_address(self.addr)
        decrypted_pk = decrypt_pk(walletdata[2], passw, walletdata[3])
        if decrypted_pk is not None:
            addr, pk = wallet_from_pkhex(decrypted_pk)
            address = addr
            privkey = pk
            balance_buffer = walletdata[4]
            self.close()
            mainWindow.mainUI.address_text.setText(address)
            mainWindow.show_balance(addr)
            mainWindow.show()
        else:
            error = Error()
            error.error.label.setText("Invalid password!")
            error.show()
            error.exec_()


class Confirm(QDialog):
    def __init__(self):
        super(Confirm, self).__init__()
        self.confirm = Ui_Dialog_Confrim()
        self.setWindowTitle("Warthog Network")
        self.confirm.setupUi(self)
        self.confirm.ok_btn.clicked.connect(self.confirm_btn)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def confirm_btn(self):
        global PEER
        global tx_buffer
        global privkey

        recipient = self.confirm.recipient_label.text()
        amount = float(self.confirm.amount_label.text())
        fee = float(self.confirm.amount_label_2.text())
        amount_int = round(amount * 10 ** 8)
        fee_int = round(fee * 10 ** 8)
        tx_buffer = [recipient, amount_int, fee_int, privkey]
        print(tx_buffer)

        try:
            r = send_tx(tx_buffer[0], tx_buffer[1], tx_buffer[2], tx_buffer[3], PEER)
            print(r)
            if r['code'] == 0:
                error = Error()
                error.error.label.setText("Success")
                self.hide()
                error.show()
                error.exec_()
                self.close()
            else:
                print(str(r))
                error = Error()
                error.error.label.setText('Error')
                self.hide()
                error.show()
                error.exec_()

        except requests.exceptions.RequestException as e:
            print(e)
            error = Error()
            error.error.label.setText('Connection error.')
            self.hide()
            error.show()
            error.exec_()
            self.close()






class MainWindow(QMainWindow):

    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.mainUI = Ui_MainWindow_Wart()
        self.mainUI.setupUi(self)
        self.parent = parent
        self.parent.hide()
        self.mainUI.pushButton_4.clicked.connect(self.showMinimized)
        self.mainUI.stackedWidget.setCurrentIndex(1)
        self.setWindowTitle("Warthog Network")
        self.mainUI.send_button.clicked.connect(self.send_window)
        self.mainUI.address_button.clicked.connect(self.address_button_click)
        self.mainUI.discord_btn.clicked.connect(self.discord)
        self.mainUI.telegram_btn.clicked.connect(self.telegram)
        self.mainUI.twitter_btn.clicked.connect(self.twitter)
        self.mainUI.browser_btn.clicked.connect(self.website)
        self.mainUI.git_btn.clicked.connect(self.github)
        self.mainUI.contact_button.clicked.connect(self.address_page)
        self.mainUI.transactions_button.clicked.connect(self.transaction_page)
        self.mainUI.miners_button.clicked.connect(self.miners_page)
        self.mainUI.send_btn.clicked.connect(self.send_wart)
        self.mainUI.add_bttn.clicked.connect(self.add_friend)
        self.mainUI.show_miners.clicked.connect(self.list_miners)
        self.mainUI.show_btn.clicked.connect(self.list_transactions)
        self.mainUI.notes.clicked.connect(self.notes)
        self.timer()
        self.get_friends()
        self.mainUI.copy_btn.clicked.connect(self.copy_to_clipboard)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def get_friends(self):
        friends_list = db.get_friends()
        self.mainUI.friends.clear()
        for friend in friends_list:
            QApplication.processEvents()
            self.mainUI.friends.addItem(f'{friend[2]} - {friend[1]}')
    def print_(self):
        QApplication.processEvents()
        print('test')
        self.mainUI.balance.setText(get_balance(f'{PEER}',address))

    def add_friend(self):
        friend = self.mainUI.addr_text_3.text()
        name = self.mainUI.addr_text_2.text()
        db.insert_friend(friend, name)
        self.get_friends()
    def address_button_click(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)

    def copy_to_clipboard(self):
        text = self.mainUI.address_text.toPlainText()
        pyperclip.copy(str(text))
        print('copied to clipboard', self.mainUI.addr_text.text())
    def send_window(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.print_)
        timer.start(40000)

    def show_balance(self, wallet):
        QApplication.processEvents()
        global address
        address = wallet
        balance = get_balance(PEER, wallet)
        print(balance)
        balance_buffer = balance
        self.mainUI.balance.setText(str(balance))

    def address_page(self):
        self.mainUI.stackedWidget.setCurrentIndex(4)

    def transaction_page(self):
        self.mainUI.stackedWidget.setCurrentIndex(5)

    def miners_page(self):
        self.mainUI.stackedWidget.setCurrentIndex(6)

    def notes(self):
        self.mainUI.stackedWidget.setCurrentIndex(0)
    def list_transactions(self):
        self.mainUI.friends_2.clear()
        blocks = int(self.mainUI.blocks_btn.text())
        height = requests.get(f'{PEER}/chain/head').json()['data']['height']
        list_transactions = []
        for i in range(height - blocks, height):
            QApplication.processEvents()
            self.mainUI.friends_2.addItem(f'Check block № {i}')
            url_block = f'{PEER}/chain/block/{i}'
            get_block = requests.get(url_block).json()['data']['body']['transfers']
            if len(get_block) > 0:
                for j in range(len(get_block)):
                    list_transactions.append({get_block[j]['amount']: \
                                                  {
                                                      f'from {get_block[j]["fromAddress"]}': f'to {get_block[j]["toAddress"]}'}})
        self.mainUI.friends_2.clear()

        for i in range(len(list_transactions)):
            for j, k in list_transactions[i].items():
                for h in k:
                    QApplication.processEvents()
                    res = f'{i + 1}. {j} {h} {k[h]}'
                    self.mainUI.friends_2.addItem(res)

    def list_miners(self):
        self.mainUI.miners_lst.clear()
        blocks = int(self.mainUI.blocks_btn_2.text())
        height = requests.get(f'{PEER}/chain/head').json()['data']['height']
        list_miners = {}
        for i in range(height - blocks, height):
            QApplication.processEvents()
            self.mainUI.miners_lst.addItem(f'Check block № {i}')
            url_block_info = requests.get(f'{PEER}/chain/block/{i}').json()
            if url_block_info['data']['body']['rewards'][0]['toAddress'] in list_miners:
                list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']] += 3
            else:
                list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']] = 3
        self.mainUI.miners_lst.clear()
        QApplication.processEvents()
        for miners in list_miners:
            QApplication.processEvents()
            mine = str(miners)
            amount = str(list_miners[miners])
            res = mine + ' ' + amount
            self.mainUI.miners_lst.addItem(res)
            print(res)
            QApplication.processEvents()

    def send_wart(self):
        global tx_buffer

        recipient = self.mainUI.addr_text.text()
        amount = self.mainUI.amount_text.text()
        fee = self.mainUI.fee_text.text()
        if not re.search("^[a-fA-F0-9]{48}$", recipient):
            error = Error()
            error.error.label.setText("Invalid recipient.")
            return
        try:
            amount = float(amount)
            fee = float(fee)
        except ValueError:
            error = Error()
            error.error.label.setText('Invalid amount')
            error.show()
            error.exec_()

        amount_int = round(amount * 10 ** 8)
        fee_int = round(fee * 10 ** 8)

        tx_buffer = [recipient, amount_int, fee_int, privkey]

        confirm = Confirm()
        confirm.confirm.recipient_label.setText(recipient)
        confirm.confirm.amount_label.setText(str(amount))
        confirm.confirm.amount_label_2.setText(str(fee))
        confirm.show()
        confirm.exec_()





    def discord(self):
        webbrowser.open('https://discord.com/invite/QMDV8bGTdQ')

    def website(self):
        webbrowser.open('http://warthog.network/')

    def twitter(self):
        webbrowser.open('https://twitter.com/warthognetwork')

    def github(self):
        webbrowser.open('https://github.com/warthog-network')

    def telegram(self):
        webbrowser.open('https://t.me/warthognetwork')



class PrivkeyRestore(QDialog):
    def __init__(self, parent):
        super(PrivkeyRestore, self).__init__()
        self.key = Ui_Dialog_Priv()
        self.key.setupUi(self)
        self.parent = parent
        self.key.ok_btn.clicked.connect(self.ok)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def ok(self):
        global address, privkey
        pkhex = self.key.pk_label.text()
        address, privkey = wallet_from_pkhex(pkhex)
        encrypted_pk , salt = encrypt_pk(privkey.to_string().hex(), pass1)
        db.insert_wallet(address, encrypted_pk, salt)
        self.parent.wallets.listWidget.clear()
        self.parent.load_wallets()
        self.close()


class MnemoRestore(QDialog):
    def __init__(self, parent):
        super(MnemoRestore, self).__init__()
        self.addmnemo = Ui_Dialog_Mnemo()
        self.addmnemo.setupUi(self)
        self.parent = parent
        self.addmnemo.ok_btn.clicked.connect(self.okay_btn)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)




    def okay_btn(self):
        global address, privkey
        words = self.addmnemo.pk_label.text()
        if len(words) < 40:
            error = Error()
            error.error.label.setText("Not correct mnemonic phrase")
            error.show()
            self.hide()
            error.exec_()
            return
        seed = mnemo.to_seed(words, passphrase="")
        address, privkey = wallet_from_seed(seed)
        encrypted_pk, salt = encrypt_pk(privkey.to_string().hex(), pass1)
        db.insert_wallet(address, encrypted_pk, salt)
        self.parent.wallets.listWidget.clear()
        self.parent.load_wallets()
        self.close()



class Mnemon(QDialog):
    def __init__(self, words, parent):
        super(Mnemon, self).__init__()
        self.mnemon = Ui_Dialog()
        self.mnemon.setupUi(self)
        self.words = words
        self.parent = parent
        self.mnemon.ok_btn.clicked.connect(self.ok_press)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def ok_press(self):
        self.parent.wallets.listWidget.clear()
        self.parent.load_wallets()
        self.close()




class WartWallets(QMainWindow):
    def __init__(self):
        super(WartWallets,self).__init__()
        self.wallets = Ui_WalletsWindow()
        self.wallets.setupUi(self)
        self.wallets_list = db.get_wallets()
        self.wallets.new_wallet_button.clicked.connect(self.new_wallet)
        self.wallets.mnemonic_button.clicked.connect(self.restore_mnemo)
        self.wallets.private_key_button.clicked.connect(self.restore_pk)
        self.wallets.listWidget.itemClicked.connect(self.open_main_window)
        self.wallets.listWidget.itemClicked.connect(lambda: mainWindow.show_balance)
        self.old_pos = None
        self.load_wallets()
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)


    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
    def open_main_window(self, item):
        global address, privkey, balance_buffer
        addr = str(item.text())
        address = addr
        confirm = Login(self, addr)
        confirm.exec_()
        self.close()

    def load_wallets(self):
        self.wallets_list = db.get_wallets()
        self.wallets.listWidget.clear()
        for wallet in self.wallets_list:
            print(wallet)
            QApplication.processEvents()
            self.wallets.listWidget.addItem(wallet[1])

    def hide_window(self):
        self.showMinimized()

    def restore_mnemo(self):
        global address, privkey, balance_buffer
        reg = Register(self)
        reg.exec_()
        if flag:
            box = MnemoRestore(self)
            box.show()
            box.exec_()
            self.load_wallets()
        else:
            return


    def restore_pk(self):
        global address, privkey, balance_buffer
        reg = Register(self)
        reg.exec_()
        if flag:
            box = PrivkeyRestore(self)
            box.show()
            box.exec_()
            self.load_wallets()



    def new_wallet(self):
        reg = Register(self)
        reg.exec_()
        words = mnemo.generate(strength=256)
        seed = mnemo.to_seed(words)
        address, privkey = wallet_from_seed(seed)
        encrypted_pk, salt = encrypt_pk(privkey.to_string().hex(),pass1)
        db.insert_wallet(address, encrypted_pk, salt)
        box = Mnemon(words, self)
        box.mnemon.mnemo_label.setText(words)
        box.show()
        box.exec_()
        self.load_wallets()


class Error(QDialog):
    def __init__(self):
        super(Error, self).__init__()
        self.error = Ui_Error()
        self.error.setupUi(self)
        self.error.ok_button.clicked.connect(self.okay_press)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def okay_press(self):
        self.close()



class WartEntry(QMainWindow):
    def __init__(self):
        super(WartEntry, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.public_button.clicked.connect(self.public_connect)
        self.setWindowTitle("Warthog Network")
        self.ui.connect_button.clicked.connect(self.private_connect)
        fmcenter = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fmscr = self.frameGeometry()
        fmscr.moveCenter(fmcenter)

    def close_window(self):
        self.close()

    def hide_window(self):
        self.showMinimized()

    def public_connect(self):
        global IP, PEER
        QApplication.processEvents()
        for i in PUBLIC_NODES:
            QApplication.processEvents()
            try:
                req = requests.get(f'http://{i}', timeout=1)
                if req.status_code == 200:
                    IP = i
                    PEER += IP
                    wallets.show()
                    self.close()
                    return IP,PEER
            except:
                continue
        err = Error()
        self.hide()
        err.show()
        err.exec()
        self.show()

    def private_connect(self):
        global IP,PEER
        ip = self.ui.input_field.text()
        try:
            QApplication.processEvents()
            req = requests.get(f'http://{ip}', timeout=0.5)
            if req.status_code == 200:
                IP = ip
                PEER += IP
                wallets.show()
                self.close()
                return IP,PEER
        except Exception as e:
            err = Error()
            self.hide()
            err.show()
            err.exec()
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WartEntry()
    window.show()
    wallets = WartWallets()
    wallets.hide()
    mainWindow = MainWindow(wallets)
    mainWindow.hide()
    sys.exit(app.exec())
