import './style.css'
// No pide el tipo de archivo porq se infiere que es de ts
import './Bases/asyncAwait'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div>
    <h1>Reforzamiento TypeScript</h1>
  </div>
`;

