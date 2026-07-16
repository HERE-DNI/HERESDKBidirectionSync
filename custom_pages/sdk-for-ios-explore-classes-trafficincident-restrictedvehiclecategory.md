---
title: "RestrictedVehicleCategory Enumeration Reference"
slug: "sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory"
---

# RestrictedVehicleCategory

<div class="declaration">

<div class="language">

``` highlight
public enum RestrictedVehicleCategory : UInt32, CaseIterable, Codable
```

</div>

</div>

The vehicle categories that can be restricted. Note, a vehicle can belong to several categories (e.g. a passenger motor car belongs to <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF">`TrafficIncident.RestrictedVehicleCategory.car`</a>, <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF">`TrafficIncident.RestrictedVehicleCategory.motorVehicle`</a>, and <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF">`TrafficIncident.RestrictedVehicleCategory.all`</a>). A vehicle is restricted if it belongs to the category presented in the map <a href="sdk-for-ios-explore-classes-trafficincident#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC19vehicleRestrictionsSDyAC25RestrictedVehicleCategoryOAC0G11RestrictionVGvp">`TrafficIncident.vehicleRestrictions`</a> and at least one of the vehicle properties is under the matching <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction">`TrafficIncident.VehicleRestriction`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3busyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-bus" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3busyA2EmF" class="token"><code>bus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bus.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case bus
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-car" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3caryA2EmF" class="token"><code>car</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case car
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO010heavyGoodsE0yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-heavyGoodsVehicle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO010heavyGoodsE0yA2EmF" class="token"><code>heavyGoodsVehicle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Heavy goods vehicle (or large goods vehicle). In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case heavyGoodsVehicle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5truckyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-truck" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5truckyA2EmF" class="token"><code>truck</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truck
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO10motorcycleyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-motorcycle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO10motorcycleyA2EmF" class="token"><code>motorcycle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Motorcycle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case motorcycle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-motorVehicle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO05motorE0yA2EmF" class="token"><code>motorVehicle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Motor vehicle. Definition: it is a self-propelled vehicle, that does not operate on rails and is used for the transportation of people or cargo.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case motorVehicle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO4taxiyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-taxi" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO4taxiyA2EmF" class="token"><code>taxi</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Taxi.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case taxi
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5trainyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-train" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5trainyA2EmF" class="token"><code>train</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Train.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case train
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO28transportingAbnormalSizeLoadyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-transportingAbnormalSizeLoad" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO28transportingAbnormalSizeLoadyA2EmF" class="token"><code>transportingAbnormalSizeLoad</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case transportingAbnormalSizeLoad
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO26transportingHazardousGoodsyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-transportingHazardousGoods" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO26transportingHazardousGoodsyA2EmF" class="token"><code>transportingHazardousGoods</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transporting hazardous goods.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case transportingHazardousGoods
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO18vehicleWithTraileryA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-vehicleWithTrailer" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO18vehicleWithTraileryA2EmF" class="token"><code>vehicleWithTrailer</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle with trailer.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case vehicleWithTrailer
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5otheryA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-other" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO5otheryA2EmF" class="token"><code>other</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Other vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case other
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-all" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC25RestrictedVehicleCategoryO3allyA2EmF" class="token"><code>all</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All the vehicles are applicable for this category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case all
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

