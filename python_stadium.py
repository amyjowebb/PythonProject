class Stadium:
    """create a class for stadium"""
    def __init__(self, name, city_state, capacity, sport_played, seats_available):
        """this is an instance for the stadium"""
        self.name=name
        self.city_state=city_state
        self.capacity=capacity
        self.sport_played=sport_played
        self.seats_available=seats_available
        
    def describe_stadium(self):
       print("The " + self.name+" Arena is located in " +self.city_state+ "and holds "+ self.capacity+ " fans.")
    def specific_stadium(self):
        print("The following sport is mainly played int his stadium: "+ self.sport_played)
        print("There are "+ self.seats_available+ " seats still available for tonight's game.")
stadium1=Stadium("Mercedes Benz", "Atlanta, Ga", "70,000", "Football", "15000")
stadium1.describe_stadium() 
stadium1.specific_stadium() 
