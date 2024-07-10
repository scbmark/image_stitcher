import json
import ssl
import sys
from pathlib import Path
from urllib import request

import certifi
from PIL import Image
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QMessageBox

import resources_rc

from .AboutUI import Ui_AboutWindow
from .CustomWidgets import LoadImage, QListWidgetItemPlus
from .MainUI import Ui_MainWindow
from .ManualUI import Ui_ManualWindow


class MainWindow_controller(QtWidgets.QMainWindow):
    send_update_image_count = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.version = "1.0"

        self.show_usage_warrning_window()

        self.set_statusbar()
        self.setup_control()

    def show_usage_warrning_window(self):
        """
        show the usage_warrning message
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("警告")
        messagebox.setText("任何圖片在進入此程式使用前，請務必做好備份，並且使用副本來操作，以避免一切會造成圖片原檔消失的可能性。")
        messagebox.setIcon(QMessageBox.Icon.Critical)
        messagebox.addButton("我了解了", QMessageBox.ButtonRole.AcceptRole)
        messagebox.addButton("我還沒備份", QMessageBox.ButtonRole.RejectRole)

        result = messagebox.exec()
        if result == 1:
            import sys

            sys.exit()

    def set_statusbar(self):
        """
        initialize the statusbar
        """
        self.img_count = QtWidgets.QLabel()
        self.img_count.setText(f"列表中共有 0 張圖片")
        self.status = QtWidgets.QLabel()
        self.status.setText("讀取狀態： 無")
        self.ui.statusbar.addPermanentWidget(self.img_count)
        self.ui.statusbar.addPermanentWidget(self.status)

    def setup_control(self):
        """
        initialize global variable and connect slot functions
        """

        self.send_update_image_count.connect(self.update_image_count)

        self.ui.menu_about_manual.triggered.connect(self.show_manual_window)
        self.ui.menu_about_update.triggered.connect(self.check_update)
        self.ui.menu_about_about.triggered.connect(self.show_about_window)

        self.ui.items_list.send_new_item.connect(self.add_drag_img)
        self.ui.horizon_rtn.toggled.connect(self.switch_mode)

        self.ui.clear_list_btn.clicked.connect(self.clear_list)
        self.ui.items_list.itemDoubleClicked.connect(self.show_big_img_window)

        self.ui.start_btn.clicked.connect(self.start_generate)
        self.ui.exit_btn.clicked.connect(self.app_exit)

    def update_image_count(self):
        """
        updata image count in the statusbar
        """
        self.img_count.setText(f"列表中共有 {self.ui.items_list.count()} 張圖片")

    def show_manual_window(self):
        """
        open manual window
        """
        self.ManualWindows = QtWidgets.QWidget()
        self.manual_ui = Ui_ManualWindow()
        self.manual_ui.setupUi(self.ManualWindows)
        self.ManualWindows.setFixedSize(800, 600)
        self.manual_ui.exit_btn.clicked.connect(lambda: self.ManualWindows.close())
        self.ManualWindows.show()

    def check_update(self):
        github_release_url: str = (
            "https://github.com/scbmark/image_stitcher/releases/latest"
        )
        github_release_url_api: str = (
            "https://api.github.com/repos/scbmark/image_stitcher/releases/latest"
        )

        req = request.Request(github_release_url_api)

        try:
            context = ssl.create_default_context(cafile=certifi.where())
            with request.urlopen(req, context=context) as response:
                res = json.load(response)
                latest_version = res["tag_name"]
        except:
            messagebox = QMessageBox(self)
            messagebox.warning(self, "更新", f"網路連線失敗")
            return

        if latest_version != self.version:
            messagebox = QMessageBox(self)
            messagebox.setWindowTitle("更新")
            messagebox.setText(f"發現更新\n目前版本： {self.version}\n最新版本： {res['tag_name']}")
            messagebox.setIcon(QMessageBox.Icon.Information)
            messagebox.addButton("現在更新", QMessageBox.ButtonRole.AcceptRole)
            messagebox.addButton("不要更新", QMessageBox.ButtonRole.RejectRole)

            result = messagebox.exec()
            if result == 0:
                import webbrowser

                webbrowser.open(github_release_url)
            else:
                pass
        else:
            messagebox = QMessageBox(self)
            messagebox.information(self, "檢查更新", f"目前為最新版本\n目前版本： {self.version}")

    def show_about_window(self):
        """
        open about window
        """
        self.AboutWindows = QtWidgets.QWidget()
        self.about_ui = Ui_AboutWindow()
        self.about_ui.setupUi(self.AboutWindows)
        self.about_ui.version_lb.setText(f"Version: {self.version}")
        self.AboutWindows.setFixedSize(400, 600)
        self.about_ui.exit_btn.clicked.connect(lambda: self.AboutWindows.close())
        self.AboutWindows.show()

    def switch_mode(self):
        if self.ui.horizon_rtn.isChecked():
            self.ui.max_width_value.setEnabled(True)
            self.ui.max_heigth_value.setDisabled(True)
        else:
            self.ui.max_heigth_value.setEnabled(True)
            self.ui.max_width_value.setDisabled(True)


    def add_drag_img(self, pictures: list):
        """
        add images from drag and drop
        """
        self.load_img_thread = LoadImage(pictures)
        self.load_img_thread.send_img_item.connect(self.add_img_item_to_list)
        self.load_img_thread.send_progress.connect(self.update_progress)

        self.load_img_thread.start()

        self.update_progress("無")

    def update_progress(self, progress: str):
        """
        updata image loadin progress in the statusbar
        """
        self.status.setText(f"讀取狀態： {progress}")

    def add_img_item_to_list(self, item_tuple: tuple):
        """
        create thumbnail mode QListItemWidget and add it to the QListWiget
        """
        img_w = item_tuple[0].width()
        img_h = item_tuple[0].height()

        MAXIMUM_HEIGHT = 64
        ratio = MAXIMUM_HEIGHT / img_h

        item = QListWidgetItemPlus(item_tuple[1])
        item_widget = QtWidgets.QWidget()

        pic_name_lb = QtWidgets.QLabel()
        pic_name_lb.setText(Path(item_tuple[1]).name)
        item_layout = QtWidgets.QHBoxLayout()

        pic_view = QtWidgets.QGraphicsView(self)
        pic_view.setGeometry(0, 0, int(img_w * ratio), MAXIMUM_HEIGHT)
        pic_sence = QtWidgets.QGraphicsScene()
        pic_sence.setSceneRect(0, 0, int(img_w * ratio), MAXIMUM_HEIGHT)

        pic_sence.addPixmap(item_tuple[0])
        pic_view.setScene(pic_sence)

        pic_size_lb = QtWidgets.QLabel()
        pic_size_lb.setText(f"寬：{item_tuple[2][0]} 高：{item_tuple[2][1]}")

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_item(item))

        item_layout.addWidget(pic_name_lb)
        item_layout.addWidget(pic_view)
        item_layout.addWidget(pic_size_lb)
        item_layout.addStretch()
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.items_list.addItem(item)
        self.ui.items_list.setItemWidget(item, item_widget)
        self.ui.items_list.repaint()
        self.send_update_image_count.emit()

    def delete_item(self, item: QListWidgetItemPlus):
        """
        get the QListWidgetItem and remove it from QListWidget
        """
        index = self.ui.items_list.row(item)
        self.ui.items_list.takeItem(index)
        self.send_update_image_count.emit()

    def clear_list(self):
        """
        remove all QListWidgetItems in the QListWidget
        """
        self.ui.items_list.clear()
        self.send_update_image_count.emit()

    def show_big_img_window(self, item: QListWidgetItemPlus):
        """
        open and show the big image
        """
        MAXIMUM_WIDTH = 768
        MAXIMUM_HEIGHT = 512

        with Image.open(item.text) as img:
            img.thumbnail(size=(MAXIMUM_WIDTH, MAXIMUM_HEIGHT))

            img_raw_data = img.convert("RGB").tobytes("raw", "RGB")
            img = QtGui.QImage(
                img_raw_data,
                img.size[0],
                img.size[1],
                img.size[0] * 3,
                QtGui.QImage.Format.Format_RGB888,
            )

        img = QtGui.QPixmap.fromImage(img)

        self.img_widget = QtWidgets.QLabel()

        self.img_widget.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint
        )

        self.img_widget.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop
        )

        self.img_widget.setGeometry(0, 0, int(img.width()), int(img.height()))
        self.img_widget.setWindowTitle(f"{Path(item.text).name}")
        self.img_widget.setPixmap(img)
        self.img_widget.show()

    def select_output_dir(self):
        """
        show the file dialog and get the path where the report is exported
        """
        dir_path = QtWidgets.QFileDialog.getSaveFileName(caption="選取目標資料夾")[0]
        return dir_path

    def start_generate(self):
        """
        the main function to generate the report
        """
        picture_counts = self.ui.items_list.count()
        picture_list = list()

        for index in range(picture_counts):
            item_obj = self.ui.items_list.item(index)
            picture_list.append(item_obj.text)

        if not picture_list:
            messabebox = QMessageBox(self)
            messabebox.warning(self, "Error", "列表中無圖片")
            return

        output_dir = self.select_output_dir()

        self.img_stich(picture_list, output_dir)

        messabebox = QMessageBox(self)
        messabebox.information(self, "Success", "輸出完成")

    def img_stich(self, picture_list: list, output_dir: str):
        images = [Image.open(x) for x in picture_list]
        widths, heights = zip(*(i.size for i in images))

        if self.ui.horizon_rtn.isChecked():
            total_width = sum(widths)
            max_height = max(heights)

            new_im = Image.new("RGB", (total_width, max_height))

            x_offset = 0
            for img in images:
                new_im.paste(img, (x_offset, 0))
                x_offset += img.size[0]

            if self.ui.max_width_value.text():
                set_width = int(self.ui.max_width_value.text())
                new_im = new_im.resize((set_width, int(set_width/total_width*max_height)))

        else:
            max_width = max(widths)
            total_height = sum(heights)

            new_im = Image.new("RGB", (max_width, total_height))

            y_offset = 0
            for img in images:
                new_im.paste(img, (0, y_offset))
                y_offset += img.size[1]

            if self.ui.max_heigth_value.text():
                set_height = int(self.ui.max_heigth_value.text())
                new_im = new_im.resize((int(set_height/total_height*max_width), set_height))

        new_im.save(f"{output_dir}.jpg")

    def app_exit(self):
        """
        close this program
        """
        sys.exit()
