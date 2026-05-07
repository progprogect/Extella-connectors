# Онбординг: GitHub (PAT)

## 1. Что вы получите

См. [capabilities.md](capabilities.md). Минимум: проверка токена и чтение профиля; дальше — отдельные эксперты под issues, repos и т.д.

## 2. Что подготовить

- Доступ к https://github.com/settings/tokens (classic) или fine-grained tokens

## 3. Способ доступа

**Рекомендуется:** Personal Access Token (fine-grained с минимальными repo/metadata правами или classic с нужными scopes).

Альтернатива: OAuth App / GitHub App — см. [oauth-broker.md](../../docs/oauth-broker.md).

## 4. Пошаговые действия (PAT)

### Fine-grained (рекомендуется для новых интеграций)

1. Откройте [Fine-grained tokens](https://github.com/settings/personal-access-tokens/new).
2. Выберите владельца ресурсов (user или org), срок, минимальные repository permissions (например **Metadata** read-only для healthcheck).
3. Создайте токен и **сразу скопируйте** значение (повторно не показывается).

### Classic

1. Откройте [Classic PAT](https://github.com/settings/tokens/new).
2. Выберите срок и scopes (для `GET /user` достаточно минимального набора; для репозиториев добавьте `repo` или выборочно).

### Запись в Extella KV

Имя ключа: `connector_github_pat` (см. [kv.schema.json](kv.schema.json)).

```bash
curl -s -X POST https://api.extella.ai/api/kv/set \
  -H "X-Auth-Token: $EXTELLA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "connector_github_pat",
    "value": "<PASTE_TOKEN_HERE>",
    "description": "GitHub PAT for connector; user-managed; rotate in GitHub settings."
  }'
```

Агент может подставлять значение в параметр эксперта из KV (как в других пресетах).

## 5. Проверка

Запустите эксперт `connector_github_healthcheck` с параметром `connector_github_pat` (значение из KV).

Ожидаемый результат: `status: success` и поле `login` — см. [HEALTHCHECK.md](HEALTHCHECK.md).

## 6. Устранение неполадок

См. [concepts/troubleshooting.md](concepts/troubleshooting.md) и [concepts/api_limits.md](concepts/api_limits.md).
