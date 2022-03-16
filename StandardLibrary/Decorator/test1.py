class geeks:
    course = 'DSA'
    
    def purshase(obj):
        print("Purchase course: ", obj.course)
geeks.purshase =  classmethod(geeks.purshase)
geeks.purshase()
print(geeks.course)