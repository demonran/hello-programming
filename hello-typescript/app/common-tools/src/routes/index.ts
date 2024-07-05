import { Express } from 'express';

function routes(app: Express) {
    app.get('/', (req, res) => {
        res.status(200).send('Hello World113122')
    })
}

export default routes