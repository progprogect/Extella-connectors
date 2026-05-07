# Мини-пресеты коннекторов

Каждый подкаталог — отдельный коннектор с одинаковой структурой файлов. Копируйте [`_template/`](_template/) как основу для нового сервиса.

| Путь | Назначение |
|------|------------|
| `_template/` | Эталонная структура (пустой шаблон) |
| `github/` | Пример: Personal Access Token + healthcheck |
| `stripe/` | Пример: Secret key + webhook, healthcheck |

Документация:

- [Матрица провайдеров](../docs/provider-matrix.md) — все 21 сервисов, паттерны auth, ссылки на консоли
- [OAuth-брокер (MVP)](../docs/oauth-broker.md) — PKCE, redirect, запись в KV
- [Безопасность коннекторов](../docs/connector-security.md)

Секреты храните только в **Extella KV** (`api/kv/set`), не в концептах и не в git.
