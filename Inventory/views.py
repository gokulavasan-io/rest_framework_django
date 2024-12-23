from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializers import *

class ProductsView(APIView):
    def post(self, request):
        serializer = ProductsSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({"message": "Data Saved", "data": serializer.data})


    
    def get(self,request):
        all_products=Products.objects.all()
        serializedProducts=ProductsSerializer(all_products,many=True).data
        return Response(serializedProducts)
    


class ProductsViewById(APIView):
    # def get(self,request,id):
    #     product=Products.objects.get(id=id)
    #     single_product={"id":product.id,
    #             "product_name":product.product_name,
    #             "code":product.code,
    #             "price":product.price,}
        
    #     return Response(single_product)
    
    def get(self,request,id):
        product=Products.objects.get(id=id)
        single_product=ProductsSerializer(product).data
        
        return Response(single_product)
    
    def patch(self,request,id):
        product=Products.objects.filter(id=id)
        product.update(product_name=request.data["product_name"],code=request.data["code"],price=request.data["price"])    
        return Response("Updated")
    
    def delete(self,request,id):
        product=Products.objects.get(id=id)
        product.delete()
        return Response("deleted")



