# Extella-connectors

Рабочая область для коннекторов и пресетов под [Extella](https://api.extella.ai): эксперты (fython / nohup), концепты, CSPL и REST API.

## Документация (`docs/`)

| Файл | Содержание |
|------|------------|
| [docs/extella-cli.md](docs/extella-cli.md) | CLI и API: токены, `expert/run`, устройства, KV, концепты, асинхронность, типичные ошибки |
| [docs/api-reference.md](docs/api-reference.md) | Справочник по эндпоинтам API |
| [docs/cspl.md](docs/cspl.md) | CSPL / fython: `$extens`, `include`, структура экспертов |
| [docs/concept-examples.md](docs/concept-examples.md) | Как устроены **концепты** в Extella и примеры текстов |
| [docs/examples/nohup-expert-example.md](docs/examples/nohup-expert-example.md) | Пример **nohup**-эксперта (скрипт верхнего уровня, `{{placeholder}}`) |

### Концепты пресета планировки (пример из `plan-creation-preset`)

| Файл | Назначение |
|------|------------|
| [docs/concepts/master_preset_floorplan.md](docs/concepts/master_preset_floorplan.md) | Мастер-концепт оркестрации floorplan-пресета |
| [docs/concepts/domain_floorplan_geometry_export.md](docs/concepts/domain_floorplan_geometry_export.md) | Доменный концепт: геометрия, экспорт SVG/PDF/PNG |

Исходный проект с кодом экспертов остаётся в репозитории **plan-creation-preset**; здесь — база знаний и точка входа для дальнейшей работы с GitHub.

## Безопасность

Не коммитьте `.env`, API-ключи и токены. Используйте KV в Extella или локальные секреты вне репозитория.
