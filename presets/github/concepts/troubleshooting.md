# GitHub connector — troubleshooting

Текст для `concept_add`.

## Healthcheck падает с 401

- PAT удалён или истёк срок — создайте новый.
- В буфере обмена лишние пробелы — перезапишите KV.

## Fine-grained: 404 на репозиторий

- Токен не выдан на нужный repo — добавьте repository access в настройках токена.

## Org блокирует classic PAT

- Используйте fine-grained token или GitHub App согласно политике org.
