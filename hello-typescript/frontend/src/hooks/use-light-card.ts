import { onMounted, ref } from "vue";

interface IOption {
  light?: {
    width?: number,
    height?: number,
    color?: string,
    blur?: number

  }
}
export const useLightCard = (option: IOption = {}) => {

  const cardRef = ref<HTMLDivElement | null>(null);
  const lightRef = ref<HTMLDivElement>(document.createElement("div"));
  let cardOverflow = ''

  const setLightStyle = () => {

    const { width = 60, height = 60, color = '#ff4132', blur = 40 } = option.light || {}
    const lightDom = lightRef.value;
    lightDom.style.width = `${width}px`;
    lightDom.style.height = `${height}px`;
    lightDom.style.background = color;
    lightDom.style.filter = `blur(${blur}px)`;
    lightDom.style.position = 'absolute';
  }

  const setCardOverflowHidden = () => {
    const cardDom = cardRef.value;
    if (cardDom) {
      cardOverflow = cardDom.style.overflow;
      cardDom.style.overflow = "hidden";
    }
  };

  const restoreCardOverflow = () => {
    const cardDom = cardRef.value;
    if (cardDom) {
      cardDom.style.overflow = cardOverflow;
    }
  };

  const onMouseMove = (e: MouseEvent) => {
    const { clientX, clientY } = e

    const cardDom = cardRef.value;
    const lightDom = lightRef.value;
    if (cardDom && lightDom) {
      const { x, y } = cardDom.getBoundingClientRect()
      const { width, height } = lightDom.getBoundingClientRect()

      lightDom.style.left = `${clientX - x - width / 2}px`
      lightDom.style.top = `${clientY - y - height / 2}px`

    }
  }

  const onMouseEnter = () => {
    setCardOverflowHidden();
    const cardDom = cardRef.value;
    if(cardDom) {
      cardDom.appendChild(lightRef.value)
    }
  };

  const onMouseLeave = () => {
    restoreCardOverflow();
    const cardDom = cardRef.value;
    if(cardDom) {
      cardDom.removeChild(lightRef.value)
    }
  };



  onMounted(() => {
    console.log("onMounted");
    setLightStyle()
    cardRef.value?.addEventListener('mouseenter', onMouseEnter)
    cardRef.value?.addEventListener('mouseleave', onMouseLeave)
    cardRef.value?.addEventListener('mousemove', onMouseMove)
  })


  return {
    cardRef
  }
};

