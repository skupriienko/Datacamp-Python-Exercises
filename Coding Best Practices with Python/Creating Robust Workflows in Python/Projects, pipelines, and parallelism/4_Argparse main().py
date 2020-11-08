def main():
    parser = argparse.ArgumentParser(description="Scikit datasets only!")
    # Set the default for the dataset argument
    parser.add_argument("dataset", nargs="?", default="diabetes")
    parser.add_argument("model", nargs="?", default="linear_model.Ridge")
    args = parser.parse_args()
    # Create a dictionary of the shell arguments
    kwargs = dict(dataset=args.dataset, model=args.model)
    return (classify(**kwargs) if args.dataset in ("digits", "iris", "wine")
            else regress(**kwargs) if args.dataset in ("boston", "diabetes")
            else print(f"{args.dataset} is not a supported dataset!"))

if __name__ == "__main__":
    main()
