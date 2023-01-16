import requests
import sys

class DisplaySuper:
    def __init__(self, city:str, item_list:str) -> None:
        self.city = city
        self.items = self.break_item_list(item_list)

    def break_item_list(self, item_list:str) -> dict:
        ans = {}
        items = item_list.split(',')
        # ['bira-corona', 'shampoo-dove']
        for item in items:
            new_item = item.split('-')
            # ['bira', 'corona']
            ans[(new_item[0])] = new_item[1]
        return ans
    
    def get_supers(self):
        URL = "http://172.17.0.3:8000/displaysuper/getsupers"

        PARAM = {"city":self.city}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")

        if data["ans"] == 'error':
            return data

        super_ids = self.supers_to_list(data)

        res = {}
        index = 1
        for super_id in super_ids:
            supers_data = self.calculate_cart(super_id)
            if supers_data["ans"] == 'error':
               pass
            else:
                res[f'super{index}'] = self.super_data_to_string(supers_data)
                index += 1
        res["ans"] = "success"
        return res




    def supers_to_list(self, data:dict):
        ans = []
        for super_id in data.keys():
            if super_id != "ans":
                ans.append(super_id)
        return ans

    def calculate_cart(self, super_id):
        URL = "http://172.17.0.3:8000/displaysuper/calculatecart"

        PARAM = {"superid":super_id}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")

        if data["ans"] == "error":
            return {"ans":'error'}

        products = data
        total_price = 0
        subs = 0
        missing_items = 0
        for item_quantity,brand in self.items.items():
            item_quantity_dis = item_quantity.split('_')
            item = item_quantity_dis[0]
            quantity = 1
            if len(item_quantity_dis) == 2:
                quantity = int(item_quantity_dis[1])
            
            if item in products:
                if item == 'ans':
                    pass
                elif (products.get(item) is not None) and ((products.get(item)).get(brand) is not None):
                    pr = int(products[item][brand]) * quantity
                    total_price += pr
                else:
                    min = sys.maxsize
                    subs += quantity
                    curr_price = 0
                    for brand_name, price in products.get(item).items():
                        print("----------------------")
                        print(f"brand is {brand_name}")
                        print("----------------------")
                        print(f"min is {min}")
                        print("----------------------")
                        print(f"curr_price is {curr_price}")
                        curr_price = int(price)
                        if(curr_price < min):
                            min = curr_price
                        print("----------------------")
                        print(f"new min is {min}")
                        print("----------------------")
                        print("----------------------")
                        print("----------------------")
                    total_price += (min*quantity)
            else:
                missing_items += quantity

        rating = self.get_rating(super_id)
        num_comments = self.get_num_comments(super_id)
        super_name = self.get_super_name(super_id)

        if rating == 'error' or num_comments == 'error' or super_name == 'error':
            return {"ans":'error'}

        print(total_price)
        print(subs)
        print(missing_items)
        return {"ans":"success", "super_name":super_name, "missing_items":missing_items, 
        "substitute_item":subs, "total_price":total_price, "rating":rating, "num_comments":num_comments}
        
        

    def get_rating(self, super_id):
        URL = "http://172.17.0.3:8000/displaysuper/getrating"

        PARAM = {"superid":super_id}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")
        return data["ans"]

    def get_num_comments(self, super_id):
        URL = "http://172.17.0.3:8000/displaysuper/getnumcomments"

        PARAM = {"superid":super_id}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")
        return data["ans"]

    def get_super_name(self, super_id):
        URL = "http://172.17.0.3:8000/displaysuper/getsupername"

        PARAM = {"superid":super_id}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")
        return data["ans"]

    def super_data_to_string(self, supers_data:dict):
        ans = ""
        for key,val in supers_data.items():
            if key == "ans":
                pass
            else:
                ans += f"{key}-{val},"
        return ans
    


    


