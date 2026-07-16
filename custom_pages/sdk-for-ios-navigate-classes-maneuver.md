---
title: "Maneuver Class Reference"
slug: "sdk-for-ios-navigate-classes-maneuver"
---

# Maneuver

<div class="declaration">

<div class="language">

``` highlight
public class Maneuver
```

``` highlight
extension Maneuver: NativeBase
```

``` highlight
extension Maneuver: Hashable
```

</div>

</div>

This class provides all the information for a maneuver. The directional information (e.g. road names, road numbers and signpost direction) is stored in <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp">`Maneuver.roadTexts`</a> and <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp">`Maneuver.nextRoadTexts`</a> attributes. As for the motorway exit information, it can be obtained from <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp">`Maneuver.exitSignTexts`</a> attribute.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC6actionAA0B6ActionOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-action" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC6actionAA0B6ActionOvp" class="token"><code>action</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the maneuver action.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var action: ManeuverAction { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maneuveraction">ManeuverAction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic coordinates where the maneuver is located.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC6offsets5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-offset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC6offsets5Int32Vvp" class="token"><code>offset</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index over <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC8geometryAA11GeoPolylineVvp">`Section.geometry`</a> where the maneuver is located.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offset: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC11countryCodeSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC11countryCodeSSSgvp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The country code of the maneuver position. The value is `nil` when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-exitSignTexts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp" class="token"><code>exitSignTexts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The textual attributes of the exit sign. These might contain exit number(s) and/or name(s). These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var exitSignTexts: LocalizedTexts { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtexts">LocalizedTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC14lengthInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC14lengthInMeterss5Int32Vvp" class="token"><code>lengthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of the maneuver in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInMeters: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadTexts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp" class="token"><code>roadTexts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information. **Note:** These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadTexts: RoadTexts { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-roadtexts">RoadTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-nextRoadTexts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp" class="token"><code>nextRoadTexts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var nextRoadTexts: RoadTexts { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-roadtexts">RoadTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC8signpostAA8SignpostVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-signpost" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC8signpostAA8SignpostVSgvp" class="token"><code>signpost</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the <a href="sdk-for-ios-navigate-structs-signpost">`Signpost`</a> object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var signpost: Signpost? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-signpost">Signpost</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC17intersectionNamesAA14LocalizedTextsVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-intersectionNames" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC17intersectionNamesAA14LocalizedTextsVvp" class="token"><code>intersectionNames</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The textual attributes of the intersection. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. **Note:** Routes calculated with OfflineRoutingEngine are not supported.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var intersectionNames: LocalizedTexts { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtexts">LocalizedTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC4textSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-text" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC4textSSvp" class="token"><code>text</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maneuver instruction. The text is formatted and localized as specified via <a href="sdk-for-ios-navigate-structs-routetextoptions">`RouteTextOptions`</a>. **Note for users of the Navigate license:** This text is meant to be displayed in a preview context, whereas real-time `EventTextListener` texts are meant to be used for spoken voice announcements during a trip.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var text: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC12sectionIndexs5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-sectionIndex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC12sectionIndexs5Int32Vvp" class="token"><code>sectionIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index over <a href="sdk-for-ios-navigate-classes-route#sdk-for-ios-navigate-s-7heresdk5RouteC8sectionsSayAA7SectionCGvp">`Route.sections`</a> indicating the section to which the maneuver belongs to.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionIndex: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC9spanIndexs5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-spanIndex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC9spanIndexs5Int32Vvp" class="token"><code>spanIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index over <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC5spansSayAA4SpanCGvp">`Section.spans`</a> indicating the first span after the maneuver point. **Note:** The span index for the last maneuvers (those maneuvers with maneuver action set to <a href="sdk-for-ios-navigate-enums-maneuveraction#sdk-for-ios-navigate-s-7heresdk14ManeuverActionO6arriveyA2CmF">`ManeuverAction.arrive`</a>) cannot be used, since these maneuvers are placed after the last span of the route and the span index for them would be greater than the span list size.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spanIndex: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC8durationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC8durationSdvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated time in seconds needed to perform the maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: TimeInterval { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC18turnAngleInDegreesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-turnAngleInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC18turnAngleInDegreesSdSgvp" class="token"><code>turnAngleInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The angle of the turn component of the maneuver. The angle increases clockwise and small values are used for going straight, i.e. a positive number means there is a right turn and a negative number is a left turn. Some maneuvers like Depart, Arrive and Roundabout pass doesn’t have a well defined angle, so the value is omitted. **Note:** These attributes are only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var turnAngleInDegrees: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8ManeuverC24roundaboutAngleInDegreesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roundaboutAngleInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maneuver#sdk-for-ios-navigate-s-7heresdk8ManeuverC24roundaboutAngleInDegreesSdSgvp" class="token"><code>roundaboutAngleInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout. This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive in right-hand side driving country, and negative in left-hand side countries. Note that the value is available for both the enter roundabout actions and the exit roundabout actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the roundabout itself is not representing a perfect circle, then the accuracy of the angle may be compromised. **Note:** These attributes are only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roundaboutAngleInDegrees: Double? { get }
  ```

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

