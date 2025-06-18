import { vitePreprocess } from '@sveltejs/kit/vite';

const config = {
    preprocess: vitePreprocess(),
    kit: {
        // Specify the adapter for deployment
        adapter: {
            name: '@sveltejs/adapter-auto',
            options: {}
        },
        // Other configurations can be added here
    }
};

export default config;