from functools import reduce
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class CalculatorView(APIView):
   def post(self,request,*args,**kw):
      n1=request.data.get('num1')
      n2=request.data.get('num2')
      sum=n1+n2
      return Response(data=sum)
class SubstractView(APIView):
   def post(self,request,*args,**kw):
      a=request.data.get('no1')
      b=request.data.get('no2')
      sub=a-b
      return Response(data=sub)
class MultipleView(APIView):
   def post(self,request,*args,**kw):
      c=request.data.get('num1')
      d=request.data.get('num2')
      multi=c*d
      return Response(data=multi)
class DivisionView(APIView):
   def post(self,request,*args,**kw):
      e=request.data.get('num1')
      f=request.data.get('num2')
      divi=e/f
      return Response(data=divi)
   
class FactorialView(APIView):
   def post(self,request,*args,**kw):
      n=request.data.get('num1')
      fact=1
      while(n>0):
         fact=fact*n
         n=n-1
      return Response(data=fact)

class PrimeNumberView(APIView):
   def post(self,request,*args,**kw):
        number=request.data.get('num1',0)
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    result = 'not prime'
                    break
            else:
                result = 'prime'
        else:
            result = 'not prime'

        return Response(data=result)
        # count=0
        # for i in range(2,number):
        #     if number%i==0:
        #         count=1
        #         break
        #     else:
        #         count=0
        #     if count==1:
        #         result='not prime'
        #     else: 
        #        result='prime'
        # v=result
        # return Response(data=v)
        
class AddinView(APIView):
   def post(self,request,*args,**kwargs):
      
      numbers=request.data.get('numbers')
    #   x=reduce(lambda x,y:x if x>y else y,numbers)
    #   return Response(data=x)
      number=[str(i) for i in numbers]
      number.sort()
      out=reduce(lambda x,y:x+y if x+y>y+x else y+x,number)
    #   return Response(data=number)


    #   numbers=request.data.get('numbers',[])
    #   numbers=sorted(map(str,numbers),reverse=True,key=lambda x:x*10)
    #   largest_num=''.join(numbers)
    #   result=largest_num
      return Response(data=out)
   
   
