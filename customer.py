class Customer:
    def __init__(self,customer_id,name,rented_cars=None):
        self.customer_id=customer_id
        self.name=name
        self.rented_cars=rented_cars or []

    def rent_car(self,car):
        if car.rent() and car not in self.rented_cars:
            self.rented_cars.append(car)
            return True
    def return_car(self,car):
        if car in self.rented_cars:
            car.return_car()
            self.rented_cars.remove(car)
        else:
            return False

