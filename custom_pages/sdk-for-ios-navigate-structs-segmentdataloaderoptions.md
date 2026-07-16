---
title: "SegmentDataLoaderOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-segmentdataloaderoptions"
---

# SegmentDataLoaderOptions

<div class="declaration">

<div class="language">

``` highlight
public struct SegmentDataLoaderOptions : Hashable
```

</div>

</div>

Specifies which data should be loaded by the <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> function.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadTravelDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp" class="token"><code>loadTravelDirection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, the <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp">`SegmentSpanData.travelDirection`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadTravelDirection: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadFunctionalRoadClass" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp" class="token"><code>loadFunctionalRoadClass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, the <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp">`SegmentSpanData.functionalRoadClass`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadFunctionalRoadClass: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadTransportModesAccess" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp" class="token"><code>loadTransportModesAccess</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp">`SegmentSpanData.allowedTransportModes`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadTransportModesAccess: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadSpeedLimits" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp" class="token"><code>loadSpeedLimits</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp">`SegmentSpanData.positiveDirectionSpeedLimit`</a>, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp">`SegmentSpanData.negativeDirectionSpeedLimit`</a> and <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp">`SegmentSpanData.speedLimit`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadSpeedLimits: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadBaseSpeeds" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp" class="token"><code>loadBaseSpeeds</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp">`SegmentSpanData.positiveDirectionBaseSpeedInMetersPerSecond`</a>, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp">`SegmentSpanData.negativeDirectionBaseSpeedInMetersPerSecond`</a> and <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp">`SegmentSpanData.baseSpeedInMetersPerSecond`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadBaseSpeeds: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadLocalRoadCharacteristics" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp" class="token"><code>loadLocalRoadCharacteristics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp">`SegmentSpanData.localRoadCharacteristics`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadLocalRoadCharacteristics: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadStreetNamesAndRoadNumbers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp" class="token"><code>loadStreetNamesAndRoadNumbers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp">`SegmentSpanData.streetNames`</a> and <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp">`SegmentSpanData.roadNumbers`</a> and will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadStreetNamesAndRoadNumbers: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadRoadAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp" class="token"><code>loadRoadAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp">`SegmentSpanData.physicalAttributes`</a> and <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp">`SegmentSpanData.roadUsages`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadRoadAttributes: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadTrafficSignals" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp" class="token"><code>loadTrafficSignals</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentdata#sdk-for-ios-navigate-s-7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp">`SegmentData.trafficSignals`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadTrafficSignals: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadRoadSigns" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp" class="token"><code>loadRoadSigns</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentdata#sdk-for-ios-navigate-s-7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp">`SegmentData.roadSigns`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadRoadSigns: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadAdministrativeRules" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp" class="token"><code>loadAdministrativeRules</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp">`SegmentSpanData.administrativeRules`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadAdministrativeRules: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadRailwayCrossings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp" class="token"><code>loadRailwayCrossings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentdata#sdk-for-ios-navigate-s-7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp">`SegmentData.railwayCrossings`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadRailwayCrossings: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadUrban" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp" class="token"><code>loadUrban</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC7isUrbanSbSgvp">`SegmentSpanData.isUrban`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadUrban: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadSpecialSpeedSituations" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp" class="token"><code>loadSpecialSpeedSituations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentspandata#sdk-for-ios-navigate-s-7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp">`SegmentSpanData.specialSpeedSituations`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> is called. **Note:** To get timezone offset and daylight saving time values for TimeRule, \[sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules\] must also be set to `true`. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadSpecialSpeedSituations: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-loadTollPoints" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp" class="token"><code>loadTollPoints</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If it is true, <a href="sdk-for-ios-navigate-classes-segmentdata#sdk-for-ios-navigate-s-7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp">`SegmentData.tollPoints`</a> will be loaded when <a href="sdk-for-ios-navigate-classes-segmentdataloader#sdk-for-ios-navigate-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var loadTollPoints: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV19loadTravelDirection0F19FunctionalRoadClass0F20TransportModesAccess0F11SpeedLimits0F10BaseSpeeds0f5LocalJ15Characteristics0f14StreetNamesAndJ7Numbers0fJ10Attributes0F14TrafficSignals0fJ5Signs0F19AdministrativeRules0F16RailwayCrossings0F5Urban0f7SpecialO10Situations0F10TollPointsACSb_S14btcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-loadTravelDirection-loadFunctionalRoadClass-loadTransportModesAccess-loadSpeedLimits-loadBaseSpeeds-loadLocalRoadCharacteristics-loadStreetNamesAndRoadNumbers-loadRoadAttributes-loadTrafficSignals-loadRoadSigns-loadAdministrativeRules-loadRailwayCrossings-loadUrban-loadSpecialSpeedSituations-loadTollPoints" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#sdk-for-ios-navigate-s-7heresdk24SegmentDataLoaderOptionsV19loadTravelDirection0F19FunctionalRoadClass0F20TransportModesAccess0F11SpeedLimits0F10BaseSpeeds0f5LocalJ15Characteristics0f14StreetNamesAndJ7Numbers0fJ10Attributes0F14TrafficSignals0fJ5Signs0F19AdministrativeRules0F16RailwayCrossings0F5Urban0f7SpecialO10Situations0F10TollPointsACSb_S14btcfc" class="token"><code>init(loadTravelDirection:</code><wbr></wbr><code>loadFunctionalRoadClass:</code><wbr></wbr><code>loadTransportModesAccess:</code><wbr></wbr><code>loadSpeedLimits:</code><wbr></wbr><code>loadBaseSpeeds:</code><wbr></wbr><code>loadLocalRoadCharacteristics:</code><wbr></wbr><code>loadStreetNamesAndRoadNumbers:</code><wbr></wbr><code>loadRoadAttributes:</code><wbr></wbr><code>loadTrafficSignals:</code><wbr></wbr><code>loadRoadSigns:</code><wbr></wbr><code>loadAdministrativeRules:</code><wbr></wbr><code>loadRailwayCrossings:</code><wbr></wbr><code>loadUrban:</code><wbr></wbr><code>loadSpecialSpeedSituations:</code><wbr></wbr><code>loadTollPoints:</code><wbr></wbr><code>)</code></a> 

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
  public init(loadTravelDirection: Bool = false, loadFunctionalRoadClass: Bool = false, loadTransportModesAccess: Bool = false, loadSpeedLimits: Bool = false, loadBaseSpeeds: Bool = false, loadLocalRoadCharacteristics: Bool = false, loadStreetNamesAndRoadNumbers: Bool = false, loadRoadAttributes: Bool = false, loadTrafficSignals: Bool = false, loadRoadSigns: Bool = false, loadAdministrativeRules: Bool = false, loadRailwayCrossings: Bool = false, loadUrban: Bool = false, loadSpecialSpeedSituations: Bool = false, loadTollPoints: Bool = false)
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

