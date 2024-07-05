import sharp from 'sharp'
import express from 'express'
import TextToSVG from 'text-to-svg'
const textToSVG = TextToSVG.loadSync();
import routes from './routes';

// const svgOptions = { x: 0, y: 0, fontSize: 72, anchor: "top", attributes: { fill: "red", stroke: "black" } };

// const svg = textToSVG.getSVG("hello", svgOptions);

// class Hello {
//     name: string
//     constructor(name: string){
//         this.name = name
//     }
// }

// async function saveFile() {
//     const b = sharp('./src/image.png');

//     // const text = await sharp(Buffer.from("测试文字"))
//     // .resize({width: 300})
//     // .png()
//     // .toBuffer()

//     const image =  b.composite([
//         {input: Buffer.from(svg), top: 100, left:10}
//     ])
//     image.png().toFile('./img.png')
// }

// saveFile()





const app = express()


app.listen(8000, async () => {
    routes(app)
})