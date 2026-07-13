---
title: "Fare constructor - Fare - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-fare-fare"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Fare-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Fare</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Fare</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-price" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-fareprice-class">FarePrice</a>?</span> <span class="parameter-name">price</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-reason" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-farereason">FareReason</a></span> <span class="parameter-name">reason</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `name` Name of a fare
- `price` Price of a fare. It is `null` when no price data is available.
- `reason` Reason of this cost.

</div>

## Implementation

``` dart
Fare(this.name, this.price, this.reason);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

