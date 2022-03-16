import materclass
o = materclass.opt()
o.a = 1
o.b = 2


def main():
    print(o.b - o.a)
    
if __name__ == "__main__":
    main()