# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LyricsPage(object):
    def setupUi(self, LyricsPage):
        LyricsPage.setObjectName("LyricsPage")
        LyricsPage.resize(643, 470)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        LyricsPage.setFont(font)
        self.lyricspage_gridLayout = QtWidgets.QGridLayout(LyricsPage)
        self.lyricspage_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lyricspage_gridLayout.setSpacing(0)
        self.lyricspage_gridLayout.setObjectName("lyricspage_gridLayout")
        self.change_color_frame = QtWidgets.QFrame(LyricsPage)
        self.change_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.change_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.change_color_frame.setObjectName("change_color_frame")
        self.ChangeColorGridLayout_2 = QtWidgets.QGridLayout(self.change_color_frame)
        self.ChangeColorGridLayout_2.setObjectName("ChangeColorGridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ChangeColorGridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.color_label = QtWidgets.QLabel(self.change_color_frame)
        self.color_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.color_label.setObjectName("color_label")
        self.ChangeColorGridLayout_2.addWidget(self.color_label, 0, 0, 1, 2)
        self.lyricsdefault_button = QtWidgets.QPushButton(self.change_color_frame)
        self.lyricsdefault_button.setMinimumSize(QtCore.QSize(100, 32))
        self.lyricsdefault_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lyricsdefault_button.setObjectName("lyricsdefault_button")
        self.ChangeColorGridLayout_2.addWidget(self.lyricsdefault_button, 1, 4, 1, 1)
        self.shadow_color_frame = QtWidgets.QFrame(self.change_color_frame)
        self.shadow_color_frame.setMaximumSize(QtCore.QSize(132, 32))
        self.shadow_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shadow_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadow_color_frame.setObjectName("shadow_color_frame")
        self.ShadowColorHorizontalLayout_2 = QtWidgets.QHBoxLayout(self.shadow_color_frame)
        self.ShadowColorHorizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ShadowColorHorizontalLayout_2.setSpacing(0)
        self.ShadowColorHorizontalLayout_2.setObjectName("ShadowColorHorizontalLayout_2")
        self.shadow_color_label = QtWidgets.QLabel(self.shadow_color_frame)
        self.shadow_color_label.setMinimumSize(QtCore.QSize(32, 32))
        self.shadow_color_label.setMaximumSize(QtCore.QSize(32, 32))
        self.shadow_color_label.setText("")
        self.shadow_color_label.setObjectName("shadow_color_label")
        self.ShadowColorHorizontalLayout_2.addWidget(self.shadow_color_label)
        self.shadow_color_button = QtWidgets.QPushButton(self.shadow_color_frame)
        self.shadow_color_button.setMinimumSize(QtCore.QSize(100, 32))
        self.shadow_color_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.shadow_color_button.setObjectName("shadow_color_button")
        self.ShadowColorHorizontalLayout_2.addWidget(self.shadow_color_button)
        self.ChangeColorGridLayout_2.addWidget(self.shadow_color_frame, 1, 2, 1, 1)
        self.lyrics_color_frame = QtWidgets.QFrame(self.change_color_frame)
        self.lyrics_color_frame.setMaximumSize(QtCore.QSize(132, 32))
        self.lyrics_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lyrics_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lyrics_color_frame.setObjectName("lyrics_color_frame")
        self.LyricsColorHorizontalLayout_2 = QtWidgets.QHBoxLayout(self.lyrics_color_frame)
        self.LyricsColorHorizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LyricsColorHorizontalLayout_2.setSpacing(0)
        self.LyricsColorHorizontalLayout_2.setObjectName("LyricsColorHorizontalLayout_2")
        self.lyrics_color_label = QtWidgets.QLabel(self.lyrics_color_frame)
        self.lyrics_color_label.setMinimumSize(QtCore.QSize(32, 32))
        self.lyrics_color_label.setMaximumSize(QtCore.QSize(32, 32))
        self.lyrics_color_label.setText("")
        self.lyrics_color_label.setObjectName("lyrics_color_label")
        self.LyricsColorHorizontalLayout_2.addWidget(self.lyrics_color_label)
        self.lyrics_color_button = QtWidgets.QPushButton(self.lyrics_color_frame)
        self.lyrics_color_button.setMinimumSize(QtCore.QSize(100, 32))
        self.lyrics_color_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lyrics_color_button.setObjectName("lyrics_color_button")
        self.LyricsColorHorizontalLayout_2.addWidget(self.lyrics_color_button)
        self.ChangeColorGridLayout_2.addWidget(self.lyrics_color_frame, 1, 1, 1, 1)
        self.color_comboBox = QtWidgets.QComboBox(self.change_color_frame)
        self.color_comboBox.setMinimumSize(QtCore.QSize(100, 32))
        self.color_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.color_comboBox.setObjectName("color_comboBox")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.ChangeColorGridLayout_2.addWidget(self.color_comboBox, 1, 0, 1, 1)
        self.lyricspage_gridLayout.addWidget(self.change_color_frame, 3, 0, 1, 1)
        self.lyrics_trans_frame = QtWidgets.QFrame(LyricsPage)
        self.lyrics_trans_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lyrics_trans_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lyrics_trans_frame.setObjectName("lyrics_trans_frame")
        self.LyricsTransVerticalLayout_2 = QtWidgets.QVBoxLayout(self.lyrics_trans_frame)
        self.LyricsTransVerticalLayout_2.setObjectName("LyricsTransVerticalLayout_2")
        self.lyrics_trans_label = QtWidgets.QLabel(self.lyrics_trans_frame)
        self.lyrics_trans_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lyrics_trans_label.setObjectName("lyrics_trans_label")
        self.LyricsTransVerticalLayout_2.addWidget(self.lyrics_trans_label)
        self.trans_checkBox = QtWidgets.QCheckBox(self.lyrics_trans_frame)
        self.trans_checkBox.setObjectName("trans_checkBox")
        self.LyricsTransVerticalLayout_2.addWidget(self.trans_checkBox)
        self.romoji_checkBox = QtWidgets.QCheckBox(self.lyrics_trans_frame)
        self.romoji_checkBox.setObjectName("romoji_checkBox")
        self.LyricsTransVerticalLayout_2.addWidget(self.romoji_checkBox)
        self.lyricspage_gridLayout.addWidget(self.lyrics_trans_frame, 0, 0, 1, 1)
        self.font_frame = QtWidgets.QFrame(LyricsPage)
        self.font_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.font_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.font_frame.setObjectName("font_frame")
        self.FontVerticalLayout_2 = QtWidgets.QVBoxLayout(self.font_frame)
        self.FontVerticalLayout_2.setObjectName("FontVerticalLayout_2")
        self.font_label = QtWidgets.QLabel(self.font_frame)
        self.font_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.font_label.setObjectName("font_label")
        self.FontVerticalLayout_2.addWidget(self.font_label)
        self.font_comboBox = QtWidgets.QComboBox(self.font_frame)
        self.font_comboBox.setMinimumSize(QtCore.QSize(0, 32))
        self.font_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.font_comboBox.setObjectName("font_comboBox")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.font_comboBox.addItem("")
        self.FontVerticalLayout_2.addWidget(self.font_comboBox)
        self.lyricspage_gridLayout.addWidget(self.font_frame, 2, 0, 1, 1)
        self.always_front_frame = QtWidgets.QFrame(LyricsPage)
        self.always_front_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.always_front_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.always_front_frame.setObjectName("always_front_frame")
        self.AlwaysFrontVerticalLayout_3 = QtWidgets.QVBoxLayout(self.always_front_frame)
        self.AlwaysFrontVerticalLayout_3.setObjectName("AlwaysFrontVerticalLayout_3")
        self.always_front_label = QtWidgets.QLabel(self.always_front_frame)
        self.always_front_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.always_front_label.setObjectName("always_front_label")
        self.AlwaysFrontVerticalLayout_3.addWidget(self.always_front_label)
        self.enable_front_checkBox = QtWidgets.QCheckBox(self.always_front_frame)
        self.enable_front_checkBox.setObjectName("enable_front_checkBox")
        self.AlwaysFrontVerticalLayout_3.addWidget(self.enable_front_checkBox)
        self.lyricspage_gridLayout.addWidget(self.always_front_frame, 1, 0, 1, 1)

        self.retranslateUi(LyricsPage)
        self.color_comboBox.setCurrentIndex(1)
        self.font_comboBox.setCurrentIndex(44)
        QtCore.QMetaObject.connectSlotsByName(LyricsPage)

    def retranslateUi(self, LyricsPage):
        _translate = QtCore.QCoreApplication.translate
        LyricsPage.setWindowTitle(_translate("LyricsPage", "LyricsPage"))
        self.color_label.setText(_translate("LyricsPage", "更改歌词颜色:"))
        self.lyricsdefault_button.setText(_translate("LyricsPage", "恢复默认"))
        self.shadow_color_button.setText(_translate("LyricsPage", "阴影"))
        self.lyrics_color_button.setText(_translate("LyricsPage", "歌词"))
        self.color_comboBox.setItemText(0, _translate("LyricsPage", "自定义"))
        self.color_comboBox.setItemText(1, _translate("LyricsPage", "蓝"))
        self.color_comboBox.setItemText(2, _translate("LyricsPage", "红"))
        self.color_comboBox.setItemText(3, _translate("LyricsPage", "紫"))
        self.color_comboBox.setItemText(4, _translate("LyricsPage", "绿"))
        self.color_comboBox.setItemText(5, _translate("LyricsPage", "橘"))
        self.color_comboBox.setItemText(6, _translate("LyricsPage", "黄"))
        self.color_comboBox.setItemText(7, _translate("LyricsPage", "棕"))
        self.color_comboBox.setItemText(8, _translate("LyricsPage", "青"))
        self.color_comboBox.setItemText(9, _translate("LyricsPage", "粉"))
        self.lyrics_trans_label.setText(_translate("LyricsPage", "歌词翻译:"))
        self.trans_checkBox.setText(_translate("LyricsPage", "显示翻译"))
        self.romoji_checkBox.setText(_translate("LyricsPage", "显示音译"))
        self.font_label.setText(_translate("LyricsPage", "字体:"))
        self.font_comboBox.setItemText(0, _translate("LyricsPage", "Ebrima"))
        self.font_comboBox.setItemText(1, _translate("LyricsPage", "Gadugi"))
        self.font_comboBox.setItemText(2, _translate("LyricsPage", "Leelawadee"))
        self.font_comboBox.setItemText(3, _translate("LyricsPage", "Leelawadee UI"))
        self.font_comboBox.setItemText(4, _translate("LyricsPage", "Lucida Sans Unicode"))
        self.font_comboBox.setItemText(5, _translate("LyricsPage", "MS Gothic"))
        self.font_comboBox.setItemText(6, _translate("LyricsPage", "MS Mincho"))
        self.font_comboBox.setItemText(7, _translate("LyricsPage", "MS PGothic"))
        self.font_comboBox.setItemText(8, _translate("LyricsPage", "MS PMincho"))
        self.font_comboBox.setItemText(9, _translate("LyricsPage", "MS UI Gothic"))
        self.font_comboBox.setItemText(10, _translate("LyricsPage", "Malgun Gothic"))
        self.font_comboBox.setItemText(11, _translate("LyricsPage", "Malgun Gothic Semilight"))
        self.font_comboBox.setItemText(12, _translate("LyricsPage", "Meiryo"))
        self.font_comboBox.setItemText(13, _translate("LyricsPage", "Meiryo UI"))
        self.font_comboBox.setItemText(14, _translate("LyricsPage", "Microsoft JhengHei UI"))
        self.font_comboBox.setItemText(15, _translate("LyricsPage", "Microsoft JhengHei UI Light"))
        self.font_comboBox.setItemText(16, _translate("LyricsPage", "Microsoft Sans Serif"))
        self.font_comboBox.setItemText(17, _translate("LyricsPage", "Microsoft YaHei UI"))
        self.font_comboBox.setItemText(18, _translate("LyricsPage", "Microsoft YaHei UI Light"))
        self.font_comboBox.setItemText(19, _translate("LyricsPage", "Nirmala UI"))
        self.font_comboBox.setItemText(20, _translate("LyricsPage", "Nirmala UI Semilight"))
        self.font_comboBox.setItemText(21, _translate("LyricsPage", "Segoe UI"))
        self.font_comboBox.setItemText(22, _translate("LyricsPage", "Segoe UI Light"))
        self.font_comboBox.setItemText(23, _translate("LyricsPage", "Segoe UI Semibold"))
        self.font_comboBox.setItemText(24, _translate("LyricsPage", "Segoe UI Semilight"))
        self.font_comboBox.setItemText(25, _translate("LyricsPage", "SimSun-ExtB"))
        self.font_comboBox.setItemText(26, _translate("LyricsPage", "Tahoma"))
        self.font_comboBox.setItemText(27, _translate("LyricsPage", "Yu Gothic UI"))
        self.font_comboBox.setItemText(28, _translate("LyricsPage", "Yu Gothic UI Light"))
        self.font_comboBox.setItemText(29, _translate("LyricsPage", "Yu Gothic UI Semibold"))
        self.font_comboBox.setItemText(30, _translate("LyricsPage", "Yu Gothic UI Semilight"))
        self.font_comboBox.setItemText(31, _translate("LyricsPage", "仿宋"))
        self.font_comboBox.setItemText(32, _translate("LyricsPage", "华文中宋"))
        self.font_comboBox.setItemText(33, _translate("LyricsPage", "华文仿宋"))
        self.font_comboBox.setItemText(34, _translate("LyricsPage", "华文宋体"))
        self.font_comboBox.setItemText(35, _translate("LyricsPage", "华文彩云"))
        self.font_comboBox.setItemText(36, _translate("LyricsPage", "华文新魏"))
        self.font_comboBox.setItemText(37, _translate("LyricsPage", "华文楷体"))
        self.font_comboBox.setItemText(38, _translate("LyricsPage", "华文琥珀"))
        self.font_comboBox.setItemText(39, _translate("LyricsPage", "华文细黑"))
        self.font_comboBox.setItemText(40, _translate("LyricsPage", "华文行楷"))
        self.font_comboBox.setItemText(41, _translate("LyricsPage", "华文隶书"))
        self.font_comboBox.setItemText(42, _translate("LyricsPage", "宋体"))
        self.font_comboBox.setItemText(43, _translate("LyricsPage", "幼圆"))
        self.font_comboBox.setItemText(44, _translate("LyricsPage", "微软雅黑"))
        self.font_comboBox.setItemText(45, _translate("LyricsPage", "微软雅黑 Light"))
        self.font_comboBox.setItemText(46, _translate("LyricsPage", "新宋体"))
        self.font_comboBox.setItemText(47, _translate("LyricsPage", "方正姚体"))
        self.font_comboBox.setItemText(48, _translate("LyricsPage", "方正舒体"))
        self.font_comboBox.setItemText(49, _translate("LyricsPage", "楷体"))
        self.font_comboBox.setItemText(50, _translate("LyricsPage", "等线"))
        self.font_comboBox.setItemText(51, _translate("LyricsPage", "等线 Light"))
        self.font_comboBox.setItemText(52, _translate("LyricsPage", "隶书"))
        self.font_comboBox.setItemText(53, _translate("LyricsPage", "黑体"))
        self.always_front_label.setText(_translate("LyricsPage", "总在最前:"))
        self.enable_front_checkBox.setText(_translate("LyricsPage", "启用总在最前"))
