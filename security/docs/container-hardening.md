# Container hardening lab

- non-root `USER`;
- bind published port to `127.0.0.1`;
- `read_only: true` + `tmpfs` для временных данных;
- `no-new-privileges`;
- healthcheck;
- минимальный сервис без секретов и внешней сети.

Лаборатория демонстрирует подход, а не production-конфигурацию инфраструктуры компании.
