# Healthcheck: `connector_github_healthcheck`

## Контракт ответа (нормализованный)

Эксперт возвращает **dict** (JSON-совместимый):

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `"success"` или `"error"` |
| `connector_id` | string | всегда `"github"` |
| `message` | string | Пусто при успехе; при ошибке — краткий текст |
| `provider_http_status` | int \| null | HTTP-код ответа GitHub |
| `login` | string \| null | Логин пользователя при успехе |

### Пример успеха

```json
{
  "status": "success",
  "connector_id": "github",
  "message": "",
  "provider_http_status": 200,
  "login": "octocat"
}
```

### Пример ошибки

```json
{
  "status": "error",
  "connector_id": "github",
  "message": "HTTP 401: Bad credentials",
  "provider_http_status": 401,
  "login": null
}
```

## Код для `expert/save`

Файл: [connector_github_healthcheck.py](connector_github_healthcheck.py)
