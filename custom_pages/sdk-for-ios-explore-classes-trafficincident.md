---
title: "TrafficIncident Class Reference"
slug: "sdk-for-ios-explore-classes-trafficincident"
---

# TrafficIncident

<div class="declaration">

<div class="language">

``` highlight
public class TrafficIncident : TrafficIncidentBase
```

``` highlight
extension TrafficIncident: NativeBase
```

``` highlight
extension TrafficIncident: Hashable
```

</div>

</div>

TrafficIncident provides details about a traffic incident.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC6impactAA0bC6ImpactOvp"></span>` `<span id="//apple_ref/swift/Property/impact" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC6impactAA0bC6ImpactOvp" class="token"><code>impact</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The impact of the incident. The value is <a href="sdk-for-ios-explore-enums-trafficincidentimpact#/s:7heresdk21TrafficIncidentImpactO7unknownyA2CmF">`TrafficIncidentImpact.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var impact: TrafficIncidentImpact { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC4typeAA0bC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC4typeAA0bC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The category of the incident. The value is <a href="sdk-for-ios-explore-enums-trafficincidenttype#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">`TrafficIncidentType.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: TrafficIncidentType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC11descriptionAA13LocalizedTextVvp"></span>` `<span id="//apple_ref/swift/Property/description" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC11descriptionAA13LocalizedTextVvp" class="token"><code>description</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var description: LocalizedText { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC9startTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/startTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC9startTime10Foundation4DateVSgvp" class="token"><code>startTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time from which the incident is valid, before this time the incident should not be considered. The value is `nil` if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startTime: Date? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC7endTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/endTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC7endTime10Foundation4DateVSgvp" class="token"><code>endTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time until which the incident is valid, after this time the incident should not be considered. The value is `nil` if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var endTime: Date? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC2idSSvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC2idSSvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique current identifier for a traffic incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC10originalIdSSvp"></span>` `<span id="//apple_ref/swift/Property/originalId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC10originalIdSSvp" class="token"><code>originalId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique identifier of the first traffic incident. The original id remains the same whenever the traffic incident is updated and <a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC2idSSvp">`TrafficIncident.id`</a> is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using

      TrafficEngine.lookupIncident(...)

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var originalId: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC8parentIdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/parentId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC8parentIdSSSgvp" class="token"><code>parentId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The identifier of another incident to which this incident is linked. The value is `nil` if the incident doesn’t have a parent.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentId: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC23junctionsTraversabilityAA09JunctionsE0Ovp"></span>` `<span id="//apple_ref/swift/Property/junctionsTraversability" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC23junctionsTraversabilityAA09JunctionsE0Ovp" class="token"><code>junctionsTraversability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traversability of junctions along the affected road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var junctionsTraversability: JunctionsTraversability { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC12isRoadClosedSbvp"></span>` `<span id="//apple_ref/swift/Property/isRoadClosed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC12isRoadClosedSbvp" class="token"><code>isRoadClosed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The flag indicates whether road is closed or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRoadClosed: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC5codesSays5Int32VGvp"></span>` `<span id="//apple_ref/swift/Property/codes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC5codesSays5Int32VGvp" class="token"><code>codes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category. Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var codes: [Int32] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp"></span>` `<span id="//apple_ref/swift/Property/summary" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp" class="token"><code>summary</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The human readable summary of the incident. The summary field provides a short version of the description containing no location information. The expected summary language can be managed via <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp">`TrafficIncidentsQueryOptions.languageCode`</a> and <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions#/s:7heresdk28TrafficIncidentLookupOptionsV12languageCodeAA08LanguageG0OSgvp">`TrafficIncidentLookupOptions.languageCode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var summary: LocalizedText { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC9entryTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/entryTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC9entryTime10Foundation4DateVSgvp" class="token"><code>entryTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time the incident was entered into the system. The value is `nil` if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var entryTime: Date? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC8locationAA0B8LocationVvp"></span>` `<span id="//apple_ref/swift/Property/location" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC8locationAA0B8LocationVvp" class="token"><code>location</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The location of the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var location: TrafficLocation { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp"></span>` `<span id="//apple_ref/swift/Property/vehicleRestrictions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp" class="token"><code>vehicleRestrictions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map of restricted vehicle categories to restrictions. A vehicle is restricted if at least one restriction field is applicable for it. If the map is empty, there’re no restricted vehicles for the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleRestrictions: [TrafficIncident.RestrictedVehicleCategory : TrafficIncident.VehicleRestriction] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO"></span>` `<span id="//apple_ref/swift/Enum/RestrictedVehicleCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO" class="token"><code>RestrictedVehicleCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vehicle categories that can be restricted. Note, a vehicle can belong to several categories (e.g. a passenger motor car belongs to <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF">`TrafficIncident.RestrictedVehicleCategory.car`</a>, <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF">`TrafficIncident.RestrictedVehicleCategory.motorVehicle`</a>, and <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#/s:7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF">`TrafficIncident.RestrictedVehicleCategory.all`</a>). A vehicle is restricted if it belongs to the category presented in the map <a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp">`TrafficIncident.vehicleRestrictions`</a> and at least one of the vehicle properties is under the matching <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction">`TrafficIncident.VehicleRestriction`</a>.

  <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RestrictedVehicleCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/VehicleRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-trafficincident#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV" class="token"><code>VehicleRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vehicle restriction representing a vehicle category and relevant restriction rules.

  <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct VehicleRestriction : Hashable
  ```

  </div>

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

