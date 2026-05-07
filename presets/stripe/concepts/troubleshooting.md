# Stripe connector — troubleshooting

Текст для `concept_add`.

## Healthcheck: 401 или invalid API key

- Неверный ключ или ключ от другого режима (test vs live).
- Лишние кавычки/пробелы в KV — перезапишите значение.

## Restricted key: permission denied

- Добавьте permission на чтение balance или расширьте restricted key в Dashboard.

## Webhook: invalid signature

- Убедитесь, что используете **текущий** `whsec_` для данного endpoint.
- Сырое тело запроса должно быть **байт-в-байт** как от Stripe до парсинга JSON.
