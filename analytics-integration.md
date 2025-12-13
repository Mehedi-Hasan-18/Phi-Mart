# Vercel Web Analytics Integration Guide

## Overview
This project now includes Vercel Web Analytics for tracking user interactions and performance metrics. The analytics are configured for both server-side and client-side tracking.

## Installation

The following dependencies have been installed:
- `@vercel/analytics` - Vercel's web analytics package

### Installation Command
```bash
npm install
```

This creates the necessary `node_modules` and `package-lock.json` for production deployment.

## Implementation

### For Frontend Applications
If you have a separate frontend (React, Vue, Next.js, etc.) that communicates with this Django API:

**For Next.js:**
```javascript
// app/layout.js or pages/_app.js
import { Analytics } from '@vercel/analytics/react';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

**For React:**
```javascript
// src/main.jsx or src/App.jsx
import { Analytics } from '@vercel/analytics/react';

export default function App() {
  return (
    <>
      {/* Your app content */}
      <Analytics />
    </>
  );
}
```

**For Plain HTML:**
```html
<!-- Add to the end of your HTML body -->
<script defer src="/_vercel/insights/script.js"></script>
```

### For Django Backend Integration
The Django backend can log analytics events programmatically:

**In your Django views:**
```python
# Optionally track server-side events
# Note: For comprehensive analytics, client-side integration is recommended
from django.http import JsonResponse

def api_endpoint(request):
    # Your API logic here
    return JsonResponse({'status': 'success'})
```

## How It Works

1. **Client-Side Tracking**: When injected into a frontend application, `@vercel/analytics` automatically tracks:
   - Page views
   - Web vitals (CLS, FID, LCP)
   - Custom events
   - User interactions

2. **Server-Side Events**: Can be extended to track:
   - API response times
   - Database query performance
   - Error rates and exceptions
   - Custom business metrics

## Vercel Dashboard

Track your analytics in the [Vercel Dashboard](https://vercel.com/dashboard/analytics):
- Visit your project
- Navigate to the Analytics tab
- View real-time visitor data and performance metrics

## File Structure

```
phi-mart/
├── analytics.js                  # Analytics initialization (client-side)
├── package.json                  # Node.js dependencies
├── package-lock.json             # Locked dependency versions
├── analytics-integration.md       # This file
├── phi_mart/                      # Django backend
│   ├── wsgi.py
│   └── settings.py
└── [other Django files]
```

## Notes

- `@vercel/analytics` must run on the client side in a browser environment
- The `inject()` function is automatically called when using framework integrations
- Analytics data is collected in real-time and visible in the Vercel dashboard
- No additional configuration is needed once the package is installed and the injection code is added

## References

- [Vercel Analytics Documentation](https://vercel.com/docs/analytics)
- [Analytics Integration Guide](https://vercel.com/docs/analytics/guides/integration)
- [@vercel/analytics Package](https://www.npmjs.com/package/@vercel/analytics)

## Troubleshooting

**Analytics not showing in dashboard:**
- Ensure the injection code is in your client-side application
- Verify the application is deployed to Vercel
- Check that the application has received traffic
- Wait a few minutes for data to appear in the dashboard

**For Django-only deployments:**
- Consider creating a companion frontend application that communicates with this API
- The frontend can include the analytics integration
- This allows tracking of user interactions with the entire application
