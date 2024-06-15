import streamlit as str 

str.title("Hitung Modal Jastip")
str.text("Asumsi 1 IDR = 3.500 MYR")

def input_ringgit_price():
    ringgit_price = str.number_input("Masukkan harga Ringgit", 0)
    return ringgit_price
    
def calculate_rupiah(ringgit_price):
    calculate = str.button("Hitung dalam Rupiah")
    ringgit_to_rupiah = ringgit_price * 3500 # Assume that 1 IDR = RM3,500
    return ringgit_to_rupiah

def input_selling_price(rupiah_price):
    selling_price = str.slider("Mau dijual dengan harga berapa?", rupiah_price, rupiah_price+1000000, value=rupiah_price, step=500)
    return selling_price

def calculate_estimated_profit(rupiah_price, selling_price):   
    estimated_profit = selling_price - rupiah_price
    return estimated_profit 

def main():
    ringgit_price = input_ringgit_price()
    rupiah_price = calculate_rupiah(ringgit_price)
    
    formatted_rupiah_price = f"{rupiah_price:,}".replace(",",".")
    str.markdown(f"Harga dalam Rupiah: **{formatted_rupiah_price}**")
    
    selling_price = input_selling_price(rupiah_price)
    estimated_profit = calculate_estimated_profit(rupiah_price, selling_price)
    
    formatted_estimated_profit = f"{estimated_profit:,}".replace(",",".")
    str.markdown(f"Perkiraan profit: ***{formatted_estimated_profit}***")
    
if __name__ == "__main__":
    main()
    