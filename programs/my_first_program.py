from nada_dsl import *

def nada_main():
    # Define Party1
    party1 = Party(name="Party1")
    
    # Define secret integer inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Compute the sum of my_int1 and my_int2
    sum_result = my_int1 + my_int2
    
    # Define the output to be returned
    output_result = Output(sum_result, "sum_output", party1)
    
    # Return the output as a list (though it's just one output in this case)
    return [output_result]

# Example usage
if __name__ == "__main__":
    result = nada_main()
    print("Result:", result)
