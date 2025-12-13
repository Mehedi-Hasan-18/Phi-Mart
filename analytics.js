/**
 * Vercel Web Analytics Configuration
 * 
 * This module initializes Vercel Web Analytics for server-side tracking.
 * Note: The @vercel/analytics package includes client-side support through
 * its injection methods, but this file serves as an example of how analytics
 * could be initialized in a Node.js environment alongside the Django backend.
 */

import { inject } from '@vercel/analytics';

// Initialize Vercel Analytics
// This must run on the client side in a browser environment
if (typeof window !== 'undefined') {
  try {
    inject();
    console.log('Vercel Analytics initialized successfully');
  } catch (error) {
    console.error('Failed to initialize Vercel Analytics:', error);
  }
}

export default inject;
