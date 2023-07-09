from utils import get_data, get_sorted_data, get_filtered_data, get_formatted


def main():
    print("курсовая")
    data = get_data()
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    data = get_formatted(data)

    print(data)



if __name__ ==  '__main__':
    main()

