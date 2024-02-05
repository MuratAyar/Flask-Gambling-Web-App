import stripe


class Event(object):
    @classmethod
    def retrieve(cls, event_id):
        
        return stripe.Event.retrieve(event_id)


class Customer(object):
    @classmethod
    def create(cls, token=None, email=None, coupon=None, plan=None):
        
        params = {
            'source': token,
            'email': email
        }

        if plan:
            params['plan'] = plan

        if coupon:
            params['coupon'] = coupon

        return stripe.Customer.create(**params)


class Charge(object):
    @classmethod
    def create(cls, customer_id=None, currency=None, amount=None):
        
        return stripe.Charge.create(
            amount=amount,
            currency=currency,
            customer=customer_id,
            statement_descriptor='SNAKEEYES COINS')


class Coupon(object):
    @classmethod
    def create(cls, code=None, duration=None, amount_off=None,
               percent_off=None, currency=None, duration_in_months=None,
               max_redemptions=None, redeem_by=None):
        
        return stripe.Coupon.create(id=code,
                                    duration=duration,
                                    amount_off=amount_off,
                                    percent_off=percent_off,
                                    currency=currency,
                                    duration_in_months=duration_in_months,
                                    max_redemptions=max_redemptions,
                                    redeem_by=redeem_by)

    @classmethod
    def delete(cls, id=None):
        
        coupon = stripe.Coupon.retrieve(id)
        return coupon.delete()


class Card(object):
    @classmethod
    def update(cls, customer_id, stripe_token=None):
        
        customer = stripe.Customer.retrieve(customer_id)
        customer.source = stripe_token

        return customer.save()


class Invoice(object):
    @classmethod
    def upcoming(cls, customer_id):
        
        return stripe.Invoice.upcoming(customer=customer_id)


class Subscription(object):
    @classmethod
    def update(cls, customer_id=None, coupon=None, plan=None):
        
        customer = stripe.Customer.retrieve(customer_id)
        subscription_id = customer.subscriptions.data[0].id
        subscription = customer.subscriptions.retrieve(subscription_id)

        subscription.plan = plan

        if coupon:
            subscription.coupon = coupon

        return subscription.save()

    @classmethod
    def cancel(cls, customer_id=None):
        
        customer = stripe.Customer.retrieve(customer_id)
        subscription_id = customer.subscriptions.data[0].id

        return customer.subscriptions.retrieve(subscription_id).delete()


class Plan(object):
    @classmethod
    def retrieve(cls, plan):
        
        try:
            return stripe.Plan.retrieve(plan)
        except stripe.error.StripeError as e:
            print(e)

    @classmethod
    def list(cls):
        
        try:
            return stripe.Plan.all()
        except stripe.error.StripeError as e:
            print(e)

    @classmethod
    def create(cls, id=None, name=None, amount=None, currency=None,
               interval=None, interval_count=None, trial_period_days=None,
               metadata=None, statement_descriptor=None):
        
        try:
            return stripe.Plan.create(id=id,
                                      name=name,
                                      amount=amount,
                                      currency=currency,
                                      interval=interval,
                                      interval_count=interval_count,
                                      trial_period_days=trial_period_days,
                                      metadata=metadata,
                                      statement_descriptor=statement_descriptor
                                      )
        except stripe.error.StripeError as e:
            print(e)

    @classmethod
    def update(cls, id=None, name=None, metadata=None,
               statement_descriptor=None):
        
        try:
            plan = stripe.Plan.retrieve(id)

            plan.name = name
            plan.metadata = metadata
            plan.statement_descriptor = statement_descriptor
            return plan.save()
        except stripe.error.StripeError as e:
            print(e)

    @classmethod
    def delete(cls, plan):
        
        try:
            plan = stripe.Plan.retrieve(plan)
            return plan.delete()
        except stripe.error.StripeError as e:
            print(e)
