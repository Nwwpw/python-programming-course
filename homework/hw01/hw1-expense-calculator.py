#1. เขียน comment อธิบาย code ในจุดที่สำคัญ ๆ และขอให้มี comment ข้อมูลของผู้เขียนโปรแกรม

"""
Personal Finance Calculator
Student: Wipawin Tungwattanakittikul
Date: 23 July 2025
Purpose: Calculate monthly budget and savings
"""

#2. ขอข้อมูลจากผู้ใช้ในประเด็นรายได้ (income) และค่าใช้จ่าย (expense)
monthly_income = float(input("User's monthly income in THB: ")) #รายได้ต่อเดือน
rent_cost = float(input("Monthly rent/housing cost: ")) #ค่าเช่า
food_budget = int(input("Monthly food budget in THB: ")) #ค่ากิน
transportation_cost = float(input("Monthly transportation expenses: ")) #ค่าเดินทาง
entertainment_budget = int(input("Monthly entertainment budget: ")) #ค่าพักผ่อน
emergency_fund_percent = float(input("Percentage to save for emergency: ")) #เผื่อสำหรับฉุกเฉิน
investment_percent = float(input("Percentage to invest: ")) #เงินลงทุน

#3. คำนวณข้อมูล
Total_fixed_Expenses = rent_cost + transportation_cost #ค่าใช้จ่ายคงที่(ค่าเช่า + ค่าเดินทาง)
Total_Variable_Expenses = food_budget + entertainment_budget #ค่าใช้จ่ายไม่คงที่(ค่ากิน + ค่าพักผ่อน)
Total_Expenses = Total_fixed_Expenses + Total_Variable_Expenses #ค่าใช้จ่ายทั้งหมด(ค่าใช้จ่ายคงที่+ค่าใช้จ่ายไม่คงที่)
Remaining_Income = monthly_income - Total_Expenses #รายได้คงเหลือ(รายได้ต่อเดือน-ค่าใช้จ่ายทั้งหมด)
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100) #เงินฉุกเฉิน(รายได้ต่อเดือนx(เผื่อสำหรับฉุกเฉิน ÷ 100))
Investment_Amount = monthly_income * (investment_percent / 100) #เงินลงทุน(รายได้ต่อเดือนx(เงินลงทุน ÷ 100))
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount #เงินเหลือสำหรับออม(รายได้คงเหลือ-เงินฉุกเฉิน-เงินลงทุน)
Expense_Ratio = (Total_Expenses / monthly_income) * 100 #สัดส่วนค่าใช้จ่ายต่อรายได้((ค่าใช้จ่ายทั้งหมด ÷ รายได้ต่อเดือน) × 100)

#4. จากนั้นแสดงออกข้อมูลออกทางหน้าจอ ตามตัวอย่าง
#fด้านหน้า คือf-string ใช้แสดงค่าตัวแปรในข้อความ (ตัวแปรอยู่ใน{})
#ทศนิยม2ตำแหน่ง คือ :.2f
print("=== MONTHLY BUDGET REPORT ===") #หัวข้อรายงานงบประมาณรายเดือน
print(f"Income: {monthly_income:.2f} THB") #รายได้ต่อเดือน
print(f"Fixed Expenses: {Total_fixed_Expenses:.2f} THB") #ค่าใช้จ่ายคงที่
print(f"Variable Expenses: {Total_Variable_Expenses:.2f} THB") #ค่าใช้จ่ายไม่คงที่
print(f"Total Expenses: {Total_Expenses:.2f} THB") #ค่าใช้จ่ายทั้งหมด
print(f"Remaining: {Remaining_Income:.2f} THB") #รายได้ที่เหลือ หลังหักค่าใช้จ่าย

print("=== SAVINGS BREAKDOWN ===") #การแบ่งเงินออม
print(f"Emergency Fund (10%): {Emergency_Fund_Amount:.2f} THB") #เงินฉุกเฉิน
print(f"Investment (15%): {Investment_Amount:.2f} THB") #เงินลงทุน
print(f"Available for Savings: {Available_for_Savings:.2f} THB") #เงินที่เหลือสำหรับออม

print("=== ANALYSIS ===") #หัวข้อการวิเคราะห์
print(f"Expense Ratio:{Expense_Ratio:.2f}%") #สัดส่วนค่าใช้จ่ายต่อรายได้