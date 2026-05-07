# Матрица провайдеров (мини-пресеты)

Сводка по сервисам из дорожной карты: **паттерн авторизации**, **консоль разработчика**, **MVP-объём**, **блокеры**.

Консоли и политики меняются — перед релизом пресета проверьте актуальную документацию провайдера.

| # | Сервис | Паттерн auth | Консоль / старт документации | MVP scope | Блокеры / риски |
|---|--------|----------------|------------------------------|-----------|-----------------|
| 1 | Gmail | OAuth2 (Google) | [Google Cloud Console](https://console.cloud.google.com/) | Отправка/чтение писем по выбранным scopes | [Чувствительные scopes](https://developers.google.com/workspace/gmail/api/auth/scopes), верификация приложения Google |
| 2 | Google Calendar | OAuth2 (Google) | [Google Cloud Console](https://console.cloud.google.com/) | CRUD событий выбранных календарей | Те же, что Google OAuth; квоты Calendar API |
| 3 | Google Drive | OAuth2 (Google) | [Google Cloud Console](https://console.cloud.google.com/) | Загрузка/скачивание файлов, метаданные | Sensitive scopes; ограничения на типы файлов |
| 4 | Notion | OAuth2 | [Notion Developers](https://developers.notion.com/) | Страницы/БД в пределах выданного workspace | Интеграция только к выбранным ресурсам |
| 5 | GitHub | PAT / OAuth App / GitHub App | [GitHub Developer settings](https://github.com/settings/developers) | REST/GraphQL в пределах прав токена | Fine-grained vs classic PAT; org policies |
| 6 | Slack | OAuth (Slack app) | [Slack API](https://api.slack.com/apps) | Bot + при необходимости user token | Разделение bot vs user scopes |
| 7 | Linear | OAuth2 | [Linear Developers](https://developers.linear.app/) | GraphQL issues/projects | Организационные политики |
| 8 | monday.com | OAuth / API token | [monday.com API](https://developer.monday.com/) | Доски, items по доке | Уточнить поддерживаемый тип токена в аккаунте |
| 9 | HubSpot | OAuth2 / Private App | [HubSpot Developers](https://developers.hubspot.com/) | CRM объекты по scope | Лимиты API; разные продукты HubSpot |
| 10 | Stripe | Secret / restricted key | [Stripe Dashboard](https://dashboard.stripe.com/apikeys) | Balance, customers, payments по ключу | PCI; только restricted keys где возможно |
| 11 | Hugging Face | User Access Token | [HF Settings tokens](https://huggingface.co/settings/tokens) | Inference / Hub API по правам токена | Платные модели / очереди |
| 12 | Supabase / Postgres | URL + service_role / connection string | [Supabase Dashboard](https://supabase.com/dashboard) | PostgREST, RPC, SQL (осторожно) | `service_role` = полный доступ; SSRF не применим к DB URL в прокси |
| 13 | Atlassian (Jira / Confluence) | OAuth2 3LO / API token (Cloud) | [Atlassian Developer](https://developer.atlassian.com/) | REST в пределах cloud-сайта | Cloud vs Data Center — разные API |
| 14 | Instagram | Meta Graph API + OAuth | [Meta for Developers](https://developers.facebook.com/) | То, что разрешено для Business/Creator | Сильные ограничения; часто App Review |
| 15 | Instagram Creator Marketplace | Meta партнёрские программы | [Meta for Developers](https://developers.facebook.com/) | Зависит от доступа к программе | Доступ не у всех аккаунтов |
| 16 | Meta Ads Manager | Marketing API + OAuth | [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis) | Рекламные объекты по правам | Business Manager, верификация, лимиты |
| 17 | Zapier | API / Partner (сценарий-зависимо) | [Zapier Platform](https://platform.zapier.com/) | **Два трека:** вызов ваших триггеров vs управление Zapier | Уточнить продуктовый use-case до пресета |
| 18 | Similarweb | API key (коммерческий) | [Similarweb API](https://www.similarweb.com/corp/developer/) | Данные, доступные по подписке | Нет «полного бесплатного» API |
| 19 | Nano Banana Pro | API key (REST, провайдер-зависимо) | Документация выбранного вендора (несколько хостингов API) | Генерация изображений по их API | Зафиксировать base URL и ToS выбранного поставщика |
| 20 | Custom REST | Bearer / Basic / custom header | N/A (ваш API) | Прокси к одному allowlist base_url | **SSRF** — см. [connector-security.md](connector-security.md) |
| 21 | Custom MCP Server | URL + auth (header / OAuth) | N/A | Вызов tools MCP | Исходящие запросы; валидация сервера |

## Группировка для реализации

- **Общий Google OAuth пресет** (один проект Cloud, разные наборы scopes): Gmail, Calendar, Drive.
- **Быстрые ключи:** Stripe, Hugging Face, Similarweb (если есть ключ), Nano Banana (ключ), Supabase, Custom REST.
- **OAuth средней сложности:** Notion, Slack, Linear, HubSpot, Atlassian, monday.com.
- **Отдельный трек Meta:** Instagram, Creator Marketplace, Ads — единые предпосылки Business, правовой статус, App Review.

## Связанные документы

- [oauth-broker.md](oauth-broker.md)
- [connector-security.md](connector-security.md)
- [presets/README.md](../presets/README.md)
