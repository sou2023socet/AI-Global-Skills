description: 'Apply the source-derived Cross Platform Mobile Engineering capability.'
---
id: cross-platform-mobile-engineering
name: Skill - 003 - Cross Platform Mobile Engineering
version: 1.0.0
status: structurally_validated
source: global-skills:skills\cross-platform-mobile-engineering\SKILL.md
---

# Skill - 003 - Cross Platform Mobile Engineering

## Purpose
Apply the reusable Cross Platform Mobile Engineering capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Cross Platform Mobile Engineering.
- Confirm project identity, scope, required evidence, and permission boundaries first.
- Do not activate for unrelated work or when a more specific canonical skill owns the task.

## Required procedure
1. Inspect the project context, applicable contracts, and existing implementation before acting.
2. Follow the source capability contract below, adapting examples to the actual project.
3. Record inputs, decisions, outputs, evidence, failures, and unresolved limitations.
4. Validate the acceptance criteria with the smallest approved check; never claim an unrun check.

## Failure handling
Stop on missing prerequisites, unknown project identity, unsafe permissions, or contradictory
evidence. Preserve partial work, report the exact blocker, and return control to the
orchestrator rather than inventing a successful result.

## Permissions
Read-only inspection is the default. File changes require task scope; execution, external
access, persistent writes, production impact, and generated artifacts require explicit
command-scoped approval.

## Acceptance criteria
- The requested capability is applied to the identified project and scope.
- Outputs are actionable, traceable to evidence, and free of secrets.
- Failures and unverified steps are explicit.

## Source capability contract

The following source-preserving contract is the basis for this canonical package:

# Cross-Platform Mobile Engineering

## Purpose and Scope
Design, adapt, optimize, and maintain cross-platform mobile applications and mobile-responsive web interfaces. Bridges enterprise web architectures (Angular, React) to native mobile runtimes (Capacitor, Cordova, React Native, PWA), ensuring responsive viewports, touch-friendly interactions, offline caching, and native hardware API adapters.

## Trigger Conditions
- Packaging a web SPA into a cross-platform mobile binary (Android APK/AAB, iOS IPA).
- Adapting desktop-oriented layouts (split canvases, complex math toolbars) for small mobile touchscreens.
- Configuring mobile build toolchains (Capacitor CLI, Android SDK, Gradle).
- Auditing viewport scaling, touch target sizes ($\ge 44 \times 44\text{ px}$), and virtual keyboard ergonomics.
- Implementing offline caching strategies (Service Workers, IndexedDB).

## Non-Trigger Conditions
- Do not trigger for purely desktop-only or server-side backend logic.
- Do not trigger for raw database migrations (use `database-architecture-migration`).
- Do not trigger for low-level native C/C++ NDK drivers.

## Prerequisites and Inputs
- Working mobile-responsive web application or SPA bundle.
- Mobile bridge manifest (`capacitor.config.json` or `manifest.json`).
- Mobile build SDKs when packaging native binaries (Android Studio, JDK 21).

## Execution Workflow
1. **Viewport & Responsive Layout Adaptation**:
   - Verify viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">`.
   - Implement responsive breakpoints: Mobile Portrait (<600px), Tablet (600-1024px), Desktop (>1024px).
   - Convert multi-column layouts into collapsible bottom sheets, off-canvas drawers, or swipeable tab strips.
2. **Touch Target & Ergonomics Verification**:
   - Enforce WCAG touch target guidelines: Interactive buttons and input fields must measure at least $44 \times 44$ CSS pixels with adequate spacing.
   - Adjust input modes for numeric and math inputs (`inputmode="decimal"`, `inputmode="numeric"`).
3. **Cross-Platform Bridge Integration (Capacitor)**:
   - Initialize Capacitor wrapper: `npx cap init <app-name> <app-id>`.
   - Copy built web assets to mobile platforms: `npx cap copy`.
4. **Network Resilience & Offline Fallbacks**:
   - Implement HTTP interceptors detecting network disconnection and surfacing non-blocking offline badges.
   - Cache static assets using Service Workers for PWA compliance.
5. **Virtual Keyboard & Safe Area Handling**:
   - Handle mobile safe areas: `padding-top: env(safe-area-inset-top)`, `padding-bottom: env(safe-area-inset-bottom)`.
   - Ensure input fields remain visible above the on-screen virtual keyboard.

## Commands and Examples
```powershell
# Add Android platform to Capacitor project
npx cap add android

# Sync latest frontend web build into mobile native assets
npm run build
npx cap sync
```

```css
/* Mobile Safe Area & Touch Ergonomics */
.mobile-app-shell {
  padding-top: max(16px, env(safe-area-inset-top));
  padding-bottom: max(16px, env(safe-area-inset-bottom));
}

.touch-target-button {
  min-height: 48px;
  min-width: 48px;
  touch-action: manipulation;
}
```

## Deliverables and Outputs
- Responsive CSS media queries and mobile layout templates.
- Mobile bridge configuration files (`capacitor.config.json`).
- Generated native wrapper assets for Android or iOS.

## Quality Gates and Acceptance Criteria
- UI elements do not overflow horizontally on standard 360px and 390px mobile viewports.
- All interactive controls satisfy the minimum $44 \times 44\text{ px}$ touch target standard.
- Input focus does not obscure interactive forms behind the mobile virtual keyboard.

## Security and Safety Rules
- Do not store sensitive authentication tokens in unencrypted mobile webview local storage.
- Restrict webview navigation strictly to trusted application domains; disallow loading arbitrary external URLs.
