---
title: "alternatives property - RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoptions-alternatives"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- alternatives.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">alternatives</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">alternatives</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

</div>

## Implementation

``` dart
int alternatives;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
