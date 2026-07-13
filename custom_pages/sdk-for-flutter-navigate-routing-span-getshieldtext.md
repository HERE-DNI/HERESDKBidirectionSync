---
title: "getShieldText method - Span class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-span-getshieldtext"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Span-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getShieldText</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">String</span> <span class="name">getShieldText</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getShieldText-param-roadNumber" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-class">LocalizedRoadNumber</a></span> <span class="parameter-name">roadNumber</span></span>

)

</div>

<div class="section desc markdown">

Converts full route number to the value to be displayed on the road shield.

The results are based on country code and state code of `Span` object and route type of passed `road_number` argument.

- `roadNumber` Route number to convert to shield text.

Returns `String`. Text on the road shield to display.

</div>

## Implementation

``` dart
String getShieldText(LocalizedRoadNumber roadNumber);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

