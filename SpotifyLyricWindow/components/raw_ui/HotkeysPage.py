# Form implementation generated from reading ui file 'E:\code\git-code\Spotify-lyrics-window\SpotifyLyricWindow\resource\ui\ui_file\HotkeysPage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HotkeysPage(object):
    def setupUi(self, HotkeysPage):
        HotkeysPage.setObjectName("HotkeysPage")
        HotkeysPage.resize(867, 566)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        HotkeysPage.setFont(font)
        self.hotkeyspage_gridLayout = QtWidgets.QGridLayout(HotkeysPage)
        self.hotkeyspage_gridLayout.setContentsMargins(50, 20, 30, 40)
        self.hotkeyspage_gridLayout.setObjectName("hotkeyspage_gridLayout")
        self.hotkeys_default_button = QtWidgets.QPushButton(parent=HotkeysPage)
        self.hotkeys_default_button.setMinimumSize(QtCore.QSize(100, 32))
        self.hotkeys_default_button.setMaximumSize(QtCore.QSize(100, 32))
        self.hotkeys_default_button.setObjectName("hotkeys_default_button")
        self.hotkeyspage_gridLayout.addWidget(self.hotkeys_default_button, 1, 2, 1, 1)
        self.enable_hotkeys_checkBox = QtWidgets.QCheckBox(parent=HotkeysPage)
        self.enable_hotkeys_checkBox.setMinimumSize(QtCore.QSize(0, 32))
        self.enable_hotkeys_checkBox.setMaximumSize(QtCore.QSize(16777215, 32))
        self.enable_hotkeys_checkBox.setObjectName("enable_hotkeys_checkBox")
        self.hotkeyspage_gridLayout.addWidget(self.enable_hotkeys_checkBox, 1, 0, 1, 1)
        self.hotkeys_frame = QtWidgets.QFrame(parent=HotkeysPage)
        self.hotkeys_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hotkeys_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hotkeys_frame.setObjectName("hotkeys_frame")
        self.HotkeysFrameGridLayout = QtWidgets.QGridLayout(self.hotkeys_frame)
        self.HotkeysFrameGridLayout.setContentsMargins(0, 0, 0, 0)
        self.HotkeysFrameGridLayout.setSpacing(0)
        self.HotkeysFrameGridLayout.setObjectName("HotkeysFrameGridLayout")
        self.hotkeyslabel_frame = QtWidgets.QFrame(parent=self.hotkeys_frame)
        self.hotkeyslabel_frame.setMinimumSize(QtCore.QSize(0, 32))
        self.hotkeyslabel_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hotkeyslabel_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hotkeyslabel_frame.setObjectName("hotkeyslabel_frame")
        self.HotkeysLabelFrameVerticalLayout = QtWidgets.QVBoxLayout(self.hotkeyslabel_frame)
        self.HotkeysLabelFrameVerticalLayout.setContentsMargins(0, -1, -1, -1)
        self.HotkeysLabelFrameVerticalLayout.setObjectName("HotkeysLabelFrameVerticalLayout")
        self.pause_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.pause_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.pause_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.pause_hotkey_label.setObjectName("pause_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.pause_hotkey_label)
        self.last_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.last_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.last_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.last_hotkey_label.setObjectName("last_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.last_hotkey_label)
        self.next_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.next_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.next_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.next_hotkey_label.setObjectName("next_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.next_hotkey_label)
        self.lock_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.lock_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.lock_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lock_hotkey_label.setObjectName("lock_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.lock_hotkey_label)
        self.calibration_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.calibration_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.calibration_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.calibration_hotkey_label.setObjectName("calibration_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.calibration_hotkey_label)
        self.trans_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.trans_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.trans_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.trans_hotkey_label.setObjectName("trans_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.trans_hotkey_label)
        self.show_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.show_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.show_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.show_hotkey_label.setObjectName("show_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.show_hotkey_label)
        self.close_hotkey_label = QtWidgets.QLabel(parent=self.hotkeyslabel_frame)
        self.close_hotkey_label.setMinimumSize(QtCore.QSize(0, 32))
        self.close_hotkey_label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.close_hotkey_label.setObjectName("close_hotkey_label")
        self.HotkeysLabelFrameVerticalLayout.addWidget(self.close_hotkey_label)
        self.HotkeysFrameGridLayout.addWidget(self.hotkeyslabel_frame, 0, 0, 1, 1)
        self.hotkeyslineedit_frame = QtWidgets.QFrame(parent=self.hotkeys_frame)
        self.hotkeyslineedit_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hotkeyslineedit_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hotkeyslineedit_frame.setObjectName("hotkeyslineedit_frame")
        self.HotkeysLineEditFrameVerticalLayout = QtWidgets.QVBoxLayout(self.hotkeyslineedit_frame)
        self.HotkeysLineEditFrameVerticalLayout.setContentsMargins(20, -1, -1, -1)
        self.HotkeysLineEditFrameVerticalLayout.setObjectName("HotkeysLineEditFrameVerticalLayout")
        self.HotkeysFrameGridLayout.addWidget(self.hotkeyslineedit_frame, 0, 1, 1, 1)
        self.hotkeyspage_gridLayout.addWidget(self.hotkeys_frame, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(164, 29, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hotkeyspage_gridLayout.addItem(spacerItem, 1, 1, 1, 1)

        self.retranslateUi(HotkeysPage)
        QtCore.QMetaObject.connectSlotsByName(HotkeysPage)

    def retranslateUi(self, HotkeysPage):
        _translate = QtCore.QCoreApplication.translate
        HotkeysPage.setWindowTitle(_translate("HotkeysPage", "LyricsPage"))
        self.hotkeys_default_button.setText(_translate("HotkeysPage", "恢复默认"))
        self.enable_hotkeys_checkBox.setText(_translate("HotkeysPage", "启用快捷键"))
        self.pause_hotkey_label.setText(_translate("HotkeysPage", "暂停/继续"))
        self.last_hotkey_label.setText(_translate("HotkeysPage", "上一首"))
        self.next_hotkey_label.setText(_translate("HotkeysPage", "下一首"))
        self.lock_hotkey_label.setText(_translate("HotkeysPage", "锁定"))
        self.calibration_hotkey_label.setText(_translate("HotkeysPage", "校准"))
        self.trans_hotkey_label.setText(_translate("HotkeysPage", "切换翻译"))
        self.show_hotkey_label.setText(_translate("HotkeysPage", "显示"))
        self.close_hotkey_label.setText(_translate("HotkeysPage", "关闭"))
