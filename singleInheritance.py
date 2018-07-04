class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to ",self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearofManufacture = 2017

    def manufactureDetails(self):
        print("This MacBook was manufacture in the year {} by {}".format(self.yearofManufacture, self.manufacturer))

macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()