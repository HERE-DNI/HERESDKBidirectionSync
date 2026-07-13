---
title: "customLocationIndicator property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customLocationIndicator.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">customLocationIndicator</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>?</span> <span class="name">customLocationIndicator</span>

</div>

<div class="section desc markdown">

Custom location indicator <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> which <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, since <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is `null`, which means the default indicator is used, and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls. Gets the currently set `LocationIndicator`.

</div>

## Implementation

``` dart
LocationIndicator? get customLocationIndicator;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">customLocationIndicator=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-customLocationIndicator-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Custom location indicator <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> which <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, since <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is `null`, which means the default indicator is used, and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls. Sets a custom <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, so that <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses the provided one instead of the default.

</div>

## Implementation

``` dart
set customLocationIndicator(LocationIndicator? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
