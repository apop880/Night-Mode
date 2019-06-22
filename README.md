# Night Mode

_Lowers the default brightness of lights at night._

## Installation

This app is best installed using
[HACS](https://github.com/custom-components/hacs), so that you can easily track
and download updates.

Alternatively, you can download the `nightmode` directory from inside the `apps` directory here to your
local `apps` directory, then add the configuration to enable the `nightmode`
module.

## How it works

You will need to create an entity called `input_boolean.night_mode`. When this
`input_boolean` is turned on, whether manually or by another automation you
create, night mode will be activated for the lights you define in `apps.yaml`.
Any lights that are on will dim to the level you have specified in `apps.yaml`.
If a light is turned on while night mode is on, that light will dim to the night
mode brightness automatically.

If night mode hasn't already been turned off manually or by another automation,
it will be turned off automatically at sunrise. The app will attempt to store
the previous daytime brightness of any lights turned on at night and restore
that level during the day. There is one known issue with this, as the daytime
values are not stored in a persistent fashion and therefore won't persist in the
event the app or Home Assistant are restarted. However, improvements to this
functionality are on the roadmap.

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

## Issues/Feature Requests

Please log any issues or feature requests in this GitHub repository for me to review.