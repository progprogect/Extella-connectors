# Возможности: GitHub (PAT)

| Операция | API | Права токена | Примечание |
|----------|-----|--------------|------------|
| Проверка учётки | `GET /user` | metadata / user read | Используется healthcheck |
| Список репозиториев | `GET /user/repos` | `repo` или fine-grained repo read | Пагинация |
| Issues | `GET/POST /repos/{owner}/{repo}/issues` | `issues` / repo scope | Rate limits |

Полная документация: [GitHub REST](https://docs.github.com/en/rest).

## Вне scope этого мини-пресета

- GitHub Apps установка, marketplace, секреты Actions — отдельные пресеты.
