from coffee.pipeline import run_pipeline

def main():
    cafe, cappuccino_index = run_pipeline()
    print(cafe.head())
    print(cappuccino_index.head())
    
if __name__ == "__main__":
    main()