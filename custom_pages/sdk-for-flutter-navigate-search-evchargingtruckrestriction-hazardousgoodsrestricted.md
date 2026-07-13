---
title: "hazardousGoodsRestricted property - EVChargingTruckRestriction class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingtruckrestriction-hazardousgoodsrestricted"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVChargingTruckRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">hazardousGoodsRestricted</span> property

</div>

<div class="section multi-line-signature">

bool? <span class="name">hazardousGoodsRestricted</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Indication if vehicles carrying hazardous / dangerous goods (ADR) can enter the EV Charging Location.

- True means the access is restricted. The client should assume the restriction covers all ADR classes.
- False means there are no restrictions.
- Absence means the information is not known.

</div>

## Implementation

``` dart
bool? hazardousGoodsRestricted;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

