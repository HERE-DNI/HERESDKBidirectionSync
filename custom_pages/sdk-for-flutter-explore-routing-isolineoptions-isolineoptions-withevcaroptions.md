---
title: "IsolineOptions.withEVCarOptions constructor - IsolineOptions - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withevcaroptions"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/IsolineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">IsolineOptions.withEVCarOptions</span> constructor

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the constructor with \`RoutingOptions\` parameter instead.")

</div>

<span class="name deprecated">IsolineOptions.withEVCarOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withEVCarOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span>
2.  <span id="sdk-for-flutter-explore-withEVCarOptions-param-evCarOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span> <span class="parameter-name">evCarOptions</span></span>

)

</div>

<div class="section desc markdown">

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.

- `calculationOptions` The options to be used to calculate this isoline.

- `evCarOptions` The options that should influence the possible routes within the isoline. This determines also the transportation type.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")

factory IsolineOptions.withEVCarOptions(IsolineOptionsCalculation calculationOptions, EVCarOptions evCarOptions) => $prototype.withEVCarOptions(calculationOptions, evCarOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

