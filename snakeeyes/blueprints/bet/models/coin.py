def add_subscription_coins(coins, previous_plan, plan, cancelled_on):
    
    previous_plan_coins = 0
    plan_coins = plan['metadata']['coins']

    if previous_plan:
        previous_plan_coins = previous_plan['metadata']['coins']

    if cancelled_on is None and plan_coins == previous_plan_coins:
        coin_adjustment = plan_coins
    elif plan_coins <= previous_plan_coins:
        return coins
    else:
        
        coin_adjustment = plan_coins - previous_plan_coins

    return coins + coin_adjustment
