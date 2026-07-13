---
title: "occupantsNumber property - TruckOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-truckoptions-occupantsnumber"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TruckOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">occupantsNumber</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">occupantsNumber</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.

**Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="sdk-for-flutter-explore-routing-truckoptions-allowoptions">TruckOptions.allowOptions</a> and such lanes are available in the selected country.

</div>

## Implementation

``` dart
int occupantsNumber;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

