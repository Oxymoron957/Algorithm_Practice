"""
부가가치세 계산기
"""

from math import ceil

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료

    if orderAmount-serviceFee - taxFreeAmount == 1:
        return  0
    else:             
        taxAmount = (1/11)*(orderAmount-serviceFee - taxFreeAmount)
        return ceil(taxAmount)

print(solution(1000, 300, 100))
