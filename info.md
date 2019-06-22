## App configuration

```yaml
night_mode:
  module: nightmode
  class: NightMode
  light: light.kitchen_sink,light.kitchen_table,light.stairs
  night_brightness: 3
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `nightmode`
`class` | False | string | | `NightMode`
`light` | True | string || A comma-delimited list of entities you want to automatically control the default brightness of during night mode.
`night_brighness` | True | number from 1-255 || The default brightness of the lights listed above during night mode.