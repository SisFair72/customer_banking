# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    initial_balance_cd = 1000.0
    annual_interest_rate_cd = 0.05
    cd_duration_months = 36

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"CD Account - Initial Balance: ${initial_balance_cd:.2f}")
    print(f"CD Account - Interest Earned: ${interest_earned_cd:2f}")
    print(f"CD Account - Updated Balance: ${updated_balance_cd:2f}")
    

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    def get_cd_account_details():
        """ 
        try:
        initial_balance = float(input("Enter the initial balance for the CD
    account: "))
        annual_interest_rate = float(input("Enter the annual interest rate
    for the CD account (as a decimal, e.g., 0.05 for 5%): "))
        cd_duration_months = int(input("Enter the duration of the CD in
    months: "))
        return initial_balance, annual_interest_rate, cd_duration_months
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get cd_account_details():
        
    def get_savings_account_details():
        """ 
        try:
            initial_balance = float(input("Enter the initial balance for the CD
    account:  "))
            annual_interest-rate = float(input("Enter the annual interest rate
    for the savings account (as a decimal, e.g.,0.03 for 3%): "))
            years = int(input("Enter the duration in years: "))
            return initial_balance, annual_interest_rate, years
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_savings_account_details()
    
    def main():
            initial_balance_cd,annual_interest_rate_cd, cd_duration_months =
    get_cd_account_details()
    
        updated_balance_cd, interest_earned_cd =
    create_cd_account(initial_balance_cd, annual_interest_rate_cd,
    cd_duration_months)
    
            
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
        print(f"\ncd Account - Initial Balance: ${initial_balance_cd:.2f}")
        print(f"CD Account - Interest Earned: ${interest_earned_cd:.2f}")
        print(f"CD Account - Updated Balance: ${updated_balaance_cd:.2f}")
        

if __name__ == "__main__":
    
    initial_balance_savings, annual_interest_rate_savings, years =
get_savings_accounts_details()

    updated_balance_savings, interest_earned_savings =
create_savings_account(initial_balance_savings, annual_interest_rate_savings,
years)

        print(f"\nSavings Account - Initial Balance: $
    {initial_balance_savings:.2f}")
        print(f"Savings Account -Interest Earned: $
    {interest_earned_savings:.2f}")
        print(f"Savings Account - Updated Balance: $
        {updated_balance_savings:.2f}")
        

