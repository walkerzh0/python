#!/usr/bin/python
#coding=utf-8


class HouseItem:
	def __init__(self, name, area):
		self.name = name
		self.area = area
		
class House:
	def __init__(self, area, item_list):
		self.area = area
		self.item_list = item_list
		self.free_area = area
		
	def add_item(self, item):
		self.item_list.append(item)
		self.free_area -= item.area
	
	def __str__(self):
		str = "area: %d, free_area: %d\n" % (self.area, self.free_area)
		for item in self.item_list:
			str += item.name + " "
			
		return str
			
		
mHouse = House(100, [])
print(mHouse)
mHouse.add_item(HouseItem("洗衣机", 2))
mHouse.add_item(HouseItem("电视", 1))
mHouse.add_item(HouseItem("桌子", 4))
mHouse.add_item(HouseItem("床", 6))
print(mHouse)

		
		