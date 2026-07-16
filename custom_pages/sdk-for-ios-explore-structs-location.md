---
title: "Location Structure Reference"
slug: "sdk-for-ios-explore-structs-location"
---

# Location

<div class="declaration">

<div class="language">

``` highlight
public struct Location : Hashable
```

</div>

</div>

Describes a location in the world at a given time.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV16bearingInDegreesSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-bearingInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV16bearingInDegreesSdSgvp" class="token"><code>bearingInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bearing (also known as course) is the device’s horizontal direction of travel. Starts at 0 in the geographical north and rotates around the compass in a clockwise direction. This means for going north it is equal to 0, for northeast it is 45, for east it is 90 and so on. Note that this may be different from the orientation of the device. If it cannot be determined, the value is `nil`. Otherwise, it is guaranteed to be in the range \[0, 360).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearingInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV22speedInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV22speedInMetersPerSecondSdSgvp" class="token"><code>speedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current speed of the device. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-time" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp" class="token"><code>time</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time at which the location was determined.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var time: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-horizontalAccuracyInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp" class="token"><code>horizontalAccuracyInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var horizontalAccuracyInMeters: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV24verticalAccuracyInMetersSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-verticalAccuracyInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV24verticalAccuracyInMetersSdSgvp" class="token"><code>verticalAccuracyInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimated vertical accuracy. Given that the received Location contains the altitude, the real value of the altitude is estimated to lie within the following range: \[altitude - vertical accuracy, altitude + vertical accuracy\]. For example, when the altitude is equal to 50 and the vertical accuracy is 8, then the actual value is most likely in the range \[42, 58\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var verticalAccuracyInMeters: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV24bearingAccuracyInDegreesSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-bearingAccuracyInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV24bearingAccuracyInDegreesSdSgvp" class="token"><code>bearingAccuracyInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimated bearing accuracy for this location, in degrees. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearingAccuracyInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV30speedAccuracyInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedAccuracyInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV30speedAccuracyInMetersPerSecondSdSgvp" class="token"><code>speedAccuracyInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimated speed accuracy of this location, in meters per second. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedAccuracyInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV18timestampSinceBootSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timestampSinceBoot" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV18timestampSinceBootSdSgvp" class="token"><code>timestampSinceBoot</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time at which the location was determined, relative to device boot time. This time is monotonic and not affected by leap time or other system time adjustments, so this is the recommended basis for general purpose interval timing between location updates. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timestampSinceBoot: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV18locationTechnologyAA0bD0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-locationTechnology" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV18locationTechnologyAA0bD0OSgvp" class="token"><code>locationTechnology</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional technology or provider of this location. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var locationTechnology: LocationTechnology?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationtechnology">LocationTechnology</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV6sourceAA0B6SourceOSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-source" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV6sourceAA0B6SourceOSgvp" class="token"><code>source</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional source of this location. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var source: LocationSource?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationsource">LocationSource</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV8gnssTimeSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-gnssTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV8gnssTimeSdSgvp" class="token"><code>gnssTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional gnss time at which the location was determined. It is a time interval from the Unix time epoch in milliseconds. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var gnssTime: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV14pitchInDegreesSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-pitchInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV14pitchInDegreesSdSgvp" class="token"><code>pitchInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Pitch of this location, in degrees. If it cannot be determined, the value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pitchInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8LocationV11coordinates16bearingInDegrees05speedE15MetersPerSecond4time018horizontalAccuracyeH008verticalmeH00dmeF00gmehiJ018timestampSinceBoot18locationTechnology6source8gnssTime05pitcheF0AcA14GeoCoordinatesV_SdSgAS10Foundation4DateVSgA5sA0bS0OSgAA0B6SourceOSgA2Stcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-coordinates-bearingInDegrees-speedInMetersPerSecond-time-horizontalAccuracyInMeters-verticalAccuracyInMeters-bearingAccuracyInDegrees-speedAccuracyInMetersPerSecond-timestampSinceBoot-locationTechnology-source-gnssTime-pitchInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV11coordinates16bearingInDegrees05speedE15MetersPerSecond4time018horizontalAccuracyeH008verticalmeH00dmeF00gmehiJ018timestampSinceBoot18locationTechnology6source8gnssTime05pitcheF0AcA14GeoCoordinatesV_SdSgAS10Foundation4DateVSgA5sA0bS0OSgAA0B6SourceOSgA2Stcfc" class="token"><code>init(coordinates:</code><wbr></wbr><code>bearingInDegrees:</code><wbr></wbr><code>speedInMetersPerSecond:</code><wbr></wbr><code>time:</code><wbr></wbr><code>horizontalAccuracyInMeters:</code><wbr></wbr><code>verticalAccuracyInMeters:</code><wbr></wbr><code>bearingAccuracyInDegrees:</code><wbr></wbr><code>speedAccuracyInMetersPerSecond:</code><wbr></wbr><code>timestampSinceBoot:</code><wbr></wbr><code>locationTechnology:</code><wbr></wbr><code>source:</code><wbr></wbr><code>gnssTime:</code><wbr></wbr><code>pitchInDegrees:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of the class with specified parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(coordinates: GeoCoordinates, bearingInDegrees: Double? = nil, speedInMetersPerSecond: Double? = nil, time: Date? = nil, horizontalAccuracyInMeters: Double? = nil, verticalAccuracyInMeters: Double? = nil, bearingAccuracyInDegrees: Double? = nil, speedAccuracyInMetersPerSecond: Double? = nil, timestampSinceBoot: TimeInterval? = nil, locationTechnology: LocationTechnology? = nil, source: LocationSource? = nil, gnssTime: TimeInterval? = nil, pitchInDegrees: Double? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-locationtechnology">LocationTechnology</a>
  - <a href="sdk-for-ios-explore-enums-locationsource">LocationSource</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

