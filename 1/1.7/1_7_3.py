from string import ascii_uppercase

class CardCheck:
    
    @staticmethod
    def check_card_number (cn):
        if len(cn.split("-"))!=4:
            return False
        
        for i in cn.split("-"):
            for j in i:
                if not j.isdigit():
                    return False
            return True

    @staticmethod
    def check_name (cn):
        if len(cn.split(" "))!=2:
            return False
        for i in cn.split(" "):
            for j in i:
                if not j in set(ascii_uppercase):
                    return False
            return True