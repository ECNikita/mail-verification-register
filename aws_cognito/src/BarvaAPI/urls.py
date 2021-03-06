from django.urls import path
from BarvaAPI.view.registerViews import *
from BarvaAPI.view.Product_masterViews import ProductInsert,DeleteProduct,ProductUpdate,ProductGET
from BarvaAPI.view.Producer_masterViews import ProducerInsert,ProducerUpdate,DeleteProducer,ProducerGET
from BarvaAPI.view.Lotunit_masterViews import LotInsert,LotUpdate,LotDelete,LotGET
from BarvaAPI.view.Product_pricebyproducerViews import *
from BarvaAPI.view.TraderroleViews import *
from BarvaAPI.view.Trader_detailsViews import *
from BarvaAPI.view.Bid_masterViews import *
from BarvaAPI.view.CustomerProducer_Bid_detailsViews import *
from BarvaAPI.view.Producer_paymentdetailsViews import *
from BarvaAPI.view.Order_detailsViews import *
from BarvaAPI.view.Order_ticketdetailsViews import *
from BarvaAPI.view.TransportViews import *
from BarvaAPI.view.WarehouseViews import *
from BarvaAPI.view.BiddingforProductView import *
from BarvaAPI.view.Producer_calculationView import ProducerCalGet

urlpatterns = [
    path('registerinsert',RegisterInsert.as_view()),
     path('registerupdate',RegisterUpdate.as_view()),
    path('registerdelete',DeleteRegisterUserByID.as_view()),
   

    path('productget',ProductGET.as_view()),
    path('productinsert',ProductInsert.as_view()),
    path('deleteproduct',DeleteProduct.as_view()),
    path('updateproduct',ProductUpdate.as_view()),

    path('producerget',ProducerGET.as_view()),
    path('producerinsert',ProducerInsert.as_view()),
    path('producerupdate',ProducerUpdate.as_view()),
    path('producerdelete',DeleteProducer.as_view()),

    path('lotget',LotGET.as_view()),
    path('lotinsert',LotInsert.as_view()),
    path('lotupdate',LotUpdate.as_view()),
    path('lotdelete',LotDelete.as_view()),

    path('productbyproducerget',Product_pricebyproducerGET.as_view()),
    path('productbyproducerinsert',Product_pricebyproducerInsert.as_view()),
    path('productbyproducerupdate',Product_pricebyproducerUpdate.as_view()),
    path('productbyproducerdelete',Product_pricebyproducerDelete.as_view()),

    path('traderroleget',TraderroleGET.as_view()),
    path('taderroleinsert',TraderroleInsert.as_view()),
    path('traderroleupdate',TraderroleUpdate.as_view()),
    path('traderroledelete',TraderroleDelete.as_view()),

    path('traderget',Trader_detailsGET.as_view()),
    path('traderinsert',Trader_detailsInsert.as_view()),
    path('traderupdate',Trader_detailsUpdate.as_view()),
    path('traderdelete',Trader_detailsDelete.as_view()),

    path('bidget',BidGet.as_view()),
    path('bidinsert',BidInsert.as_view()),
    path('bidupdate',BidUpdate.as_view()),
    path('biddelete',BidDelete.as_view()),

    path('custbidget',CustBidGet.as_view()),
    path('custbidinsert',CustBidInsert.as_view()),
    path('custbidupdate',CustBidUpdate.as_view()),
    path('custbiddelete',CustBidDelete.as_view()),
    
    path('producer_paymentget',Producer_paymentGET.as_view()),
    path('producer_paymentinsert',Producer_paymentInsert.as_view()),
    path('producer_paymentupdate',Producer_paymentUpdate.as_view()),
    path('producer_paymentdelete',Producer_paymentDelete.as_view()),
    
    path('order_detailsget',Order_detailsGET.as_view()),
    path('order_detailsinsert',Order_detailsInsert.as_view()),
    path('order_detailsupdate',Order_detailsUpdate.as_view()),
    path('order_detailsdelete',Order_detailsDelete.as_view()),
    
    path('order_ticket_detailsget',Order_ticket_detailsGET.as_view()),
    path('order_ticket_detailsinsert',Order_ticket_detailsInsert.as_view()),
    path('order_ticket_detailsupdate',Order_ticket_detailsUpdate.as_view()),
    path('order_ticket_detailsdelete',Order_ticket_detailsDelete.as_view()), 
    
    path('transportdelete',TransportDelete.as_view()),
    path('transportget',TransportGET.as_view()),
    path('transportinsert',TransportInsert.as_view()),
    path('transportupdate',TransportUpdate.as_view()),
    
    path('warehouseget',WarehouseGET.as_view()),
    path('warehouseinsert',WarehouseInsert.as_view()),
    path('warehouseupdate',WarehouseUpdate.as_view()),
    path('warehousedelete',WarehouseDelete.as_view()),
    
    path('bid_calc',BiddingCalc.as_view()),
    path('producerCalget',ProducerCalGet.as_view()),
     
    path('getchart',GETquanchart.as_view())
]
