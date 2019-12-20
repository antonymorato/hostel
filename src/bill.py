class Bill:
    def __init__(self, type, dict) -> None:
        self.dict = dict
        self.type = type

    def returnSum(self):
        if self.type == "accom_bill":
            return 529

