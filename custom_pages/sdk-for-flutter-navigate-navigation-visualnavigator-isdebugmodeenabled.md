---
title: "isDebugModeEnabled property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-isdebugmodeenabled"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isDebugModeEnabled</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isDebugModeEnabled</span>

</div>

<div class="section desc markdown">

When enabled, it shows useful information for debugging purposes.

- A semi-transparent location marker indicating the map-matched location.
- A gray, semi-transparent location marker indicating the raw (or original) input location.
- A red polyline indicating the most probable path.
- A SVG overlay, on the middle-left of the screen, showing the following:
  - IN - Input location: coordinates \[bearing\] \[speed\] \[accuracy\]
  - RM - Route-matched location: coordinates bearing (distance-to-raw-location)
  - MM - Map-Matched location: coordinates bearing (distance-to-raw-location)
  - RM-MM - distance-between-route-and-map-matched-locations
  - RP - Route progress: remaining-duration remaining-distance
  - SP - Section progress: section-index/sections-count remaining-duration remaining-distance
  - MP - Maneuver progress: maneuver-index remaining-duration remaining-distance
  - CPU - CPU usage: cpu-usage current-date-time
  - MS - Milestone status: section-index MISSED\|REACHED when
  - RD - Route deviation: last-traveled-section-index last-traveled-section-distance when
  - FPS - Frames per second: frames-per-second

Fields between brackets (\[\]'s) are omitted if not available.

Example:

``` dart
IN: 53.96880,14.77903 167° 8m/s
RM: 53.96880,14.77903 167° (0.0m)
MM: 53.96879,14.77903 167° (0.5m)
RM-MM: 0.5m
RP: 49h0m3s 4302km
SP: 0/16 1h2m20s 58km
MP: 1 5s 25m
CPU: 7% 2024-01-01 13:21:59
MS: 1 REACHED 12:34:22
RD: 2 345m 11:13:55
FPS: 30.0
```

**Note:** This API should be used for debugging purposes only. Gets the current debug mode state.

</div>

## Implementation

``` dart
bool get isDebugModeEnabled;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isDebugModeEnabled=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isDebugModeEnabled-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

When enabled, it shows useful information for debugging purposes.

- A semi-transparent location marker indicating the map-matched location.
- A gray, semi-transparent location marker indicating the raw (or original) input location.
- A red polyline indicating the most probable path.
- A SVG overlay, on the middle-left of the screen, showing the following:
  - IN - Input location: coordinates \[bearing\] \[speed\] \[accuracy\]
  - RM - Route-matched location: coordinates bearing (distance-to-raw-location)
  - MM - Map-Matched location: coordinates bearing (distance-to-raw-location)
  - RM-MM - distance-between-route-and-map-matched-locations
  - RP - Route progress: remaining-duration remaining-distance
  - SP - Section progress: section-index/sections-count remaining-duration remaining-distance
  - MP - Maneuver progress: maneuver-index remaining-duration remaining-distance
  - CPU - CPU usage: cpu-usage current-date-time
  - MS - Milestone status: section-index MISSED\|REACHED when
  - RD - Route deviation: last-traveled-section-index last-traveled-section-distance when
  - FPS - Frames per second: frames-per-second

Fields between brackets (\[\]'s) are omitted if not available.

Example:

``` dart
IN: 53.96880,14.77903 167° 8m/s
RM: 53.96880,14.77903 167° (0.0m)
MM: 53.96879,14.77903 167° (0.5m)
RM-MM: 0.5m
RP: 49h0m3s 4302km
SP: 0/16 1h2m20s 58km
MP: 1 5s 25m
CPU: 7% 2024-01-01 13:21:59
MS: 1 REACHED 12:34:22
RD: 2 345m 11:13:55
FPS: 30.0
```

**Note:** This API should be used for debugging purposes only. Sets whether to enable debug mode or not.

</div>

## Implementation

``` dart
set isDebugModeEnabled(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

