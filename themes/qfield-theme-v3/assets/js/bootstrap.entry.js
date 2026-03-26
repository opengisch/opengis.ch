import Alert from 'bootstrap/js/dist/alert'
import Carousel from 'bootstrap/js/dist/carousel'
import Collapse from 'bootstrap/js/dist/collapse'
import Dropdown from 'bootstrap/js/dist/dropdown'
import Tooltip from 'bootstrap/js/dist/tooltip'

window.bootstrap = {
  ...(window.bootstrap || {}),
  Alert,
  Carousel,
  Collapse,
  Dropdown,
  Tooltip,
}
