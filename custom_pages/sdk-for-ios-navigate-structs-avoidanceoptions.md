---
title: "AvoidanceOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-avoidanceoptions"
---

# AvoidanceOptions

<div class="declaration">

<div class="language">

``` highlight
public struct AvoidanceOptions : Hashable
```

</div>

</div>

The options to specify restrictions for route calculations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV12roadFeaturesSayAA04RoadE0OGvp"></span>` `<span id="//apple_ref/swift/Property/roadFeatures" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV12roadFeaturesSayAA04RoadE0OGvp" class="token"><code>roadFeatures</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Features which routes should avoid. Best effort only (not enforced).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadFeatures: [RoadFeatures]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV9countriesSayAA11CountryCodeOGvp"></span>` `<span id="//apple_ref/swift/Property/countries" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV9countriesSayAA11CountryCodeOGvp" class="token"><code>countries</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Countries that the route must avoid. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>. **Note:** This avoidance option is not supported in <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a> for isoline calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countries: [CountryCode]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV021avoidBoundingBoxAreasC0SayAA05Avoidef4AreaC0VGvp"></span>` `<span id="//apple_ref/swift/Property/avoidBoundingBoxAreasOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV021avoidBoundingBoxAreasC0SayAA05Avoidef4AreaC0VGvp" class="token"><code>avoidBoundingBoxAreasOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of rectangular shapes which routes must not cross and additional options for this area.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidBoundingBoxAreasOptions: [AvoidBoundingBoxAreaOptions]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV017avoidPolygonAreasC0SayAA05Avoide4AreaC0VGvp"></span>` `<span id="//apple_ref/swift/Property/avoidPolygonAreasOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV017avoidPolygonAreasC0SayAA05Avoide4AreaC0VGvp" class="token"><code>avoidPolygonAreasOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of polygon shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of polygons is limited to 20.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidPolygonAreasOptions: [AvoidPolygonAreaOptions]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV018avoidCorridorAreasC0SayAA05Avoide4AreaC0VGvp"></span>` `<span id="//apple_ref/swift/Property/avoidCorridorAreasOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV018avoidCorridorAreasC0SayAA05Avoide4AreaC0VGvp" class="token"><code>avoidCorridorAreasOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of corridor shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of corridors is limited to 20.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidCorridorAreasOptions: [AvoidCorridorAreaOptions]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp"></span>` `<span id="//apple_ref/swift/Property/zoneCategories" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp" class="token"><code>zoneCategories</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zone categories which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF">`SectionNoticeCode.violatedZoneRestriction`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoneCategories: [ZoneCategory]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV8segmentsSayAA16SegmentReferenceVGvp"></span>` `<span id="//apple_ref/swift/Property/segments" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV8segmentsSayAA16SegmentReferenceVGvp" class="token"><code>segments</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments that routes will avoid going through. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>.

  **Notes:**

  - This avoidance option is not supported in <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a> for isoline calculation.
  - The engine does not support an unlimited number of segments to avoid. The limit is defined by the HERE backend services and may change. For now, the maximum number of segments to avoid should be below 250. This value may change on the backend and it is therefore not guaranteed to be stable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segments: [SegmentReference]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV13exceptZoneIdsSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/exceptZoneIds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV13exceptZoneIdsSaySSGvp" class="token"><code>exceptZoneIds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Exception to `AvoidanceOptions.zone_categories`, which can be specified by list of zone identifiers. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under “<https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview>”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var exceptZoneIds: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV7zoneIdsSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/zoneIds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV7zoneIdsSaySSGvp" class="token"><code>zoneIds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List containing identifiers of zones that routes should avoid going through. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under “<https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview>”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoneIds: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16AvoidanceOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp"></span>` `<span id="//apple_ref/swift/Property/avoidedTruckRoadTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp" class="token"><code>avoidedTruckRoadTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a list of avoided truck road types for vehicle. Refer to <a href="sdk-for-ios-navigate-enums-truckroadtype">`TruckRoadType`</a> for the available options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidedTruckRoadTypes: [TruckRoadType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(roadFeatures: countries: avoidBoundingBoxAreasOptions: avoidPolygonAreasOptions: avoidCorridorAreasOptions: zoneCategories: segments: exceptZoneIds: zoneIds: avoidedTruckRoadTypes: )

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

    - roadFeatures: Features which routes should avoid. Best effort only (not enforced).
    - countries: Countries that the route must avoid. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>. **Note:** This avoidance option is not supported in <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a> for isoline calculation.
    - avoidBoundingBoxAreasOptions: List of rectangular shapes which routes must not cross and additional options for this area.
    - avoidPolygonAreasOptions: List of polygon shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of polygons is limited to 20.
    - avoidCorridorAreasOptions: List of corridor shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of corridors is limited to 20.
    - zoneCategories: Zone categories which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO23violatedZoneRestrictionyA2CmF">`SectionNoticeCode.violatedZoneRestriction`</a>.
    - segments: Segments that routes will avoid going through. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>.

    **Notes:**

    - This avoidance option is not supported in <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a> for isoline calculation.
    - The engine does not support an unlimited number of segments to avoid. The limit is defined by the HERE backend services and may change. For now, the maximum number of segments to avoid should be below 250. This value may change on the backend and it is therefore not guaranteed to be stable.
      - exceptZoneIds: Exception to `AvoidanceOptions.zone_categories`, which can be specified by list of zone identifiers. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under “<https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview>”.
      - zoneIds: List containing identifiers of zones that routes should avoid going through. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under “<https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview>”.
      - avoidedTruckRoadTypes: Specifies a list of avoided truck road types for vehicle. Refer to <a href="sdk-for-ios-navigate-enums-truckroadtype">`TruckRoadType`</a> for the available options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( roadFeatures : [ RoadFeatures ] = [], countries : [ CountryCode ] = [], avoidBoundingBoxAreasOptions : [ AvoidBoundingBoxAreaOptions ] = [], avoidPolygonAreasOptions : [ AvoidPolygonAreaOptions ] = [], avoidCorridorAreasOptions : [ AvoidCorridorAreaOptions ] = [], zoneCategories : [ ZoneCategory ] = [], segments : [ SegmentReference ] = [], exceptZoneIds : [ String ] = [], zoneIds : [ String ] = [], avoidedTruckRoadTypes : [ TruckRoadType ] = [])
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

