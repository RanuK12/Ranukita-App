# 🤖 Ranukita App — Tu Jarvis Personal en el Bolsillo

> App móvil (iOS + Android) que conecta con tu asistente AI personal Ranukita.

## Visión

Una app premium que te da acceso a tu Jarvis personal desde cualquier lugar. No es un chatbot genérico — es TU asistente que conoce tus proyectos, tu vida, tus objetivos, y trabaja 24/7 para vos.

## Features Core

### 💬 Chat Inteligente
- Conversación fluida con Ranukita (mismo cerebro que Telegram)
- Voz bidireccional (hablar y escuchar)
- Envío de fotos para análisis
- Archivos adjuntos

### 📊 Dashboard Personal
- Estado de proyectos en tiempo real
- Objetivos con progress bars
- Ingresos y métricas
- Calendario integrado

### 🎯 Objetivos & Tracking
- Goals con deadlines y progreso
- Sugerencias diarias de acciones
- Historial de logros

### 🔔 Notificaciones Inteligentes
- Briefing matutino
- Oportunidades laborales
- Alertas de mercado/crypto
- Recordatorios proactivos

### 🛠 Control Remoto
- Ejecutar comandos en tu Mac
- Ver estado de daemons
- Controlar bots de producción
- Navegar archivos

### 💰 Monetización (Suscripciones)

| Plan | Precio | Features |
|------|--------|----------|
| Free | $0 | Chat básico, 10 msgs/día, sin voz |
| Pro | $9.99/mes | Chat ilimitado, voz, dashboard, notificaciones |
| Business | $29.99/mes | Todo Pro + control remoto + API + múltiples dispositivos |
| Enterprise | $99/mes | White-label, custom AI, soporte prioritario |

## Stack Técnico

| Capa | Tecnología |
|------|-----------|
| Frontend | React Native (Expo) — iOS + Android |
| UI | NativeWind (Tailwind para RN) |
| Backend | FastAPI (Python) — mismo server que el bot |
| Auth | Supabase Auth (Google, Apple, Email) |
| DB | Supabase (PostgreSQL) |
| Realtime | WebSocket para chat |
| Push | Firebase Cloud Messaging |
| Voz | ElevenLabs + Whisper |
| AI | DeepSeek + MiMo (mismo orchestrator) |
| Hosting | Vercel (frontend) + DigitalOcean (backend) |
| Payments | RevenueCat (suscripciones iOS/Android) |

## Arquitectura

```
App (React Native)
    ↕ WebSocket + REST API
Backend (FastAPI)
    ↕
Ranukita Orchestrator (DeepSeek + Tools)
    ├─ Mismo cerebro que Telegram
    ├─ Misma memoria (Qdrant)
    ├─ Mismas tools (bash, chrome, adobe, etc.)
    └─ Historial compartido entre app y Telegram
```

## Diseño UX

### Pantallas principales:
1. **Chat** — Interfaz tipo iMessage, burbujas, voz, adjuntos
2. **Dashboard** — Cards con métricas, gráficos, estado
3. **Objetivos** — Lista con progress, deadlines, acciones sugeridas
4. **Perfil** — Settings, suscripción, conexiones

### Principios de diseño:
- Dark mode por defecto (como la marca Ranukita)
- Colores: violeta oscuro + rosa/fucsia + cyan
- Tipografía: Inter (misma que el dashboard web)
- Animaciones suaves (Reanimated)
- Haptic feedback en acciones importantes
- Onboarding en 3 pasos

## Roadmap

### Fase 1 — MVP (2 semanas)
- [ ] Setup Expo + NativeWind
- [ ] Pantalla de Chat funcional
- [ ] Conexión WebSocket al backend
- [ ] Auth con Supabase
- [ ] Push notifications básicas

### Fase 2 — Features (2 semanas)
- [ ] Dashboard con métricas
- [ ] Voz (grabar + reproducir)
- [ ] Envío de fotos
- [ ] Objetivos panel

### Fase 3 — Monetización (1 semana)
- [ ] RevenueCat integrado
- [ ] Planes Free/Pro/Business
- [ ] Paywall

### Fase 4 — Launch
- [ ] TestFlight (iOS)
- [ ] Google Play Beta
- [ ] Landing page
- [ ] Marketing

## Cómo contribuir

Este proyecto lo desarrolla Ranukita (el bot) durante las noches como tarea autónoma. Emilio revisa y aprueba los PRs.

## Licencia

MIT — © 2026 Ranuk IT Solutions | ranuk.dev
