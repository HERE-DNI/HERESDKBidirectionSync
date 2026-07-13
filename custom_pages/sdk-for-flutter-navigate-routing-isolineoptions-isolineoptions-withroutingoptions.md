---
title: "IsolineOptions.withRoutingOptions constructor - IsolineOptions - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-isolineoptions-isolineoptions-withroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptions.withRoutingOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/IsolineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">IsolineOptions.withRoutingOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">IsolineOptions.withRoutingOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withRoutingOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withRoutingOptions-param-routingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">routingOptions</span></span>

)

</div>

<div class="section desc markdown">

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options.

**Notes**

- By default all vehicle specifications from <a href="sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> are set to `null` and the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> is set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.
- A route can be calculated with only the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> set.

<!-- -->

- `calculationOptions` The options to be used to calculate this isoline.

- `routingOptions` The options that should influence the possible routes within the isoline. This determines also the transportation type.

</div>

## Implementation

``` dart
factory IsolineOptions.withRoutingOptions(IsolineOptionsCalculation calculationOptions, RoutingOptions routingOptions) => $prototype.withRoutingOptions(calculationOptions, routingOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
