# Healthcheck: `connector_stripe_healthcheck`

## Контракт ответа

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `"success"` или `"error"` |
| `connector_id` | string | `"stripe"` |
| `message` | string | Ошибка или пусто |
| `provider_http_status` | int \| null | HTTP код |
| `livemode` | bool \| null | Из ответа Stripe balance |
| `available_currencies` | list \| null | Список кодов валют из `available` (кратко) |

### Пример успеха

```json
{
  "status": "success",
  "connector_id": "stripe",
  "message": "",
  "provider_http_status": 200,
  "livemode": false,
  "available_currencies": ["usd"]
}
```

### Пример ошибки

```json
{
  "status": "error",
  "connector_id": "stripe",
  "message": "HTTP 401: ...",
  "provider_http_status": 401,
  "livemode": null,
  "available_currencies": null
}
```

## Код для `expert/save`

Файл: [connector_stripe_healthcheck.py](experts/connector_stripe_healthcheck.py)
