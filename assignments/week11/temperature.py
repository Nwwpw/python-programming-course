"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values(ค่าที่กำหนดส่งล่วงหน้า))
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

#"Create a function get_temperatures()"
def get_temperatures():
    # ใช้ list เก็บค่าอุณหภูมิ 7 วัน (ค่าที่กำหนดส่งล่วงหน้า)
    temporatures = [32, 35, 33, 32, 29, 31, 30]
    return temporatures

#"Create a function analyze_temps(temp_list)"
def analyze_temps(temp_list):
    avg_temp = 0    #สร้างตัวแปรสำหรับค่าเฉลี่ย (local variable)
    highest_temp = max(temp_list)   # หาค่าสูงสุดใน list
    lowest_temp = min(temp_list)    # หาค่าต่ำสุดใน list

    sum = 0
    for temp in temp_list:
        sum = sum + temp
    avg_temp = sum/len(temp_list)   # คำนวณค่าเฉลี่ย
    return  (avg_temp, highest_temp, lowest_temp)

#"Create a function display_analysis(avg, high, low)"
def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print("Average: %.2f C"%(avg))
    print(f"Highest: {high} C")
    print("Lowest: ", low, "C")
    #ทำวิธีไหนก็ได้(43-45)

my_temps = get_temperatures()   # เรียกใช้ฟังก์ชัน get_temperatures() เพื่อรับ list อุณหภูมิ
analyzed_temps = analyze_temps(my_temps)    # ส่ง list ไปวิเคราะห์ หาค่าเฉลี่ย สูงสุด ต่ำสุด
display_analysis(analyzed_temps[0], analyzed_temps[1], analyzed_temps[2])
                #ค่าเฉลี่ย, อุณหภูมิมากสุด, อุณหภูมิต่ำสุด