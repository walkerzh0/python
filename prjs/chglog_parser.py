#!/usr/bin/env python

# 使用之前先pip install reportlab安装绘图库

import re
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

class GaugeData:
    GAUGE_BAT_TEMP = 0
    GAUGE_AVGVBAT = GAUGE_BAT_TEMP + 1
    GAUGE_MINVBAT = GAUGE_AVGVBAT + 1
    GAUGE_ICHG = GAUGE_MINVBAT + 1
    GAUGE_OTHER = GAUGE_ICHG + 1
    GAUGE_REALSOC = GAUGE_OTHER + 1
    GAUGE_UISOC = GAUGE_REALSOC + 1

    def __init__(self, drawdata_file):
        self.drawdata_file = drawdata_file
        self.gaugedata = []

    def parser(self):
        gauge = []
        drawdata_file = open(self.drawdata_file, 'r', encoding='utf-8')
        dataline = drawdata_file.readline()
        print(dataline)
        gaugedata = self.gaugedata
        while dataline:
            gauge_dataunit = []
            tmpgaugedata = re.search(r'GAUGE.*?]', dataline).group()
            print(tmpgaugedata)
            gaugedatalist = tmpgaugedata.split(' ')
            print(gaugedatalist)
            srcidx = 1
            dstidx = 0
            while True:
                gauge_dataunit.append(gaugedatalist[srcidx])
                dstidx = dstidx + 1
                srcidx = srcidx + 2
                if dstidx == 8:
                    break
            gaugedata.append(gauge_dataunit)
            dataline = drawdata_file.readline()
        drawdata_file.close()
        # print(self.gaugedata)
        self.draw()

    def draw(self):
        len = self.gaugedata.__len__()
        gauge_batemp = []
        times = [i for i in range(len)]
        gauge_tbat = [int(data[0]) for data in self.gaugedata]
        gauge_avgvbat = [(int(data[1]) / 20) for data in self.gaugedata]
        gauge_minvbat = [(int(data[2]) / 20) for data in self.gaugedata]
        gauge_ichg = [int(data[3]) for data in self.gaugedata]
        gauge_other = [int(data[4]) for data in self.gaugedata]
        gauge_realsoc = [(int(data[5]) * 2) for data in self.gaugedata]
        gauge_uisoc = [(int(data[6]) * 2) for data in self.gaugedata]
        print(times)
        print('{}{}'.format(times.__len__(), gauge_batemp.__len__()))

        drawing = Drawing(500, 500)
        drawing.add(PolyLine(list(zip(times, gauge_tbat)), strokeColor=colors.blue))
        drawing.add(PolyLine(list(zip(times, gauge_avgvbat)), strokeColor=colors.red))
        drawing.add(PolyLine(list(zip(times, gauge_minvbat)), strokeColor=colors.yellow))
        drawing.add(PolyLine(list(zip(times, gauge_ichg)), strokeColor=colors.green))
        drawing.add(PolyLine(list(zip(times, gauge_other)), strokeColor=colors.pink))
        drawing.add(PolyLine(list(zip(times, gauge_realsoc)), strokeColor=colors.silver))
        drawing.add(PolyLine(list(zip(times, gauge_uisoc)), strokeColor=colors.orange))

        renderPDF.drawToFile(drawing, 'gauge_battemp.pdf', 'Sunspots1')

class ChgLogTool:
    def __init__(self, mobilelog_path):
        self.mobilelog_path = mobilelog_path
        self.mobilelog = []
        self.kernellog = []
        self.kernellog_file = r'E:\oppo\logs\kernel_log_4__2020_0101_011456'
        self.mobilelog_file = ''
        self.drawdata_file = r'E:\oppo\logs\drawdata_file.txt'

    def drawdata(self):
        kernellog_file = open(self.kernellog_file, 'r', encoding='utf-8')
        drawdata_file = open(self.drawdata_file, 'w', encoding='utf-8')
        dataline = kernellog_file.readline()
        print('dataline is :', dataline)
        while dataline:
            ret = re.search(r'.*GAUGE.*', dataline)
            if ret:
                #print(ret)
                drawdata_file.write(ret.group() + '\n')
            dataline = kernellog_file.readline()
        print('itera complete')
        drawdata_file.close()
        kernellog_file.close()
        # ChargerData(self.drawdata_file).parser()
        # BatData(self.drawdata_file).parser()
        GaugeData(self.drawdata_file).parser()
        # StatusData(self.drawdata_file).parser()

mChgLogTool = ChgLogTool(r'E:\oppo\logs')
mChgLogTool.get_drawdata()