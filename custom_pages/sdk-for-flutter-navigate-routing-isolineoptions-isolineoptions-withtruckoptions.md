---
title: "IsolineOptions.withTruckOptions constructor - IsolineOptions - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-isolineoptions-isolineoptions-withtruckoptions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/IsolineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">IsolineOptions.withTruckOptions</span> constructor

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the constructor with \`RoutingOptions\` parameter instead.")

</div>

<span class="name deprecated">IsolineOptions.withTruckOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withTruckOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withTruckOptions-param-truckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a></span> <span class="parameter-name">truckOptions</span></span>

)

</div>

<div class="section desc markdown">

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.

- `calculationOptions` The options to be used to calculate this isoline.

- `truckOptions` The options that should influence the possible routes within the isoline. This determines also the transportation type.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")

factory IsolineOptions.withTruckOptions(IsolineOptionsCalculation calculationOptions, TruckOptions truckOptions) => $prototype.withTruckOptions(calculationOptions, truckOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

