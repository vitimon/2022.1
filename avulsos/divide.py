def divide(divident,divisor):
    return divide(divident - divisor, divisor) + 1 if divident >= divisor else 0