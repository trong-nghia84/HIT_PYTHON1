def format_phone_number(list_phone_number):
    cleaned_number = ''.join(char for char in list_phone_number if char.isdigit())
    if len(cleaned_number) != 10 or cleaned_number[0] != '0':
        return "Invalid phone number"
    else:
        return cleaned_number
list_phone_number=['-034661--+6434','      0394857434','827374744','+-d034dsfff3445567','374583']
for number in list_phone_number:
    formatted_number = format_phone_number(number)
    print(f"Số điện thoại: {number} -> Định dạng: {formatted_number}")
