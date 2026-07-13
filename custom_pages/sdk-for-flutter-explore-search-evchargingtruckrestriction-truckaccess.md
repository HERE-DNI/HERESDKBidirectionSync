---
title: "truckAccess property - EVChargingTruckRestriction class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingtruckrestriction-truckaccess"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingTruckRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">truckAccess</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-transport-truckclass">TruckClass</a></span>\></span> <span class="name">truckAccess</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Access categories for trucks and light commercial vehicles that the EV charging location is designed to serve.

While the classifications used as basis for the categories are solely based on vehicle mass, in EV charging context they can be interpreted to give an idea of the dimensional class too, as well as possible other restrictions set by the operator. If there are true dimensional or weight limits at the EV charging location, they are specified separately in vehicleLimitations.

The classification is available only to a subset of EV charging locations, depending on the information available from the operators. Hence, at least vehicles belonging to the <a href="sdk-for-flutter-explore-transport-truckclass">TruckClass.lightClass</a> category can be charged also in many EV charging locations not having explicit signaling for the <a href="sdk-for-flutter-explore-transport-truckclass">TruckClass.lightClass</a> category.

Furthermore, although the classification is based on mass/weight ranges in growing order, an upper class does not automatically mean that also all lower class vehicles are welcome to charge. For example, a location marked only with category <a href="sdk-for-flutter-explore-transport-truckclass">TruckClass.heavyClass</a> is reserved for long-haul trucks only.

</div>

## Implementation

``` dart
List<TruckClass> truckAccess;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

