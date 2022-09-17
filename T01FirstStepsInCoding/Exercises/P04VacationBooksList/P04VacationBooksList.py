number_of_pages_in_current_book = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_to_reed_the_book = number_of_pages_in_current_book / pages_per_hour
hours_to_read_per_day = hours_to_reed_the_book / number_of_days
print(hours_to_read_per_day)