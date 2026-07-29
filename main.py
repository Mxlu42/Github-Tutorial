class world:

    def greeting_world(self):
        return 'Hello World'

    def hallo_welt(self):
        print('Hallo Welt')

    def ist_schaltjahr(self, jahr):
        return jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0)


if __name__ == '__main__':
    b = 'hello'
    a = world()
    print(a.greeting_world())

print('Hello World')