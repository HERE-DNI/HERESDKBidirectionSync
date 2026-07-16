---
title: "SegmentSpanData Class Reference"
slug: "sdk-for-ios-navigate-classes-segmentspandata"
---

# SegmentSpanData

<div class="declaration">

<div class="language">

``` highlight
public class SegmentSpanData
```

``` highlight
extension SegmentSpanData: NativeBase
```

``` highlight
extension SegmentSpanData: Hashable
```

</div>

</div>

Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19startOffsetInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-startOffsetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19startOffsetInMeterss5Int32Vvp" class="token"><code>startOffsetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start offset. The offset in meters from the beginning of the segment to the start of the span in positive direction or from the end of the segment to the start of the span in negative direction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startOffsetInMeters: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC18spanLengthInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-spanLengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC18spanLengthInMeterss5Int32Vvp" class="token"><code>spanLengthInMeters</code></a> 

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
  public var spanLengthInMeters: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-travelDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp" class="token"><code>travelDirection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-enums-traveldirection">`TravelDirection`</a> object representing the allowed travel directions. Gets the <a href="sdk-for-ios-navigate-enums-traveldirection">`TravelDirection`</a> object for the portion of the segment. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp">`SegmentDataLoaderOptions.loadTravelDirection`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var travelDirection: TravelDirection? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-traveldirection">TravelDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-allowedTransportModes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp" class="token"><code>allowedTransportModes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-allowedtransportmodes">`AllowedTransportModes`</a> object representing the allowed transport modes. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp">`SegmentDataLoaderOptions.loadTransportModesAccess`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowedTransportModes: AllowedTransportModes? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-allowedtransportmodes">AllowedTransportModes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-functionalRoadClass" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp" class="token"><code>functionalRoadClass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-enums-functionalroadclass">`FunctionalRoadClass`</a> object representing the polyline of this segment. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp">`SegmentDataLoaderOptions.loadFunctionalRoadClass`</a> is set to `false`.

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

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-positiveDirectionSpeedLimit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp" class="token"><code>positiveDirectionSpeedLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span in the positive tavel direction. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">`SegmentDataLoaderOptions.loadSpeedLimits`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var positiveDirectionSpeedLimit: SegmentSpeedLimit? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">SegmentSpeedLimit</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-negativeDirectionSpeedLimit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp" class="token"><code>negativeDirectionSpeedLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span in the negative travel direction. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">`SegmentDataLoaderOptions.loadSpeedLimits`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var negativeDirectionSpeedLimit: SegmentSpeedLimit? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">SegmentSpeedLimit</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-speedLimit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp" class="token"><code>speedLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span. Will be loaded if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">`SegmentDataLoaderOptions.loadSpeedLimits`</a> is `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimit: SegmentSpeedLimit? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-segmentspeedlimit">SegmentSpeedLimit</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-positiveDirectionBaseSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp" class="token"><code>positiveDirectionBaseSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The average speed expected for this segment in positive direction with a car or a similar vehicle. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">`SegmentDataLoaderOptions.loadBaseSpeeds`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var positiveDirectionBaseSpeedInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-negativeDirectionBaseSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp" class="token"><code>negativeDirectionBaseSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The average speed expected for this segment in negative direction with a car or a similar vehicle. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">`SegmentDataLoaderOptions.loadBaseSpeeds`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var negativeDirectionBaseSpeedInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-baseSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp" class="token"><code>baseSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The average speed expected for this segment span with a car or a similar vehicle. Will be loaded if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">`SegmentDataLoaderOptions.loadBaseSpeeds`</a> is `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var baseSpeedInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-localRoadCharacteristics" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp" class="token"><code>localRoadCharacteristics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The local road characteristics of the segment: frontage, parking lot road, or POI access road. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp">`SegmentDataLoaderOptions.loadLocalRoadCharacteristics`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localRoadCharacteristics: [LocalRoadCharacteristic]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-localroadcharacteristic">LocalRoadCharacteristic</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-streetNames" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp" class="token"><code>streetNames</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The street names on the span. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp">`SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var streetNames: LocalizedTexts? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtexts">LocalizedTexts</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadNumbers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp" class="token"><code>roadNumbers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp">`SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadNumbers: LocalizedRoadNumbers? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedroadnumbers">LocalizedRoadNumbers</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-physicalAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp" class="token"><code>physicalAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The physical attributes of the segment. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp">`SegmentDataLoaderOptions.loadRoadAttributes`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var physicalAttributes: PhysicalAttributes? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-physicalattributes">PhysicalAttributes</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadUsages" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp" class="token"><code>roadUsages</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The road usages of the segment. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp">`SegmentDataLoaderOptions.loadRoadAttributes`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadUsages: RoadUsages? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-roadusages">RoadUsages</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-administrativeRules" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp" class="token"><code>administrativeRules</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-administrativerules">`AdministrativeRules`</a> for the segment, containing information about country code, state code, unit system, tolls, pre-trip planning and other administrative information. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp">`SegmentDataLoaderOptions.loadAdministrativeRules`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var administrativeRules: AdministrativeRules? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-administrativerules">AdministrativeRules</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC7isUrbanSbSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isUrban" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC7isUrbanSbSgvp" class="token"><code>isUrban</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The urban attribute of the segment. Returns `nil` if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp">`SegmentDataLoaderOptions.loadUrban`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isUrban: Bool? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-specialSpeedSituations" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp" class="token"><code>specialSpeedSituations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The special speed situations of the segment. Will be loaded if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp">`SegmentDataLoaderOptions.loadSpecialSpeedSituations`</a> is `true`. **Note:** To get timezone offset and daylight saving time values for TimeRule, \[sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules\] must also be set to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var specialSpeedSituations: [SegmentSpecialSpeedSituation]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a>

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

