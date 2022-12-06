class Facility:
    fac_list= []
    def __init__(self, facilities= ""):
        self.facilities= facilities 

    def addFacility(self):
        facilit_add= input("Enter Facility: \n")
        self.fac_list.append(facilit_add)

    def displayFacilities(self):
        facility_open= open("information/facilities.txt", "r")
        lines= facility_open.readlines()
        for l in lines:
            print(l)
    def writeListsOffacilitiesToFile(self):
                facility_open= open("information/facilities.txt", "a")
                for facility in self.fac_list:
                    facility_open.write("\n " + facility)

class Mangement:
    Facility().addFacility()
    Facility().writeListsOffacilitiesToFile()
                



