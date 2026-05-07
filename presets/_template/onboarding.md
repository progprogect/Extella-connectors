# Онбординг: `<connector_id>`

## 1. Что вы получите

См. [capabilities.md](capabilities.md).

## 2. Что подготовить

- Учётная запись у провайдера
- Права (админ / владелец приложения), если требуется
- Для OAuth: возможность создать приложение в консоли разработчика

## 3. Выбор способа доступа

Выберите одну ветку:

| Способ | Когда использовать |
|--------|-------------------|
| **A. OAuth через брокер** | Есть развёрнутый [OAuth-брокер](../../docs/oauth-broker.md), минимум ручных копирований токенов |
| **B. Свой OAuth client** | Пользователь регистрирует приложение у провайдера, кладёт `client_id` / `client_secret` в KV |
| **C. API key / PAT** | Провайдер выдаёт ключ или токен вручную — вставка в KV |

## 4. Пошаговые действия

### Ветка C (пример)

1. Откройте консоль провайдера: `<URL>`
2. Создайте ключ / токен с областями: `<scopes>`
3. В Extella выполните `POST /api/kv/set` для каждого ключа из [kv.schema.json](kv.schema.json)

Пример `curl` (подставьте `EXTELLA_TOKEN`):

```bash
curl -s -X POST https://api.extella.ai/api/kv/set \
  -H "X-Auth-Token: $EXTELLA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"key":"<key_name>","value":"<paste_secret_here>","description":"Neutral label for search"}'
```

## 5. Проверка (healthcheck)

Запустите эксперт `connector_<connector_id>_healthcheck` с параметрами из [experts.manifest.yaml](experts.manifest.yaml).

Ожидаемый ответ: `{"status": "success", ...}`.

## 6. Ключи KV

См. таблицу в [kv.schema.json](kv.schema.json) (поле `keys`).

**Не** указывайте реальные секреты в описании ключа — только нейтральный текст для семантического поиска.

## 7. Устранение неполадок

Тексты для `concept_search` — в [concepts/](concepts/).
