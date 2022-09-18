import typing as t

def main() -> None:
    egt_peak: t.Union[str, int] = input("EGT Peak: ")
    
    try:
        egt_peak = int(egt_peak)
    except ValueError:
        print("Not a valid base 10 integer")
        main()

        exit(0)
    
    rop: str = f"""================
= Rich of Peak =
=              =
=              =
\t{egt_peak - 75}
=              =
=              =
================
"""
    print(rop)

if __name__ == "__main__":
    while (True):
        main()
        
        input("Press enter to start new calculation... ")
    