---
title: "SpeedLimit Structure Reference"
slug: "sdk-for-ios-navigate-structs-speedlimit"
---

# SpeedLimit

<div class="declaration">

<div class="language">

``` highlight
public struct SpeedLimit : Hashable
```

</div>

</div>

Represents the speed limit of the current road. Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits, the HERE SDK internally reads the current device time and notifies only on speed limits that are currently active.

It is recommended to use

    SpeedLimit.effectiveSpeedLimitInMetersPerSecond(...)

when an application does not offer dedicated speed limit indicators for other cases, such as weather-dependent speed limits.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/speedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp" class="token"><code>speedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Regular speed limit if available. In case of unbounded speed limit, the value is zero.

  **Note:** When following a route, then this value will depend on the selected transport mode. For other speed limits, like weather-dependent speed limits only the value as shown on the local road sign is provided. It may not be applicable to all transport modes. For tracking mode (without following a route), the VehicleProfile is ignored and only the speed limit from the local road sign is provided or the regular speed limit for a particular type of road or area like regular inner-city speed limits.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV08advisorybC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/advisorySpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV08advisorybC17InMetersPerSecondSdSgvp" class="token"><code>advisorySpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.

  - Advisory speed signs due to construction are not included.
  - A speed value is published for advisory signs.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var advisorySpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV04snowbC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/snowSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV04snowbC17InMetersPerSecondSdSgvp" class="token"><code>snowSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var snowSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV04rainbC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/rainSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV04rainbC17InMetersPerSecondSdSgvp" class="token"><code>rainSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rainSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV03fogbC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/fogSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV03fogbC17InMetersPerSecondSdSgvp" class="token"><code>fogSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fogSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/optimalWeatherSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp" class="token"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility is optimal due to weather conditions.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  **Note:** This speed limit is conditioned by factors not expressed by the other ones. For example, it may be a time-related speed limit or a vehicle-related one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var optimalWeatherSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/schoolZoneSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp" class="token"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. School zone signs are often placed to slow drivers before reaching an intersection where children are crossing.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var schoolZoneSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/timeDependentSpeedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp" class="token"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device’s clock.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeDependentSpeedLimitInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(speedLimitInMetersPerSecond: advisorySpeedLimitInMetersPerSecond: snowSpeedLimitInMetersPerSecond: rainSpeedLimitInMetersPerSecond: fogSpeedLimitInMetersPerSecond: optimalWeatherSpeedLimitInMetersPerSecond: schoolZoneSpeedLimitInMetersPerSecond: timeDependentSpeedLimitInMetersPerSecond: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - speedLimitInMetersPerSecond: Regular speed limit if available. In case of unbounded speed limit, the value is zero.

    **Note:** When following a route, then this value will depend on the selected transport mode. For other speed limits, like weather-dependent speed limits only the value as shown on the local road sign is provided. It may not be applicable to all transport modes. For tracking mode (without following a route), the VehicleProfile is ignored and only the speed limit from the local road sign is provided or the regular speed limit for a particular type of road or area like regular inner-city speed limits.

    - advisorySpeedLimitInMetersPerSecond: A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.
      - Advisory speed signs due to construction are not included.
      - A speed value is published for advisory signs.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    - snowSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    - rainSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    - fogSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    - optimalWeatherSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility is optimal due to weather conditions.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    **Note:** This speed limit is conditioned by factors not expressed by the other ones. For example, it may be a time-related speed limit or a vehicle-related one.

    - schoolZoneSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. School zone signs are often placed to slow drivers before reaching an intersection where children are crossing.

    A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    - timeDependentSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device’s clock.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( speedLimitInMetersPerSecond : Double ? = nil , advisorySpeedLimitInMetersPerSecond : Double ? = nil , snowSpeedLimitInMetersPerSecond : Double ? = nil , rainSpeedLimitInMetersPerSecond : Double ? = nil , fogSpeedLimitInMetersPerSecond : Double ? = nil , optimalWeatherSpeedLimitInMetersPerSecond : Double ? = nil , schoolZoneSpeedLimitInMetersPerSecond : Double ? = nil , timeDependentSpeedLimitInMetersPerSecond : Double ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      effectiveSpeedLimitInMetersPerSecond()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the effective (lowest) speed limit between <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp">`SpeedLimit.speedLimitInMetersPerSecond`</a>, <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp">`SpeedLimit.schoolZoneSpeedLimitInMetersPerSecond`</a>, <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp">`SpeedLimit.timeDependentSpeedLimitInMetersPerSecond`</a> and <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp">`SpeedLimit.optimalWeatherSpeedLimitInMetersPerSecond`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func effectiveSpeedLimitInMetersPerSecond () -> Double ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Returns the lowest value between: <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp">`SpeedLimit.speedLimitInMetersPerSecond`</a>, <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp">`SpeedLimit.schoolZoneSpeedLimitInMetersPerSecond`</a>, <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp">`SpeedLimit.timeDependentSpeedLimitInMetersPerSecond`</a> and <a href="sdk-for-ios-navigate-structs-speedlimit#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp">`SpeedLimit.optimalWeatherSpeedLimitInMetersPerSecond`</a>.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

