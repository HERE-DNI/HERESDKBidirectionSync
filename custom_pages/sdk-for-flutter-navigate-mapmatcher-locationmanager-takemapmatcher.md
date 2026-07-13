---
title: "takeMapMatcher method - LocationManager class - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-takemapmatcher"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/LocationManager-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">takeMapMatcher</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>?</span> <span class="name">takeMapMatcher</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Retrieves and removes the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> from <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

**Note:** After calling this method, <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a> will no longer use the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> at all. the caller regains full ownership and responsibility for the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>.

Returns <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher?</a>. The <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> instance previously set, or `null` if none was set.

</div>

## Implementation

``` dart
MapMatcher? takeMapMatcher();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

