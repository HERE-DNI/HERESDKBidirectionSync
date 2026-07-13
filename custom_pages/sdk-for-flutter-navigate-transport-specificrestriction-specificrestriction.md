---
title: "SpecificRestriction constructor - SpecificRestriction - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-specificrestriction-specificrestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpecificRestriction.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/SpecificRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SpecificRestriction</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SpecificRestriction</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType</a></span> <span class="parameter-name">type</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a></span> <span class="parameter-name">value</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `type` Type of restriction.

- `value` Values for which the restriction applies. Examples:

-     (min, max)

  → Restriction applies for all values between min and max inclusive.

-     (n, n)

  → Restriction applies to an exact value.

-     (n, 0)

  or

      (n, null)

  → Restriction applies for values greater than or equal to min (unbounded upper limit).

</div>

## Implementation

``` dart
SpecificRestriction(this.type, this.value);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
