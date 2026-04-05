import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("data.csv")
    print("✅ Data Loaded Successfully\n")
    
    # Show data
    print("📋 Data Preview:")
    print(df.head())

    # Cleaning
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Filtering
    it_employees = df[df['Department'] == 'IT']
    print("\n👨‍💻 IT Employees:")
    print(it_employees)

    # Grouping
    avg_salary = df.groupby('Department')['Salary'].mean()
    print("\n💰 Average Salary by Department:")
    print(avg_salary)

    # Insights
    print("\n📊 Insights:")
    print("Total Employees:", len(df))
    print("Highest Salary:", df['Salary'].max())
    print("Lowest Salary:", df['Salary'].min())

    # Graph
    avg_salary.plot(kind='bar')
    plt.show()

except Exception as e:
    print("❌ Error:", e)
    