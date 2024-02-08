from payment_service import handle
from payment.adapter import PaymentAdapter, PaymentAdapterMock, PaymentAdapterImpl


if __name__ == "__main__":
    handle(
        {"song": "1 step forward 3 steps backwards", "artist": "olivia rodrigo"},
        paymentAdapter=PaymentAdapter(PaymentAdapterImpl()),
    )
