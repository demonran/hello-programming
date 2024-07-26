
export type View = {
    path: string
    name: string
}

export const CssViews: View[] = [
    { path: 'LearnCss', name: '半透明边框' },
    { path: 'MultipleBorder', name: '多重边框' },
    { path: 'InnerBorder', name: '边框内圆角' },
    { path: 'fluid-fixed', name: '全背景等宽内容局中' },
    { path: 'stripes-background', name: '进度条' }
]

export const TailwindViews: View[] = [
    { path: 'ChitChat', name: 'ChitChat' },
    { path: 'stacked', name: 'stacked' },
    { path: 'responsive', name: 'responsive' },
]