# Connector: GitHub (Personal Access Token)

Мини-пресет для вызовов **GitHub REST API** с **PAT** (classic или fine-grained). Секрет хранится в Extella KV под ключом `connector_github_pat`.

## Предпосылки

- Учётная запись GitHub
- Права на создание PAT в org (если org ограничивает токены)

## Документы

- [onboarding.md](onboarding.md)
- [capabilities.md](capabilities.md)
- [kv.schema.json](kv.schema.json)
- [HEALTHCHECK.md](HEALTHCHECK.md) — контракт ответа healthcheck

## Статус

- [x] структура пресета
- [ ] эксперт опубликован вручную через `expert/save`
