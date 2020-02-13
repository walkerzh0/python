# -*- coding: utf-8 -*-
# import xdrlib ,sys
# Author:walkersOnWay
# Time:2019-03-14
# Environment:python2.7


import xlrd                     #读取excel数据
import xlwt                     #创建表格并写入数据
from xlutils.copy import copy   #更新已存在的表格数据

class ExcelHelper:
    def __init__(self, excelFile, excelSheet):
        self.excelFile = excelFile
        self.excelSheet = excelSheet
        self.nrows = 0
        self.ncols = 0
        self.__data = self.openExcel(excelFile)
        #print "file:sheet = %s, %s; nrows, ncols = %d, %d", self.excelFile, self.excelSheet, self.nrows, self.ncols

    #打开文件
    def openExcel(self, excelFile):
        try:
            data = xlrd.open_workbook(excelFile)
            return data
        except Exception, e:
            print str(e)

    #根据sheet名读取sheet数据
    def getSheetDataByName(self):
        listRows = []
        table = self.__data.sheet_by_name(self.excelSheet)
        self.nrows = table.nrows    #行数
        self.ncols = table.ncols    #列数

        for idx in range(0, self.nrows):
            listRows.append(table.row_values(idx))
        return listRows

    #获取单元格数据
    def getCellData(self, row, col):
        table = self.__data.sheet_by_name(self.excelSheet)
        #print "[%d, %d] = " % (row, col), table.cell(row, col).__class__   #此处耗费时间很长,1、在于没返回值 2、返回值的类型不对
        print "table.cell(row, col).value", table.cell(row, col).value
        return table.cell(row, col).value

    #更新单元格数据
    def updataCellData(self, row, col, newData):
        newDataObj = copy(self.__data)          # 类型为worksheet 无nrows 方法
        newSheet = newDataObj.get_sheet(1)
        newSheet.write(row, col, newData)
        newDataObj.save(self.excelFile)         #此处需要保存成xls的格式,保存成xlsx会损坏数据,导致打开失败

    #获取列数据
    def getCol(self, col):
        table = self.__data.sheet_by_name(self.excelSheet)
        colList = table.col_values(col)
        return colList

    #打印整张表格数据
    def showSheetListRows(self, listRows):
        print "file:sheet = %s, %s; nrows, ncols = %d, %d", self.excelFile, self.excelSheet, self.nrows, self.ncols
        for tmpList in listRows:
            for k in range(0, self.ncols):
                print " ", tmpList[k],
            print "\n"

class ExcelHandler:
    #def __init__(self, oldExcel, newExcel）
    def __init__(self, oldExcel, newExcel, handleColIdxList):   #改进
        self.oldExcel = oldExcel                                #旧文件
        self.newExcel = newExcel                                #新文件
        self.handleColIdxList = handleColIdxList                #改进:要处理的列

    #用旧表更新新表
    def flushSheet(self, oldSheet, newSheet):
        oldExcelHelper = ExcelHelper(self.oldExcel, oldSheet)
        oldColList = oldExcelHelper.getCol(3)

        newExcelHelper = ExcelHelper(self.newExcel, newSheet)
        newColList = newExcelHelper.getCol(3)

        oldCurRow = 0
        newCurRow = 0
        for oldVal in oldColList:
            newCurRow = 0
            for newVal in newColList:
                if 0 == oldCurRow or 0 == newCurRow:
                    newCurRow += 1
                    continue
                if(oldVal == newVal):
                    #for idx in range(4, 8):                    #ok
                    for idx in self.handleColIdxList:           #改进,自定义要处理的列
                        oldExcelHelper = ExcelHelper(self.oldExcel, oldSheet)
                        newExcelHelper = ExcelHelper(self.newExcel, newSheet)
                        newExcelHelper.updataCellData(newCurRow, idx, oldExcelHelper.getCellData(oldCurRow, idx))
                        oldExcelHelper = ExcelHelper(self.oldExcel, oldSheet)
                        newExcelHelper = ExcelHelper(self.newExcel, newSheet)
                        newExcelHelper.updataCellData(newCurRow, 10, "old")
                newCurRow += 1
            oldCurRow += 1
#test
#读取并打印Excel中Sheet数据
#excelHelper1 = ExcelHelper("data/file1.xls", "0329")
#print "3 list is \n", excelHelper1.getCol(3)
#excelHelper1.showSheetListRows(excelHelper1.getSheetDataByName())
#excelHelper2 = ExcelHelper("data/file.xlsx", "0330")
#excelHelper2.showSheetListRows(excelHelper2.getSheetDataByName())

#读写单元格
#excelHelper1.getCellData(2, 3)
#excelHelper1.updataCellData(1, 0, "BIT_OPERATION_ERROR_NEW111222")

#同步两张sheet表格数据
handleColIdxList = [4, 6, 7]                                                        #改进:自定义需要更新的列索引
mExcelHandler = ExcelHandler("data/file1.xls", "data/file1.xls", handleColIdxList)  #改进
#mExcelHandler = ExcelHandler("data/file1.xls", "data/file1.xls")
mExcelHandler.flushSheet("0329", "0330")
