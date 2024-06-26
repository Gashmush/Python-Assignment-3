def calculate_discount(price,discout_percent):
    if discount_percent>=20:
        discount_amount=price*(discount_percent/100)
        final_price=price-discount_amount
        return final_price
    else:
        return price
def main():
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print("No discount applied. Final price: ${:.2f}".format(final_price))
    else:
        print("Final price after applying {}% discount: ${:.2f}".format(discount_percent, final_price))

if __name__ == "__main__":
    main()