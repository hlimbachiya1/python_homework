import pandas as pd
import sqlite3

def main():  #Task 5: Read data into a DataFrame and perform analysis
    
    try:
        with sqlite3.connect("../db/lesson.db") as conn:
            
            # 1
            print("STEP 1: Reading data from database")
            sql_statement = """
            SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            """
            
            df = pd.read_sql_query(sql_statement, conn)
            print("First 5 rows of the DataFrame:")
            print(df.head())
            print(f"\nDataFrame shape: {df.shape}")
            
            # 2
            print("\nSTEP 2: Adding total column")
            df['total'] = df['quantity'] * df['price']
            print("First 5 rows with total column:")
            print(df.head())
            
            # 3
            print("\nSTEP 3: Grouping and aggregating data")
            grouped_df = df.groupby('product_id').agg({
                'line_item_id': 'count',    # Count no. of times each product was ordered
                'total': 'sum',             # Summing total value for each product
                'product_name': 'first'     # Get product name (same for each product_id)
            }).reset_index()
            
            grouped_df = grouped_df.rename(columns={  #Renaming columns for clarity
                'line_item_id': 'order_count',
                'total': 'total_revenue'
            })
            
            print("First 5 rows of grouped DataFrame:")
            print(grouped_df.head())
            
            # 4
            print("\nSTEP 4: Sorting by product name") 
            grouped_df = grouped_df.sort_values('product_name')
            print("First 5 rows after sorting:")
            print(grouped_df.head())
            
            # 5
            print("\nSTEP 5: Writing to CSV file")
            csv_filename = "order_summary.csv"
            grouped_df.to_csv(csv_filename, index=False)
            print(f"Data written to {csv_filename}")
            
            # Now display the final summary
            print("\nFINAL SUMMARY")
            print(f"Total number of unique products: {len(grouped_df)}")
            print(f"Total revenue across all products: ${grouped_df['total_revenue'].sum():.2f}")
            print(f"Most ordered product: {grouped_df.loc[grouped_df['order_count'].idxmax(), 'product_name']} "
                  f"({grouped_df['order_count'].max()} orders)")
            print(f"Highest revenue product: {grouped_df.loc[grouped_df['total_revenue'].idxmax(), 'product_name']} "
                  f"(${grouped_df['total_revenue'].max():.2f})")
            
            print(f"\nComplete summary saved to {csv_filename}")
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except FileNotFoundError as e:
        print(f"Database file not found: {e}")
        print("Reminder: run load_db.py from the python_homework folder first!")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()