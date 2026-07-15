---
title: "EventText Structure Reference"
slug: "sdk-for-ios-navigate-structs-eventtext"
---

# EventText

<div class="declaration">

<div class="language">

``` highlight
public struct EventText : Hashable
```

</div>

</div>

Contains all the information regarding the next text announcement.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the type of text announcement

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: TextNotificationType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EventTextV16distanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV16distanceInMetersSdvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance in meters to the location of the event for which the text notification is given.

  **Note:** For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or greater rounds up, else down) to simplify the distance phrase in `ManeuverNotifications` texts during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers are rounded to 4 kilometers and the notification will begin with `After 4 kilometers...`. However, 3.5 miles are not rounded up and the notification will begin with `After three and a half miles...`. Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself are defined in the <a href="sdk-for-ios-navigate-enums-unitsystem">`UnitSystem`</a> class.

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

  ` `<span id="/s:7heresdk9EventTextV4textSSvp"></span>` `<span id="//apple_ref/swift/Property/text" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV4textSSvp" class="token"><code>text</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text notification instruction. The text is formatted and localized as specified via <a href="sdk-for-ios-navigate-structs-routetextoptions">`RouteTextOptions`</a>.

  **Note:** During navigation, the text will be always empty when the <a href="sdk-for-ios-navigate-classes-maneuver">`Maneuver`</a> is taken from the <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a> instance via the provided index. The text instruction that can be accessed from the <a href="sdk-for-ios-navigate-classes-route">`Route`</a> instance is meant as preview and it is not necessarily matching the more comprehensive maneuver information you can access during navigation. This information can be enhanced with real-time `ManeuverNotifications` texts that can be used for spoken text notifications during a trip.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var text: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EventTextV27maneuverNotificationDetailsAA08ManeuvereF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/maneuverNotificationDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV27maneuverNotificationDetailsAA08ManeuvereF0VSgvp" class="token"><code>maneuverNotificationDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Information about the next maneuver. Is non-`nil` only for <a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp">`EventText.type`</a> equals to <a href="sdk-for-ios-navigate-enums-textnotificationtype#/s:7heresdk20TextNotificationTypeO8maneuveryA2CmF">`TextNotificationType.maneuver`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverNotificationDetails: ManeuverNotificationDetails?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EventTextV26spatialNotificationDetailsAA07SpatialeF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/spatialNotificationDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV26spatialNotificationDetailsAA07SpatialeF0VSgvp" class="token"><code>spatialNotificationDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Information for a spatial text notifications. When <a href="sdk-for-ios-navigate-structs-eventtextoptions#/s:7heresdk16EventTextOptionsV18enableSpatialAudioSbvp">`EventTextOptions.enableSpatialAudio`</a> is false, then this attribute will be `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spatialNotificationDetails: SpatialNotificationDetails?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(type: distanceInMeters: text: maneuverNotificationDetails: spatialNotificationDetails: )

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

    - type: Indicates the type of text announcement
    - distanceInMeters: Distance in meters to the location of the event for which the text notification is given.

    **Note:** For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or greater rounds up, else down) to simplify the distance phrase in `ManeuverNotifications` texts during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers are rounded to 4 kilometers and the notification will begin with `After 4 kilometers...`. However, 3.5 miles are not rounded up and the notification will begin with `After three and a half miles...`. Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself are defined in the <a href="sdk-for-ios-navigate-enums-unitsystem">`UnitSystem`</a> class.

    - text: The text notification instruction. The text is formatted and localized as specified via <a href="sdk-for-ios-navigate-structs-routetextoptions">`RouteTextOptions`</a>.

    **Note:** During navigation, the text will be always empty when the <a href="sdk-for-ios-navigate-classes-maneuver">`Maneuver`</a> is taken from the <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a> instance via the provided index. The text instruction that can be accessed from the <a href="sdk-for-ios-navigate-classes-route">`Route`</a> instance is meant as preview and it is not necessarily matching the more comprehensive maneuver information you can access during navigation. This information can be enhanced with real-time `ManeuverNotifications` texts that can be used for spoken text notifications during a trip.

    - maneuverNotificationDetails: Information about the next maneuver. Is non-`nil` only for <a href="sdk-for-ios-navigate-structs-eventtext#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp">`EventText.type`</a> equals to <a href="sdk-for-ios-navigate-enums-textnotificationtype#/s:7heresdk20TextNotificationTypeO8maneuveryA2CmF">`TextNotificationType.maneuver`</a>.
    - spatialNotificationDetails: Information for a spatial text notifications. When <a href="sdk-for-ios-navigate-structs-eventtextoptions#/s:7heresdk16EventTextOptionsV18enableSpatialAudioSbvp">`EventTextOptions.enableSpatialAudio`</a> is false, then this attribute will be `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( type : TextNotificationType , distanceInMeters : Double , text : String , maneuverNotificationDetails : ManeuverNotificationDetails ? = nil , spatialNotificationDetails : SpatialNotificationDetails ? = nil )
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

