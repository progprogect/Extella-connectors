# Возможности: Stripe

| Операция | API | Ключ | Примечание |
|----------|-----|------|------------|
| Проверка ключа | `GET /v1/balance` | Secret / restricted | Healthcheck |
| Клиенты | Customers API | По правам ключа | PCI: не хранить полные карты |
| Платежи | PaymentIntents и др. | По правам | Соблюдать Stripe compliance |

Документация: [Stripe API](https://docs.stripe.com/api).

## Webhooks

Приём событий — отдельный endpoint + проверка `Stripe-Signature` с `connector_stripe_webhook_secret`.
