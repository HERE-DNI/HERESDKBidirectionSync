---
title: "setMapMatcher method - LocationManager class - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-setmapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMapMatcher.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/LocationManager-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMapMatcher</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setMapMatcher</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setMapMatcher-param-mapMatcher" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>?</span> <span class="parameter-name">mapMatcher</span></span>

)

</div>

<div class="section desc markdown">

Sets the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> for exclusive use by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

**Threading:** This method is asynchronous and performs the switch in an internal thread of <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>. **Note:** After calling this method, the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> is owned and used exclusively by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a> in its internal processing thread. Do not use or access the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> elsewhere while it is set.

- `mapMatcher` The <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> instance to be used exclusively by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

</div>

## Implementation

``` dart
void setMapMatcher(MapMatcher? mapMatcher);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
