import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

import { ClerkProvider } from '@clerk/clerk-react'
import ClerkAuth from './components/auth/ClerkAuth'

//  Use the correct env variable name from your .env file
const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;
console.log("CLERK KEY:", PUBLISHABLE_KEY);

if (!PUBLISHABLE_KEY) {
  throw new Error('Missing Publishable Key')
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ClerkProvider publishableKey={PUBLISHABLE_KEY} afterSignOutUrl='/login'>
      <ClerkAuth>
        <App />
      </ClerkAuth>
    </ClerkProvider>
  </StrictMode>,
)
