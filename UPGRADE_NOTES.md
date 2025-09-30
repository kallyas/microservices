# Microservices Project - Technology Update

This project has been updated to use the latest versions of all major technologies.

## Changes Summary

### Main Service (Flask)
- **Flask**: Updated from 2.2.5 to 3.0.3
- **SQLAlchemy**: Updated from 1.3.20 to 2.0.35
- **Flask-SQLAlchemy**: Updated from 2.4.4 to 3.1.1
- **Flask-Migrate**: Updated from 2.5.3 to 4.0.7
- **Flask-Cors**: Updated from 6.0.0 to 5.0.0
- **Flask-Script**: Removed (deprecated)
- **pika**: Updated from 1.1.0 to 1.3.2
- **requests**: Updated from 2.32.0 to 2.32.3
- **mysqlclient**: Updated from 2.0.1 to 2.2.4

#### Code Changes
- Updated `main.py` to use SQLAlchemy 2.0 syntax with `DeclarativeBase`
- Fixed `UniqueConstraint` to be properly defined in `__table_args__`
- Updated `manager.py` to remove Flask-Script dependency

#### Running Migrations
Instead of using `python manager.py db`, now use Flask's CLI:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Admin Service (Django)
- **Django**: Updated from 4.2.20 to 5.1.1
- **djangorestframework**: Updated from 3.12.4 to 3.15.2
- **django-cors-headers**: Updated from 3.7.0 to 4.4.0
- **django-mysql**: Updated from 3.12.0 to 4.14.0
- **pika**: Updated from 1.2.0 to 1.3.2
- **mysqlclient**: Updated from 2.0.3 to 2.2.4

#### Code Changes
- Removed deprecated `USE_L10N` setting (automatic in Django 5.1)
- Added `DEFAULT_AUTO_FIELD` setting
- Updated documentation references from Django 3.2 to 5.1

### Frontend (React with Vite)
Complete migration from Create React App to Vite:

- **React**: Updated from 17.0.2 to 18.3.1
- **react-dom**: Updated from 17.0.2 to 18.3.1
- **react-router-dom**: Updated from 6.0.0 to 6.26.2 (with proper v6 hooks)
- **TypeScript**: Updated from 4.9.5 to 5.6.2
- **Vite**: Added 5.4.6 (replaced Create React App)
- **Tailwind CSS**: Added 3.4.12
- **shadcn/ui**: Set up with initial Button component

#### Major Changes
1. **Build System**: Migrated from react-scripts to Vite
   - Faster development server
   - Better HMR (Hot Module Replacement)
   - Optimized production builds

2. **UI Framework**: Added shadcn/ui with Tailwind CSS
   - Modern, accessible components
   - Utility-first CSS framework
   - Customizable design system

3. **React Router**: Updated to v6 hooks
   - Replaced `<Route component={...}>` with `<Route element={...}>`
   - Used `useNavigate()` instead of `<Redirect>`
   - Used `useParams()` instead of `props.match.params`

4. **React 18**: Updated to use `createRoot` API
   - Better concurrent rendering support
   - Improved TypeScript support

#### New Scripts
```bash
npm run dev      # Start development server (port 3000)
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

#### Removed Files
- `reportWebVitals.ts`
- `serviceWorker.ts`
- `setupTests.ts`
- `App.test.tsx`
- `react-app-env.d.ts`
- `yarn.lock`

#### Added Files
- `vite.config.ts` - Vite configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `postcss.config.js` - PostCSS configuration
- `tsconfig.node.json` - TypeScript config for Node (Vite)
- `components.json` - shadcn/ui configuration
- `src/vite-env.d.ts` - Vite type definitions
- `src/lib/utils.ts` - Utility functions for shadcn/ui
- `src/components/ui/button.tsx` - Example shadcn/ui Button component

## Getting Started

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup (Main)
```bash
cd main
pip install -r requirements.txt
flask run
```

### Backend Setup (Admin)
```bash
cd admin
pip install -r requirements.txt
python manage.py runserver
```

## Notes
- All services now use the latest stable versions as of September 2024
- Frontend is now significantly faster with Vite
- shadcn/ui components can be added on demand using their CLI
- TypeScript configuration is optimized for Vite's bundler mode
