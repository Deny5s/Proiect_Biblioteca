import datetime

def logare_actiuni(functie):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        linie_log = f"[{timestamp}] Functia '{functie.__name__}' a fost apelata\n"

        try:
            with open("log.txt", "a") as f:
                f.write(linie_log)
        except Exception as e:
            print(f"[Eroare la scrierea in log.txt] {e}")

        return functie(*args, **kwargs)
    
    return wrapper

