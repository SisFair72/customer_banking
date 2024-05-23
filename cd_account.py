"""Import the Account class from the Account.py file.""


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    class Account:
        def __init__(self, balance, interest=0):
            self.balance = balance
            self.balance = interest
        def display_account_info(self):
            print(f"Balance: ${self.balance}")
            print(f"Interest Rate: {self.interest}%")
     my_account = Account(1000, 5)
     
     my_account.display_account_info()
     
     default_interest_account = Account(1000)
     
     default_interest_account.display_account_info()
            
    

    # Calculate interest earned
    monthly_interest_rate = interest_rate / 12 /100
    interest_earned = balance * monthly_interest_rate * months

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned
    
    return updated_balance, interest_earned
    
    initial_balance = 1000.0
    annual_interest_rate = 5.0
    cd_duration_months = 12
    
    print(f"Updated Balance: ${updated_balance:.2f"})
    print(f"Interest Earned: ${interest_earned:.2f}")
    

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    updated_balance, interest_earned = create_cd_account(initial_balance,
    annual_interest_rate, cd_duration_month)
    class CDAccount:
        def __init__(self,initial_balance, annual_interest_rate, 
    cd_duration_month):
            """
            Initialize a CDAccount instance.

            Args:
                initial_balance (float): The initial balance of the CD account.
                annual_interest_rate (float): The annual interest rate (as a 
        decimal).
                cd_duration_months (int): The duration of cd in months.
            """
            self.initial_balance = intial_balance
            self.annual_interest_rate = annual_interest_rate
            self.cd_duration_months = cd_duration_months
            self.updated_balance +intitial = initial_balance
            self.interest_earned = 0
            
        def calculate_interest(self):
            """ 
            Calculate the interest earned over the CD duration.
            
            Returns:
            float: The interest earned.
            """ 
            years = self.cd_duration_months / 12
            self.interest_earned = self.initial_balance *
        self.annual_interest_rate * years
            return  self.interest_earned
            
        def set_balance(self):
            """ 
            Calculate the balance by adding the interest earned to the initial
        balance.
            
            Returns:
            float: The updated balance.
            """ 
            self.updated_balance = self.initial_balance + 
        self.calculate_interest()
            return self.updated_balance
        
        def create_cd_account(initial_balance, annual_interest_rate,
        cd_duration_months):
            """ 
            Create a CD account and return the updated balance and interest earned.
            
            Args:
            intial_balance (float): The initial balance of the CD account.
            annual_interest_rate (float): The annual interest rate (as a decimal)
            cd_duaration_months (int): The duration of the CD in months.
            
            Returns:
            tuple: A tuple containing the updated balance and the interest earned.
            """ 
            cd_account = CDAccount(initial-balance, annual_interest_rate, 
        cd_duration_months)
            updated-balance = cd_account.set_balance()
            interest_earned = cd_account.interest-earned
            return updated_balance, interest_earned
            
        initial_balance = 1000.0
        annual_interest_rate = 0.05
        cd_duration_months = 36
        
        updated_balance, interest_earned = create_cd_account(initial_balance,
        annual_interest_rate, cd_duration_months)
        
        print(f"Initial Balance: ${initial_balance:2f}")
        print(f"Interest Earned: ${interest_earned:2f}")
        print(f"Updated Balance: ${updated_balance:2}")
            

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    def calculate_interest(balance,annual_interest_rate,years):
        """
        Calculate the interest earned on a given balance over a certain number of
    years.

        Args:
        balance (float): The initial balance.
        annual_interest_rate (float): The annual interest rate (as a decimal).
        years (int): The number of years the interest is applied.
        
        Returns:
        float: The interest earned.
        """
        return balance * annual_interest_rate * years
        
    
    
    # Return the updated balance and interest earned.
    def get_balance_and_interest(balance,annual_interest_rate,years):
        interest = calculate_interest(balance, annual_interest_rate, years)
        new_balance = updated(balance, annual_interest_rate,years)
        return new_balance, interest
        
            
