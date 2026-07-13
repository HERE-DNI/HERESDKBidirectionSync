---
title: "validityPeriod property - FarePrice class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-fareprice-validityperiod"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/FarePrice-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">validityPeriod</span> property

</div>

<div class="section multi-line-signature">

Duration? <span class="name">validityPeriod</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

When set, the price is paid for a specific duration.

**Examples**:

3600 seconds - price for one hour

28800 seconds - price for eight hours

86400 seconds - price for one day

**Note:** When the ticket validity period starts depends on the <a href="sdk-for-flutter-explore-routing-agency-class">Agency</a> providing the service. Defaults to `null`.

</div>

## Implementation

``` dart
Duration? validityPeriod;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

