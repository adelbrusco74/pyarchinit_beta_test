# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_image_viewer_dialog.ui'
#
# Created: Fri Oct 19 22:21:46 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogImageViewer(object):
    def setupUi(self, DialogImageViewer):
        DialogImageViewer.setObjectName(_fromUtf8("DialogImageViewer"))
        DialogImageViewer.resize(986, 664)
        self.gridLayout_2 = QtGui.QGridLayout(DialogImageViewer)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(DialogImageViewer)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_img_visualizzate = QtGui.QLabel(self.layoutWidget)
        self.label_img_visualizzate.setText(_fromUtf8(""))
        self.label_img_visualizzate.setObjectName(_fromUtf8("label_img_visualizzate"))
        self.gridLayout.addWidget(self.label_img_visualizzate, 0, 3, 1, 1)
        self.label_num_tot_immagini = QtGui.QLabel(self.layoutWidget)
        self.label_num_tot_immagini.setText(_fromUtf8(""))
        self.label_num_tot_immagini.setObjectName(_fromUtf8("label_num_tot_immagini"))
        self.gridLayout.addWidget(self.label_num_tot_immagini, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.iconListWidget = QtGui.QListWidget(self.layoutWidget)
        self.iconListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.iconListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.iconListWidget.setLineWidth(2)
        self.iconListWidget.setMidLineWidth(2)
        self.iconListWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.iconListWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.iconListWidget.setIconSize(QtCore.QSize(150, 150))
        self.iconListWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.iconListWidget.setMovement(QtGui.QListView.Snap)
        self.iconListWidget.setResizeMode(QtGui.QListView.Adjust)
        self.iconListWidget.setLayoutMode(QtGui.QListView.Batched)
        self.iconListWidget.setGridSize(QtCore.QSize(154, 154))
        self.iconListWidget.setViewMode(QtGui.QListView.IconMode)
        self.iconListWidget.setModelColumn(0)
        self.iconListWidget.setUniformItemSizes(False)
        self.iconListWidget.setBatchSize(1000)
        self.iconListWidget.setObjectName(_fromUtf8("iconListWidget"))
        self.gridLayout.addWidget(self.iconListWidget, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(DialogImageViewer)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.formLayout = QtGui.QFormLayout(self.tab_1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButton_delete = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout_5.addWidget(self.pushButton_delete, 2, 0, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon1)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout_5.addWidget(self.pushButton_new_search, 2, 2, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon2)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout_5.addWidget(self.pushButton_search_go, 2, 3, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon3)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout_5.addWidget(self.pushButton_sort, 2, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon4)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout_5.addWidget(self.pushButton_view_all, 2, 4, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(self.tab_1)
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon5)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout_5.addWidget(self.pushButton_last_rec, 0, 0, 1, 1)
        self.pushButton_first_rec = QtGui.QPushButton(self.tab_1)
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon6)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout_5.addWidget(self.pushButton_first_rec, 0, 1, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(self.tab_1)
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon7)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout_5.addWidget(self.pushButton_prev_rec, 0, 2, 1, 1)
        self.pushButton_next_rec = QtGui.QPushButton(self.tab_1)
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon8)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout_5.addWidget(self.pushButton_next_rec, 0, 3, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon9)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout_5.addWidget(self.pushButton_new_rec, 0, 4, 1, 1)
        self.pushButton_save = QtGui.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon10)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout_5.addWidget(self.pushButton_save, 0, 6, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.label_29 = QtGui.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_openMedia = QtGui.QPushButton(self.tab_1)
        self.pushButton_openMedia.setObjectName(_fromUtf8("pushButton_openMedia"))
        self.gridLayout_4.addWidget(self.pushButton_openMedia, 0, 1, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.gridLayout_4)
        self.pushButton_chose_dir = QtGui.QPushButton(self.tab_1)
        self.pushButton_chose_dir.setObjectName(_fromUtf8("pushButton_chose_dir"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_chose_dir)
        self.label_5 = QtGui.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.tableWidget_tags = QtGui.QTableWidget(self.tab_1)
        self.tableWidget_tags.setObjectName(_fromUtf8("tableWidget_tags"))
        self.tableWidget_tags.setColumnCount(3)
        self.tableWidget_tags.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tags.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tags.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tags.setHorizontalHeaderItem(2, item)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.tableWidget_tags)
        self.toolButton_tags_on_off = QtGui.QToolButton(self.tab_1)
        self.toolButton_tags_on_off.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolButton_tags_on_off.setCheckable(True)
        self.toolButton_tags_on_off.setAutoRepeatDelay(300)
        self.toolButton_tags_on_off.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_tags_on_off.setObjectName(_fromUtf8("toolButton_tags_on_off"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.toolButton_tags_on_off)
        self.line = QtGui.QFrame(self.tab_1)
        self.line.setMinimumSize(QtCore.QSize(500, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.line)
        self.pushButton_remove_tags = QtGui.QPushButton(self.tab_1)
        self.pushButton_remove_tags.setObjectName(_fromUtf8("pushButton_remove_tags"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.pushButton_remove_tags)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_addRow_US = QtGui.QPushButton(self.tab_2)
        self.pushButton_addRow_US.setObjectName(_fromUtf8("pushButton_addRow_US"))
        self.horizontalLayout.addWidget(self.pushButton_addRow_US)
        self.pushButton_removeRow_US = QtGui.QPushButton(self.tab_2)
        self.pushButton_removeRow_US.setObjectName(_fromUtf8("pushButton_removeRow_US"))
        self.horizontalLayout.addWidget(self.pushButton_removeRow_US)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidgetTags_US = QtGui.QTableWidget(self.tab_2)
        self.tableWidgetTags_US.setObjectName(_fromUtf8("tableWidgetTags_US"))
        self.tableWidgetTags_US.setColumnCount(3)
        self.tableWidgetTags_US.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_US.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_US.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_US.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_US.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidgetTags_US)
        self.pushButton_assignTags_US = QtGui.QPushButton(self.tab_2)
        self.pushButton_assignTags_US.setObjectName(_fromUtf8("pushButton_assignTags_US"))
        self.verticalLayout_2.addWidget(self.pushButton_assignTags_US)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pushButton_addRow_MAT = QtGui.QPushButton(self.tab)
        self.pushButton_addRow_MAT.setObjectName(_fromUtf8("pushButton_addRow_MAT"))
        self.horizontalLayout_2.addWidget(self.pushButton_addRow_MAT)
        self.pushButton_removeRow_MAT = QtGui.QPushButton(self.tab)
        self.pushButton_removeRow_MAT.setObjectName(_fromUtf8("pushButton_removeRow_MAT"))
        self.horizontalLayout_2.addWidget(self.pushButton_removeRow_MAT)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tableWidgetTags_MAT = QtGui.QTableWidget(self.tab)
        self.tableWidgetTags_MAT.setObjectName(_fromUtf8("tableWidgetTags_MAT"))
        self.tableWidgetTags_MAT.setColumnCount(2)
        self.tableWidgetTags_MAT.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_MAT.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_MAT.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTags_MAT.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.tableWidgetTags_MAT)
        self.pushButton_assignTags_MAT = QtGui.QPushButton(self.tab)
        self.pushButton_assignTags_MAT.setObjectName(_fromUtf8("pushButton_assignTags_MAT"))
        self.verticalLayout_3.addWidget(self.pushButton_assignTags_MAT)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 461, 87))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton_delete_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete_2.setFont(font)
        self.pushButton_delete_2.setText(_fromUtf8(""))
        self.pushButton_delete_2.setIcon(icon)
        self.pushButton_delete_2.setObjectName(_fromUtf8("pushButton_delete_2"))
        self.gridLayout_8.addWidget(self.pushButton_delete_2, 2, 0, 1, 1)
        self.pushButton_new_search_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search_2.setFont(font)
        self.pushButton_new_search_2.setText(_fromUtf8(""))
        self.pushButton_new_search_2.setIcon(icon1)
        self.pushButton_new_search_2.setObjectName(_fromUtf8("pushButton_new_search_2"))
        self.gridLayout_8.addWidget(self.pushButton_new_search_2, 2, 2, 1, 1)
        self.pushButton_search_go_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go_2.setFont(font)
        self.pushButton_search_go_2.setText(_fromUtf8(""))
        self.pushButton_search_go_2.setIcon(icon2)
        self.pushButton_search_go_2.setObjectName(_fromUtf8("pushButton_search_go_2"))
        self.gridLayout_8.addWidget(self.pushButton_search_go_2, 2, 3, 1, 1)
        self.pushButton_sort_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort_2.setFont(font)
        self.pushButton_sort_2.setText(_fromUtf8(""))
        self.pushButton_sort_2.setIcon(icon3)
        self.pushButton_sort_2.setObjectName(_fromUtf8("pushButton_sort_2"))
        self.gridLayout_8.addWidget(self.pushButton_sort_2, 2, 6, 1, 1)
        self.pushButton_view_all_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all_2.setFont(font)
        self.pushButton_view_all_2.setText(_fromUtf8(""))
        self.pushButton_view_all_2.setIcon(icon4)
        self.pushButton_view_all_2.setObjectName(_fromUtf8("pushButton_view_all_2"))
        self.gridLayout_8.addWidget(self.pushButton_view_all_2, 2, 4, 1, 1)
        self.pushButton_last_rec_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_last_rec_2.setText(_fromUtf8(""))
        self.pushButton_last_rec_2.setIcon(icon5)
        self.pushButton_last_rec_2.setObjectName(_fromUtf8("pushButton_last_rec_2"))
        self.gridLayout_8.addWidget(self.pushButton_last_rec_2, 0, 0, 1, 1)
        self.pushButton_first_rec_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_first_rec_2.setText(_fromUtf8(""))
        self.pushButton_first_rec_2.setIcon(icon6)
        self.pushButton_first_rec_2.setObjectName(_fromUtf8("pushButton_first_rec_2"))
        self.gridLayout_8.addWidget(self.pushButton_first_rec_2, 0, 1, 1, 1)
        self.pushButton_prev_rec_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_prev_rec_2.setText(_fromUtf8(""))
        self.pushButton_prev_rec_2.setIcon(icon7)
        self.pushButton_prev_rec_2.setObjectName(_fromUtf8("pushButton_prev_rec_2"))
        self.gridLayout_8.addWidget(self.pushButton_prev_rec_2, 0, 2, 1, 1)
        self.pushButton_next_rec_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_next_rec_2.setText(_fromUtf8(""))
        self.pushButton_next_rec_2.setIcon(icon8)
        self.pushButton_next_rec_2.setObjectName(_fromUtf8("pushButton_next_rec_2"))
        self.gridLayout_8.addWidget(self.pushButton_next_rec_2, 0, 3, 1, 1)
        self.pushButton_new_rec_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec_2.setFont(font)
        self.pushButton_new_rec_2.setText(_fromUtf8(""))
        self.pushButton_new_rec_2.setIcon(icon9)
        self.pushButton_new_rec_2.setObjectName(_fromUtf8("pushButton_new_rec_2"))
        self.gridLayout_8.addWidget(self.pushButton_new_rec_2, 0, 4, 1, 1)
        self.pushButton_save_2 = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save_2.setFont(font)
        self.pushButton_save_2.setText(_fromUtf8(""))
        self.pushButton_save_2.setIcon(icon10)
        self.pushButton_save_2.setAutoDefault(False)
        self.pushButton_save_2.setObjectName(_fromUtf8("pushButton_save_2"))
        self.gridLayout_8.addWidget(self.pushButton_save_2, 0, 6, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 2)
        self.label_30 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 1)
        self.pushButton_openMedia_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_openMedia_2.setObjectName(_fromUtf8("pushButton_openMedia_2"))
        self.gridLayout_7.addWidget(self.pushButton_openMedia_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(DialogImageViewer)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DialogImageViewer)

    def retranslateUi(self, DialogImageViewer):
        DialogImageViewer.setWindowTitle(QtGui.QApplication.translate("DialogImageViewer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogImageViewer", "Numero Totale Immagini", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogImageViewer", "Immagini visualizzate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DialogImageViewer", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openMedia.setText(QtGui.QApplication.translate("DialogImageViewer", "Apri Immagini", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_chose_dir.setText(QtGui.QApplication.translate("DialogImageViewer", "Carica le immagini nel DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogImageViewer", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_tags.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DialogImageViewer", "ID tag", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_tags.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DialogImageViewer", "Categoria Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_tags.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DialogImageViewer", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_tags_on_off.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Attiva/disattiva la visualizzazione dei tags", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_tags_on_off.setText(QtGui.QApplication.translate("DialogImageViewer", "Tags viewer on/off", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remove_tags.setText(QtGui.QApplication.translate("DialogImageViewer", "Rimuovi tags", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("DialogImageViewer", "Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogImageViewer", "Tags manager", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_addRow_US.setText(QtGui.QApplication.translate("DialogImageViewer", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removeRow_US.setText(QtGui.QApplication.translate("DialogImageViewer", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTags_US.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DialogImageViewer", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTags_US.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DialogImageViewer", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTags_US.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("DialogImageViewer", "US", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_assignTags_US.setText(QtGui.QApplication.translate("DialogImageViewer", "Assegna i tags", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("DialogImageViewer", "Tags Unita\' Stratigrafiche", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogImageViewer", "Tags manager", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_addRow_MAT.setText(QtGui.QApplication.translate("DialogImageViewer", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removeRow_MAT.setText(QtGui.QApplication.translate("DialogImageViewer", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTags_MAT.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DialogImageViewer", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTags_MAT.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DialogImageViewer", "Numero Inventario", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_assignTags_MAT.setText(QtGui.QApplication.translate("DialogImageViewer", "Assegna i tags", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("DialogImageViewer", "Tags Inventario Materiali", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save_2.setToolTip(QtGui.QApplication.translate("DialogImageViewer", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("DialogImageViewer", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openMedia_2.setText(QtGui.QApplication.translate("DialogImageViewer", "Apri Immagini", None, QtGui.QApplication.UnicodeUTF8))
