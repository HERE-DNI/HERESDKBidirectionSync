---
title: "forbiddenHazardousGoods property - ViolatedRestrictionDetails class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenhazardousgoods"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- forbiddenHazardousGoods.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ViolatedRestrictionDetails-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">forbiddenHazardousGoods</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-transport-hazardousmaterial">HazardousMaterial</a></span>\></span> <span class="name">forbiddenHazardousGoods</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials">VehicleSpecification.hazardousMaterials</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>. This property is the intersection of the two lists.

**Note** `RoadSignWarning` events and `RouteViolations` are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

</div>

## Implementation

``` dart
List<HazardousMaterial> forbiddenHazardousGoods;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
