class ElectricalAppliance(object):
    def __init__(self,dict):
        self.dict = dict

    def getTariff(self):
        if self.type == "elect_bill":
            bill = 25
            bill += 43.54 if self.dict["electrical_appliance"]["pc"] else 0
            bill += 37.46 if self.dict["electrical_appliance"]["fridge"] else 0
            bill += 28 if self.dict["electrical_appliance"]["microwave"] else 0
            bill += 20 if self.dict["electrical_appliance"]["kettle"] else 0
            return bill