# HANDOFF — Ranukita App

## Estado: Planificación

### Qué hay
- README con visión completa
- Stack definido
- Roadmap con fases
- Modelo de monetización

### Próximos pasos
1. Inicializar proyecto Expo con NativeWind
2. Crear backend FastAPI con WebSocket
3. Conectar al orchestrator existente
4. Implementar auth con Supabase

### Decisiones tomadas
- React Native (Expo) para iOS + Android con un solo codebase
- Mismo orchestrator que Telegram (no duplicar lógica)
- Supabase para auth + DB (gratis con Student Pack)
- RevenueCat para suscripciones (maneja Apple + Google)
- Dark mode como identidad visual

### Notas
- El backend puede ser el mismo server que ya corre el bot
- Solo necesita un endpoint WebSocket nuevo para la app
- La app es un "frontend premium" del mismo cerebro
