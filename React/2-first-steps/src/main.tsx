import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ItemList } from './shopping-cart/itemCounter'
// import { AppWithComponents, ComponentWithAttributes, ComponentWithStyles, FirstStepsApp, MyAwesomeApp, SecondComponent } from './firstStepsApp'

createRoot(document.getElementById('root')!).render(
  //El modo estricto nos ayuda a detectar posibles problemas en nuestra aplicacion
  <StrictMode>
    {/* <FirstStepsApp />
    <SecondComponent />
    <MyAwesomeApp />
    <AppWithComponents />
    <ComponentWithAttributes />
    <ComponentWithStyles /> */}
    <ItemList />

  </StrictMode>,
)