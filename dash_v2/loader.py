import pandas as pd

class Loader:

    def __init__(self):
        self.df = None
        self.leads_count = None
        self.calls_count = None
        self.pitches_count = None
        self.deals_count = None

    def read(self, url):
        self.df = pd.read_csv(url)
        self.__create_leads()
        self.__create_calls()
        self.__create_pitches()
        self.__create_deals()

    def __create_leads(self):
        self.leads_count = self.df["leads"].sum()

    def __create_calls(self):
        self.calls_count = self.df["calls"].sum()

    def __create_pitches(self):
        self.pitches = self.df["pitches"].sum()

    def __create_deals(self):
        self.deals_count = self.df["deals"].sum()

