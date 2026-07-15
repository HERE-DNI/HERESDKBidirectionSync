---
title: "EnvironmentalZoneWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-environmentalzonewarning"
---

# EnvironmentalZoneWarning

<div class="declaration">

<div class="language">

``` highlight
public struct EnvironmentalZoneWarning : Hashable
```

</div>

</div>

Represents Environmental zones.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific environmental zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV16distanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV16distanceInMetersSdvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the current location to the environmental zone.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV16distanceInMetersSdvp">`EnvironmentalZoneWarning.distanceInMeters`</a> is greater than 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV6zoneIdSSvp"></span>` `<span id="//apple_ref/swift/Property/zoneId" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV6zoneIdSSvp" class="token"><code>zoneId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the environmental zone id in the map data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoneId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV4nameSSvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV4nameSSvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the official name of the environmental zone.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV11descriptionAA14LocalizedTextsVvp"></span>` `<span id="//apple_ref/swift/Property/description" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV11descriptionAA14LocalizedTextsVvp" class="token"><code>description</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the description of the environmental zone in the available languages.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var description: LocalizedTexts
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV10websiteUrlSSSgvp"></span>` `<span id="//apple_ref/swift/Property/websiteUrl" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-environmentalzonewarning#/s:7heresdk24EnvironmentalZoneWarningV10websiteUrlSSSgvp" class="token"><code>websiteUrl</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the website of the environmental zone, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var websiteUrl: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceInMeters: distanceType: zoneId: name: description: websiteUrl: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( id : Int32 = 0 , distanceInMeters : Double , distanceType : DistanceType , zoneId : String , name : String , description : LocalizedTexts = LocalizedTexts (), websiteUrl : String ? = nil )
  ```

  </pre>

  </div>

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

