def status(status):
    match status:
        case 106:
            return "Goodd"
        case 100:
            return "OOOOOOOOooooo"
        case _:
            return "Unknown status"

print(status(106))
