---
title: "Span Class Reference"
slug: "sdk-for-ios-navigate-classes-span"
---

# Span

<div class="declaration">

<div class="language">

``` highlight
public class Span
```

``` highlight
extension Span: NativeBase
```

``` highlight
extension Span: Hashable
```

</div>

</div>

A span is a part of the <a href="sdk-for-ios-navigate-classes-section">`Section`</a> which is traversable or navigable. Each span usually has some geometry associated with it.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC8geometryAA11GeoPolylineVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-geometry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC8geometryAA11GeoPolylineVvp" class="token"><code>geometry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a> object representing the polyline of this span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometry: GeoPolyline { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geopolyline">GeoPolyline</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC14lengthInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC14lengthInMeterss5Int32Vvp" class="token"><code>lengthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of this span in meters.

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

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC13noticeIndexesSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-noticeIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC13noticeIndexesSays5Int32VGvp" class="token"><code>noticeIndexes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of indexes to <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a>s carefully before proceeding.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var noticeIndexes: [Int32] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-segmentReference" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp" class="token"><code>segmentReference</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The segment reference of this span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentReference: SegmentReference { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-segmentreference">SegmentReference</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficIncidentIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp" class="token"><code>trafficIncidentIndexes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The indexes of traffic incidents from the field <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">`Section.trafficIncidents`</a> of the parent <a href="sdk-for-ios-navigate-classes-section">`Section`</a>. Each matching incident takes at least a whole <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC8geometryAA11GeoPolylineVvp">`Span.geometry`</a>. The same incident can take other spans and an area out of the built route as well.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficIncidentIndexes: [Int32] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC21sectionPolylineOffsets5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-sectionPolylineOffset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC21sectionPolylineOffsets5Int32Vvp" class="token"><code>sectionPolylineOffset</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The position of the span inside the section’s geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans’ geometry share a point in the section’s geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionPolylineOffset: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-dynamicSpeedInfo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp" class="token"><code>dynamicSpeedInfo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The dynamic speed information on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dynamicSpeedInfo: DynamicSpeedInfo? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-dynamicspeedinfo">DynamicSpeedInfo</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC16streetAttributesSayAA06StreetD0OGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-streetAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC16streetAttributesSayAA06StreetD0OGvp" class="token"><code>streetAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of street attributes on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var streetAttributes: [StreetAttributes] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-streetattributes">StreetAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC13carAttributesSayAA06AccessD0OGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-carAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC13carAttributesSayAA06AccessD0OGvp" class="token"><code>carAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of car access attributes on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var carAttributes: [AccessAttributes] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-accessattributes">AccessAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC15truckAttributesSayAA06AccessD0OGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-truckAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC15truckAttributesSayAA06AccessD0OGvp" class="token"><code>truckAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of truck access attributes on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckAttributes: [AccessAttributes] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-accessattributes">AccessAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC17scooterAttributesSayAA06AccessD0OGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-scooterAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC17scooterAttributesSayAA06AccessD0OGvp" class="token"><code>scooterAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of scooter access attributes on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var scooterAttributes: [AccessAttributes] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-accessattributes">AccessAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC14walkAttributesSayAA04WalkD0OGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-walkAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC14walkAttributesSayAA04WalkD0OGvp" class="token"><code>walkAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of walk attributes on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var walkAttributes: [WalkAttributes] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-walkattributes">WalkAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC11streetNamesAA14LocalizedTextsVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-streetNames" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC11streetNamesAA14LocalizedTextsVvp" class="token"><code>streetNames</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The street names on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var streetNames: LocalizedTexts { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtexts">LocalizedTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC11roadNumbersAA013LocalizedRoadD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadNumbers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC11roadNumbersAA013LocalizedRoadD0Vvp" class="token"><code>roadNumbers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<a href="sdk-for-ios-navigate-enums-routetype">`RouteType`</a>).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadNumbers: LocalizedRoadNumbers { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedroadnumbers">LocalizedRoadNumbers</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC27speedLimitInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-speedLimitInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC27speedLimitInMetersPerSecondSdSgvp" class="token"><code>speedLimitInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed limit in meters per second on the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimitInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC26consumptionInKilowattHoursSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-consumptionInKilowattHours" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC26consumptionInKilowattHoursSdSgvp" class="token"><code>consumptionInKilowattHours</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The power consumption in kilowatt per hour necessary to traverse the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var consumptionInKilowattHours: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC19functionalRoadClassAA010FunctionaldE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-functionalRoadClass" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC19functionalRoadClassAA010FunctionaldE0OSgvp" class="token"><code>functionalRoadClass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The functional road class of the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var functionalRoadClass: FunctionalRoadClass? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-functionalroadclass">FunctionalRoadClass</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC8durationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC8durationSdvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp">`Span.dynamicSpeedInfo`</a>. This duration takes also into consideration the delays caused by the traffic.

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

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC12baseDurationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-baseDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC12baseDurationSdvp" class="token"><code>baseDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp">`Span.dynamicSpeedInfo`</a> without taking into consideration the delays caused by the traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var baseDuration: TimeInterval { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC11countryCodeSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC11countryCodeSSSgvp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The country code of the span. The value is `nil` when no data is available.

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

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC9stateCodeSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-stateCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC9stateCodeSSSgvp" class="token"><code>stateCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `nil` when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var stateCode: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC28noThroughRestrictionsIndexesSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-noThroughRestrictionsIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC28noThroughRestrictionsIndexesSays5Int32VGvp" class="token"><code>noThroughRestrictionsIndexes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of indexes to <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp">`Section.noThroughRestrictions`</a> the parent section owns. In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction’s carefully before proceeding.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var noThroughRestrictionsIndexes: [Int32] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4SpanC13getShieldText10roadNumberSSAA013LocalizedRoadG0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getShieldText-roadNumber" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC13getShieldText10roadNumberSSAA013LocalizedRoadG0V_tF" class="token"><code>getShieldText(roadNumber:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Converts full route number to the value to be displayed on the road shield. The results are based on country code and state code of `Span` object and route type of passed `road_number` argument.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getShieldText(roadNumber: LocalizedRoadNumber) -> String
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedroadnumber">LocalizedRoadNumber</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>roadNumber</code></em><code> </code></td>
  <td><div>
  <p>Route number to convert to shield text.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Text on the road shield to display.

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

