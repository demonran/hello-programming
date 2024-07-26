import { createApp, createRouter, defineEventHandler, toNodeListener } from 'h3';
import { createServer } from 'http';

const app = createApp()

const router = createRouter()

app.use(router)

router.get('/', 
    defineEventHandler((event) => {
    return 'Hello world!';
})
)


createServer(toNodeListener(app)).listen(3000);



