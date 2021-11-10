from django.db import models


class Order_ticketdetailsModel(models.Model):
    Ticket_id = models.BigIntegerField(blank=True ,null=True)
    Order_id = models.BigIntegerField(blank=True ,null=True)
    Customerticket_no = models.CharField(max_length=100)
    Producerticket_no = models.CharField(max_length=100)
    Notification = models.CharField(max_length=100)
    
    
    def __init__(self,tic_id,ord_id,cust_no,prod_no,noti):
        self.Ticket_id = tic_id
        self.Order_id = ord_id
        self.Customerticket_no = cust_no
        self.Producerticket_no = prod_no
        self.Notification = noti