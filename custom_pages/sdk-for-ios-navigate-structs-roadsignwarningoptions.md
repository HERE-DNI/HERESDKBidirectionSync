---
title: "RoadSignWarningOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-roadsignwarningoptions"
---

# RoadSignWarningOptions

<div class="declaration">

<div class="language">

``` highlight
public struct RoadSignWarningOptions : Hashable
```

</div>

</div>

A struct that provides road sign warning options. Set the options for filtering of road sign notifications.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22RoadSignWarningOptionsV11typesFilterSayAA0bC4TypeOGvp"></span>` `<span id="//apple_ref/swift/Property/typesFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadsignwarningoptions#/s:7heresdk22RoadSignWarningOptionsV11typesFilterSayAA0bC4TypeOGvp" class="token"><code>typesFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of road sign types for which a warning will be given. If the list is empty, road signs are not filtered by type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var typesFilter: [RoadSignType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RoadSignWarningOptionsV16categoriesFilterSayAA0bC8CategoryOGvp"></span>` `<span id="//apple_ref/swift/Property/categoriesFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadsignwarningoptions#/s:7heresdk22RoadSignWarningOptionsV16categoriesFilterSayAA0bC8CategoryOGvp" class="token"><code>categoriesFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of road sign categories for which a warning will be given. If the list is empty, road signs are not filtered by category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var categoriesFilter: [RoadSignCategory]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RoadSignWarningOptionsV07generalD11TypesFilterSayAA07GeneraldbC4TypeOGvp"></span>` `<span id="//apple_ref/swift/Property/generalWarningTypesFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadsignwarningoptions#/s:7heresdk22RoadSignWarningOptionsV07generalD11TypesFilterSayAA07GeneraldbC4TypeOGvp" class="token"><code>generalWarningTypesFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of road sign general warning types for which a warning will be given. If the list is empty, road signs are not filtered by general warning type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var generalWarningTypesFilter: [GeneralWarningRoadSignType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RoadSignWarningOptionsV18vehicleTypesFilterSayAA0bC11VehicleTypeOGvp"></span>` `<span id="//apple_ref/swift/Property/vehicleTypesFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadsignwarningoptions#/s:7heresdk22RoadSignWarningOptionsV18vehicleTypesFilterSayAA0bC11VehicleTypeOGvp" class="token"><code>vehicleTypesFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of road sign vehicle types for which a warning will be given. If the list is empty, road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.

  **Example:** For a filter that contains only bus and trucks you will only receive specific road sign warnings for bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes. Furthermore, you will *not* get any signs that are generally applicable for all vehicles. For example, you cannot set a filter that allows to get signs for trucks *and* cars. If you want to get signs for standard vehicles like cars, then the only option is to set an empty list as filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleTypesFilter: [RoadSignVehicleType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(typesFilter: categoriesFilter: generalWarningTypesFilter: vehicleTypesFilter: )

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

    - typesFilter: The list of road sign types for which a warning will be given. If the list is empty, road signs are not filtered by type.
    - categoriesFilter: The list of road sign categories for which a warning will be given. If the list is empty, road signs are not filtered by category.
    - generalWarningTypesFilter: The list of road sign general warning types for which a warning will be given. If the list is empty, road signs are not filtered by general warning type.
    - vehicleTypesFilter: The list of road sign vehicle types for which a warning will be given. If the list is empty, road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.

    **Example:** For a filter that contains only bus and trucks you will only receive specific road sign warnings for bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes. Furthermore, you will *not* get any signs that are generally applicable for all vehicles. For example, you cannot set a filter that allows to get signs for trucks *and* cars. If you want to get signs for standard vehicles like cars, then the only option is to set an empty list as filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( typesFilter : [ RoadSignType ] = [], categoriesFilter : [ RoadSignCategory ] = [], generalWarningTypesFilter : [ GeneralWarningRoadSignType ] = [], vehicleTypesFilter : [ RoadSignVehicleType ] = [])
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

