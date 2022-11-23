
class Star:
    name = 'Star'
    x = 100

    def change():
        x = 200
        print('x is', x)

print('x Is' ,Star.x)
Star.change()
print('x Is', Star.x)

star = Star()
print('x is', star.x)
star.change()