"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var h3_1 = require("h3");
var http_1 = require("http");
var app = (0, h3_1.createApp)();
var router = (0, h3_1.createRouter)();
app.use(router);
router.get('/', (0, h3_1.defineEventHandler)(function (event) {
    return 'Hello world!';
}));
(0, http_1.createServer)((0, h3_1.toNodeListener)(app)).listen(3000);
