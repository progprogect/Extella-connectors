# Онбординг: Stripe

## 1. Что вы получите

См. [capabilities.md](capabilities.md). Healthcheck вызывает `GET /v1/balance` (безопасный read для проверки ключа).

## 2. Что подготовить

- Доступ к [API keys](https://dashboard.stripe.com/apikeys)
- Решение: test vs live режим

## 3. Способ доступа

**Secret key** или **Restricted key** с правом чтения balance (и далее — по задачам пресета).

См. [connector-security.md](../../docs/connector-security.md): не использовать publishable key на сервере.

## 4. Пошаговые действия

1. Откройте https://dashboard.stripe.com/apikeys
2. Создайте **restricted key** (рекомендуется) с минимальными разрешениями, либо скопируйте **Secret key** для песочницы.
3. Запишите в KV:

```bash
curl -s -X POST https://api.extella.ai/api/kv/set \
  -H "X-Auth-Token: $EXTELLA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "connector_stripe_secret_key",
    "value": "<sk_test_... или restricted key>",
    "description": "Stripe API secret for Extella connector; user-managed."
  }'
```

### Webhook signing secret (опционально)

Если принимаете webhooks Stripe на своём endpoint:

1. Developers → Webhooks → endpoint → **Signing secret**
2. KV:

```bash
curl -s -X POST https://api.extella.ai/api/kv/set \
  -H "X-Auth-Token: $EXTELLA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "connector_stripe_webhook_secret",
    "value": "whsec_...",
    "description": "Stripe webhook signing secret; verify Stripe-Signature header."
  }'
```

Проверка подписи — в отдельном эксперте/сервисе, не в healthcheck.

## 5. Проверка

Эксперт `connector_stripe_healthcheck` с параметром `connector_stripe_secret_key`.

## 6. Устранение неполадок

[concepts/troubleshooting.md](concepts/troubleshooting.md)
