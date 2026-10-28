description: 'Apply the source-derived Frontend Spa Engineering capability.'
---
id: frontend-spa-engineering
name: Skill - 055 - Frontend Spa Engineering
version: 1.0.0
status: structurally_validated
source: global-skills:skills\frontend-spa-engineering\SKILL.md
---

# Skill - 055 - Frontend Spa Engineering

## Purpose
Apply the reusable Frontend Spa Engineering capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Frontend Spa Engineering.
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

# Frontend Single Page Application Engineering

## Purpose and Scope
Architect, implement, optimize, and maintain responsive Single Page Applications (SPAs) using modern frameworks (Angular 18+ Standalone, React, or Vue). Enforces clean component composition, reactive state management (RxJS, Signals), route protection, HTTP client interceptors, accessible UI design, and production bundle optimization.

## Trigger Conditions
- Developing or refactoring frontend UI components (Chat views, Agent Studios, Login forms).
- Implementing reactive state streams or asynchronous message handling.
- Configuring Angular `authGuard` and HTTP `authInterceptor` for JWT propagation.
- Diagnosing frontend compilation errors or optimizing production bundle sizes.
- Implementing responsive design systems, loading skeletons, and interactive dialogs.

## Non-Trigger Conditions
- Do not trigger for backend API controller development (use `backend-spring-microservices`).
- Do not trigger for container reverse-proxy configuration (use `devops-container-orchestration`).
- Do not trigger for pure CSS graphic asset creation.

## Prerequisites and Inputs
- Node.js runtime (v20+ or v22 LTS) and npm package manager.
- Frontend workspace manifests (`package.json`, `angular.json`, `tsconfig.json`).
- Backend REST API endpoint contracts and DTO interfaces.

## Execution Workflow
1. **Component Architecture & Routing**:
   - Angular 18: Utilize Standalone Components (`standalone: true`, `imports: [...]`) eliminating legacy `NgModule`.
   - Organize by features: `core/` (services, guards, interceptors, models) and `pages/` (Login, Chat, Studio).
   - Configure lazy-loaded routing (`loadComponent: () => import(...)`).
2. **Reactive State & Event Handling**:
   - Manage real-time data flows via RxJS `BehaviorSubject`, `Observable`, or Angular Signals.
   - Decouple API calls into dedicated service singletons (`ApiService`, `AuthService`).
3. **Authentication & Token Interceptors**:
   - Implement `authInterceptor` to automatically attach `Authorization: Bearer <jwt>` to outgoing API requests.
   - Implement `authGuard` using functional guards (`CanActivateFn`) redirecting unauthenticated users to `/login`.
4. **UI/UX Ergonomics & Feedback**:
   - Provide loading states, spinners, and disable submit buttons during in-flight network requests.
   - Render tool execution badges (e.g. `[tool_name: SUCCESS]`) and human-in-the-loop approval confirmation dialogs.
5. **Production Build & Asset Optimization**:
   - Run production bundling with Vite/esbuild tree-shaking and asset compression.

## Commands and Examples
```powershell
# Run Angular development server with proxy forwarding
npm start

# Execute production optimized build
npm run build -- --configuration production

# Check bundle sizes and chunk distributions
Get-ChildItem -Path .\dist\ -Recurse -File | Select-Object Name, Length
```

```typescript
// Angular 18 Functional Auth Guard Example
export const authGuard: CanActivateFn = (route, state) => {
  const auth = inject(AuthService);
  const router = inject(Router);
  if (auth.isLoggedIn()) {
    return true;
  }
  return router.createUrlTree(['/login'], { queryParams: { returnUrl: state.url } });
};
```

## Deliverables and Outputs
- Standalone component classes (`*.component.ts`), HTML templates, and CSS stylesheets.
- Functional route guards and HTTP interceptors.
- Production-ready distribution bundles in `dist/`.

## Quality Gates and Acceptance Criteria
- Production build completes with zero errors (`npm run build`).
- Initial chunk size meets performance budget thresholds (< 500 kB raw).
- UI remains responsive during background calculation tasks without UI thread freezes.

## Security and Safety Rules
- Sanitize rendered HTML strings to prevent Cross-Site Scripting (XSS).
- Store session tokens securely; avoid leaking sensitive authorization tokens in query parameters or unencrypted local storage.
