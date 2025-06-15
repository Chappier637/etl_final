CREATE TABLE transaction (
    msno String,
    payment_method_id Uint32,
    payment_plan_days Uint32,
    plan_list_price Uint32,
    actual_amount_paid Uint32,
    is_auto_renew Uint8,
    transaction_date Uint32,
    membership_expire_date Uint32,
    is_cancel Uint8,
    PRIMARY KEY (msno)
)