# Import  Libraries
import util
import notify2 


def notify():
    
    # Fetch the current Dolar rate
    DolarMonitor = util.fetchDolarPriceMonitor()

    DolarDtoday = util.fetchDolarPriceDtoday()
    
    # initialise the d-bus connection
    notify2.init("Dolar rates notifier")
 
    # create Notification object
    n = notify2.Notification("Dolar Notifier")
        
    # Set the urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)
        
    # Set the timeout
    n.set_timeout(5000)

    result1 = "Monitor: "
    result1 = result1 + str(DolarMonitor) + "\n" + "DolarToday:" + str(DolarDtoday) + "\n"

    # Update the content
    n.update("Precio del Dolar:", result1)

    # Show the notification
    n.show()
if __name__ == "__main__":
    notify()

