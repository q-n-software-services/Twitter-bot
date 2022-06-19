# Importing built-in functions from libraries
from PyQt5.QtWidgets import QApplication, QDialog,QComboBox, QLineEdit, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber, QMessageBox, QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sys
import tweepy
import time


# Below is the GUI code written using PyQt5 library of PYTHON
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.showFullScreen()

        self.setWindowTitle("Twitter Bot")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_combo_box()

    def create_combo_box(self):

        vbox = QVBoxLayout()

        vbox1 = QVBoxLayout()

        self.label = QLabel("Twitter Bot")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Sanserif", 48))
        self.label.setFixedHeight(129)

        self.label.setStyleSheet("background-color:yellow")
        vbox.addWidget(self.label)

        self.link_title = QLabel()
        self.link_title.setAlignment(Qt.AlignCenter)
        self.link_title.setFont(QFont("Sanserif", 36))
        self.link_title.setText("LINK")
        self.link_title.setStyleSheet("background-color:white")

        vbox1.addWidget(self.link_title)

        self.link = QLineEdit()
        self.link.setFont(QFont("Sanserif", 24))
        self.link.setPlaceholderText("\tEnter the LINK to the Tweet here")
        self.link.setStyleSheet("background-color:white")

        vbox1.addWidget(self.link)

        self.comment_title = QLabel()
        self.comment_title.setFont(QFont("Sanserif", 24))
        self.comment_title.setAlignment(Qt.AlignCenter)
        self.comment_title.setFixedHeight(60)
        self.comment_title.setText("COMMENT")
        self.comment_title.setStyleSheet("background-color:white")
        vbox1.addWidget(self.comment_title)

        self.comment = QTextEdit()
        self.comment.setFont(QFont("Sanserif", 24))
        self.comment.setPlaceholderText("\tEnter your COMMENT here")
        self.comment.setStyleSheet("background-color:white")
        vbox1.addWidget(self.comment)


        btn_close = QPushButton("CLOSE")
        btn_close.setStyleSheet("Background-color:red")
        btn_close.setFont(QFont("Sanserif", 12))
        btn_close.setFixedHeight(60)
        btn_close.clicked.connect(self.closew)

        btn_minimize = QPushButton("MINIMIZE")
        btn_minimize.setStyleSheet("Background-color:yellow")
        btn_minimize.setFont(QFont("Sanserif", 12))
        btn_minimize.setFixedHeight(60)
        btn_minimize.clicked.connect(self.minimizew)

        btn_addp = QPushButton("ADD ACCOUNT")
        btn_addp.setStyleSheet("Background-color:Green")
        btn_addp.setFont(QFont("Sanserif", 12))
        btn_addp.setFixedHeight(60)
        btn_addp.clicked.connect(self.add_player)

        vbox.addLayout(vbox1)

        btn_points = QPushButton("SUBMIT")
        btn_points.setFont(QFont("sanserif", 16))
        btn_points.setStyleSheet("background-color:violet")
        btn_points.clicked.connect(self.submit_points)
        vbox.addWidget(btn_points)

        self.label_prediction_heading = QLabel("STATUS")
        self.label_prediction_heading.setAlignment(Qt.AlignCenter)
        self.label_prediction_heading.setFont(QFont("sanserif", 24))
        self.label_prediction_heading.setFixedHeight(60)

        self.label_prediction_text = QLabel('prediction_show')
        self.label_prediction_text.setAlignment(Qt.AlignCenter)
        self.label_prediction_text.setFont(QFont("Sanserif", 16))
        self.label_prediction_text.setFixedHeight(60)

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.label_prediction_heading)
        vbox3.addWidget(self.label_prediction_text)
        vbox.addLayout(vbox3)

        hbox2 = QHBoxLayout()

        hbox2.addWidget(btn_addp)
        hbox2.addWidget(btn_minimize)
        hbox2.addWidget(btn_close)

        vbox.addLayout(hbox2)

        self.setLayout(vbox)

# fuction called to close the software
    def closew(self):
        self.close()

# fuction called to minimize the software window
    def minimizew(self):
        self.showMinimized()

# Function to add player to the software and database
    def add_player(self):

        Add_account_dialog = QDialog()
        Add_account_dialog.setModal(True)
        Add_account_dialog.setWindowTitle("            ADD Account")
        Add_account_dialog.setWindowIcon(QIcon("burger.ico"))
        Add_account_dialog.setGeometry(190, 200, 1000, 400)
        vbox1 = QVBoxLayout()

        self.label_title1 = QLabel(" 1st Credential")
        self.label_title1.setFont(QFont("Sanserif", 12))
        self.label_title1.setStyleSheet("background-color:white")
        self.label_title1.setFixedWidth(120)

        self.label_title2 = QLabel(" 2nd Credential")
        self.label_title2.setFont(QFont("Sanserif", 12))
        self.label_title2.setStyleSheet("background-color:white")
        self.label_title2.setFixedWidth(120)

        self.label_title3 = QLabel(" 3rd Credential")
        self.label_title3.setFont(QFont("Sanserif", 12))
        self.label_title3.setStyleSheet("background-color:white")
        self.label_title3.setFixedWidth(120)

        self.label_title4 = QLabel(" 4th Credential")
        self.label_title4.setFont(QFont("Sanserif", 12))
        self.label_title4.setStyleSheet("background-color:white")
        self.label_title4.setFixedWidth(120)


        self.credential1 = QLineEdit()
        self.credential1.setFont(QFont("Sanserif", 24))
        self.credential1.setPlaceholderText("\tEnter the API key here")
        self.credential1.setStyleSheet("background-color:white")
        hbox_name = QHBoxLayout()
        hbox_name.addWidget(self.label_title1)
        hbox_name.addWidget(self.credential1)

        vbox1.addLayout(hbox_name)

        self.credential2 = QLineEdit()
        self.credential2.setFont(QFont("Sanserif", 24))
        self.credential2.setPlaceholderText("\tEnter the API secret key here")
        self.credential2.setStyleSheet("background-color:white")
        hbox_id = QHBoxLayout()
        hbox_id.addWidget(self.label_title2)
        hbox_id.addWidget(self.credential2)

        vbox1.addLayout(hbox_id)

        self.credential3 = QLineEdit()
        self.credential3.setFont(QFont("Sanserif", 24))
        self.credential3.setPlaceholderText("\tEnter the Access token here")
        self.credential3.setStyleSheet("background-color:white")
        hbox_rating = QHBoxLayout()
        hbox_rating.addWidget(self.label_title3)
        hbox_rating.addWidget(self.credential3)
        vbox1.addLayout(hbox_rating)

        self.credential4 = QLineEdit()
        self.credential4.setFont(QFont("Sanserif", 24))
        self.credential4.setPlaceholderText("\tEnter the Access token secret here")
        self.credential4.setStyleSheet("background-color:white")
        hbox_credential4 = QHBoxLayout()
        hbox_credential4.addWidget(self.label_title4)
        hbox_credential4.addWidget(self.credential4)

        vbox1.addLayout(hbox_credential4)

        btn_submit = QPushButton("SUBMIT")
        btn_submit.setFont(QFont("sanserif", 16))
        btn_submit.setStyleSheet("background-color:green")
        btn_submit.clicked.connect(self.submit_addplayer)
        vbox1.addWidget(btn_submit)

        Add_account_dialog.setLayout(vbox1)
        Add_account_dialog.exec_()

# fuction to submit data to the software for new player added
    def submit_addplayer(self):
        global cur
        global conn
        credential1 = self.credential1.text().lstrip().rstrip()
        credential2 = self.credential2.text().lstrip().rstrip()
        credential3 = self.credential3.text().lstrip().rstrip()
        credential4 = self.credential4.text().lstrip().rstrip()

        f_write = open('accounts_data.txt', 'a')
        f_write.write(" API key :\t{}\n API secret key :\t{}\n Access token :\t{}\n Access token secret :\t{}\n\n".format(credential1, credential2, credential3, credential4))
        f_write.close()
        self.label_prediction_text.setText("\tProcess Successful")

# function to submit points entered to the software that were scored by a player
    def submit_points(self):
        print("clicked")
        tweet_id = self.link.text().lstrip().rstrip()
        comment_text = self.comment.toPlainText()

        c = 0
        lines_list = []
        f_read = open('accounts_data.txt', 'r')
        for i, line in enumerate(f_read):
            c += 1
            if c <= 4:
                credential = line.split(':')[1].lstrip().rstrip()
                lines_list.append(credential)
            else:
                c = 0
                print(lines_list)
                API_key = lines_list[0]
                API_secret_key = lines_list[1]
                Access_token = lines_list[2]
                Access_token_secret = lines_list[3]

                lines_list = []

                auth = tweepy.OAuthHandler(API_key, API_secret_key)

                auth.set_access_token(Access_token, Access_token_secret)

                api = tweepy.API(auth, wait_on_rate_limit=True)

                # Retweeting
                api.retweet(tweet_id)

                # Liking
                api.create_favorite(tweet_id)

                # comment / reply
                tweet = api.get_status(tweet_id)
                api.update_status(f"@{tweet.user.screen_name()}{comment_text}", tweet_id)

                # following tweet author
                # user = api.get_user(tweet.user.screen_name())
                api.create_friendship(tweet.user.screen_name())
        c = 0
        print(lines_list)
        API_key = lines_list[0]
        API_secret_key = lines_list[1]
        Access_token = lines_list[2]
        Access_token_secret = lines_list[3]

        lines_list = []

        auth = tweepy.OAuthHandler(API_key, API_secret_key)

        auth.set_access_token(Access_token, Access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        # Retweeting
        api.retweet(tweet_id)

        # Liking
        api.create_favorite(tweet_id)

        # comment / reply
        tweet = api.get_status(tweet_id)
        api.update_status(f"@{tweet.user.screen_name()}{comment_text}", tweet_id)

        # following tweet author
        # user = api.get_user(tweet.user.screen_name())
        api.create_friendship(tweet.user.screen_name())


# GUI window setup clauses

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())








