---
title: "OpeningHours constructor - OpeningHours - search library - Dart API"
slug: "sdk-for-flutter-explore-search-openinghours-openinghours"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/OpeningHours-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">OpeningHours</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">OpeningHours</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-text" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">text</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-isOpen" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isOpen</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-scheduleDetailsList" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-scheduledetails-class">ScheduleDetails</a></span>\></span></span> <span class="parameter-name">scheduleDetailsList</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `text` The list of opening hours presented as localized text.
- `isOpen` Boolean flag informing if the place is open or closed at the time when the search request was initiated. For offline search, this is calculated using device's time, so it may give incorrect value if device and place are located in different time zones.
- `scheduleDetailsList` The list of schedule details.
- `categories` The list of categories related to opening hours information. This data is not available in offline search.

</div>

## Implementation

``` dart
OpeningHours(this.text, this.isOpen, this.scheduleDetailsList, this.categories);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

